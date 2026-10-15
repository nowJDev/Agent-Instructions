# 자체 제작 스킬 패키지의 독립성·공개 경계·Markdown 링크를 검증한다.
import ipaddress
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ROOT / 'Owned-Skills'
EXPECTED_NEW = {
    'cancel-ralph', 'claude-api', 'claude-news', 'code-review', 'deep-research',
    'delete-session', 'feature-dev', 'fewer-permission-prompts',
    'figma-generate-project-plan', 'handover', 'help', 'init',
    'keybindings-help', 'loop', 'new-sdk-app', 'ralph-loop', 'review',
    'review-pr', 'run', 'security-review', 'simplify', 'update-config', 'verify',
}
EXISTING = {'design-driven-delivery'}
PRIVATE_PATTERNS = (
    r'(?i)[a-z]:[\\/]+Users[\\/]+(?!Public(?:[\\/]|$))[^\\/\s]+',
    r'/(?:Users|home)/[A-Za-z0-9_.-]+/',
    r'(?i)\.codex[\\/]+backups[\\/]',
    r'(?i)-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----',
    r'\b(?:sk-ant-[A-Za-z0-9_-]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{16,})\b',
    r'\bAKIA[0-9A-Z]{16}\b',
    r'\bAIza[0-9A-Za-z_-]{35}\b',
    r'(?i)\bBearer\s+[A-Za-z0-9_.-]{20,}',
)
VENDORED_PATTERNS = (
    r'(?m)^allowed-tools\s*:',
    r'(?m)^hide-from-slash-command-tool\s*:',
    r'\$\{CLAUDE_PLUGIN_ROOT\}',
    r'(?m)^\s*```!',
    r'(?im)^#\s+Ralph Loop Command\s*$',
)


def frontmatter_fields(text):
    """Accept the packages' flat string-only YAML subset without dependencies."""
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
    if not match:
        raise ValueError('Missing YAML frontmatter')
    fields = {}
    for line in match[1].splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        entry = re.fullmatch(r'([a-z][a-z0-9_-]*):[ \t]+(.+)', line)
        if not entry or entry[1] in fields:
            raise ValueError('Invalid or duplicate frontmatter field')
        key, value = entry[1], entry[2].strip()
        if value.startswith('"'):
            value = json.loads(value)
        elif (not value or re.search(r"[:\[\]{}&*!|>'\"%@`#]", value)
              or re.match(r'[-?]\s', value)
              or value.lower() in {'null', 'true', 'false', 'yes', 'no', 'on', 'off', '~'}
              or re.fullmatch(r'[-+]?\d+(?:\.\d+)?', value)):
            raise ValueError('Use a plain string or JSON-quoted string')
        if not isinstance(value, str) or not value.strip():
            raise ValueError('Frontmatter values must be nonempty strings')
        fields[key] = value
    return fields


def prose_only(markdown):
    """Remove fenced and inline code before inspecting actual Markdown links."""
    kept = []
    fence = None
    for line in markdown.splitlines():
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            kept.append('')
        elif match:
            fence = match[1]
            kept.append('')
        else:
            kept.append(line)
    text = '\n'.join(kept)
    return re.sub(r'(?<!\\)(`+)(?!`)(.*?)\1(?!`)', '', text, flags=re.S)


def markdown_links(markdown):
    text = prose_only(markdown)
    definitions = {}
    for match in re.finditer(r'(?m)^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)', text):
        definitions[' '.join(match[1].lower().split())] = match[2].strip('<>')
    text = re.sub(r'(?m)^\s{0,3}\[[^\]]+\]:.*$', '', text)
    links = [m[1].strip('<>') for m in re.finditer(
        r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["\x27][^\n]*?["\x27])?\s*\)', text)]
    for match in re.finditer(r'!?\[([^\]\n]+)\]\[([^\]\n]*)\]', text):
        label = ' '.join((match[2] or match[1]).lower().split())
        if label not in definitions:
            raise ValueError('Undefined Markdown reference: ' + label)
        links.append(definitions[label])
    for match in re.finditer(r'(?<![!\]])\[([^\]\n]+)\](?![\[(])', text):
        label = ' '.join(match[1].lower().split())
        if label in definitions:
            links.append(definitions[label])
    links.extend(m[1] for m in re.finditer(r'<(https?://[^>]+)>', text))
    return links


