<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-14-chrome-devtools-mcp 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-10-14-chrome-devtools-mcp.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/specs/2026-10-14-chrome-devtools-mcp.md).

<!-- Chrome DevTools MCP 사용 지침의 승인 범위와 완료 기준을 기록한다. -->
<a id="spec--chrome-devtools-mcp-문서-반영-설계"></a>
### Chrome DevTools MCP 문서 반영 설계.

- 승인 범위는 기존 MCP 분류에 사용 안내를 추가하고 Codex 전역 지침에도 반영하는 것이다.
- 웹 UI 테스트·브라우저 디버깅은 사용자 지정 도구를 우선하며, 지정이 없으면 사용 가능한 Chrome DevTools MCP를 우선한다.
- 기본 실행은 별도 Chrome 프로필의 자동 실행이다. 기존 로그인·탭이 필요하면 Chrome 플러그인을 선택한다. 검색·자료 수집의 Firecrawl 선택은 유지한다.
- 루트와 전역 템플릿에는 선택 규칙·링크만 두고, 상세 설명·자동 실행·검증·등록 예제는 `MCP/chrome-devtools.md`에서 관리한다. 인덱스와 이식 표도 연결한다.
- Codex 설치 상태를 다른 클라이언트의 설치 완료로 표시하지 않는다. 실제 전역 지침의 사용자 고유 내용을 보존하며 변경 파일만 동기화한다. 개인 설정은 커밋하지 않는다.
- 서버 설치·설정 변경은 없다. UTF-8·링크·지침 일치·기존 테스트·전체 diff와 독립 리뷰를 확인하고 한글 커밋 후 로컬 main에 반영한다.
- 완료 기준은 원본과 전역 문서가 같은 선택 정책을 안내하고, 자동 실행과 기존 Chrome 연결의 차이를 확인할 수 있는 것이다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-14-chrome-devtools-mcp.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-14-chrome-devtools-mcp.md).

<!-- Chrome DevTools MCP 안내와 전역 지침 반영 순서를 기록한다. -->
<a id="plan--chrome-devtools-mcp-문서-반영-계획"></a>
### Chrome DevTools MCP 문서 반영 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 독립 조사·리뷰는 `rules/02`에 따라 위임한다.

Goal: 승인된 MCP 사용 방침을 저장소와 Codex 전역 지침에 반영한다.
Architecture: [설계](#spec)에 따라 기존 분류를 유지하고 상세 안내 한 문서를 연결한다.
Tech Stack: Markdown, Python unittest, Git, Windows PowerShell.

<a id="plan--task-1-카탈로그와-선택-규칙"></a>
#### Task 1. 카탈로그와 선택 규칙.

Files: `AGENTS.md`, `codex-global-AGENTS.md`, `MCP/README.md`, `MCP/chrome-devtools.md`, `PORTABILITY.md`, `rules/02_tool-boundaries.md`, `CHANGELOG.md`.

- [x] 사용자 지정 도구 우선·Chrome DevTools MCP 우선·Firecrawl 유지 규칙을 작성하고 상세 문서에서 자동 실행·별도 프로필·공식 출처·설치 상태를 안내한다.
- [x] `python -X utf8 -B -m unittest discover -s tests -v`, `git diff --check`와 UTF-8·BOM·상대링크 검사를 통과하고 전체 diff를 독립 리뷰한다. 문서 수정이므로 구현 RED·TDD는 해당하지 않는다.

<a id="plan--task-2-전역-반영과-통합"></a>
#### Task 2. 전역 반영과 통합.

Files: 이 계획과 `docs/reviews/2026-10-14-chrome-devtools-mcp.md`. 개인 경로는 저장소에 기록하지 않는다.

- [x] 실제 Codex 전역 지침의 사용자 고유 내용을 보존하고 변경 문서를 전역 복제본에 동기화한다. 파일 내용과 링크를 검증한다.
- [x] 검증·리뷰 결과를 기록하고 관련 파일만 한글 커밋한다. 로컬 main에 반영한 뒤 임시 브랜치·작업 폴더를 정리한다. 원격 푸시는 하지 않는다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-14-chrome-devtools-mcp.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-14-chrome-devtools-mcp.md).

<!-- Chrome DevTools MCP 문서와 Codex 전역 지침 반영의 검증 결과를 기록한다. -->
<a id="review--chrome-devtools-mcp-문서-반영-검증"></a>
### Chrome DevTools MCP 문서 반영 검증.

- 기준선은 `981744c`이며 승인 범위는 저장소 MCP 문서와 Codex 전역 지침에 Chrome DevTools MCP 사용 방침을 추가하는 것이다.
- 새 상세 문서와 MCP 인덱스·이식 표를 연결하고 루트·Codex 전역 템플릿에 사용자 지정 도구 우선과 웹 UI 테스트·디버깅의 Chrome DevTools MCP 우선 규칙을 반영했다. Firecrawl 검색·자료 수집과 프로젝트 Playwright 검증은 유지한다.
- 기본 별도 프로필 자동 실행과 기존 Chrome 연결 옵션, 기존 로그인 상태·사용자 탭 보존·외부 작업 권한을 구분했다. Codex 등록 사실을 다른 클라이언트의 설치 완료로 표시하지 않는다.
- 전체 64개 기존 회귀 테스트가 32.302초에 통과했고 실패·스킵은 0개다. 명령은 `python -X utf8 -B -m unittest discover -s tests -v`다.
- 변경 문서의 UTF-8·BOM 없음·LF·한글 보존·상대링크와 `git diff --check`를 검사했다. PowerShell 기본 ASCII 파이프로 손상된 새 작업 문서는 UTF-8 파이프로 다시 작성한 후 검사했다. 원본 사용자 문서는 손상되지 않았다.
- 독립 에이전트가 전체 변경과 새 문서, 공식 실행 옵션·등록 문서를 검토했고 중요한 발견은 없었다.
- 실제 Codex 전역 지침은 백업 후 필요한 두 줄만 병합했다. 역치환 비교로 기존 내용과 개인 마무리 지침 보존을 확인했고 전역 복제본과 변경 파일이 일치함을 검사했다. 개인 설정 파일은 변경하거나 커밋하지 않는다.
- 통합 범위는 한글 커밋과 로컬 main 반영이며 원격 푸시는 포함하지 않는다. 새 Codex 세션의 지침 자동 로딩과 다른 PC·클라이언트 설치는 이번 문서 변경에서 검증하지 않았다.

2026-10-15 사용자가 전체 push·병합·정리를 추가 승인했다. 기존 커밋 `b77f3ed`를 공개 범위 관점에서 독립 재검토했고 차단·중요 발견은 없었다. CI PR #1과 함께 일반 merge로 이력을 보존했으며 통합 main의 전체 64개 테스트가 통과했다. 최초 작업에서 제외했던 원격 전달은 이번 추가 승인 범위에 포함한다.
