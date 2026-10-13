<!-- 클라이언트별 최소 CLI 세팅 안내의 구현과 검증 계획을 기록한다. -->
# 클라이언트별 최소 CLI 세팅 구현 계획.

For agentic workers: REQUIRED SUB-SKILL: subagent-driven-development. 승인 설계에 따른 실행·검증·전체 커밋·푸시를 진행한다.

## Goal.

“이거대로 세팅해줘”를 현재 Codex 또는 Claude Code의 최소 CLI 세팅 요청으로 연결한다.

## Architecture.

설치·선택·지침은 GETTING_STARTED.md, 공통 Windows 바로가기 실행은 references/windows-cli-shortcut.md에 둔다. 이전 Codex 문서 주소를 유지하며 Claude 확장 설치와 기본 설치를 구분한다. 새 설치기는 작성하지 않는다.

## Tech Stack.

Markdown, HTML, Windows PowerShell, WScript.Shell COM, Git. CLI 설치 명령은 공식 문서로 확인하며 검증 중 실제 설치나 로그인은 수행하지 않는다.

## Task 1. 공통 진입점과 두 클라이언트 안내.

Files: Modify README.md, GETTING_STARTED.md, AGENTS.md, codex-global-AGENTS.md, PORTABILITY.md, index.html, CHANGELOG.md, references/codex-windows-shortcut.md, references/claude-code-cli-setup.md. Create references/windows-cli-shortcut.md.

- [x] 수정 대상 전체를 UTF-8로 읽고 기본 요청과 확장 요청의 연결을 확인한다.
- [x] 다음 공통 프롬프트와 클라이언트 판별 규칙을 반영한다.

```text
이거대로 세팅해줘.
https://github.com/nowJDev/Agent-Instructions
```

- [x] 선택한 CLI만 공식 설치·재사용·버전 확인을 수행하는 안내를 작성한다.
- [x] 사용자 지침을 보존하며 Codex 전역 AGENTS.md 및 Claude 전역 CLAUDE.md에 기본 규칙을 연결하는 절차를 작성한다.
- [x] Codex·Claude Code의 공식 아이콘·바로가기 이름·CLI 명령을 명시적으로 선택하는 공통 PowerShell 예제를 작성한다. WT가 없으면 cmd를 사용한다. Source 고정, 루트·세미콜론 인용, 기존 파일 확인, 실패 throw를 유지한다.
- [x] 이전 Codex 문서 주소와 Claude 확장 안내를 보존하고 스킬·MCP·플러그인 등이 기본 범위에 들어오지 않게 맞춘다.
- [x] HTML과 CHANGELOG를 같은 세팅 계약으로 갱신한다.

## Task 2. 검증·리뷰.

Files: Verify Task 1 files and process documents. Create docs/reviews/2026-10-13-client-cli-setup-review.md.

- [x] 변경 전 검사로 공통 요청·Claude 공식 아이콘·cmd 대체 분기 누락을 확인한다.
- [x] UTF-8, 코드 펜스, 상대 링크·앵커와 HTML 구조를 검사한다. 누락 0개여야 한다.
- [x] 모든 새 PowerShell 예제의 Parser.ParseInput 오류가 0개인지 확인한다.
- [x] 임시 경로에서 두 클라이언트×WT·cmd 4분기의 실제 COM 생성·검증, 버전 실행, 기존 바로가기 갱신과 bat 보존을 확인한다.
- [x] 누락된 CLI·아이콘·폴더, 잘못된 속성, 동명 CLI, 공백·한글·쉼표·세미콜론·드라이브 루트 회귀를 확인한다.
- [x] HTML의 공통 요청과 결과 표를 브라우저에서 확인한다.
- [x] 스펙 리뷰 후 품질 리뷰를 수행하고 발견 사항을 해결한다.
- [x] `git diff --check` exit 0과 실제 검증 증거를 기록한다.

## 커밋·통합 절차.

검증한 관련 문서만 한글 제목·빈 줄·bullet 본문으로 커밋한다. 깨끗한 원본 main에 fast-forward하고 origin/main에 일반 push한다. `git ls-remote origin refs/heads/main`과 로컬 HEAD를 비교한다. 커밋·푸시 결과는 이후 Git 이력과 원격 브랜치에서 확인한다.

## 검증 증거.

- 기준선에서 공통 요청 문구와 공통 바로가기 문서 누락을 확인한 뒤 구현 후 같은 문서 검사가 통과했다.
- 구현 문서 10개 UTF-8·BOM 없음·코드 펜스·로컬 링크 및 앵커 94개 누락 0개다. PowerShell 블록 8개 파서 오류 0개다.
- 두 클라이언트×WT·CMD 4분기에서 실제 Windows COM 생성·갱신·독립 검증을 통과했다. 기본·사용자·드라이브 루트 폴더와 동명 CLI를 포함한 숨긴 CLI 실행 24회, 실패 조건 37개가 통과했다. 검증 횟수는 최종 assert로 확인했다.
- 실제 CLI 버전은 Codex CLI 0.162.1과 Claude Code 2.1.181이다. 임시 작업 폴더의 동명 CLI는 실행되지 않았으며 기존 Desktop 바로가기 해시와 bat를 보존했다.
- Chrome에서 공통 요청과 두 클라이언트 결과 표를 확인했다. console warn/error는 0개다.
- 스펙 리뷰와 품질 리뷰가 순서대로 통과했다. 독립 품질 검사에서 구현·과정 문서 12개 UTF-8·BOM 없음, PowerShell 8개 구문 및 추가 내용의 시크릿 패턴 검사가 통과했다. `git diff --check` exit 0이다. [전체 리뷰](../../reviews/2026-10-13-client-cli-setup-review.md)에 결과를 기록한다.
- 실제 설치·로그인·전역 지침 수정·새 대화형 세션·Terminal GUI·별도 PC의 OneDrive·공식 아이콘 신규 다운로드와 PNG 변환은 실행하지 않았다. 아이콘 경로 검증에는 임시 ICO fixture를 사용했으며 Claude 공식 이미지의 확인 증거로 간주하지 않는다.