def public_https(target):
    parsed = urlsplit(target)
    if parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password:
        return False
    host = parsed.hostname.lower()
    if host == 'localhost' or '.' not in host or host.endswith(('.localhost', '.local', '.internal', '.test', '.invalid')):
        return False
    try:
        return ipaddress.ip_address(host).is_global
    except ValueError:
        return True


class OwnedSkillPackageTests(unittest.TestCase):
    def test_exact_new_package_set(self):
        actual = {p.name for p in PACKAGES.iterdir() if p.is_dir()} - EXISTING
        self.assertEqual(actual, EXPECTED_NEW)

    def test_frontmatter(self):
        for name in sorted(EXPECTED_NEW):
            with self.subTest(skill=name):
                text = (PACKAGES / name / 'SKILL.md').read_text(encoding='utf-8')
                fields = frontmatter_fields(text)
                self.assertEqual(fields.get('name'), name)
                self.assertRegex(name, r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
                self.assertTrue(fields.get('description', '').strip())
                self.assertLessEqual(len(fields['description']), 1024)

    def test_frontmatter_rejects_invalid_scalar_syntax(self):
        for description in ('foo: bar', 'foo:bar', '"valid" trailing',
                            "'unterminated", '[one, two]', 'true', '|'):
            with self.subTest(description=description):
                with self.assertRaises(ValueError):
                    frontmatter_fields('---\nname: sample\ndescription: ' + description + '\n---\n')
        self.assertEqual(
            frontmatter_fields('---\nname: sample\ndescription: "A quoted: description"\n---\n'),
            {'name': 'sample', 'description': 'A quoted: description'})

    def test_links_stay_in_package_or_public_https(self):
        for name in sorted(EXPECTED_NEW):
            package = (PACKAGES / name).resolve()
            for document in package.rglob('*.md'):
                with self.subTest(document=document.relative_to(ROOT)):
                    for target in markdown_links(document.read_text(encoding='utf-8')):
                        parsed = urlsplit(target)
                        if parsed.scheme or parsed.netloc:
                            self.assertTrue(public_https(target), target)
                            continue
                        self.assertNotIn('\\', parsed.path, target)
                        path = (document.parent / unquote(parsed.path)).resolve()
                        self.assertTrue(path.is_relative_to(package), target)
                        self.assertTrue(path.exists(), target)

    def test_no_private_data_or_vendored_plugin_packages(self):
        for name in sorted(EXPECTED_NEW):
            for path in (PACKAGES / name).rglob('*'):
                with self.subTest(path=path.relative_to(ROOT)):
                    self.assertNotIn(path.name.lower(), {'upstream', 'original.md', 'original-command.md'})
                    self.assertFalse(path.name.lower().startswith(('license', 'notice')), str(path))
                    if not path.is_file():
                        continue
                    text = path.read_text(encoding='utf-8')
                    for pattern in PRIVATE_PATTERNS + VENDORED_PATTERNS:
                        self.assertIsNone(re.search(pattern, text), pattern)
                    for target in re.findall(r'https?://[^\s<>\x22\x27)]+', text):
                        self.assertTrue(public_https(target), target)

    def test_markdown_code_examples_are_not_links(self):
        sample = '[real](https://example.com/doc)\n`[inline](../outside)`\n~~~md\n[fenced](../outside)\n~~~\n[ref][id]\n[id]: local.md\n'
        self.assertEqual(markdown_links(sample), ['https://example.com/doc', 'local.md'])

    def test_private_urls_are_rejected(self):
        for target in ('http://example.com', 'https://localhost/path',
                       'https://127.0.0.1/path', 'https://192.168.1.5/path',
                       'https://docs.internal/path', 'https://user:password@example.com'):
            with self.subTest(target=target):
                self.assertFalse(public_https(target))


if __name__ == '__main__':
    unittest.main()
