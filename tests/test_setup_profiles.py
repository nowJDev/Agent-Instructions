# 사용자 지정 설정 홈과 CLI 경로 및 다운로드 실패의 보존 계약을 검증한다.
import base64
import json
import os
import re
import subprocess
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

import test_review_regressions as fixtures

ROOT = Path(__file__).resolve().parents[1]


def blocks(name, language):
    return re.findall(r'```' + language + r'\n(.*?)```',
                      (ROOT / name).read_text(encoding='utf-8'), re.S)


class SetupProfileTests(unittest.TestCase):
    def test_settings_merge_uses_active_config_home(self):
        case = fixtures.SetupExampleTests()
        case.setUp()
        self.addCleanup(case.doCleanups)
        custom = Path(case.temp.name) / 'custom-profile'
        custom.mkdir()
        active = custom / 'settings.json'
        active.write_text('{"custom":"active","language":"english"}', encoding='utf-8')
        case.target.write_text('{"custom":"default"}', encoding='utf-8')
        dotfiles = Path(case.temp.name) / 'dotfiles'
        dotfiles.mkdir()
        (dotfiles / 'settings.json').write_text('{}', encoding='utf-8')
        namespace = {}
        previous_cwd = Path.cwd()
        try:
            os.chdir(case.temp.name)
            with patch.object(Path, 'home', return_value=Path(case.temp.name)), \
                    patch.dict(os.environ, {'CLAUDE_CONFIG_DIR': str(custom)}), \
                    patch('builtins.input', return_value='6'):
                exec(compile(case.load_code, '<load settings>', 'exec'), namespace)
                exec(compile(case.code, '<merge settings>', 'exec'), namespace)
        finally:
            os.chdir(previous_cwd)
        self.assertEqual(json.loads(active.read_text(encoding='utf-8')),
                         {'custom': 'active', 'language': 'korean'})
        self.assertEqual(case.target.read_text(encoding='utf-8'), '{"custom":"default"}')

    def test_backup_uses_active_config_home(self):
        case = fixtures.BackupTests()
        case.setUp()
        self.addCleanup(case.doCleanups)
        custom = Path(case.temp.name) / 'custom-profile'
        custom.mkdir()
        (custom / 'CLAUDE.md').write_text('active profile', encoding='utf-8')
        result = subprocess.run([case.bash, '--noprofile', '--norc', '-c', case.code],
                                env=dict(os.environ, CLAUDE_CONFIG_DIR=custom.as_posix()),
                                capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        backups = list(custom.glob('backup_*'))
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / 'CLAUDE.md').read_text(encoding='utf-8'), 'active profile')
        self.assertFalse(list(case.claude.glob('backup_*')))


