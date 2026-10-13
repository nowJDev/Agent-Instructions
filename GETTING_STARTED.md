<!-- 이 문서는 Agent-Instructions 저장소를 처음 적용하는 절차를 안내한다. -->
# Getting Started

이 저장소는 설치 프로그램이 아니라 AI 에이전트가 읽고 따를 운영 지침이다. 링크만 전달해도 어느 정도 적용할 수 있지만, AI별로 웹 접근·파일 읽기·MCP 지원 범위가 다르므로 아래 순서로 안내하면 가장 안정적이다.

## 1. AI에게 바로 줄 프롬프트

```text
이 저장소를 읽고 내 작업 지침으로 적용해줘.
먼저 README.md를 읽고, 그 다음 AGENTS.md와 PORTABILITY.md를 읽어.
Claude 전용 기능은 네 환경의 동등 기능으로 번역하고, 없는 기능은 건너뛰어.
이 저장소는 토큰이나 개인 설정 파일을 포함하지 않는 공개용 운영 지침 카탈로그야.
https://github.com/nowJDev/Agent-Instructions
```

AI가 GitHub 링크를 직접 열 수 없다면 저장소를 내려받은 뒤, 루트의 `README.md`, `AGENTS.md`, `PORTABILITY.md` 내용을 순서대로 제공한다.

Windows에서 현재 클라이언트의 최소 CLI 환경을 세팅하려면 다음 공통 프롬프트를 전달한다.

```text
이거대로 세팅해줘.
https://github.com/nowJDev/Agent-Instructions
```

단순 "지침 적용"은 규칙을 읽고 따르는 의미다. "이거대로 세팅해줘"는 §4.1의 CLI 준비·전역 기본 지침·공식 아이콘 바로가기·실행 확인을 요청한다. 사용자가 Codex 또는 Claude Code를 명시하면 그 대상을 우선한다. 미지정이면 신뢰할 수 있는 현재 세션의 실제 클라이언트 정보를 사용한다. 모델 이름이나 설치된 CLI 목록으로 추정하지 않는다. 판별할 수 없으면 대상만 한 번 질문하고 결정 전에는 설치·설정을 변경하지 않는다. 두 CLI가 함께 설치돼 있어도 선택한 하나만 처리한다.

## 2. 적용 순서

1. `README.md`를 읽어 저장소 구조와 의사결정 지도를 파악한다.
2. `AGENTS.md`를 현재 세션의 행동 규칙으로 적용한다.
3. Claude Code가 아닌 환경이라면 `PORTABILITY.md`를 읽고 Claude 전용 기능을 번역하거나 제외한다.
4. 작업 중 특정 스킬이나 MCP가 필요하면 `Skill/README.md`와 `MCP/README.md`에서 해당 문서를 찾아 읽는다.
5. 실제 토큰, 인증 헤더, 개인 설정 파일은 각 사용자 환경에서만 설정하고 저장소에는 넣지 않는다.

## 3. AI별 사용법

### Claude Code

- `README.md`와 `AGENTS.md`를 프로젝트 지침으로 읽게 한다.
- 타사 Skill과 MCP는 이 저장소에서 자동 설치되지 않는다. 필요한 항목은 각 원본 플러그인이나 MCP 서버 문서를 기준으로 별도 설치한다.
- 자체 제작 Skill은 `Owned-Skills/` 패키지를 Claude Code가 사용하는 사용자 Skill 경로에 복사할 수 있다.
- Claude 전용 규칙은 그대로 적용할 수 있지만, 사용자 환경에 없는 MCP나 플러그인은 건너뛴다.

### Codex

- `AGENTS.md`의 행동 규칙은 그대로 적용한다.
- Claude 전용 도구명은 Codex의 파일 읽기, 검색, 셸, MCP 도구로 번역한다.
- `PORTABILITY.md`의 대체 표를 먼저 확인한다.
- `design-driven-delivery`를 쓰려면 `Owned-Skills/design-driven-delivery`를 `~/.agents/skills/design-driven-delivery`에 복사하고 새 세션을 시작한다.

### Cursor, Gemini, Copilot 등

- Agent Skills를 직접 지원하지 않으면 `Skill/` 문서는 자동 트리거가 아니라 참조 문서로 사용한다.
- MCP를 지원하는 클라이언트는 `PORTABILITY.md`의 클라이언트별 예시를 따른다. VS Code `.vscode/mcp.json`은 `servers`, Cursor `.cursor/mcp.json`은 `mcpServers`를 사용한다.
- OAuth나 토큰이 필요한 MCP는 각 사용자 계정으로 직접 인증한다.

