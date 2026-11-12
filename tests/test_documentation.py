# 통합 카탈로그·보관 기록·문서 링크의 구조와 실패 조건을 검증한다.
from collections import Counter
from html import unescape
from pathlib import Path
import re
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

from test_owned_skill_packages import markdown_links, prose_only

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    '_builtin': 13, '_personal': 5, 'superpowers': 15,
    'huggingface-skills': 18, 'firecrawl': 11, 'figma': 9,
    'plugin-dev': 8, 'chrome-devtools-mcp': 6, 'ralph-loop': 3,
    'claude-md-management': 2, 'qodo-skills': 2, 'agent-sdk-dev': 1,
    'pr-review-toolkit': 1, 'feature-dev': 1, 'claude-code-setup': 1,
    'skill-creator': 1, 'frontend-design': 1, 'playground': 1, 'kordoc': 1,
    'anthropic-skills': 19, 'office-design-tools': 3,
    '_disabled/vercel': 13, '_disabled/hookify': 5, '_disabled/neon': 2,
    '_disabled/railway': 1, '_disabled/semgrep': 1,
}
HISTORY = {
    '2026-10-12-readme-mermaid': 1, '2026-10-13-client-cli-setup': 3,
    '2026-10-13-codex-windows-setup': 3, '2026-10-13-review-fixes': 2,
    '2026-10-13-review-followup': 2, '2026-10-13-starred-repo-adoption': 3,
    '2026-10-14-beginner-readme-and-audit-fixes': 3,
    '2026-10-14-chrome-devtools-mcp': 3, '2026-10-14-repository-review': 2,
    '2026-10-15-portable-skill-workflows': 3, '2026-10-15-regression-ci': 3,
    '2026-11-05-superpowers-update': 3, '2026-11-06-codex-skills-update': 3,
    '2026-11-06-skill-provenance': 3,
    '2026-11-09-document-consolidation': 3,
    '2026-11-11-readme-bilingual': 3,
    '2026-11-11-coplay-funplay-unity-mcp': 3,
    '2026-11-12-anthropic-skills': 3,
    '2026-11-12-anthropic-functional': 2,
    '2026-11-12-office-design-tools': 3,
}


def prose_lines(text):
    """Keep source line positions while ignoring fenced code."""
    fence = None
    for index, line in enumerate(text.splitlines(keepends=True)):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\r\n'))
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence) and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1]
        else:
            yield index, line
    if fence:
        raise ValueError('Unclosed Markdown fence')


def catalog_sections(text):
    """Extract H2 item boundaries without reading headings inside code."""
    lines = text.splitlines(keepends=True)
    starts = [(index, match[1]) for index, line in prose_lines(text)
              if (match := re.fullmatch(r'## ([a-z0-9_-]+)\s*', line))]
    sections = {}
    for offset, (index, name) in enumerate(starts):
        if name in sections:
            raise ValueError('Duplicate catalog item: ' + name)
        end = starts[offset + 1][0] if offset + 1 < len(starts) else len(lines)
        sections[name] = ''.join(lines[index + 1:end])
    return sections


def heading_slug(title):
    title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
    title = re.sub(r'<[^>]+>', '', title)
    return re.sub(r'[^\w\-\s]', '', unescape(title).lower()).replace(' ', '-')


