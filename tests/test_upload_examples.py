# 문서의 업로드 예제가 비공개 확인과 승인된 파일 범위를 지키는지 검증한다.
import ast
import os
import re
import sys
import tempfile
import unittest
from pathlib import Path
from types import ModuleType, SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / 'Skill/huggingface-skills'


class UploadExampleTests(unittest.TestCase):
    def upload_example(self, filename):
        text = (CATALOG / filename).read_text(encoding='utf-8')
        blocks = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
        blocks = [block for block in blocks if 'api.upload_' in block]
        self.assertEqual(len(blocks), 1, '실행 가능한 업로드 예시가 하나 있어야 합니다.')
        tree = ast.parse(blocks[0])
        start = 0
        if filename == 'huggingface-lora-space-builder.md':
            start = next(index for index, node in enumerate(tree.body)
                         if isinstance(node, ast.ImportFrom)
                         and any(name.name == 'SpaceHardware' for name in node.names))
        return compile(ast.Module(body=tree.body[start:], type_ignores=[]), filename, 'exec')

    def run_example(self, filename, privacy=True, query_error=None, folder=None):
        events = []

        def repo_info(**kwargs):
            events.append(('repo_info', kwargs))
            if query_error:
                raise query_error
            return SimpleNamespace(private=privacy)

        api = SimpleNamespace(
            create_repo=lambda **kwargs: events.append(('create_repo', kwargs)),
            repo_info=repo_info,
            upload_file=lambda **kwargs: events.append(('upload_file', kwargs)),
            upload_folder=lambda **kwargs: events.append(('upload_folder', kwargs)),
            add_space_secret=lambda **kwargs: events.append(('add_space_secret', kwargs)),
        )
        sdk = ModuleType('huggingface_hub')
        sdk.HfApi = lambda **kwargs: api
        sdk.SpaceHardware = SimpleNamespace(ZERO_A10G='zero-a10g')
        api.whoami = lambda: {'name': 'fixture'}
        namespace = dict(hf_token='fake-build-token', space_name='repo',
                         HF_TOKEN='fake-runtime-token')
        previous_directory = Path.cwd()
        try:
            if folder:
                os.chdir(folder.parent)
            with patch.dict(sys.modules, {'huggingface_hub': sdk}):
                exec(self.upload_example(filename), namespace)
        except Exception as error:
            return events, error
        finally:
            os.chdir(previous_directory)
        return events, None

    def test_public_or_unknown_repo_blocks_every_transfer(self):
        for filename in ('huggingface-datasets.md', 'huggingface-lora-space-builder.md'):
            for privacy in (False, None, 'true', 1):
                with self.subTest(filename=filename, privacy=privacy):
                    events, error = self.run_example(filename, privacy=privacy)
                    self.assertEqual([event[0] for event in events], ['create_repo', 'repo_info'])
                    self.assertIsInstance(error, RuntimeError)

    def test_visibility_query_error_blocks_every_transfer(self):
        failure = OSError('fixture query failure')
        for filename in ('huggingface-datasets.md', 'huggingface-lora-space-builder.md'):
            with self.subTest(filename=filename):
                events, error = self.run_example(filename, query_error=failure)
                self.assertEqual([event[0] for event in events], ['create_repo', 'repo_info'])
                self.assertIs(error, failure)

    def test_private_space_uploads_files_then_secret(self):
        events, error = self.run_example('huggingface-lora-space-builder.md')
        self.assertIsNone(error)
        self.assertEqual([event[0] for event in events],
                         ['create_repo', 'repo_info', 'upload_file', 'upload_file',
                          'upload_file', 'add_space_secret'])
        self.assertEqual(events[1][1]['repo_type'], 'space')

    def test_private_dataset_sends_only_prepared_project_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            prepared = root / 'approved-traces'
            prepared.mkdir()
            (prepared / 'approved-session.jsonl').write_text('{}\n', encoding='utf-8')
            other = root / 'sessions/other-project'
            other.mkdir(parents=True)
            (other / 'unapproved-session.jsonl').write_text('{}\n', encoding='utf-8')
            events, error = self.run_example('huggingface-datasets.md', folder=prepared)
            self.assertIsNone(error)
            self.assertEqual([event[0] for event in events],
                             ['create_repo', 'repo_info', 'upload_folder'])
            self.assertEqual(events[1][1]['repo_type'], 'dataset')
            sent = root / events[-1][1]['folder_path']
            self.assertEqual(sent, prepared)
            self.assertEqual([path.name for path in sent.rglob('*.jsonl')],
                             ['approved-session.jsonl'])


if __name__ == '__main__':
    unittest.main()
