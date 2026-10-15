# 전체 리뷰에서 재현된 문서 예제와 작업 스크립트의 오류를 검증한다.
import ast
import contextlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / 'Owned-Skills/design-driven-delivery/scripts'
sys.path.insert(0, str(SCRIPTS))


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)

    def write(self, relative, text='완료.\n- [x] 확인.\n'):
        path = self.project / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')
        return path

    def run_cli(self, name, *args):
        return subprocess.run([sys.executable, '-X', 'utf8', '-B', str(SCRIPTS / f'{name}.py'),
                               '--project', str(self.project), *args],
                              capture_output=True, text=True, encoding='utf-8')

    def complete_project(self):
        for path in ('docs/current-state.md', 'docs/design-progress-checklist.md',
                     'docs/specs/current.md', 'docs/plans/current.md', 'docs/reviews/current.md'):
            self.write(path)

    def test_bootstrap_preserves_existing_layout_and_completion(self):
        self.complete_project()
        self.assertEqual(self.run_cli('validate_workflow').returncode, 0)
        result = self.run_cli('bootstrap_workflow')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.project / 'docs/superpowers').exists())
        self.assertEqual(self.run_cli('validate_workflow').returncode, 0)

    def test_bootstrap_does_not_overwrite_concurrent_creation(self):
        module = load_script('bootstrap_workflow')
        destination = self.project / 'docs/current-state.md'
        original_exists = Path.exists

        def concurrent_exists(path):
            if path == destination and not original_exists(path):
                path.write_text('다른 작업자의 문서.', encoding='utf-8')
                return False
            return original_exists(path)

        with patch.object(sys, 'argv', ['bootstrap', '--project', str(self.project)]), \
                patch.object(Path, 'exists', concurrent_exists), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(module.main(), 0)
        self.assertEqual(destination.read_text(encoding='utf-8'), '다른 작업자의 문서.')

    def test_selected_current_documents_ignore_unfinished_history(self):
        self.complete_project()
        self.write('docs/plans/superseded.md', '- [ ] 취소된 작업.\n')
        result = self.run_cli('validate_workflow', '--spec', 'docs/specs/current.md',
                              '--plan', 'docs/plans/current.md', '--review', 'docs/reviews/current.md')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_selected_incomplete_document_fails(self):
        self.complete_project()
        self.write('docs/plans/current.md', '- [ ] 남은 작업.\n')
        result = self.run_cli('validate_workflow', '--spec', 'docs/specs/current.md',
                              '--plan', 'docs/plans/current.md', '--review', 'docs/reviews/current.md')
        self.assertEqual(result.returncode, 1)
        self.assertIn('미완료', result.stderr)

    def test_selected_missing_document_fails(self):
        self.complete_project()
        result = self.run_cli('validate_workflow', '--plan', 'docs/plans/missing.md')
        self.assertEqual(result.returncode, 1)
        self.assertIn('필수 문서', result.stderr)

    def test_selected_path_outside_project_fails(self):
        self.complete_project()
        result = self.run_cli('validate_workflow', '--plan', '../outside.md')
        self.assertEqual(result.returncode, 1)
        self.assertIn('프로젝트 밖', result.stderr)

    def test_bootstrap_dry_run_writes_nothing(self):
        result = self.run_cli('bootstrap_workflow', '--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.project.iterdir()), [])

    def test_new_project_bootstrap_uses_defaults_and_preserves_edits(self):
        self.assertEqual(self.run_cli('bootstrap_workflow').returncode, 0)
        self.assertTrue((self.project / 'docs/superpowers/specs').is_dir())
        self.assertTrue((self.project / 'docs/superpowers/plans').is_dir())
        path = self.write('docs/current-state.md', '사용자 문서.')
        self.assertEqual(self.run_cli('bootstrap_workflow').returncode, 0)
        self.assertEqual(path.read_text(encoding='utf-8'), '사용자 문서.')

    def test_repeated_selection_checks_every_selected_document(self):
        self.complete_project()
        self.write('docs/plans/extra.md', '- [ ] 남은 추가 작업.\n')
        result = self.run_cli('validate_workflow', '--plan', 'docs/plans/current.md',
                              '--plan', 'docs/plans/extra.md')
        self.assertEqual(result.returncode, 1)
        self.assertIn('extra.md', result.stderr)

    def test_selected_non_markdown_file_fails(self):
        self.complete_project()
        self.write('docs/plans/current.txt')
        result = self.run_cli('validate_workflow', '--plan', 'docs/plans/current.txt')
        self.assertEqual(result.returncode, 1)
        self.assertIn('Markdown', result.stderr)

    def test_bootstrap_rejects_directory_in_file_position(self):
        (self.project / 'docs/current-state.md').mkdir(parents=True)
        self.assertEqual(self.run_cli('bootstrap_workflow').returncode, 1)

    def test_template_read_failure_leaves_no_empty_document(self):
        module = load_script('bootstrap_workflow')
        original_open = Path.open

        def unreadable_template(path, *args, **kwargs):
            if path.name == 'current-state-template.md':
                raise PermissionError('template unavailable')
            return original_open(path, *args, **kwargs)

        with patch.object(sys, 'argv', ['bootstrap', '--project', str(self.project)]), \
                patch.object(Path, 'open', unreadable_template), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(module.main(), 1)
        self.assertFalse((self.project / 'docs/current-state.md').exists())

    def test_copy_failure_removes_partial_document_and_retry_succeeds(self):
        module = load_script('bootstrap_workflow')

        def interrupted_copy(source, destination):
            destination.write(b'partial')
            raise OSError('disk write failed')

        with patch.object(sys, 'argv', ['bootstrap', '--project', str(self.project)]), \
                patch.object(module.shutil, 'copyfileobj', interrupted_copy), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(module.main(), 1)
        self.assertFalse((self.project / 'docs/current-state.md').exists())
        self.assertEqual(self.run_cli('bootstrap_workflow').returncode, 0)
        self.assertTrue((self.project / 'docs/current-state.md').read_text(encoding='utf-8'))

    def link_directory(self, link, target):
        if os.name == 'nt':
            result = subprocess.run(['cmd', '/c', 'mklink', '/J', str(link), str(target)],
                                    capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.addCleanup(os.rmdir, link)
        else:
            link.symlink_to(target, target_is_directory=True)
            self.addCleanup(link.unlink)

    def test_junction_outside_project_rejected_before_creation(self):
        with tempfile.TemporaryDirectory() as outside:
            self.link_directory(self.project / 'docs', Path(outside))
            for dry_run in ([], ['--dry-run']):
                result = self.run_cli('bootstrap_workflow', *dry_run)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn('프로젝트 밖', result.stderr)
            self.assertEqual(list(Path(outside).iterdir()), [])

    def test_default_validation_rejects_external_document(self):
        self.complete_project()
        original = self.project / 'docs/plans/current.md'
        original.unlink()
        (self.project / 'docs/plans').rmdir()
        with tempfile.TemporaryDirectory() as external:
            (Path(external) / 'current.md').write_text('완료.', encoding='utf-8')
            self.link_directory(self.project / 'docs/plans', Path(external))
            result = self.run_cli('validate_workflow')
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn('프로젝트 밖', result.stderr)

    def test_copy_failure_preserves_concurrent_user_save(self):
        module = load_script('bootstrap_workflow')
        target = self.project / 'docs/current-state.md'

        def failed_copy(source, destination):
            destination.write(b'partial')
            destination.close()
            replacement = target.with_suffix('.new')
            replacement.write_text('사용자가 저장한 새 문서.', encoding='utf-8')
            os.replace(replacement, target)
            raise OSError('copy interrupted after user save')

        with patch.object(sys, 'argv', ['bootstrap', '--project', str(self.project)]), \
                patch.object(module.shutil, 'copyfileobj', failed_copy), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(module.main(), 1)
        self.assertEqual(target.read_text(encoding='utf-8'), '사용자가 저장한 새 문서.')

    def test_all_markdown_list_markers_block_incomplete_work(self):
        self.complete_project()
        for marker in ('-', '*', '+'):
            with self.subTest(marker=marker):
                self.write('docs/plans/current.md', f'{marker} [ ] pending\n')
                self.assertEqual(self.run_cli('validate_workflow').returncode, 1)

    def test_markdown_code_examples_do_not_block_completed_work(self):
        self.complete_project()
        for example in ('```markdown\n- [ ] example\nTODO\n```',
                        '~~~~markdown\n+ [ ] example\n[REQUIRED]\n~~~~',
                        '설명에서 `TODO`와 `[REQUIRED]`를 예시로 쓴다.'):
            with self.subTest(example=example):
                self.write('docs/plans/current.md', '- [x] done\n' + example)
                result = self.run_cli('validate_workflow')
                self.assertEqual(result.returncode, 0, result.stderr)

    def test_inline_delimiters_cannot_hide_real_pending_work(self):
        self.complete_project()
        for text in ('```literal```\n\n- [ ] pending verification\n',
                     '`unmatched opening\n\n- [ ] pending verification\n``'):
            with self.subTest(text=text):
                self.write('docs/plans/current.md', text)
                self.assertEqual(self.run_cli('validate_workflow').returncode, 1)

    def test_required_template_fields_are_not_treated_as_examples(self):
        self.complete_project()
        templates = SCRIPTS.parent / 'assets/templates'
        for name, prefix in (('plan-template.md', '- 생성:'),
                             ('review-template.md', '**기준:**'),
                             ('handover-template.md', '**저장소:**')):
            with self.subTest(template=name):
                field = next(line for line in (templates / name).read_text(encoding='utf-8').splitlines()
                             if line.startswith(prefix))
                self.write('docs/plans/current.md', '- [x] done\n' + field)
                result = self.run_cli('validate_workflow')
                self.assertEqual(result.returncode, 1)
                self.assertIn('자리표시자', result.stderr)

    def test_failed_publication_preserves_existing_document_and_removes_only_temp(self):
        module = load_script('bootstrap_workflow')
        target = self.project / 'docs/current-state.md'

        def failed_link(source, destination):
            destination.write_text('사용자 문서.', encoding='utf-8')
            raise OSError('hard links unavailable')

        with patch.object(sys, 'argv', ['bootstrap', '--project', str(self.project)]), \
                patch.object(module.os, 'link', failed_link), \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(module.main(), 1)
        self.assertEqual(target.read_text(encoding='utf-8'), '사용자 문서.')
        self.assertFalse(list(target.parent.glob('.workflow-*')))


class HookMergeTests(unittest.TestCase):
    def setUp(self):
        content = (ROOT / 'references/claude-code-cli-setup.md').read_text(encoding='utf-8')
        tree = ast.parse(next(code for code in re.findall(r'```python\n(.*?)```', content, re.S)
                              if 'def merge_hooks' in code))
        function = next(node for node in tree.body if isinstance(node, ast.FunctionDef))
        namespace = {}
        exec(compile(ast.Module(body=[function], type_ignores=[]), '<documented merge>', 'exec'), namespace)
        self.merge = namespace['merge_hooks']

    def test_same_matcher_preserves_distinct_security_handler(self):
        target = {'hooks': {'PreToolUse': [{'matcher': 'Bash', 'hooks': [{'type': 'command', 'command': 'log'}]}]}}
        guard = {'matcher': 'Bash', 'hooks': [{'type': 'command', 'command': 'guard'}]}
        source = {'hooks': {'PreToolUse': [guard]}}
        self.merge(target, source, 'PreToolUse')
        self.merge(target, source, 'PreToolUse')
        self.assertEqual(len(target['hooks']['PreToolUse']), 2)
        self.assertIn(guard, target['hooks']['PreToolUse'])

    def test_matcher_optional_and_repeated_import_idempotent(self):
        entry = {'hooks': [{'type': 'command', 'command': 'verify'}]}
        target = {'hooks': {'SessionStart': [entry]}}
        source = {'hooks': {'SessionStart': [entry]}}
        self.merge(target, source, 'SessionStart')
        self.assertEqual(target['hooks']['SessionStart'], [entry])


class BackupTests(unittest.TestCase):
    def setUp(self):
        self.bash = shutil.which('bash')
        if not self.bash and shutil.which('git'):
            candidate = Path(shutil.which('git')).parent.parent / 'bin/bash.exe'
            if candidate.is_file():
                self.bash = str(candidate)
        if not self.bash:
            self.skipTest('백업 예제 검증에 필요한 Bash가 없습니다.')
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.claude = Path(self.temp.name) / '.claude'
        self.claude.mkdir()
        for relative in ('CLAUDE.md', 'settings.json', 'skills/sample/SKILL.md'):
            target = self.claude / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('fixture', encoding='utf-8')
        content = (ROOT / 'references/claude-code-cli-setup.md').read_text(encoding='utf-8')
        self.code = re.search(r'### Step 3:.*?```bash\n(.*?)```', content, re.S).group(1)
        self.code = self.code.replace('$HOME/.claude', self.claude.as_posix())

    def run_backup(self, prefix='', suffix=''):
        return subprocess.run([self.bash, '--noprofile', '--norc', '-c', prefix + self.code + suffix],
                              env=dict(os.environ, CLAUDE_CONFIG_DIR=self.claude.as_posix()),
                              capture_output=True, text=True, encoding='utf-8')

    def test_repeated_backup_copies_only_originals(self):
        for _ in range(3):
            result = self.run_backup()
            self.assertEqual(result.returncode, 0, result.stderr)
        backups = list(self.claude.glob('backup_*'))
        self.assertEqual(len(backups), 3)
        for backup in backups:
            self.assertEqual(len([p for p in backup.rglob('*') if p.is_file()]), 3)
            self.assertFalse(list(backup.rglob('backup_*')))

    def test_copy_failure_stops_before_installation(self):
        result = self.run_backup('cp() { return 7; };\n', '\nprintf installation-started\n')
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('installation-started', result.stdout)

    def test_selected_theme_home_files_are_backed_up(self):
        for name in ('.bashrc', '.minttyrc', '.elephant_walk.py'):
            (Path(self.temp.name) / name).write_text('original theme', encoding='utf-8')
        code = self.code.replace('$HOME', Path(self.temp.name).as_posix()).replace(
            'selected_items=""', 'selected_items="13"')
        result = subprocess.run([self.bash, '--noprofile', '--norc', '-c',
                                 'selected_items="13"\n' + code],
                                env=dict(os.environ, CLAUDE_CONFIG_DIR=self.claude.as_posix()),
                                capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        backup = next(self.claude.glob('backup_*'))
        for name in ('.bashrc', '.minttyrc', '.elephant_walk.py'):
            self.assertEqual((backup / 'home' / name).read_text(encoding='utf-8'), 'original theme')


class SetupExampleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.target = Path(self.temp.name) / '.claude/settings.json'
        self.target.parent.mkdir()
        content = (ROOT / 'references/claude-code-cli-setup.md').read_text(encoding='utf-8')
        self.load_code = re.findall(r'```python\n(.*?)```', content, re.S)[0]
        self.code = next(c for c in re.findall(r'```python\n(.*?)```', content, re.S)
                         if 'def merge_hooks' in c)
        self.source = {'hooks': {'PreToolUse': [{'hooks': [{'type': 'command', 'command': 'guard'}]}],
                                 'SessionStart': [{'hooks': [{'type': 'command', 'command': 'verify'}]}]},
                       'permissions': {'allow': ['Bash(example)']}, 'language': 'korean'}

    def execute(self, selected):
        dotfiles = Path(self.temp.name) / 'dotfiles'
        dotfiles.mkdir(exist_ok=True)
        (dotfiles / 'settings.json').write_text(json.dumps(self.source), encoding='utf-8')
        if not self.target.exists():
            self.target.write_text('{"custom":"keep"}', encoding='utf-8')
        namespace = {}
        previous_cwd = Path.cwd()
        try:
            os.chdir(self.temp.name)
            with patch.object(Path, 'home', return_value=Path(self.temp.name)), \
                    patch.dict(os.environ, {'CLAUDE_CONFIG_DIR': str(self.target.parent)}), \
                    patch('builtins.input', return_value=' '.join(map(str, selected))):
                exec(compile(self.load_code, '<load settings>', 'exec'), namespace)
                exec(compile(self.code, '<setup example>', 'exec'), namespace)
        finally:
            os.chdir(previous_cwd)
        return json.loads(self.target.read_text(encoding='utf-8'))

    def test_selected_hooks_are_saved_without_unselected_permissions(self):
        saved = self.execute({2})
        self.assertEqual(saved.get('hooks'), self.source['hooks'])
        self.assertNotIn('permissions', saved)
        self.assertEqual(saved['custom'], 'keep')

    def test_selected_permissions_saved_without_unselected_hooks(self):
        saved = self.execute({7})
        self.assertEqual(saved['permissions'], self.source['permissions'])
        self.assertNotIn('hooks', saved)

    def test_all_selected_sections_are_saved_and_existing_plugins_preserved(self):
        self.target.write_text('{"custom":"keep","enabledPlugins":{"existing":true}}', encoding='utf-8')
        self.source.update({'statusLine': {'type': 'command', 'command': 'status'},
                            'enabledPlugins': {'new': True}})
        for event in ('Notification', 'PostToolUse'):
            self.source['hooks'][event] = [{'hooks': [{'type': 'command', 'command': event}]}]
        saved = self.execute({2, 3, 5, 6, 7, 14, 15})
        self.assertEqual(saved['hooks'], self.source['hooks'])
        self.assertEqual(saved['enabledPlugins'], {'existing': True, 'new': True})
        self.assertEqual(saved['statusLine'], self.source['statusLine'])
        self.assertEqual(saved['language'], 'korean')

    def test_invalid_selection_does_not_write_settings(self):
        self.target.write_text('{"custom":"keep"}', encoding='utf-8')
        with self.assertRaises(ValueError):
            self.execute({21})
        self.assertEqual(self.target.read_text(encoding='utf-8'), '{"custom":"keep"}')

    def test_write_failure_preserves_existing_settings(self):
        original = '{"custom": "original"}'
        self.target.write_text(original, encoding='utf-8')

        def interrupted_dump(obj, stream, **kwargs):
            stream.write('{')
            stream.flush()
            raise OSError('write interrupted')

        with patch.object(json, 'dump', interrupted_dump):
            with self.assertRaises(OSError):
                self.execute({2})
        self.assertEqual(self.target.read_text(encoding='utf-8'), original)
        self.assertEqual(list(self.target.parent.iterdir()), [self.target])


if __name__ == '__main__':
    unittest.main()