def anchor_ids(text):
    result = set()
    seen = Counter()
    for anchor in re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)["\x27]\s*>', prose_only(text), re.I):
        if anchor in result:
            raise ValueError('Duplicate anchor: ' + anchor)
        result.add(anchor)
    for _, line in prose_lines(text):
        if match := re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', line):
            base = heading_slug(match[1])
            count = seen[base]
            seen[base] += 1
            value = base + ('-' + str(count) if count else '')
            if value in result:
                raise ValueError('Duplicate anchor: ' + value)
            result.add(value)
    return result


def link_errors(root, relative, text):
    errors = []
    source = root / relative
    for target in markdown_links(text):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        path = unquote(parsed.path)
        # 전역 배포 템플릿은 실제 설치 위치에서만 알려진 접두사를 해석한다.
        if relative.as_posix() == 'codex-global-AGENTS.md' and path.startswith('Agent-Instructions/'):
            path = path[len('Agent-Instructions/'):]
        destination = (source.parent / path).resolve() if path else source.resolve()
        if not destination.is_relative_to(root.resolve()) or not destination.exists():
            errors.append(target)
            continue
        if destination.is_dir():
            destination = destination / 'README.md'
        if parsed.fragment and destination.suffix.lower() == '.md' and destination.is_file():
            if unquote(parsed.fragment) not in anchor_ids(destination.read_text(encoding='utf-8')):
                errors.append(target)
    return errors


class DocumentationTests(unittest.TestCase):
    def test_task_navigation_routes_existing_entries(self):
        document = ROOT / 'Skill/BY-TASK.md'
        self.assertTrue(document.is_file(), '분야별 안내가 필요하다.')
        text = document.read_text(encoding='utf-8')
        routes = {
            'task-excel': 'anthropic-skills/README.md#anthropic-xlsx',
            'task-ppt': 'office-design-tools/README.md#ppt-master',
            'task-documents': 'kordoc/README.md#kordoc',
            'task-visual-design': 'anthropic-skills/README.md#anthropic-canvas-design',
            'task-web-ui': 'figma/README.md#figma-generate-design',
            'task-research': '_personal/README.md#deep-research',
            'task-development': 'superpowers/README.md#writing-plans',
            'task-debug-review': 'superpowers/README.md#systematic-debugging',
            'task-ai-training': 'huggingface-skills/README.md#huggingface-llm-trainer',
            'task-agent-integration': '../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md',
            'task-environment': '_personal/README.md#handover',
            'task-deployment': '_disabled/railway/README.md#use-railway',
        }
        self.assertEqual({a for a in anchor_ids(text) if a.startswith('task-')}, set(routes))
        catalog = markdown_links((ROOT / 'Skill/CATALOG.md').read_text(encoding='utf-8'))
        allowed = set(catalog) | {'README.md', 'CATALOG.md', '../Owned-Skills/README.md'}
        allowed.update('../' + p.relative_to(ROOT).as_posix()
                       for p in (ROOT / 'Owned-Skills').glob('*/SKILL.md'))
        allowed.update('#' + anchor for anchor in routes)
        self.assertEqual(set(markdown_links(text)) - allowed, set())
        self.assertEqual(link_errors(ROOT, Path('Skill/BY-TASK.md'), text), [])
        for anchor, target in routes.items():
            with self.subTest(anchor=anchor):
                self.assertIn('#' + anchor, markdown_links(text))
                section = text.split('<a id="' + anchor + '"></a>', 1)[1].split('<a id="task-', 1)[0]
                self.assertIn(target, markdown_links(section))

    def test_task_navigation_entry_points(self):
        for source, target in {
            'README.md': 'Skill/BY-TASK.md',
            'README.en.md': 'Skill/BY-TASK.md',
            'Skill/README.md': 'BY-TASK.md',
            'Skill/CATALOG.md': 'BY-TASK.md',
        }.items():
            with self.subTest(source=source):
                text = (ROOT / source).read_text(encoding='utf-8')
                self.assertIn(target, markdown_links(text))

    def test_task_navigation_preserves_shared_tools_and_call_boundaries(self):
        document = ROOT / 'Skill/BY-TASK.md'
        self.assertTrue(document.is_file(), '분야별 안내가 필요하다.')
        text = document.read_text(encoding='utf-8')
        for anchor in ('task-excel', 'task-ppt', 'task-documents'):
            section = text.split('<a id="' + anchor + '"></a>', 1)[1].split('<a id="task-', 1)[0]
            self.assertIn('office-design-tools/README.md#officecli', markdown_links(section))
        explicit = ('anthropic-xlsx', 'anthropic-pptx', 'anthropic-docx', 'anthropic-pdf',
                    'ppt-master', 'officecli', 'huashu-design')
        for name in explicit:
            rows = [line for line in text.splitlines()
                    if line.startswith('|') and '#' + name + ')' in line]
            self.assertTrue(rows, name)
            self.assertTrue(all('명시 호출' in row for row in rows), name)
        deployment = text.split('<a id="task-deployment"></a>', 1)[1]
        self.assertIn('작성 당시 비활성', deployment)

    def test_catalog_layout(self):
        actual = {p.parent.relative_to(ROOT / 'Skill').as_posix()
                  for p in (ROOT / 'Skill').rglob('README.md') if p.parent != ROOT / 'Skill'}
        self.assertEqual(actual, set(GROUPS))
        expected_links = set()
        for group, count in GROUPS.items():
            document = ROOT / 'Skill' / group / 'README.md'
            sections = catalog_sections(document.read_text(encoding='utf-8'))
            self.assertEqual(len(sections), count, group)
            expected_links.update(group + '/README.md#' + name for name in sections)
            self.assertEqual(list(document.parent.glob('*.md')), [document])
        links = [target for target in markdown_links((ROOT / 'Skill/CATALOG.md').read_text(encoding='utf-8'))
                 if 'README.md#' in target]
        self.assertEqual(len(links), 144)
        self.assertEqual(set(links), expected_links)

    def test_catalog_boundaries_ignore_code_and_reject_duplicates(self):
        text = '## first\n```md\n## fake\n```\n## second\nbody\n'
        self.assertEqual(set(catalog_sections(text)), {'first', 'second'})
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            catalog_sections('## first\na\n## first\nb\n')
        with self.assertRaisesRegex(ValueError, 'Unclosed'):
            catalog_sections('## first\n```python\nprint(1)')

    def test_history_layout(self):
        directory = ROOT / 'docs/history'
        self.assertEqual({p.stem for p in directory.glob('*.md') if p.name != 'README.md'}, set(HISTORY))
        sources = []
        for name, count in HISTORY.items():
            text = (directory / (name + '.md')).read_text(encoding='utf-8')
            originals = re.findall(r'^원본 경로: `(docs/[^\n`]+\.md)`', text, re.M)
            self.assertEqual(len(originals), count, name)
            sources.extend(originals)
        self.assertEqual(len(sources), 54)
        self.assertEqual(len(set(sources)), 54)
        self.assertTrue((directory / 'README.md').is_file())

    def test_repository_links(self):
        errors = []
        for document in ROOT.rglob('*.md'):
            if '.git' in document.parts or '.superpowers' in document.parts:
                continue
            relative = document.relative_to(ROOT)
            text = document.read_text(encoding='utf-8')
            anchor_ids(text)
            errors.extend((relative.as_posix(), target) for target in link_errors(ROOT, relative, text))
        self.assertEqual(errors, [])

    def test_setup_selection_policy_precedes_cli_commands(self):
        text = (ROOT / 'GETTING_STARTED.md').read_text(encoding='utf-8')
        selection = text.split('### 4.1 Windows Codex 환경 세팅', 1)[1].split('#### CLI 준비.', 1)[0]
        for rule in ('사용자가 Codex 또는 Claude Code를 명시', '신뢰할 수 있는 현재 세션',
                     '모델 이름이나 설치된 CLI 목록', '한 번 질문', '결정 전에는 설치·설정을 변경하지 않는다'):
            self.assertIn(rule, selection)

    def test_inline_anchor_example_cannot_satisfy_real_fragment(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'target.md').write_text('`<a id="fake"></a>`\n', encoding='utf-8')
            self.assertEqual(link_errors(root, Path('source.md'), '[bad](target.md#fake)'),
                             ['target.md#fake'])

    def test_daily_work_report_evidence_is_archived(self):
        text = (ROOT / 'docs/history/2026-10-15-portable-skill-workflows.md').read_text(encoding='utf-8')
        self.assertIn('daily-work-report-verification', anchor_ids(text))
        for evidence in ('15/15', '13/15', '배치 시뮬레이션', '12줄'):
            self.assertIn(evidence, text)

    def test_link_checker_handles_fragments_references_and_examples(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / 'target.md').write_text('# Target\n<a id="stable"></a>\n## Repeated\n## Repeated\n', encoding='utf-8')
            source = Path('source.md')
            good = '[one](target.md#stable)\n[two][id]\n[id]: target.md#repeated-1\n'
            good += '`[ignored](missing.md)`\n```md\n[ignored](missing.md)\n```\n'
            self.assertEqual(link_errors(root, source, good), [])
            self.assertEqual(link_errors(root, source, '[bad](target.md#absent)'), ['target.md#absent'])
            self.assertEqual(link_errors(root, source, '[bad](missing.md)'), ['missing.md'])
            with self.assertRaisesRegex(ValueError, 'Duplicate'):
                anchor_ids('<a id="duplicate"></a>\n<a id="duplicate"></a>\n')
            installed = root / 'README.md'
            installed.write_text('# Installed\n', encoding='utf-8')
            self.assertEqual(link_errors(root, Path('codex-global-AGENTS.md'),
                                         '[global](Agent-Instructions/README.md#installed)'), [])
            self.assertEqual(link_errors(root, Path('ordinary.md'),
                                         '[bad](Agent-Instructions/README.md)'), ['Agent-Instructions/README.md'])


if __name__ == '__main__':
    unittest.main()