@unittest.skipUnless(os.name == 'nt', 'Windows CMD 실행 계약이다.')
class WindowsCliTests(unittest.TestCase):
    def run_ps(self, code, env):
        encoded = base64.b64encode(code.encode('utf-16le')).decode('ascii')
        return subprocess.run(['powershell', '-NoProfile', '-NonInteractive', '-EncodedCommand', encoded],
                              env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')

    def test_percent_cli_source_stops_before_execution(self):
        version_blocks = [code for name in ('GETTING_STARTED.md', 'references/windows-cli-shortcut.md')
                          for code in blocks(name, 'powershell') if 'chcp 65001' in code]
        self.assertEqual(len(version_blocks), 3)
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            literal = base / '%AGENT_REVIEW_SEGMENT%'
            expanded = base / 'expanded'
            literal.mkdir()
            expanded.mkdir()
            marker = base / 'executed.txt'
            for directory in (literal, expanded):
                (directory / 'codex.cmd').write_text('@echo executed>"' + str(marker) + '"\n@exit /b 0\n')
            env = dict(os.environ, USERPROFILE=temporary, AGENT_REVIEW_SEGMENT='expanded')
            prefix = ('[Console]::OutputEncoding = [Text.Encoding]::UTF8\n'
                      'function Get-Command { param($Name, $CommandType, $ErrorAction)\n'
                      "if ($Name -ne 'wt.exe') { [pscustomobject]@{Source='" +
                      str(literal / 'codex.cmd').replace("'", "''") + "'} } }\n")
            for code in version_blocks:
                with self.subTest(block=code[:80]):
                    marker.unlink(missing_ok=True)
                    code = code.split('$shell =')[0]
                    code = code.replace("[Environment]::GetFolderPath('DesktopDirectory')", '$env:USERPROFILE')
                    result = self.run_ps(prefix + code, env)
                    self.assertFalse(marker.exists(), '확인된 Source와 다른 CLI가 실행됐다.')
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn('%', result.stderr)

    def test_icon_profiles_follow_selected_and_default_client_home(self):
        code = blocks('references/windows-cli-shortcut.md', 'powershell')[1]
        code = code.split('$wtCommand =')[0]
        # Desktop 조회는 읽기만 수행하며 이 부분의 폴더 검사만 fixture로 대체한다.
        code = code.replace("[Environment]::GetFolderPath('DesktopDirectory')", '$env:USERPROFILE')
        with tempfile.TemporaryDirectory() as temporary:
            for client, variable in (('codex', 'CODEX_HOME'), ('claude-code', 'CLAUDE_CONFIG_DIR')):
                for custom in (False, True):
                    with self.subTest(client=client, custom=custom):
                        profile = Path(temporary) / (client if custom else '.codex' if client == 'codex' else '.claude')
                        env = dict(os.environ, USERPROFILE=temporary, CODEX_HOME='', CLAUDE_CONFIG_DIR='')
                        env[variable] = str(profile) if custom else ''
                        result = self.run_ps(code.replace("$client = 'codex'", "$client = '" + client + "'") +
                                             '\n[Console]::Write($iconTarget)', env)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertEqual(Path(result.stdout), profile / 'assets/icons' /
                                         (client + '-official.ico'))

    def test_version_invocation_disables_delayed_expansion(self):
        code = next(code for code in blocks('GETTING_STARTED.md', 'powershell') if 'chcp 65001' in code)
        invocation = next(line for line in code.splitlines() if '& $env:ComSpec' in line)
        with tempfile.TemporaryDirectory() as temporary:
            cli = Path(temporary) / 'cli!AGENT_REVIEW_SEGMENT!.cmd'
            cli.write_text('@echo exact-source\n@exit /b 0\n')
            env = dict(os.environ, AGENT_REVIEW_SEGMENT='expanded')
            source = str(cli).replace("'", "''")
            prefix = "$cliCommand = [pscustomobject]@{Source='" + source + "'}\n"
            # 부모가 /v:on이어도 생성한 자식 CMD는 자체 /v:off를 사용해야 한다.
            invocation = invocation.replace('/d /v:off /c', '/d /v:on /v:off /c').replace('/d /c', '/d /v:on /c')
            result = self.run_ps(prefix + invocation, env)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('exact-source', result.stdout)

    def test_shortcuts_create_and_verify_for_both_clients_and_shells(self):
        generation, verification = blocks('references/windows-cli-shortcut.md', 'powershell')[1:3]
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            cli = base / 'cli!AGENT_REVIEW_SEGMENT!.cmd'
            cli.write_text('@echo fixture-version\n@exit /b 0\n')
            for client in ('codex', 'claude-code'):
                profile = base / client
                icons = profile / 'assets/icons'
                icons.mkdir(parents=True)
                (icons / (client + '-official.ico')).write_bytes(b'icon fixture')
                for terminal in (False, True):
                    with self.subTest(client=client, terminal=terminal):
                        env = dict(os.environ, USERPROFILE=temporary, CODEX_HOME=str(profile),
                                   CLAUDE_CONFIG_DIR=str(profile), AGENT_REVIEW_SEGMENT='expanded')
                        prefix = ('function Get-Command { param($Name, $CommandType, $ErrorAction)\n'
                                  "if ($Name -eq 'wt.exe') { " +
                                  ('[pscustomobject]@{Source=$env:ComSpec}' if terminal else '') +
                                  " } else { [pscustomobject]@{Source='" + str(cli).replace("'", "''") + "'} } }\n")
                        script = generation + '\n' + verification
                        script = script.replace("$client = 'codex'", "$client = '" + client + "'")
                        script = script.replace("$workingDir = ''", '$workingDir = $env:USERPROFILE')
                        script = script.replace("[Environment]::GetFolderPath('DesktopDirectory')", '$env:USERPROFILE')
                        result = self.run_ps(prefix + script, env)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertIn('/v:off', result.stdout)
                        shortcut = base / ('Codex.lnk' if client == 'codex' else 'Claude Code.lnk')
                        self.assertTrue(shortcut.is_file())


class JqDownloadTests(unittest.TestCase):
    def test_download_verifies_success_and_preserves_existing_binary_on_failure(self):
        case = fixtures.BackupTests()
        case.setUp()
        self.addCleanup(case.doCleanups)

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(status)
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *args):
                pass

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for status, body, success in ((404, b'Not Found', False), (200, b'Invalid executable', False),
                                          (200, b'#!/bin/sh\nprintf "jq-fixture\\n"\n', True)):
                with self.subTest(status=status, success=success), tempfile.TemporaryDirectory() as temporary:
                    target = Path(temporary) / 'bin/jq.exe'
                    target.parent.mkdir()
                    target.write_bytes(b'existing binary')
                    code = next(code for code in blocks('references/claude-code-cli-setup.md', 'bash')
                                if 'jq-windows-amd64.exe' in code)
                    code = code.split('# Linux')[0]
                    code = code.replace('~/bin', '"' + target.parent.as_posix() + '"')
                    code = code.replace('$HOME', Path(temporary).as_posix())
                    code = re.sub(r'https://github.com/\S+jq-windows-amd64.exe',
                                  f'http://127.0.0.1:{server.server_port}/jq.exe', code)
                    result = subprocess.run([case.bash, '--noprofile', '--norc', '-c', code],
                                            capture_output=True, text=True, encoding='utf-8')
                    self.assertEqual(result.returncode == 0, success, result.stderr)
                    self.assertEqual(target.read_bytes(), body if success else b'existing binary')
                    self.assertEqual(list(target.parent.iterdir()), [target])
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == '__main__':
    unittest.main()