## 4. Codex에서 헷갈리기 쉬운 부분

Codex CLI는 `AGENTS.md`를 자동으로 찾지만, 모든 링크 문서를 자동으로 펼쳐 읽는 방식은 아니다. 이 절의 `~/.codex`는 기본 위치이며 `CODEX_HOME`이 지정됐으면 그 설정 홈에서 전역 지침·override·복제본을 읽고 백업·병합한다.

- Codex는 실행 또는 TUI 세션 시작 시점에 `~/.codex/AGENTS.override.md`가 있으면 그것을, 없으면 `~/.codex/AGENTS.md`를 전역 지침으로 읽는다.
- 프로젝트에서는 Git 루트부터 현재 작업 디렉터리까지 `AGENTS.override.md`, `AGENTS.md`, 설정된 fallback 파일을 순서대로 찾고, 디렉터리마다 최대 1개만 포함한다.
- 이 instruction chain은 실행 시작 시 구성된다. 전역 지침이나 복제 문서를 고친 뒤에는 새 Codex 세션을 시작해야 반영이 확실하다.
- `AGENTS.md` 안의 `README.md를 읽어라`, `rules/01을 보라` 같은 문구는 행동 지시다. 해당 파일 내용이 자동으로 프롬프트에 모두 포함된다는 뜻은 아니다.
- 이 저장소의 `rules/*.md`는 운영 지침 문서다. Codex의 `~/.codex/rules/*.rules`는 명령 승인 정책 파일이며, 둘은 다른 기능이다.
- `~/.codex/Agent-Instructions`처럼 전역에 복제해서 쓰는 경우, GitHub 저장소를 업데이트해도 로컬 복제본은 자동 갱신되지 않는다. 복제본을 다시 동기화하거나 `git pull` 가능한 위치로 관리해야 한다.
- 더 강하게 동작시키려면 핵심 규칙을 링크된 `rules/*.md`에만 두지 말고 `AGENTS.md` 본문에 직접 둔다. 이 저장소는 검증·보안·파일 읽기·중단 조건을 `AGENTS.md`와 `codex-global-AGENTS.md`에 중복 배치한다.
- Codex 전역에 적용할 때는 기존 `~/.codex/AGENTS.md`를 전체 읽고 백업한 뒤 사용자 고유 지침을 보존하며 `codex-global-AGENTS.md`의 기본 지침을 병합한다. 저장소 전체는 `~/.codex/Agent-Instructions`에 동기화한다. 기존 `AGENTS.override.md`가 있으면 `AGENTS.md`보다 우선하므로 새 지침이 가려질 수 있다. 임의로 삭제하지 않고 충돌을 보고한다. 변경 후에는 새 Codex 세션을 시작한다. 로딩 기준은 [공식 AGENTS.md 문서](https://developers.openai.com/codex/guides/agents-md/)를 따른다.

현재 Codex가 실제로 어떤 지침을 읽는지 확인하려면 새 세션에서 아래처럼 요청한다.

```text
현재 활성화된 instruction sources를 나열하고, 전역 AGENTS.md와 프로젝트 AGENTS.md의 핵심 규칙을 요약해줘.
링크된 README나 rules 문서를 아직 읽지 않았다면 읽었는지 여부도 구분해서 말해줘.
```

Codex CLI 명령으로는 다음 식의 확인도 가능하다.

```powershell
codex "Summarize the current instructions and list which instruction files are active."
```

### 4.1 Windows Codex 환경 세팅

이 앵커는 기존 링크를 유지한다. 공통 요청의 Codex·Claude Code 최소 세팅 모두 아래 순서를 따른다.

#### CLI 준비.

1. 선택한 CLI의 실행 파일을 확인한다. Codex는 `Get-Command codex.cmd, codex.exe -CommandType Application`, Claude Code는 `Get-Command claude.cmd, claude.exe -CommandType Application`으로 확인하고 `Source` 전체 경로를 기록한다. 전체 경로에 `%`가 있으면 CMD 재확장을 막기 위해 실행 전에 중단하고 `%`가 없는 설치 경로로 옮기는 방법을 안내한다. 아래 버전 예제로 확인해 성공하면 재사용한다. 설치된 다른 CLI는 변경하지 않는다.
2. 없으면 선택한 CLI만 현재 공식 설치 절차로 설치한다. 아래는 Windows 공식 PowerShell 명령이다. 설치 명령의 성공만으로 완료하지 않으며 다음 단계의 전체 경로·버전 검사를 수행한다.

Codex는 [공식 CLI 설치 안내](https://learn.chatgpt.com/docs/codex/cli)의 새 PowerShell 설치 절차를 따른다.

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
if ($LASTEXITCODE -ne 0) { throw 'Codex 설치 명령이 실패했습니다.' }
```

이 `ByPass`는 공식 설치 자식 프로세스의 실행 정책 옵션이며 전역 권한 변경이나 CLI의 권한 우회 옵션이 아니다. 이미 Node.js/npm을 사용하는 환경은 공식 대안인 `npm install -g @openai/codex`를 선택할 수 있다. 두 설치 방법을 동시에 적용하지 않는다.

Claude Code는 [공식 설치 안내](https://code.claude.com/docs/en/setup)의 사용자 영역 설치를 따른다. 관리자 권한이나 Git for Windows를 최소 세팅의 필수 조건으로 추가하지 않는다. 현재 공식 안내는 Git Bash가 없는 Windows에서도 PowerShell 도구를 지원한다.

```powershell
$ErrorActionPreference = 'Stop'
irm https://claude.ai/install.ps1 | iex
```

3. 설치 후 새 터미널을 열어 PATH가 반영됐는지 확인한다. 선택한 실행 파일의 `Source` 전체 경로로 `--version`을 다시 실행한다. 예를 들어 아래에서 `$client`를 선택한 값으로 지정한다. 명령이 계속 없거나 종료 코드가 실패하면 미완료다.

```powershell
$ErrorActionPreference = 'Stop'
$client = 'codex' # Claude Code를 선택했으면 'claude-code'로 바꾼다.
$commandNames = switch ($client) {
    'codex' { 'codex.cmd'; 'codex.exe' }
    'claude-code' { 'claude.cmd'; 'claude.exe' }
    default { throw 'client는 codex 또는 claude-code여야 합니다.' }
}
$cliCommand = Get-Command $commandNames -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $cliCommand -or -not (Test-Path -LiteralPath $cliCommand.Source -PathType Leaf)) {
    throw '선택한 CLI가 없습니다. 새 터미널과 PATH를 확인하세요.'
}
if ($cliCommand.Source.Contains('%')) {
    throw 'CLI 경로의 %는 CMD에서 재확장됩니다. %가 없는 설치 경로로 옮긴 뒤 다시 실행하세요.'
}
$cliCommand.Source
& $env:ComSpec /d /v:off /c ('chcp 65001 > nul & "{0}" --version' -f $cliCommand.Source)
if ($LASTEXITCODE -ne 0) { throw 'CLI 전체 경로의 버전 실행이 실패했습니다.' }
```

#### 전역 기본 지침과 바로가기.

선택한 클라이언트의 실제 설정 홈을 먼저 결정한다. 아래 `$client`는 선택한 값으로 입력하며 설정 홈은 백업·지침·복제본·아이콘·확장 설정에 공통으로 사용한다. 환경변수는 세팅과 새 CLI 실행에서 동일해야 한다. 기본 홈으로 임의 대체하거나 환경변수를 지우지 않는다.

```powershell
$client = 'codex' # Claude Code를 선택했으면 'claude-code'로 바꾼다.
$clientHome = switch ($client) {
    'codex' { if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' } }
    'claude-code' { if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $env:USERPROFILE '.claude' } }
    default { throw 'client는 codex 또는 claude-code여야 합니다.' }
}
$clientHome = [IO.Path]::GetFullPath($clientHome)
$clientHome
```

`CODEX_HOME`은 [공식 Codex 지침 로딩 안내](https://learn.chatgpt.com/docs/agent-configuration/agents-md), `CLAUDE_CONFIG_DIR`은 [공식 Claude 설정 디렉터리 안내](https://code.claude.com/docs/en/claude-directory)를 따른다.

| 선택한 클라이언트 | 전역 기본 지침 | Windows 결과 |
|---|---|---|
| Codex | 기존 `$clientHome/AGENTS.md`에 `codex-global-AGENTS.md` 병합, 복제본 `$clientHome/Agent-Instructions` | `Codex.lnk`, `$clientHome/assets/icons/codex-official.ico` |
| Claude Code | 기존 `$clientHome/CLAUDE.md`에 `@Agent-Instructions/AGENTS.md` import 추가, 복제본 `$clientHome/Agent-Instructions` | `Claude Code.lnk`, `$clientHome/assets/icons/claude-code-official.ico` |

1. 기존 전역 지침과 복제본을 전체 읽고 변경 전에 백업한다. 사용자 고유 지침을 보존하고 충돌·중복을 확인한다. Codex는 §4의 보존 병합과 override 확인을 따른다.
2. Claude Code는 이 저장소를 `$clientHome/Agent-Instructions`에 배치·동기화하고 기존 `$clientHome/CLAUDE.md`의 내용을 유지하며 별도 줄에 `@Agent-Instructions/AGENTS.md`를 추가한다. 이미 같은 import가 있으면 중복 추가하지 않는다. 외부 dotfiles의 `CLAUDE.md`로 덮어쓰지 않는다. 상대 import는 작업 디렉터리가 아니라 **import를 선언한 파일의 위치** 기준이므로 여기서는 실제 설정 홈의 `CLAUDE.md`를 기준으로 해석된다. [공식 memory 문서](https://code.claude.com/docs/en/memory)를 따른다.
3. [공통 Windows 바로가기 절차](references/windows-cli-shortcut.md)에서 선택한 `$client`만 지정해 공식 아이콘과 실제 바탕화면의 `.lnk`를 준비한다. 기존 바로가기 속성을 먼저 확인하고 `.bat`는 보존한다. 사용자 지정 작업 폴더를 우선하고, 미지정이면 실제 바탕화면 아래 `Agent`를 만든다. Windows Terminal이 있으면 재사용하고 없으면 기본 CMD를 쓴다. Terminal 설치를 추가하지 않는다.
4. 독립 속성 검증 후 바로가기를 실제로 열어 선택한 CLI, UTF-8과 작업 폴더를 확인한다. 새 Codex 세션은 활성 instruction sources를 확인하고, 새 Claude Code 세션은 `/context`의 **Memory files**에서 전역 `CLAUDE.md`와 imported `Agent-Instructions/AGENTS.md`가 실제 로드됐는지 확인한다. 누락되면 지침 적용은 미완료다.
5. CLI가 인증을 요구하면 사용자가 직접 로그인하도록 공식 [Codex 인증 안내](https://developers.openai.com/codex/auth/) 또는 [Claude Code 로그인 안내](https://code.claude.com/docs/en/setup)를 안내한다. 인증 자료를 대신 수집하거나 저장소에 넣지 않는다. 로그인 대기, 공식 아이콘 준비 실패, 바로가기·CLI 실행 실패 또는 지침 로드 미확인은 각각 미완료로 보고한다.
6. 선택한 클라이언트, CLI 전체 경로·버전, 전역 지침·복제본·바로가기 위치, 작업 폴더, 아이콘 공식 출처, 실행·지침 로드·인증 결과와 남은 항목을 보고한다.

기본 범위는 CLI 준비·전역 기본 지침·공식 아이콘 바탕화면 바로가기·실행 확인과 필요한 사용자 로그인 안내다. 스킬·MCP·플러그인·hooks·테마·상태줄·권한 변경·bypass 옵션은 자동 포함하지 않는다. 별도 확장 요청이 있을 때만 [Claude Code 확장 가이드](references/claude-code-cli-setup.md)나 각 도구 원본 안내를 사용한다. 미지원 OS·클라이언트는 이 Windows 예제를 임의 적용하지 않고 지원 범위와 미완료 사유를 보고한다.

## 5. 이 저장소가 하는 것과 하지 않는 것

하는 것.

- AI 에이전트의 작업 순서, 검증 규칙, 도구 선택 기준을 문서화한다.
- 스킬과 MCP의 용도, 트리거, 연결 정보를 카탈로그로 제공한다.
- Claude 전용 개념을 다른 AI 환경으로 옮기는 기준을 제공한다.

하지 않는 것.

- 토큰, `.env`, 개인 설정 파일을 제공하지 않는다.
- MCP 서버나 타사 Agent Skill 실물을 재배포하지 않는다. 직접 작성한 Skill 원본만 `Owned-Skills/`에 둔다.
- 모든 AI 환경에서 자동 설치를 보장하지 않는다.

## 6. 공개 저장소 체크리스트

- [ ] `SECURITY.md`의 금지 항목을 확인했다.
- [ ] 실제 토큰·인증 헤더·개인 설정 파일을 커밋하지 않았다.
- [ ] 개인 프로젝트 지식이나 내부망 주소를 포함하지 않았다.
- [ ] 다른 AI에서 사용할 때 `PORTABILITY.md`의 번역 기준을 안내했다.
