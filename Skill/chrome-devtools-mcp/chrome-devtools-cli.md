# chrome-devtools-cli

> 터미널에서 셸 스크립트/명령으로 Chrome DevTools를 제어해 브라우저 작업을 자동화하는 스킬

## 📌 용도
`chrome-devtools-mcp` CLI를 사용해 터미널에서 직접 브라우저를 제어한다. 셸 스크립트 작성이나 셸 명령으로 브라우저 작업을 자동화할 때 사용한다. MCP 도구 호출 대신 CLI 명령으로 동일한 작업을 수행하는 것이 핵심 차이다.

**AI 워크플로**:
1. **실행**: 도구를 직접 실행(예: `chrome-devtools list_pages`). 백그라운드 서버가 암묵적으로 시작되므로 매번 `start`/`status`/`stop`을 호출하지 말 것.
2. **검사**: `list_pages`에서 얻은 `<pageId>`로 `take_snapshot <pageId>`를 호출해 요소 `<uid>`를 얻는다.
3. **액션**: `click <pageId> <uid>`, `fill <pageId> <uid> <value>` 등 실행. 상태는 명령 간 유지된다.

스냅샷 예시:
```
uid=1_0 RootWebArea "Example Domain" url="https://example.com/"
  uid=1_1 heading "Example Domain" level="1"
```

## 🎯 트리거 조건
- **언제 호출되는가**: 셸 스크립트/명령으로 브라우저 작업을 자동화할 때. CI 파이프라인, 반복 자동화, 터미널 기반 워크플로.
- **언제 쓰지 않는가**: 대화형 MCP 도구 호출이 더 적합한 단발성 디버깅(→ chrome-devtools). 최초 1회 설치는 `references/installation.md` 참조(일반 AI 워크플로에 포함되지 않음).

## 💻 사용 예시 / 명령어
기본 사용법: `chrome-devtools <tool> [arguments] [flags]`. 어떤 명령이든 `--help` 사용 가능. 출력은 기본 Markdown, `--output-format=json`으로 JSON 출력.

아래 예시는 [공식 1.10.1 배포 CLI 계약](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/e52c6b59b476c5e04d8dd9fd4bd017ba3b3d65df/skills/chrome-devtools-cli/SKILL.md)을 기준으로 한다. `1`은 `list_pages`에서 확인한 실제 `pageId`로 바꾼다. 필수 인자는 위치 인자로, 선택 인자는 플래그로 전달하며 설치 버전의 `--help`를 우선한다.

**입력 자동화**:
```bash
chrome-devtools take_snapshot 1            # UID 획득용 텍스트 스냅샷
chrome-devtools click 1 "id"                # 요소 클릭
chrome-devtools click 1 "id" --dblClick true --includeSnapshot true
chrome-devtools fill 1 "id" "text"          # 입력/선택
chrome-devtools type_text 1 "hello" --submitKey "Enter"
chrome-devtools press_key 1 "Control+A"
chrome-devtools upload_file 1 "id" "file.txt"
chrome-devtools handle_dialog 1 accept
```

**내비게이션**:
```bash
chrome-devtools navigate_page 1 --url "https://example.com"
chrome-devtools navigate_page 1 --type "reload" --ignoreCache true
chrome-devtools new_page "https://example.com" --background true
chrome-devtools list_pages
chrome-devtools select_page 1 --bringToFront true
chrome-devtools close_page 1
```

**에뮬레이션**:
```bash
chrome-devtools emulate 1 --networkConditions "Offline"
chrome-devtools emulate 1 --cpuThrottlingRate 4 --colorScheme "dark" --viewport "1920x1080"
chrome-devtools resize_page 1 1920 1080
```

**성능**:
```bash
chrome-devtools performance_start_trace 1 --reload true --autoStop true --filePath "t.json.gz"
chrome-devtools performance_stop_trace 1 --filePath "t.json"
chrome-devtools performance_analyze_insight 1 "NAVIGATION_0" "LCPBreakdown"
chrome-devtools take_heapsnapshot 1 "./snap.heapsnapshot"
```

**네트워크 / 디버깅**:
```bash
chrome-devtools list_network_requests 1 --pageSize 50 --resourceTypes fetch
chrome-devtools get_network_request 1 --reqid 1 --responseFilePath res.md
chrome-devtools evaluate_script "() => document.title" --pageId 1
chrome-devtools lighthouse_audit 1 --mode "navigation" --device "mobile"
chrome-devtools list_console_messages 1 --types error --includePreservedMessages true
chrome-devtools take_screenshot 1 --fullPage true --format "jpeg" --quality 80
```

`NAVIGATION_0`은 트레이스 결과의 실제 insight set ID로 바꾼다. `resourceTypes`는 소문자 enum(`fetch`·`image`·`font` 등)을 사용한다.

`evaluate_script`는 함수가 위치 인자이고 `pageId`는 `--pageId` 옵션이다. CLI의 위치·선택 인자는 [배포 CLI 설정](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/e52c6b59b476c5e04d8dd9fd4bd017ba3b3d65df/src/config/cli-options.ts)을 확인하며 MCP 도구의 필수 인자 순서와 혼용하지 않는다.

## 🛠️ 제공 도구 / 주요 파라미터
- **확장 프로그램**: `list_extensions`, `install_extension`, `uninstall_extension`, `reload_extension`, `trigger_extension_action`
- **실험적 기능**(플래그 필요): `click_at`(`--experimentalVision`), `screencast_start`(`--experimentalScreencast` + ffmpeg), `list_webmcp_tools`(`--categoryExperimentalWebmcp`)
- **서비스 관리**: `start`(시작/재시작), `status`(실행 확인), `stop`(중지)
- **참조 파일**: `references/installation.md`

## 📦 출처 / 설치 상태
- 플러그인: chrome-devtools-mcp@claude-plugins-official
- 활성화: ON (Chrome DevTools MCP 서버와 연동, CLI 별도 설치 필요)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.2.0/skills/chrome-devtools-cli/SKILL.md`
