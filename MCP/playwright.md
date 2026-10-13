# playwright

> Playwright 기반 브라우저 자동화 MCP 서버. 접근성 스냅샷을 통해 실제 브라우저를 제어한다.

## 📌 용도
실제 브라우저(Chromium 등)를 띄워 페이지 탐색, 클릭, 입력, 폼 작성, 스크린샷, 네트워크/콘솔 모니터링, JS 실행 등 엔드투엔드 웹 자동화를 수행한다. 시각 픽셀이 아닌 **접근성 트리(snapshot)** 기반으로 요소를 식별하므로 안정적이다.

## 🎯 트리거 조건 / 사용 맥락
- 웹 페이지를 자동으로 열고 조작/테스트해야 할 때 (로그인, 폼 제출, 페이지네이션 등)
- 동적(JS 렌더링) 페이지에서 데이터 추출/검증
- E2E 테스트, UI 동작 확인, 스크린샷/네트워크 요청 캡처
- 브라우저 콘솔/네트워크 디버깅

## 🛠️ 제공 도구 목록

아래는 [공식 0.0.83 배포 도구 계약](https://github.com/microsoft/playwright-mcp/blob/f183dad4a52965583e3cc1d59b88cdc279e2e57d/README.md#tools)의 대표 도구다. `@latest`의 도구와 인자는 바뀔 수 있으므로 연결 후 MCP `tools/list`로 설치 버전의 스키마를 확인한다. 이 버전에서 스냅샷 참조·셀렉터를 받는 인자는 `target`이며 이전 버전의 `ref`를 섞지 않는다.

### 탐색 / 페이지 상태
| 도구명 | 기능 | 주요 파라미터 |
|--------|------|----------------|
| browser_navigate | 지정 URL로 이동 | `url` |
| browser_navigate_back | 뒤로 가기 | (없음) |
| browser_snapshot | 현재 페이지의 접근성 스냅샷(요소 트리) 캡처 — 요소 식별의 기준 | `target`, `filename`, `depth` 선택 |
| browser_take_screenshot | 페이지/요소 스크린샷 저장 | `scale`(예: `css`), `filename`·`target`·`fullPage` 선택 |
| browser_resize | 뷰포트 크기 변경 | `width`, `height` |
| browser_wait_for | 텍스트 출현/사라짐 또는 시간 대기 | `text`, `textGone`, `time` |
| browser_close | 브라우저(페이지) 닫기 | (없음) |

### 상호작용
| 도구명 | 기능 | 주요 파라미터 |
|--------|------|----------------|
| browser_click | 요소 클릭 | `target` 필수, `element`·`button`·`doubleClick` 선택 |
| browser_type | 요소에 텍스트 입력 | `target`·`text` 필수, `element`·`submit` 선택 |
| browser_fill_form | 여러 폼 필드를 한 번에 채움 | `fields[]` |
| browser_press_key | 키보드 키 입력 | `key` |
| browser_hover | 요소 위로 마우스 호버 | `target` 필수, `element` 선택 |
| browser_drag | 한 요소를 다른 요소로 드래그 | `startTarget`·`endTarget` 필수, `startElement`·`endElement` 선택 |
| browser_drop | 파일·MIME 데이터를 요소에 드롭 | `target` 필수, `paths` 또는 `data` 중 하나 이상 |
| browser_select_option | 드롭다운(select) 옵션 선택 | `target`·`values` 필수, `element` 선택 |
| browser_file_upload | 파일 업로드 | `paths[]` |
| browser_handle_dialog | alert/confirm/prompt 다이얼로그 처리 | `accept`, `promptText` |

### 진단 / 실행 / 탭
| 도구명 | 기능 | 주요 파라미터 |
|--------|------|----------------|
| browser_console_messages | 콘솔 로그 조회 | `level`(예: `info`), `all`·`filename` 선택 |
| browser_network_requests | 네트워크 요청 목록 | `static`(정적 리소스 포함 여부), `filter`·`filename` 선택 |
| browser_network_request | 특정 네트워크 요청 상세 | `index`(목록의 1부터 시작하는 번호) 필수, `part`·`filename` 선택 |
| browser_evaluate | 페이지 컨텍스트에서 JS 평가 | `function` 필수, `element`·`target` 선택 |
| browser_run_code_unsafe | 임의 코드 실행(주의: unsafe) | 코드 |
| browser_tabs | 탭 목록/생성/전환/닫기 | `action`, `index` |

## 💻 사용 예시

**예시 1 — 로그인 후 대시보드 캡처**
1. `browser_navigate`(url: 로그인 페이지)
2. `browser_snapshot`으로 입력 필드 참조를 확인하고 `target`에 전달한다.
3. `browser_fill_form`(아이디/비번) → `browser_click`(로그인 버튼)
4. `browser_wait_for`(text: "대시보드") → `browser_take_screenshot`(scale: "css")

**예시 2 — 동적 페이지에서 API 응답 확인**
1. `browser_navigate`(url)
2. `browser_network_requests`(static: false)로 XHR 목록 확인 → `browser_network_request`(index: 목록 번호)로 특정 응답 상세 조회.

## 📦 출처 / 설치 상태
- 제공: **플러그인** `playwright@claude-plugins-official`
- 활성화: ON (`settings.json` → `enabledPlugins["playwright@claude-plugins-official"]: true`)
- 연결 방식: **stdio** — `npx @playwright/mcp@latest`
- 설정/캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/playwright/unknown/.mcp.json`
- 세션 내 도구 식별자 접두사: `mcp__plugin_playwright_playwright__`
