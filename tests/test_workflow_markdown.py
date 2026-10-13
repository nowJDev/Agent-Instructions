# 작업 문서의 Markdown 코드 예시와 실제 미완료 항목의 경계를 검증한다.
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / 'Owned-Skills/design-driven-delivery/scripts/validate_workflow.py'


class MarkdownBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        for relative in ('docs/current-state.md', 'docs/design-progress-checklist.md',
                         'docs/specs/current.md', 'docs/plans/current.md', 'docs/reviews/current.md'):
            path = self.project / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('- [x] done\n', encoding='utf-8')

    def check_document(self, content, expected):
        (self.project / 'docs/plans/current.md').write_text(content, encoding='utf-8')
        result = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(SCRIPT),
                                 '--project', str(self.project)],
                                capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        if expected:
            self.assertNotIn('Traceback', result.stderr)
            self.assertIn('ERROR', result.stderr)

    def test_indented_fence_cannot_hide_actual_work(self):
        for indentation in ('    ', '\t'):
            with self.subTest(indentation=indentation):
                self.check_document(indentation + '```\n\n- [ ] pending\n', 1)

    def test_inline_code_cannot_cross_paragraphs(self):
        self.check_document('`example\n\n- [ ] pending\n\nexample`\n', 1)

    def test_inline_code_cannot_cross_headings(self):
        self.check_document('`example\n## Verification\n[REQUIRED]\nexample`\n', 1)

    def test_inline_code_cannot_cross_list_items(self):
        for marker in ('-', '*', '+', '1.', '1)'):
            with self.subTest(marker=marker):
                self.check_document(f'{marker} `example\n{marker} [REQUIRED] example`\n', 1)

    def test_removed_fences_preserve_inline_block_boundary(self):
        self.check_document('`example\n~~~\ncode\n~~~\n[REQUIRED] example`\n', 1)

    def test_multiline_inline_code_inside_one_paragraph_is_preserved(self):
        for content in ('Example `first line\nTODO and [REQUIRED] example` done.\n',
                        '- [x] Example ``first line\n  TODO and `literal` example`` done.\n',
                        '> Example `first line\n> TODO and [REQUIRED] example` done.\n'):
            with self.subTest(content=content):
                self.check_document(content, 0)

    def test_escaped_opening_backticks_do_not_hide_placeholders(self):
        for backslashes in (1, 3):
            with self.subTest(backslashes=backslashes):
                self.check_document('\\' * backslashes + '`[REQUIRED]\\`\n', 1)

    def test_even_backslashes_allow_inline_code(self):
        for backslashes in (0, 2, 4):
            with self.subTest(backslashes=backslashes):
                self.check_document('\\' * backslashes + '`TODO`\n', 0)

    def test_backslash_inside_code_does_not_escape_closing_backtick(self):
        self.check_document('`TODO\\` done.\n', 0)

    def test_escaped_backtick_before_real_inline_code_is_literal(self):
        self.check_document('\\`literal `TODO` done.\n', 0)

    def test_quoted_fences_ignore_examples(self):
        for opening, closing in (('```markdown', '```'), ('```markdown', '````'),
                                 ('~~~markdown', '~~~'), ('~~~~markdown', '~~~~~')):
            with self.subTest(opening=opening, closing=closing):
                self.check_document(f'> {opening}\n> TODO\n>\n> - [ ] example\n> {closing}\n- [x] done\n', 0)

    def test_unclosed_quoted_fence_ends_at_container_exit(self):
        for pending in ('- [ ] pending', '[REQUIRED]'):
            with self.subTest(pending=pending):
                self.check_document(f'> ~~~markdown\n> TODO example\n{pending}\n', 1)

    def test_nested_quote_fence_ends_when_quote_depth_decreases(self):
        for pending in ('- [ ] pending', '[REQUIRED]'):
            with self.subTest(pending=pending):
                self.check_document(f'> > ~~~markdown\n> > TODO example\n> {pending}\n', 1)

    def test_quoted_fence_ignores_short_or_mismatched_closing(self):
        for wrong_closing in ('~~~', '```', '```` trailing'):
            with self.subTest(wrong_closing=wrong_closing):
                self.check_document(f'> ````markdown\n> {wrong_closing}\n> TODO example\n> `````\n- [x] done\n', 0)

    def test_list_continuation_fences_ignore_examples(self):
        for content in ('- [x] done\n\n    ~~~markdown\n    TODO example\n    ~~~\n',
                        '1. done\n\n   ```markdown\n   TODO example\n   ```\n',
                        '> - [x] done\n>\n>     ~~~markdown\n>     TODO example\n>     ~~~\n'):
            with self.subTest(content=content):
                self.check_document(content, 0)

    def test_unclosed_list_fence_ends_at_next_list_item(self):
        self.check_document('- [x] done\n\n    ~~~markdown\n    TODO example\n- [ ] pending\n', 1)

    def test_fence_in_quote_inside_list_ignores_examples(self):
        for content in ('- > ~~~markdown\n  > TODO example\n  > ~~~\n',
                        '- > > ```markdown\n  > > TODO example\n  > > ````\n',
                        '> - > ~~~markdown\n>   > TODO example\n>   > ~~~\n'):
            with self.subTest(content=content):
                self.check_document(content, 0)

    def test_fence_in_list_quote_does_not_hide_work_after_close(self):
        for pending in ('- [ ] pending', '[REQUIRED]'):
            with self.subTest(pending=pending):
                self.check_document(f'- > ~~~markdown\n  > ordinary example\n  > ~~~\n  > {pending}\n', 1)

    def test_unclosed_fence_in_list_quote_ends_at_container_exit(self):
        for content in ('- > ~~~markdown\n  > ordinary example\n- [ ] pending\n',
                        '- > ~~~markdown\n  > ordinary example\n  [REQUIRED]\n',
                        '- > > ~~~markdown\n  > > ordinary example\n  > - [ ] pending\n'):
            with self.subTest(content=content):
                self.check_document(content, 1)


if __name__ == '__main__':
    unittest.main()
