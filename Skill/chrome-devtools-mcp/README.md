<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# chrome-devtools-mcp 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. 활성 표시는 작성 당시 환경의 기록이다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [a11y-debugging](#a11y-debugging).
- [chrome-devtools-cli](#chrome-devtools-cli).
- [chrome-devtools](#chrome-devtools).
- [debug-optimize-lcp](#debug-optimize-lcp).
- [memory-leak-debugging](#memory-leak-debugging).
- [troubleshooting](#troubleshooting).

## a11y-debugging

> Chrome DevTools MCP를 활용해 web.dev 가이드라인 기반으로 웹 페이지의 접근성(a11y)을 디버깅·감사하는 스킬

<a id="a11y-debugging---용도"></a>
### 📌 용도
웹 페이지의 접근성 문제를 진단하고 개선 방향을 제시한다. 시맨틱 HTML, ARIA 라벨, 포커스 상태, 키보드 내비게이션, 탭 타겟 크기, 색상 대비 등을 점검한다.

핵심 개념은 **접근성 트리(Accessibility Tree) vs DOM**의 차이다. 시각적으로 요소를 숨기는 방식(`opacity: 0`)은 스크린 리더 입장에서 `display: none`이나 `aria-hidden="true"`와 다르게 동작한다. `take_snapshot` 도구가 반환하는 접근성 트리가 보조기술이 "보는" 것을 그대로 나타내므로 시맨틱 구조의 가장 신뢰할 수 있는 근거가 된다.

web.dev 문서를 읽을 때는 URL 끝에 `.md.txt`를 붙이면 깨끗한 raw 마크다운으로 받을 수 있다 (예: `https://web.dev/articles/accessible-tap-targets.md.txt`).

<a id="a11y-debugging---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 시맨틱 HTML 테스트, ARIA 라벨, 포커스 상태, 키보드 내비게이션, 탭 타겟, 색상 대비 검사 요청 시. "접근성 점검", "a11y 감사", "스크린 리더 호환성" 등의 키워드.
- **언제 쓰지 않는가**: 일반적인 디버깅·자동화(→ chrome-devtools), 성능/LCP(→ debug-optimize-lcp), 메모리 누수(→ memory-leak-debugging)는 별도 스킬 사용.

<a id="a11y-debugging---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "이 페이지 접근성 감사해줘"
- "버튼에 ARIA 라벨이 제대로 붙어 있는지 확인해줘"
- "키보드 탭 이동이 모달에 갇히는지 테스트해줘"
- "색상 대비가 WCAG 기준을 만족하는지 봐줘"

<a id="a11y-debugging---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
워크플로 패턴 8가지를 순차적으로 적용한다.

1. **자동 감사 (Lighthouse)**: `lighthouse_audit`를 `mode: "navigation"`, `outputDirPath` 지정으로 실행. `scores`(0~1) 확인, `jq`/Node.js 한 줄 스크립트로 실패 항목만 필터링(전체 리포트를 통째로 읽지 말 것).
2. **브라우저 이슈/감사**: `list_console_messages`를 `types: ["issue"]`, `includePreservedMessages: true`로 호출해 Chrome 네이티브 a11y 이슈(라벨 누락, 잘못된 ARIA 등) 확인.
3. **시맨틱 & 구조**: `take_snapshot`으로 헤딩 계층(h1~h3 건너뜀 여부) 점검, `take_screenshot`과 비교해 DOM 순서와 시각적 읽기 순서 일치 검증.
4. **라벨/폼/대체 텍스트**: 인터랙티브 요소의 접근 가능한 이름 확인, `evaluate_script` + "Find Orphaned Form Inputs" 스니펫으로 라벨 없는 입력 탐지, 이미지 `alt` 확인.
5. **포커스 & 키보드**: `press_key`로 `Tab`/`Shift+Tab` 이동 후 `take_snapshot`으로 포커스 위치 검증. 모달 포커스 트랩 확인.
6. **탭 타겟**: web.dev 기준 최소 48x48px. `evaluate_script` + "Measure Tap Target Size" 스니펫 사용(스냅샷의 `uid`를 인자로 전달).
7. **색상 대비**: `list_console_messages`로 "Low Contrast" 이슈 확인. 네이티브 감사가 못 잡으면 "Check Color Contrast" 스니펫 사용.
8. **전역 페이지 검사**: "Global Page Checks" 스니펫으로 문서 레벨 설정 점검.

**참조 파일**: `references/a11y-snippets.md` (evaluate_script용 스니펫 모음)
**주요 도구**: `take_snapshot`, `take_screenshot`, `lighthouse_audit`, `list_console_messages`, `press_key`, `evaluate_script`

<a id="a11y-debugging---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: chrome-devtools-mcp@claude-plugins-official
- 활성화: ON (Chrome DevTools MCP 서버와 연동)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.2.0/skills/a11y-debugging/SKILL.md`

## chrome-devtools-cli

> 터미널에서 셸 스크립트/명령으로 Chrome DevTools를 제어해 브라우저 작업을 자동화하는 스킬

<a id="chrome-devtools-cli---용도"></a>
### 📌 용도
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

<a id="chrome-devtools-cli---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 셸 스크립트/명령으로 브라우저 작업을 자동화할 때. CI 파이프라인, 반복 자동화, 터미널 기반 워크플로.
- **언제 쓰지 않는가**: 대화형 MCP 도구 호출이 더 적합한 단발성 디버깅(→ chrome-devtools). 최초 1회 설치는 `references/installation.md` 참조(일반 AI 워크플로에 포함되지 않음).

<a id="chrome-devtools-cli---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
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

<a id="chrome-devtools-cli---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **확장 프로그램**: `list_extensions`, `install_extension`, `uninstall_extension`, `reload_extension`, `trigger_extension_action`
- **실험적 기능**(플래그 필요): `click_at`(`--experimentalVision`), `screencast_start`(`--experimentalScreencast` + ffmpeg), `list_webmcp_tools`(`--categoryExperimentalWebmcp`)
- **서비스 관리**: `start`(시작/재시작), `status`(실행 확인), `stop`(중지)
- **참조 파일**: `references/installation.md`

<a id="chrome-devtools-cli---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: chrome-devtools-mcp@claude-plugins-official
- 활성화: ON (Chrome DevTools MCP 서버와 연동, CLI 별도 설치 필요)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.2.0/skills/chrome-devtools-cli/SKILL.md`

## chrome-devtools

> Chrome DevTools를 MCP로 활용해 효율적으로 디버깅, 트러블슈팅, 브라우저 자동화를 수행하는 핵심 스킬

<a id="chrome-devtools---용도"></a>
### 📌 용도
웹 페이지 디버깅, 브라우저 인터랙션 자동화, 성능 분석, 네트워크 요청 검사를 수행한다. chrome-devtools-mcp 플러그인의 중심 스킬로, 브라우저 제어 전반의 워크플로를 정의한다.

**브라우저 라이프사이클**: 첫 도구 호출 시 영속 Chrome 프로필로 브라우저가 자동 시작된다. MCP 서버 설정의 CLI 인자로 구성한다 (`npx chrome-devtools-mcp@latest --help`). 추가 기능은 플래그로 활성화: 확장 프로그램 도구는 `--categoryExtensions`, 메모리 도구는 `--memoryDebugging`.

**페이지 지정**: [공식 1.10.1 배포 도구 계약](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/e52c6b59b476c5e04d8dd9fd4bd017ba3b3d65df/docs/tool-reference.md)에서 페이지 도구는 `pageId`를 필수로 받는다. `list_pages`로 실제 ID를 확인해 이동·스냅샷·인터랙션 호출에 전달한다. `select_page`만으로 필수 인자가 대체되지 않으며 설치 버전의 런타임 스키마를 우선한다.

**요소 인터랙션**: `take_snapshot`으로 각 요소의 고유 `uid`를 얻어 인터랙션한다. 요소를 못 찾으면 새 스냅샷을 찍는다(페이지 변경 가능성).

<a id="chrome-devtools---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 웹 페이지 디버깅, 브라우저 인터랙션 자동화, 성능 분석, 네트워크 요청 검사 시.
- **언제 쓰지 않는가**: `--slim` 모드(MCP 설정)에는 적용 안 됨. 접근성(→ a11y-debugging), LCP 최적화(→ debug-optimize-lcp), 메모리 누수(→ memory-leak-debugging), 셸 스크립트 자동화(→ chrome-devtools-cli), 연결 문제(→ troubleshooting)는 전용 스킬.

<a id="chrome-devtools---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "이 페이지가 왜 안 뜨는지 디버깅해줘"
- "로그인 폼을 자동으로 채우고 제출해줘"
- "네트워크 요청 중 실패한 게 있는지 확인해줘"
- "Chrome 확장 프로그램을 테스트해줘"

<a id="chrome-devtools---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**페이지 인터랙션 전 워크플로**:
모든 페이지 도구에 확인한 `pageId`를 전달한다.

1. `navigate_page` 또는 `new_page`로 이동
2. `wait_for`로 콘텐츠 로딩 대기(찾을 대상을 알 때)
3. `take_snapshot`으로 페이지 구조 파악
4. 스냅샷의 `uid`로 `click`, `fill` 등 인터랙션

**효율적 데이터 검색**:
- 큰 출력(스크린샷, 스냅샷, 트레이스)은 `filePath` 파라미터로 저장
- 페이지네이션(`pageIdx`, `pageSize`)·필터링(`types`)으로 데이터 최소화
- 입력 액션에서 업데이트된 상태가 필요 없으면 `includeSnapshot: false`

**도구 선택**:
- 자동화/인터랙션 → `take_snapshot`(텍스트 기반, 빠름)
- 시각적 검사 → `take_screenshot`
- 접근성 트리에 없는 데이터 → `evaluate_script`

**병렬 실행**: 여러 도구 호출을 병렬로 보낼 수 있으나 순서 유지(navigate → wait → snapshot → interact).

**확장 프로그램 테스트**: `--categoryExtensions` 플래그 필요. `install_extension` → `list_extensions`로 ID 확인 → `trigger_extension_action` → `evaluate_script`(serviceWorkerId)로 상태 검증.

**트러블슈팅 참조**: Chrome DevTools UI 문서, [공식 troubleshooting.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/troubleshooting.md)

<a id="chrome-devtools---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: chrome-devtools-mcp@claude-plugins-official
- 활성화: ON (Chrome DevTools MCP 서버와 연동)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.2.0/skills/chrome-devtools/SKILL.md`

## debug-optimize-lcp

> Chrome DevTools MCP로 Largest Contentful Paint(LCP)를 디버깅하고 최적화하는 스킬

<a id="debug-optimize-lcp---용도"></a>
### 📌 용도
LCP(최대 콘텐츠 렌더링 시간) 성능을 진단하고 최적화한다. LCP는 페이지의 주요 콘텐츠(가장 큰 이미지/텍스트 블록)가 뷰포트에 렌더링되기까지의 시간으로, Core Web Vital 지표이며 사용자 경험과 검색 순위에 직접 영향을 준다.

- **양호**: 2.5초 이하
- **개선 필요**: 2.5~4.0초
- **불량**: 4.0초 초과

모바일 페이지 73%에서 LCP 요소는 이미지다.

**LCP 4개 하위 구간**(빈틈/중복 없이 순차적):
| 구간 | 이상적 비율 | 측정 내용 |
| --- | --- | --- |
| TTFB | ~40% | 내비게이션 시작 → HTML 첫 바이트 수신 |
| Resource load delay | <10% | TTFB → LCP 리소스 로딩 시작 |
| Resource load duration | ~40% | LCP 리소스 다운로드 시간 |
| Element render delay | <10% | 리소스 다운로드 완료 → 요소 렌더링 |

병목 구간을 파악하는 것이 효과적 최적화의 핵심이다. **흔한 함정**: 한 구간만 최적화(이미지 압축)하면 절약 시간이 다른 구간(render delay)으로 이동해 효과가 없을 수 있다.

<a id="debug-optimize-lcp---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: LCP 성능, 느린 페이지 로딩, Core Web Vitals 최적화 질문 시. "largest contentful paint", "page load speed", "CWV", 히어로 이미지/주요 콘텐츠 렌더링 속도 개선 요청.
- **언제 쓰지 않는가**: 접근성(→ a11y-debugging), 메모리(→ memory-leak-debugging), 일반 디버깅(→ chrome-devtools).

<a id="debug-optimize-lcp---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "우리 페이지 LCP가 왜 느린지 분석해줘"
- "히어로 이미지가 너무 늦게 뜨는데 개선해줘"
- "Core Web Vitals 점수를 올리고 싶어"

<a id="debug-optimize-lcp---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**디버깅 워크플로(순서대로)**:
`list_pages`에서 실제 `pageId`를 확인하고 각 페이지 도구에 전달한다. 인자는 설치 버전의 런타임 스키마를 우선하며 [공식 도구 계약](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/e52c6b59b476c5e04d8dd9fd4bd017ba3b3d65df/docs/tool-reference.md)을 확인한다.

1. **트레이스 기록**: `navigate_page` 후 `performance_start_trace`(`reload: true`, `autoStop: true`)로 전체 로딩 캡처. 출력의 insight set ID를 기록.
2. **LCP 인사이트 분석**: `performance_analyze_insight`로 드릴다운. 인사이트 이름: `LCPBreakdown`(4개 구간 타이밍), `DocumentLatency`(TTFB), `RenderBlocking`(렌더 차단 리소스), `LCPDiscovery`(조기 발견 여부).
3. **LCP 요소 식별**: `evaluate_script` + "Identify LCP Element" 스니펫으로 태그·리소스 URL·타이밍 확인. `url`이 비면 텍스트 기반 요소.
4. **네트워크 워터폴 확인**: `list_network_requests`(`resourceTypes: ["image", "font"]`), `get_network_request`로 시작 시간·duration 점검. `resourceTypes`는 소문자 enum이다.
5. **HTML 공통 이슈 점검**: `evaluate_script` + "Audit Common Issues" 스니펫으로 lazy-load 이미지, fetchpriority 누락, 렌더 차단 스크립트 확인.

**최적화 전략(우선순위)**:
1. **Resource load delay 제거**: 표준 `<img src>` 사용, LCP 이미지는 절대 lazy-load 금지, `fetchpriority="high"` 또는 `<link rel="preload">` 추가.
2. **Element render delay 제거**: 크리티컬 CSS 인라인, 비크리티컬 CSS/JS defer, 긴 작업 분할, SSR.
3. **Resource load duration 단축**: WebP/AVIF, `srcset`, CDN, `Cache-Control`, `font-display: swap`.
4. **TTFB 단축**: 리다이렉트 최소화, 엣지 캐싱(CDN), bfcache 적격화.

**검증/에뮬레이션**: 수정 후 `performance_start_trace`(`reload: true`) 재실행하여 병목 축소 확인. `emulate`(`networkConditions: "Fast 3G"`, `cpuThrottlingRate: 4`)로 제약 환경 테스트.

**참조 파일**: `references/lcp-snippets.md`

<a id="debug-optimize-lcp---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: chrome-devtools-mcp@claude-plugins-official
- 활성화: ON (Chrome DevTools MCP 서버와 연동)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.2.0/skills/debug-optimize-lcp/SKILL.md`

## memory-leak-debugging

> JavaScript/Node.js 애플리케이션의 메모리 누수를 진단·해결하는 스킬

<a id="memory-leak-debugging---용도"></a>
### 📌 용도
JavaScript와 Node.js 애플리케이션에서 메모리 누수를 찾고 진단하고 수정한다. 높은 메모리 사용량, OOM(Out of Memory) 에러, 힙 스냅샷 분석, memlab 같은 메모리 누수 탐지 도구 실행을 다룬다.

**핵심 원칙**:
- **memlab 우선**: raw `.heapsnapshot` 파일을 직접 읽지 말 것 — 매우 크고 토큰을 과도하게 소비한다. 항상 `memlab`으로 스냅샷을 처리하고 누수 트레이스를 식별한다.
- **누수 격리**: 브라우저(클라이언트) 누수인지 Node.js(서버) 누수인지 판별.
- **흔한 원인**: detached DOM 노드, 처리되지 않은 클로저, 전역 변수, 제거되지 않은 이벤트 리스너, 무한 증가 캐시. (단, detached DOM 노드는 의도적 캐시일 수 있으니 null로 만들기 전 사용자에게 확인할 것.)

<a id="memory-leak-debugging---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 높은 메모리 사용량 보고, OOM 에러, 힙 스냅샷 분석, memlab 등 메모리 누수 탐지 도구 실행 요청 시.
- **언제 쓰지 않는가**: 일반 성능/LCP(→ debug-optimize-lcp), 일반 디버깅(→ chrome-devtools)은 별도 스킬.

<a id="memory-leak-debugging---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "우리 앱 메모리가 계속 늘어나는데 누수 찾아줘"
- "이 heapsnapshot 분석해줘"
- "OOM 에러가 나는데 원인 진단해줘"
- "memlab으로 누수 트레이스 뽑아줘"

<a id="memory-leak-debugging---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**워크플로**:

1. **스냅샷 캡처**: 프론트엔드 누수 조사 시 chrome-devtools-mcp 도구(`click`, `navigate_page`, `fill` 등)로 페이지를 조작한다.
   - 인터랙션 후 원래 상태로 되돌려 메모리 해제 여부 확인.
   - 동일 인터랙션을 10회 반복해 누수를 증폭.
   - `take_heapsnapshot`으로 baseline(기준), target(액션 후), final(되돌린 후) 상태의 `.heapsnapshot`을 디스크에 저장.

2. **memlab으로 누수 탐지(권장)**: 생성된 `.heapsnapshot`을 `memlab`으로 자동 분석. 사용법은 `references/memlab.md` 참조. raw `.heapsnapshot`을 `read_file`/`cat`으로 읽지 말 것.

3. **흔한 누수 식별**: 누수 트레이스를 찾으면 `references/common-leaks.md`로 코드 내 근본 원인과 수정법 파악.

4. **폴백: 스냅샷 수동 비교**: `memlab`이 없으면 references 디렉터리의 폴백 스크립트로 두 스냅샷을 비교:
   ```bash
   node skills/memory-leak-debugging/references/compare_snapshots.js <baseline.heapsnapshot> <target.heapsnapshot>
   ```
   크기순 상위 증가 객체와 가장 흔한 3가지 누수 유형(detached DOM, 클로저, Context)을 출력한다.

**주요 도구**: `take_heapsnapshot`, chrome-devtools-mcp 인터랙션 도구, `memlab`(외부 CLI)
**참조 파일**: `references/memlab.md`, `references/common-leaks.md`, `references/compare_snapshots.js`

<a id="memory-leak-debugging---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: chrome-devtools-mcp@claude-plugins-official
- 활성화: ON (Chrome DevTools MCP 서버와 연동, `--memoryDebugging` 플래그로 메모리 도구 활성화)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.2.0/skills/memory-leak-debugging/SKILL.md`

## troubleshooting

> Chrome DevTools MCP의 연결·타겟 문제를 단계별로 진단·해결하는 트러블슈팅 마법사 스킬

<a id="troubleshooting---용도"></a>
### 📌 용도
Chrome DevTools MCP 서버 설정의 연결 문제와 타겟 문제를 진단하고 수정한다. 트러블슈팅 마법사로서 단계별 진단 프로세스를 따라 사용자의 MCP 서버 구성을 고친다.

<a id="troubleshooting---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `list_pages`, `new_page`, `navigate_page`가 실패하거나 서버 초기화가 실패할 때.
- **언제 쓰지 않는가**: 정상 동작 중인 디버깅/자동화(→ chrome-devtools), 페이지 콘텐츠 문제는 트러블슈팅이 아닌 해당 스킬.

<a id="troubleshooting---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "list_pages가 계속 실패해"
- "MCP 서버가 시작이 안 돼"
- "Could not find DevToolsActivePort 에러가 나"
- "도구가 9개밖에 안 보여"

<a id="troubleshooting---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**단계별 진단 프로세스**:

**1단계: 설정 파일 찾기/읽기**: `.mcp.json`, `gemini-extension.json`, `.claude/settings.json`, `.vscode/launch.json`, `.gemini/settings.json`을 검색. 잘못된 인자/플래그, 누락된 환경변수, 부적합 환경의 `--autoConnect` 사용 등을 식별.

**2단계: 흔한 연결 에러 분류**:
- **`Could not find DevToolsActivePort`**: `--autoConnect` 전용 에러. ① 올바른 Chrome 버전 실행 확인 → ② `chrome://inspect/#remote-debugging`에서 원격 디버깅 활성화 안내 → ③ `list_pages`로 검증(원래 명령 재시도 금지) → ④ 성공 시 해결, 실패 시 고급 단계.
- **새 빈 프로필 생성**: 플래그 오타 확인(예: `--autoBronnect`).
- **도구 누락 / 9개만 표시**: MCP 클라이언트의 read-only 모드 때문. 모든 도구는 `readOnlyHint`로 주석되어 있으며, 전체 도구는 read-only 모드 해제 필요(Gemini CLI의 Plan Mode 종료 등).
- **확장 프로그램 도구 누락/실패**: `--categoryExtensions` 플래그 확인. Chrome 149 미만은 기존 인스턴스 연결 시 확장 로드 불가.
- **기타 에러**: `Target closed`, "Tool not found"(`--slim` 사용 여부), `Network.enable timed out`, `ERR_MODULE_NOT_FOUND`, 샌드박스/호스트 검증 에러.

**3단계: 알려진 이슈 읽기**: [공식 troubleshooting.md](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/troubleshooting.md) — 샌드박스 제한(macOS Seatbelt, Linux 컨테이너), WSL 요구사항, `--autoConnect` 핸드셰이크(실행 중인 Chrome 144+ 필요).

**4단계: 구성 공식화**: 에러와 환경(OS, MCP 클라이언트)에 맞는 설정 스니펫 작성. `--browser-url=http://127.0.0.1:9222`(샌드박스 환경), 원격 디버깅 활성화, `--logFile <절대경로>`, Codex의 초 단위 `startup_timeout_sec` 확인([공식 설정](https://learn.chatgpt.com/docs/extend/mcp), [등록·대기 예제](../../MCP/chrome-devtools.md#codex-등록-예제)).

**5단계: 진단 명령 실행**:
```bash
npx chrome-devtools-mcp@latest --help
DEBUG=* npx chrome-devtools-mcp@latest --logFile=/tmp/cdm-test.log
```

**6단계: GitHub 이슈 확인**: `gh issue list --repo ChromeDevTools/chrome-devtools-mcp --search "<에러>" --state all` 또는 issues/discussions 페이지 안내.

<a id="troubleshooting---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: chrome-devtools-mcp@claude-plugins-official
- 활성화: ON (Chrome DevTools MCP 서버와 연동)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/chrome-devtools-mcp/1.2.0/skills/troubleshooting/SKILL.md`
