# 참조: Claude Code CLI 설정 설치 가이드

> "이거대로 세팅해줘"·"세팅해줘"·"설정해줘"·"설치해줘"만으로 아래 확장 설정을 적용하지 않는다. 기본 요청은 [GETTING_STARTED.md](../GETTING_STARTED.md#41-windows-codex-환경-세팅)의 선택한 CLI 준비·전역 기본 지침·공식 아이콘 바로가기·실행 확인을 따른다. Claude Code 기본 지침은 이 저장소의 `AGENTS.md`를 기존 `~/.claude/CLAUDE.md`에 import하며 외부 dotfiles로 덮어쓰지 않는다.

## 명시적 확장 요청의 범위.

아래 기존 절차는 사용자가 스킬·MCP·플러그인·hooks·테마·상태줄·권한 설정 등 **추가 환경 설정을 명시적으로 요청한 경우에만** 해당 선택 항목에 적용한다. 기본 설치에는 권한 변경과 bypass 바로가기를 자동 포함하지 않는다. 범용 규칙은 `../AGENTS.md`와 `../rules/`를 따른다. 외부 `claude-code-cli-settings` 저장소의 `dotfiles/`·`mcp-servers/`가 필요하며 이 Agent-Instructions 저장소에는 그 실물이 없다. 외부 저장소의 위치·원본·요청 항목을 확인한 뒤 진행한다.

## 저장소 구조

아래 `~/.claude`는 기본 위치다. `CLAUDE_CONFIG_DIR`이 지정돼 있으면 그 설정 홈을 백업·기본 지침 import·복제본·설정·키바인딩·스킬·에이전트의 공통 대상으로 사용한다. [공식 설정 디렉터리 안내](https://code.claude.com/docs/en/claude-directory)를 따른다. Bash 테마와 jq의 사용자 홈 파일은 별도다.

```
dotfiles/                     # 설치할 설정 파일 원본
├── CLAUDE.md                 # → ~/.claude/CLAUDE.md (글로벌 규칙)
├── settings.json             # → ~/.claude/settings.json (머지)
├── keybindings.json          # → ~/.claude/keybindings.json
├── skills/                   # → ~/.claude/skills/ (폴더째 복사)
├── agents/                   # → ~/.claude/agents/ (파일 복사)
└── bash/                     # → ~/ (홈 디렉토리에 복사)
mcp-servers/                  # MCP 서버 소스 코드
├── computer-control/server.py
└── web-fetcher/index.mjs, package.json
```

## 세팅 절차

### Step 1: 환경 확인
```bash
claude_config_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
python --version    # 3.8+ 필요
node --version      # 18+ 필요 (MCP web-fetcher 선택 시)
claude --version    # MCP 등록 시 필요
jq --version        # 상태줄에 필요 (없으면 설치)
```

### Step 2: 설치 항목 선택
전체 항목을 카테고리별로 보여주고 선택받는다. "기본/전부/추천대로" 요청이면 **추천(기본 ON)** 항목만 설치한다.

**코어 설정 (전부 추천 ON)**
| # | 항목 | 설명 |
|---|------|------|
| 1 | 글로벌 규칙 (CLAUDE.md) | 작업 프로세스 3단계, 품질·컨텍스트·Compact 규칙 |
| 2 | 안전 Hooks | rm -rf·force push·시크릿 커밋·API 키 삽입·하드코딩 절대경로 차단 |
| 3 | 한국어 상태줄 | 모델명·컨텍스트%·레이트 리밋 표시. **jq 필요**(미설치 시 자동 설치) |
| 4 | 키바인딩 | Enter=전송, Shift+Enter=줄바꿈 |
| 5 | 플러그인 활성화 | superpowers·feature-dev·firecrawl 등 30개(ON 24 + OFF 6) |
| 6 | 한국어 응답 | 응답 언어 한국어 |
| 7 | 기본 권한 규칙 | git status/diff/log 등 안전 명령 자동 허용 (19개) |

**Skills** — 8 claude-news(ON) / 9 compile-check / 10 ui-toolkit-guide / 11 profiler-analysis (9~11 Unity 전용, OFF)

**추가 기능** — 12 code-reviewer 에이전트 / 13 Bash 테마 / 14 알림 Hooks / 15 .cs 수정 알림 Hook (전부 OFF)

**도구 & 바로가기 (Windows)** — 16 Claude Code 바로가기(ON) / 17 bypass 바로가기 / 18 snap-path (OFF)

**MCP 서버 (claude CLI 필요)** — 19 computer-control(마우스/키/스크린샷) / 20 web-fetcher(HTTPS 페칭) (OFF)

### Step 3: 백업
설치 전 **반드시** 실제 Claude 설정 홈을 백업한다. 아래 블록은 독립 실행 가능하며 Step 1과 같은 홈을 사용한다.
```bash
claude_config_dir="${CLAUDE_CONFIG_DIR:-$HOME/.claude}"
selected_items="" # Step 2에서 승인한 항목 번호를 공백으로 구분해 넣는다. 테마는 13이다.
if [ -d "$claude_config_dir" ] || [[ " $selected_items " == *" 13 "* ]]; then
  backup_parent="$HOME"
  if [ -d "$claude_config_dir" ]; then backup_parent="$claude_config_dir"; fi
  backup_dir=$(mktemp -d "$backup_parent/backup_$(date +%Y%m%d_%H%M%S)_XXXXXX") || exit 1
  for backup_item in CLAUDE.md settings.json keybindings.json skills agents; do
    backup_source="$claude_config_dir/$backup_item"
    if [ -e "$backup_source" ] || [ -L "$backup_source" ]; then
      cp -R "$backup_source" "$backup_dir/" || exit 1
    fi
  done
  case " $selected_items " in
    *" 13 "*)
      mkdir "$backup_dir/home" || exit 1
      for backup_item in .bashrc .minttyrc .elephant_walk.py; do
        backup_source="$HOME/$backup_item"
        if [ -e "$backup_source" ] || [ -L "$backup_source" ]; then
          cp -R "$backup_source" "$backup_dir/home/" || exit 1
        fi
      done
      ;;
  esac
  printf '백업 위치: %s\n' "$backup_dir"
fi
```
`selected_items`에는 승인한 항목 번호만 넣는다. 테마를 선택하면 홈 파일도 `home/`에 백업하며, 설정 홈이 없어도 홈 백업을 수행한다. 해당 원본이 모두 없으면 설치 디렉터리만 생성한다: `mkdir -p "$claude_config_dir/skills" "$claude_config_dir/agents"`. 백업이 실패하면 설치를 중단하고 원인을 해결한다. 이전 백업 폴더는 복사 대상에 포함하지 않는다.

### Step 4: 설치 실행

**4-1. CLAUDE.md** — `dotfiles/CLAUDE.md → $claude_config_dir/CLAUDE.md` 단순 복사. 설치 후 사용자에게 자기 환경에 안 맞는 섹션 삭제를 안내한다(RAG 없으면 "RAG MCP" 삭제, graph-RAG-study 없으면 "글로벌 설정" 삭제, Unity 안 쓰면 "Unity" 삭제, Notion 안 쓰면 "Notion" 삭제, team-monitor 없으면 "팀 작업" 삭제).

**4-2. settings.json 머지 (항목 2~7, 14~15)** — **절대 전체 덮어쓰기 금지.** Python으로 선택된 섹션만 머지한다.

```python
import json
import os
from pathlib import Path

with Path("dotfiles/settings.json").open(encoding="utf-8") as source_file:
    source = json.load(source_file)
config_home = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude").expanduser()
target_path = config_home / "settings.json"
target = {}
if target_path.exists():
    with target_path.open(encoding="utf-8") as target_file:
        target = json.load(target_file)
selected_items = {int(item) for item in input("Step 2에서 승인한 항목 번호(공백 구분): ").split()}
if not selected_items or not selected_items <= set(range(1, 21)):
    raise ValueError("승인한 항목 번호 1~20을 입력해야 합니다.")
```

| 항목 | 머지 방법 |
|------|-----------|
| 안전 Hooks (2) | `source.hooks.PreToolUse` → target에 추가. 전체 설정 내용이 동일할 때만 스킵 |
| 상태줄 (3) | `target["statusLine"] = source["statusLine"]` (교체) |
| 플러그인 (5) | `target["enabledPlugins"].update(...)` (기존 + 신규) |
| 한국어 (6) | `target["language"] = "korean"` |
| 권한 (7) | `allow` 배열 합집합 (순서 유지, 중복 제거) |
| 알림 Hooks (14) | `source.hooks.Notification` → target에 추가. 전체 설정 내용 중복만 스킵 |
| .cs Hook (15) | `source.hooks.PostToolUse` → target에 추가. 전체 설정 내용 중복만 스킵 |
| SessionStart | hooks 항목 2·14·15 중 하나를 선택했을 때 함께 머지 |

```python
import os
import tempfile

def merge_hooks(target, source, hook_type):
    """동일 설정만 제외하고 같은 matcher의 다른 훅도 보존한다."""
    target.setdefault("hooks", {})
    src = source.get("hooks", {}).get(hook_type, [])
    tgt = target["hooks"].get(hook_type, [])
    for h in src:
        if h not in tgt:
            tgt.append(h)
    target["hooks"][hook_type] = tgt

for item, event in {2: "PreToolUse", 14: "Notification", 15: "PostToolUse"}.items():
    if item in selected_items:
        merge_hooks(target, source, event)
if selected_items & {2, 14, 15}:
    merge_hooks(target, source, "SessionStart")
if 3 in selected_items:
    target["statusLine"] = source["statusLine"]
if 5 in selected_items:
    target.setdefault("enabledPlugins", {}).update(source.get("enabledPlugins", {}))
if 6 in selected_items:
    target["language"] = "korean"
if 7 in selected_items:
    existing = target.get("permissions", {}).get("allow", [])
    new = source.get("permissions", {}).get("allow", [])
    target.setdefault("permissions", {})["allow"] = list(dict.fromkeys(existing + new))

target_path.parent.mkdir(parents=True, exist_ok=True)
temporary_path = None
try:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=target_path.parent,
        prefix=".settings-", suffix=".tmp", delete=False,
    ) as output:
        temporary_path = Path(output.name)
        json.dump(target, output, indent=2, ensure_ascii=False)
        output.flush()
        os.fsync(output.fileno())
    os.replace(temporary_path, target_path)
finally:
    if temporary_path is not None:
        temporary_path.unlink(missing_ok=True)
```

두 Python 블록은 같은 프로세스에서 순서대로 실행한다. 저장 후 JSON을 다시 읽어 선택한 섹션과 기존 사용자 설정의 보존을 확인한다. 오류가 발생하면 설치를 중단하고 임시 파일만 정리한다. 같은 settings 파일을 다른 프로세스가 동시에 변경하지 않는 상태에서 실행한다.

**4-3. 키바인딩** — `dotfiles/keybindings.json → $claude_config_dir/keybindings.json` 단순 복사.

**4-4. Skills** — 선택된 skill 폴더를 `$claude_config_dir/skills/`에 통째로 복사. 이미 있으면 덮어쓰기(최신 교체).

**4-5. Agent** — `dotfiles/agents/code-reviewer.md → $claude_config_dir/agents/code-reviewer.md`.

**4-6. Bash 테마** — `.bashrc`·`.minttyrc`·`.elephant_walk.py` 각각의 기존 내용과 Step 3의 `home/` 백업을 확인한 뒤 승인한 파일만 `~/`에 복사한다. 기존 사용자 설정을 보존하거나 병합하고, 교체가 필요하면 해당 파일의 백업·복구 경로를 확인한다. Roboto Mono 폰트는 `%LOCALAPPDATA%\Microsoft\Windows\Fonts\`에 설치.

**4-7. 바탕화면 바로가기 (Windows)** — `Claude Code.bat`:
```bat
@echo off
start "" "C:\Program Files\Git\git-bash.exe" -c "claude"
```
bypass 버전은 `claude --dangerously-skip-permissions`. Git Bash 경로는 `%PROGRAMFILES%\Git\git-bash.exe` 확인.

**4-8. snap-path (Windows)** — 부모 디렉토리에 클론 후 시작 프로그램 등록.
```bash
cd .. && git clone https://github.com/glowElephant/snap-path.git
```

**4-9. MCP 서버 (claude CLI 필요)**
```bash
# computer-control
pip install pyautogui pygetwindow keyboard Pillow pyperclip
claude mcp add --scope user --transport stdio computer-control -- python <저장소경로>/mcp-servers/computer-control/server.py

# web-fetcher
cd <저장소경로>/mcp-servers/web-fetcher && npm install
claude mcp add --scope user --transport stdio web-fetcher -- node <저장소경로>/mcp-servers/web-fetcher/index.mjs
```
`claude mcp list`에 이름이 있으면 스킵.

**4-10. jq 설치 (상태줄 의존성)**
```bash
# Windows (Git Bash)
mkdir -p "$HOME/bin" || exit 1
jq_temp=$(mktemp "$HOME/bin/.jq-XXXXXX.exe") || exit 1
if ! curl -fL -o "$jq_temp" https://github.com/jqlang/jq/releases/download/jq-1.7.1/jq-windows-amd64.exe ||
   ! chmod +x "$jq_temp" || ! "$jq_temp" --version; then
  rm -f "$jq_temp"
  exit 1
fi
mv -f "$jq_temp" "$HOME/bin/jq.exe" || { rm -f "$jq_temp"; exit 1; }
"$HOME/bin/jq.exe" --version || exit 1
```

HTTP 실패나 실행 불가능한 다운로드는 설치 실패다. 같은 폴더의 임시 파일에서 다운로드·버전을 확인한 뒤 교체하므로 실패한 다운로드가 기존 `jq.exe`를 절단하지 않는다. `~/bin`이 PATH에 없으면 상태줄에 이 전체 경로를 사용하거나 승인된 PATH 설정을 적용하고 실제 상태줄 실행을 확인한다. [curl의 HTTP 실패 처리](https://curl.se/docs/manpage.html#-f)를 따른다.

```bash
# Linux
sudo apt install jq   # 또는 brew install jq
```

### Step 5: 결과 보고
설치 후 (1) 설치된 항목 (2) 스킵된 항목 (3) 실패 항목+원인 (4) 백업 위치 (5) 다음 할 일(CLAUDE.md 정리·재시작·MCP 재시도)을 보고한다.

## 주의사항

- settings.json은 절대 전체 복사하지 말 것 — 반드시 머지한다.
- 설정 홈은 `CLAUDE_CONFIG_DIR` 지정값을 우선하고 없을 때만 사용자 홈의 `.claude`를 사용한다. 백업·설치·새 CLI 실행에 동일한 환경변수를 유지한다.
- MCP 서버는 공유 범위에 맞춰 user·project·local을 선택한다. 위 예시는 모든 프로젝트에서 사용하는 user 등록이다.
- MCP 등록은 `claude mcp add`를 우선한다. 프로젝트 `.mcp.json`과 플러그인 `.mcp.json`도 지원된다. `settings.json`의 hooks 설정과 MCP 설정을 혼동하지 않는다. [공식 MCP 안내](https://code.claude.com/docs/en/mcp)를 따른다.
- Git Bash는 `$VAR` 변수 확장을 지원한다. PowerShell·CMD에서 Bash 명령을 전달할 때 바깥 셸의 선확장과 인용을 구분하고, 경로 변수를 따옴표로 감싼다. 실제 경로를 하드코딩하지 않는다.
- 기존 hook은 전체 설정 내용으로 중복을 판별한다. matcher 생략도 유효하며 같은 matcher라도 다른 명령은 보존한다. [공식 hooks 안내](https://code.claude.com/docs/en/hooks)를 따른다.
