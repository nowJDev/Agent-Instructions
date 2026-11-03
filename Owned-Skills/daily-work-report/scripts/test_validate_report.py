# 업무보고 검사기의 형식·인코딩·오류 경로를 검증한다.
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'validate_report.py'
FIXTURES = ROOT / 'evals' / 'fixtures'
HEADING = '1.2 AI 안전관리 VR 기능 수정 (진행중, 60%, 완료예정일:10/31)'
DEFAULT = (FIXTURES / 'default-report.txt').read_text(encoding='utf-8')
CUSTOM = (FIXTURES / 'custom-report.txt').read_text(encoding='utf-8')


class ReportValidationTests(unittest.TestCase):
    def run_cli(self, text, *args):
        result = subprocess.run(
            [sys.executable, '-X', 'utf8', '-B', str(SCRIPT), '--input', '-', *args],
            input=text.encode('utf-8'), capture_output=True, timeout=10)
        result.stdout = result.stdout.decode('utf-8')
        result.stderr = result.stderr.decode('utf-8')
        return result

    def test_default_fixture_and_exact_heading(self):
        result = self.run_cli(DEFAULT, '--expected-heading', HEADING)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('PASS', result.stdout)

    def test_missing_validator_is_explicit_failure(self):
        self.assertTrue(SCRIPT.is_file(), '요구된 validate_report.py가 아직 구현되지 않음')

    def test_default_ten_and_eleven_lines(self):
        for count in (10, 11):
            with self.subTest(count=count):
                self.assertEqual(self.run_cli('\n'.join(DEFAULT.splitlines()[:count])).returncode, 0)

    def test_custom_does_not_force_default_structure(self):
        result = self.run_cli(CUSTOM, '--mode', 'custom', '--min-lines', '8', '--max-lines', '10')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_custom_unbounded_and_heading(self):
        result = self.run_cli('VTS_Unity VR\n- 요구사항 검토', '--mode', 'custom', '--expected-heading', 'VTS_Unity VR')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_heading_is_exact_not_substring(self):
        result = self.run_cli(DEFAULT.replace('60%', '70%'), '--expected-heading', HEADING)
        self.assertEqual(result.returncode, 1)
        self.assertIn('업무 헤더', result.stderr)

    def test_rejects_wrong_default_structure(self):
        variants = [DEFAULT.replace('(10/20)', '(13/40)'),
                    DEFAULT.replace('1. 주요 업무내용', '2. 주요 업무내용'),
                    DEFAULT.replace('  1.2 ', '1.2 '),
                    DEFAULT.replace('    - ', '    = ', 1),
                    DEFAULT.replace('      = ', '    - ', 1),
                    '\n'.join(DEFAULT.splitlines()[:9]),
                    DEFAULT + '      = 추가 검증\n']
        for text in variants:
            with self.subTest(text=text):
                self.assertEqual(self.run_cli(text).returncode, 1)

    def test_known_finite_endings(self):
        for ending in ('수정함', '수정했다.', '수정한다', '수정하였습니다', '검토하고 있습니다', '구현할 예정입니다', '반영했음'):
            with self.subTest(ending=ending):
                result = self.run_cli('- ' + ending, '--mode', 'custom')
                self.assertEqual(result.returncode, 1)
                self.assertIn('종결', result.stderr)

    def test_nouns_and_technical_terms_are_not_rejected(self):
        result = self.run_cli('- 통합·함수·포함 범위 검토\n- Unity XR·.vsys 연동', '--mode', 'custom')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_technical_identifiers_are_not_markdown(self):
        result = self.run_cli('- asset__revision 및 A|B 매핑 검토', '--mode', 'custom')
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_markdown_decoration_and_table_rejected(self):
        for text in ('# 업무보고', '```text\n보고\n```', '| 내용 | 결과 |', '- [x] 검증 완료', '- **검증** 완료', '> 검증 완료'):
            with self.subTest(text=text):
                self.assertEqual(self.run_cli(text, '--mode', 'custom').returncode, 1)

    def test_blank_lines_and_trailing_spaces_rejected(self):
        for text in ('', '\n' + DEFAULT, DEFAULT + '\n', DEFAULT.replace('\n', '\n\n', 1), DEFAULT.replace('수정\n', '수정 \n', 1)):
            with self.subTest(text=text):
                self.assertEqual(self.run_cli(text).returncode, 1)

    def test_zero_or_one_final_newline_and_crlf(self):
        for text in (DEFAULT.rstrip('\n'), DEFAULT.rstrip('\n') + '\n', DEFAULT.replace('\n', '\r\n')):
            with self.subTest(text=text):
                self.assertEqual(self.run_cli(text).returncode, 0)

    def test_line_limits_and_arguments(self):
        self.assertEqual(self.run_cli(CUSTOM, '--mode', 'custom', '--max-lines', '8').returncode, 1)
        for args in (('--min-lines', '12', '--max-lines', '10'), ('--min-lines', '-1'), ('--mode', 'unknown')):
            with self.subTest(args=args):
                self.assertEqual(self.run_cli(DEFAULT, *args).returncode, 2)

    def test_utf8_bom_unicode_path_read_only(self):
        with tempfile.TemporaryDirectory(prefix='업무 보고 ') as folder:
            path = Path(folder) / '한글 보고서.txt'
            path.write_bytes(b'\xef\xbb\xbf' + DEFAULT.encode('utf-8'))
            before = hashlib.sha256(path.read_bytes()).hexdigest()
            result = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(SCRIPT), '--input', str(path)], capture_output=True, text=True, encoding='utf-8', timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(before, hashlib.sha256(path.read_bytes()).hexdigest())

    def test_invalid_utf8_and_missing_input(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'bad.txt'
            path.write_bytes(b'\xff\xfe\x00')
            for target in (path, Path(folder) / 'missing.md', Path(folder)):
                with self.subTest(target=target):
                    result = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(SCRIPT), '--input', str(target)], capture_output=True, text=True, encoding='utf-8', timeout=10)
                    self.assertEqual(result.returncode, 2)
                    self.assertIn('ERROR', result.stderr)


if __name__ == '__main__':
    unittest.main()
