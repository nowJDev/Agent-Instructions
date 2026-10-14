<!-- Chrome DevTools MCP의 선택 기준과 자동 실행·검증 절차를 안내한다. -->
# Chrome DevTools MCP.

> `chrome-devtools-mcp`는 AI 에이전트가 Chrome DevTools 기능으로 실제 Chrome을 조작·검사하도록 연결하는 MCP 서버다.

## 용도와 선택 기준.

- 웹 UI 테스트·브라우저 디버깅은 사용자 지정 도구를 우선하고, 지정이 없으면 사용 가능한 `chrome-devtools` MCP를 우선한다.
- 페이지 이동·클릭·입력·스크린샷, 접근성 스냅샷, 콘솔 오류·네트워크 요청과 성능 분석에 사용한다.
- 웹 검색·자료 수집은 `firecrawl-*`를 사용한다. 기존 Chrome의 로그인·쿠키·열린 탭이 필요하면 Chrome 플러그인을 선택한다. 프로젝트의 기존 Playwright 테스트는 해당 프로젝트의 검증 명령으로 실행한다.

## 브라우저 자동 실행과 경계.

- 기본 실행 방식은 브라우저가 필요한 첫 MCP 도구 호출 때 별도 Chrome을 자동 실행한다. MCP 서버 연결만으로는 Chrome을 실행하지 않는다. 테스트 전에 사용자에게 Chrome을 수동 실행하도록 요청하지 않는다.
- `--headless`는 창 없이 실행하며 스크린샷·페이지 검사는 가능하다. 기본 프로필은 개인 Chrome과 분리되므로 기존 로그인 상태를 자동으로 이어받지 않는다.
- `--autoConnect`, `--browserUrl`, `--wsEndpoint`는 이미 실행 중인 Chrome에 연결하는 방식이다. 이를 기본 자동 실행 방식과 혼동하지 않는다.
- 테스트에서 생성한 페이지·브라우저만 정리하고 기존 사용자 탭·창·프로필은 보존한다. 연결이 실패하면 설치·도구 노출·실행 오류를 확인하며 보안 옵션을 임의로 해제하지 않는다.
- 브라우저 실행 허용은 외부 게시·전송·결제까지 허용한다는 뜻이 아니다. 해당 작업은 기존 권한 경계를 따른다.

## 제공 도구와 검증 절차.

도구 수·입력 스키마는 버전과 실행 옵션에 따라 달라진다. 연결 후 MCP `tools/list`로 설치 버전의 도구를 확인하고 그 스키마를 따른다.

1. `list_pages`로 연결과 별도 Chrome의 자동 실행을 확인한다.
2. `new_page` 또는 `navigate_page`로 승인된 테스트 URL을 연다.
3. `take_snapshot`의 최신 요소 `uid`로 `click`·`fill` 등을 수행한다. `pageId`가 필요한 도구에는 확인한 페이지 ID를 전달한다.
4. `take_screenshot`, `list_console_messages`, `list_network_requests`로 화면·오류·요청을 검증한다. 성능 검사는 `performance_start_trace`·`performance_stop_trace`를 사용한다.
5. 생성한 테스트 페이지를 `close_page`로 정리하고 실제 결과와 미검증 범위를 보고한다.

## Codex 등록 예제.

Chrome과 Node.js가 필요하다. 이 예제는 검증한 버전 `1.10.1`을 고정하며 Windows의 stdio 실행에는 `cmd.exe /d /c`를 사용한다.

```powershell
codex mcp list
codex mcp add chrome-devtools -- cmd.exe /d /c npx -y chrome-devtools-mcp@1.10.1 --headless --no-usage-statistics --no-performance-crux
codex mcp get chrome-devtools --json
```

이미 같은 서버가 등록되어 있으면 중복 등록하지 않고 기존 설정을 확인한다. Codex 전역 설정은 `~/.codex/config.toml`의 `mcp_servers.chrome-devtools`에 저장되며 시작 대기는 `startup_timeout_sec = 60`으로 구성할 수 있다. 실제 개인 설정 파일은 저장소에 넣지 않는다. 등록 후 Codex를 재시작하고 연결·자동 실행·페이지 조회·화면 캡처를 검증한다.

`--no-usage-statistics`는 MCP 사용 통계 수집을 끄고, `--no-performance-crux`는 성능 분석 URL의 CrUX API 전송을 끈다. 이 설정은 일반 웹 페이지의 네트워크 요청을 차단하지 않는다.

## 출처와 확인 상태.

- 공식 서버는 [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)다. [클라이언트별 등록](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/client-configurations.md)과 [실행 옵션](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/configuration.md)을 확인한다.
- Codex MCP 설정은 [OpenAI 공식 문서](https://learn.chatgpt.com/docs/extend/mcp?surface=cli)를 따른다.
- 2026-10-14 Codex 글로벌 환경에서 `1.10.1` 등록, 도구 30개 조회, 별도 Chrome 자동 실행·테스트 페이지 스냅샷·PNG 캡처·테스트 종료를 검증했다. 사용자도 테스트 완료를 확인했다.
- 문서 추가가 다른 PC·클라이언트의 설치를 의미하지는 않는다. Claude Code 등에 연결하려면 해당 클라이언트의 MCP 설정 형식을 사용한다.
