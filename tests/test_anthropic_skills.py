# Anthropic 설치기의 이름 변환·개인 파일 보호·멱등성과 실패 복구를 검증한다.
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/install_anthropic_skills.py'
COMMIT = 'a' * 40


class AnthropicInstallerTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(SCRIPT.is_file(), '승인된 설치기가 아직 없습니다.')
        spec = importlib.util.spec_from_file_location('anthropic_installer', SCRIPT)
        self.installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.installer)
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.home = self.root / 'home'
        self.home.mkdir()
        self.archive = self.root / 'source.zip'
        self.files = {
            'skills/frontend-design/SKILL.md': b'---\nname: frontend-design\ndescription: Design.\n---\nUse $skill-creator and ../skill-creator/SKILL.md.\nhttps://github.com/anthropics/skills/tree/main/skills/frontend-design\n',
            'skills/frontend-design/LICENSE.txt': b'original license\n',
            'skills/frontend-design/assets/pixel.bin': b'\x00\xff',
            'skills/skill-creator/SKILL.md': b'---\nname: skill-creator\ndescription: Create.\n---\nRead references/guide.md.\n',
            'skills/skill-creator/references/guide.md': b'Use skill-creator/scripts/run.py\n',
            'skills/skill-creator/LICENSE.txt': b'original license\n',
            'THIRD_PARTY_NOTICES.md': b'upstream third party notices\n',
        }
        self.manifest = {
            'schema_version': 1,
            'repository': 'https://github.com/anthropics/skills',
            'commit': COMMIT,
            'archive_sha256': '',
            'skills': [
                {'source': 'frontend-design', 'name': 'anthropic-frontend-design', 'implicit': True, 'migrate_from': 'frontend-design'},
                {'source': 'skill-creator', 'name': 'anthropic-skill-creator', 'implicit': False, 'migrate_from': 'skill-creator'},
            ],
        }
        self.write_archive()

    def write_archive(self, extras=()):
        with zipfile.ZipFile(self.archive, 'w') as archive:
            for name, content in self.files.items():
                archive.writestr('skills-' + COMMIT + '/' + name, content)
            for name, content in extras:
                archive.writestr(name, content)
        self.manifest['archive_sha256'] = hashlib.sha256(self.archive.read_bytes()).hexdigest()

    def run_install(self, apply=True):
        return self.installer.install(self.manifest, self.archive, self.home, apply=apply)

    def active(self, name):
        return self.home / '.agents/skills' / name

    def snapshot(self):
        return {p.relative_to(self.home).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.home.rglob('*') if p.is_file()}

    def legacy(self):
        for name, content in self.files.items():
            if name.startswith('skills/'):
                path = self.home / '.agents' / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)

    def test_installs_names_resources_and_explicit_policy(self):
        result = self.run_install()
        self.assertEqual(result['installed'], ['anthropic-frontend-design', 'anthropic-skill-creator'])
        design = self.active('anthropic-frontend-design')
        text = (design / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('name: anthropic-frontend-design\n', text)
        self.assertIn('$anthropic-skill-creator and ../anthropic-skill-creator/SKILL.md', text)
        self.assertIn('https://github.com/anthropics/skills/tree/main/skills/frontend-design', text)
        self.assertEqual((design / 'assets/pixel.bin').read_bytes(), b'\x00\xff')
        self.assertEqual((design / 'LICENSE.txt').read_bytes(), b'original license\n')
        self.assertEqual((design / 'UPSTREAM_THIRD_PARTY_NOTICES.md').read_bytes(), b'upstream third party notices\n')
        self.assertIn('allow_implicit_invocation: false',
                      (self.active('anthropic-skill-creator') / 'agents/openai.yaml').read_text())

    def test_second_install_and_check_leave_files_and_backups_unchanged(self):
        self.run_install()
        before = self.snapshot()
        self.assertEqual(self.run_install()['installed'], [])
        self.assertEqual(self.run_install(apply=False)['installed'], [])
        self.assertEqual(self.snapshot(), before)

    def test_check_missing_packages_does_not_create_anything(self):
        result = self.run_install(apply=False)
        self.assertEqual(result['pending'], ['anthropic-frontend-design', 'anthropic-skill-creator'])
        self.assertEqual(list(self.home.iterdir()), [])

    def test_migrates_whole_identical_legacy_packages_and_preserves_custom_skill(self):
        self.legacy()
        custom = self.active('claude-api') / 'SKILL.md'
        custom.parent.mkdir()
        custom.write_text('personal API instructions', encoding='utf-8')
        result = self.run_install()
        self.assertFalse(self.active('frontend-design').exists())
        self.assertFalse(self.active('skill-creator').exists())
        backup = Path(result['backup'])
        self.assertEqual((backup / 'legacy/frontend-design/assets/pixel.bin').read_bytes(), b'\x00\xff')
        self.assertEqual(custom.read_text(encoding='utf-8'), 'personal API instructions')

    def test_rejects_modified_legacy_before_installing_any_package(self):
        self.legacy()
        (self.active('skill-creator') / 'personal.md').write_text('keep me', encoding='utf-8')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'legacy|Legacy'):
            self.run_install()
        self.assertEqual(self.snapshot(), before)
        self.assertFalse(self.active('anthropic-frontend-design').exists())

    def test_accepts_only_explicitly_pinned_legacy_license_variant(self):
        self.legacy()
        old_license = b'older official copyright notice\n'
        license_path = self.active('skill-creator') / 'LICENSE.txt'
        license_path.write_bytes(old_license)
        self.manifest['skills'][1]['legacy_license_sha256'] = hashlib.sha256(old_license).hexdigest()
        result = self.run_install()
        self.assertEqual((Path(result['backup']) / 'legacy/skill-creator/LICENSE.txt').read_bytes(), old_license)
        self.assertEqual((self.active('anthropic-skill-creator') / 'LICENSE.txt').read_bytes(), b'original license\n')

    def test_rejects_unmanaged_existing_target(self):
        path = self.active('anthropic-skill-creator') / 'SKILL.md'
        path.parent.mkdir(parents=True)
        path.write_text('user owned', encoding='utf-8')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'unmanaged|Unmanaged'):
            self.run_install()
        self.assertEqual(self.snapshot(), before)

    def test_rejects_modified_managed_package(self):
        self.run_install()
        (self.active('anthropic-skill-creator') / 'references/guide.md').write_text('personal edit', encoding='utf-8')
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'modified|Modified'):
            self.run_install()
        self.assertEqual(self.snapshot(), before)

    def test_rejects_tampered_zip_before_changes(self):
        self.archive.write_bytes(self.archive.read_bytes() + b'tamper')
        with self.assertRaisesRegex(ValueError, 'SHA256'):
            self.run_install()
        self.assertEqual(list(self.home.iterdir()), [])

    def test_rejects_unsafe_and_duplicate_archive_members(self):
        root = 'skills-' + COMMIT + '/'
        for member in (root + '../escape', root + 'skills/frontend-design/evil:stream',
                       root + 'skills/frontend-design/skill.MD', root + 'skills/frontend-design//SKILL.md'):
            with self.subTest(member=member):
                self.write_archive([(member, self.files['skills/frontend-design/SKILL.md'])])
                with self.assertRaises(ValueError):
                    self.run_install()
                self.assertEqual(list(self.home.iterdir()), [])

    def test_rejects_symlinks_in_archive(self):
        entry = zipfile.ZipInfo('skills-' + COMMIT + '/skills/frontend-design/link')
        entry.create_system = 3
        entry.external_attr = 0o120777 << 16
        self.write_archive([(entry, b'outside')])
        with self.assertRaisesRegex(ValueError, 'link|type'):
            self.run_install()

    def test_rejects_destination_links_without_touching_target(self):
        outside = self.root / 'outside'
        outside.mkdir()
        link = self.active('anthropic-frontend-design')
        link.parent.mkdir(parents=True)
        try:
            link.symlink_to(outside, target_is_directory=True)
        except OSError:
            if os.name != 'nt':
                raise
            result = subprocess.run(['cmd', '/d', '/c', 'mklink', '/J', str(link), str(outside)],
                                    capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        with self.assertRaisesRegex(ValueError, 'link|junction'):
            self.run_install()
        self.assertEqual(list(outside.iterdir()), [])

    def test_rejects_invalid_manifest_name_before_changes(self):
        self.manifest['skills'][0]['name'] = '../outside'
        with self.assertRaises(ValueError):
            self.run_install()
        self.assertEqual(list(self.home.iterdir()), [])

    def test_path_conversion_preserves_package_resources(self):
        text = 'assets/frontend-design/example ../skill-creator/SKILL.md skill-creator/scripts/run.py'
        actual = self.installer.transform_text(text, self.manifest['skills'])
        self.assertEqual(actual, 'assets/frontend-design/example ../anthropic-skill-creator/SKILL.md anthropic-skill-creator/scripts/run.py')

    def test_path_conversion_preserves_file_format_enumeration(self):
        actual = self.installer.transform_text('(docx/pptx/anything else)', [
            {'source': 'docx', 'name': 'anthropic-docx'},
            {'source': 'pptx', 'name': 'anthropic-pptx'},
        ])
        self.assertEqual(actual, '(docx/pptx/anything else)')

    def test_cli_migration_succeeds_and_check_is_read_only(self):
        script = self.root / 'project/scripts/install_anthropic_skills.py'
        script.parent.mkdir(parents=True)
        script.write_bytes(SCRIPT.read_bytes())
        manifest = script.parent.parent / 'references/anthropic-skills.lock.json'
        manifest.parent.mkdir()
        manifest.write_text(json.dumps(self.manifest), encoding='utf-8')
        self.legacy()
        command = [sys.executable, '-X', 'utf8', '-B', str(script), '--home', str(self.home), '--archive', str(self.archive)]
        before = self.snapshot()
        checked = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', timeout=30)
        self.assertEqual(checked.returncode, 1, checked.stdout + checked.stderr)
        self.assertEqual(self.snapshot(), before)
        applied = subprocess.run(command + ['--apply'], capture_output=True, text=True, encoding='utf-8', timeout=30)
        self.assertEqual(applied.returncode, 0, applied.stdout + applied.stderr)
        before = self.snapshot()
        checked = subprocess.run(command, capture_output=True, text=True, encoding='utf-8', timeout=30)
        self.assertEqual(checked.returncode, 0, checked.stdout + checked.stderr)
        self.assertEqual(self.snapshot(), before)

    @unittest.skipUnless(os.name == 'nt', 'Windows ACL inheritance')
    def test_published_files_inherit_target_permissions(self):
        self.run_install()
        paths = [self.active('anthropic-frontend-design'),
                 self.active('anthropic-frontend-design') / 'SKILL.md',
                 self.installer.data_directory(self.home) / 'anthropic-skills-state.json']
        for path in paths:
            result = subprocess.run(['icacls', str(path)], capture_output=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(b'(I)', result.stdout, result.stdout)

    def test_rejects_target_appearing_after_preflight(self):
        real_temporary = self.installer.tempfile.TemporaryDirectory
        personal = self.active('anthropic-skill-creator') / 'personal.md'

        def concurrent_write(*args, **kwargs):
            temporary = real_temporary(*args, **kwargs)
            personal.parent.mkdir(parents=True)
            personal.write_text('keep this new file', encoding='utf-8')
            return temporary

        with patch.object(self.installer.tempfile, 'TemporaryDirectory', side_effect=concurrent_write):
            with self.assertRaisesRegex(ValueError, 'changed|appeared|Unmanaged'):
                self.run_install()
        self.assertEqual(personal.read_text(encoding='utf-8'), 'keep this new file')
        self.assertFalse(self.active('anthropic-frontend-design').exists())

    def test_publish_failure_restores_legacy_and_removes_new_packages(self):
        self.legacy()
        original = {p.relative_to(self.home).as_posix(): p.read_bytes()
                    for p in (self.home / '.agents').rglob('*') if p.is_file()}
        real_replace = self.installer.os.replace

        def fail_second_publish(source, destination):
            if Path(destination) == self.active('anthropic-skill-creator') and 'stage' in str(source):
                raise OSError('simulated publish failure')
            return real_replace(source, destination)

        with patch.object(self.installer.os, 'replace', side_effect=fail_second_publish):
            with self.assertRaisesRegex(OSError, 'simulated'):
                self.run_install()
        actual = {p.relative_to(self.home).as_posix(): p.read_bytes()
                  for p in (self.home / '.agents').rglob('*') if p.is_file()}
        self.assertEqual(actual, original)


if __name__ == '__main__':
    unittest.main()
