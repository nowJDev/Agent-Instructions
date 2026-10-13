<!-- Windows Codex 세팅 안내를 구현하고 검증·리뷰·커밋·푸시하는 계획을 기록한다. -->
# Windows Codex 세팅 구현 계획.

For agentic workers: REQUIRED SUB-SKILL: subagent-driven-development. 단계는 체크박스로 관리한다.

## Goal.

승인 설계에 따라 Windows Codex 세팅 요청에 공식 아이콘 바로가기 생성·검증을 포함한다. 사용자의 구현 요청은 설계에 따른 실행과 전체 커밋·푸시를 승인한다.

## Architecture.

기존 안내와 PowerShell 예제를 재사용한다. 실행 절차는 references/codex-windows-shortcut.md에 두고 다른 문서는 연결한다. 독립 설치 프로그램이나 의존성을 추가하지 않는다.

## Tech Stack.

Markdown, HTML, Windows PowerShell, WScript.Shell COM, Git. 문서 변경은 정합성 검사로 검증하며 PowerShell 예제는 임시 경로에서 실제 동작을 확인한다.

## Task 1. 세팅 동선과 바로가기 절차 연결.

Files: Modify README.md, GETTING_STARTED.md, AGENTS.md, codex-global-AGENTS.md, references/codex-windows-shortcut.md, index.html, CHANGELOG.md.

- [x] 수정 대상 전체를 UTF-8로 읽는다.
- [x] README·적용 안내·HTML에 아래 세팅 요청을 추가한다.

```text
이 저장소대로 Windows Codex 환경을 세팅해줘.
전역 지침 배치와 공식 아이콘 Codex.lnk 생성·검증까지 진행해줘.
GETTING_STARTED.md와 references/codex-windows-shortcut.md를 따라줘.
https://github.com/nowJDev/Agent-Instructions
```

- [x] 루트·전역 지침에 Windows Codex 세팅 요청의 실행 문서 연결을 추가한다.
- [x] 실제 바탕화면 경로를 `[Environment]::GetFolderPath('DesktopDirectory')`로 구한다. 사용자 지정 작업 폴더를 우선하며 CLI·Terminal·아이콘·작업 폴더를 생성 전에 확인한다.
- [x] 기존 바로가기를 확인하고 동일 경로를 갱신한다. 기존 bat는 보존한다. 검증 예제는 항목을 검사해 실패 시 throw한다.
- [x] CHANGELOG에 2026-10-13 변경을 기록한다.

## Task 2. 검증·리뷰.

Files: Verify Task 1 files and this plan; Create docs/reviews/2026-10-13-codex-windows-setup-review.md.

- [x] 상대 링크·앵커·코드 펜스·HTML 구조와 문서 간 완료 조건을 검사한다. 누락은 0개여야 한다.
- [x] 모든 PowerShell 예제를 Parser.ParseInput으로 검사한다. 파서 오류는 0개여야 한다.
- [x] 임시 폴더에서 생성·갱신·누락 전제·검증 실패를 검사한다. COM에서 읽은 TargetPath·Arguments·WorkingDirectory·IconLocation을 기대값과 대조한다. `codex --version` 실행도 확인한다.
- [x] HTML을 브라우저에서 열고 세팅 설명과 링크를 확인한다.
- [x] 스펙 리뷰 후 품질 리뷰를 수행하고 발견 사항을 해결한다.
- [x] `git diff --check`를 실행한다. exit 0이어야 한다.
- [x] 이 계획과 리뷰 기록에 실제 결과·제한을 반영한다.

## 커밋·통합 절차.

검증을 마친 관련 10개 문서만 스테이징하고 한글 제목·빈 줄·bullet 본문을 파일로 작성해 `git commit --file`로 커밋한다. 원본 main 작업 트리가 깨끗한지 확인하고 작업 브랜치를 main에 fast-forward한 뒤 `git push origin main`으로 일반 push한다. `git ls-remote origin refs/heads/main`과 `git rev-parse HEAD`를 비교하고 작업 트리 상태를 확인한다. 커밋·푸시의 실행 결과는 이후 Git 이력과 원격 브랜치에서 확인한다.

## 검증 증거.

- 대상 문서 7개를 UTF-8로 검사했고 로컬 링크·앵커 81개, 코드 펜스, HTML id 검사에서 누락은 0개였다.
- PowerShell 예제 4개의 Parser.ParseInput 오류는 0개였다.
- 임시 경로에서 실제 WScript.Shell COM 생성·갱신과 실패 처리 18건이 통과했다. 사용자 지정 폴더, 드라이브 루트, OneDrive를 모의한 경로, 공백·쉼표·작은따옴표·한글·세미콜론을 확인했다.
- 작업 폴더의 동명 codex.cmd가 실행되는 문제를 수정 전 실패·수정 후 통과로 확인했다. CLI Source 전체 경로로 실행을 고정했다.
- Windows CommandLineToArgvW와 Terminal의 인자 재구성·세미콜론 역변환을 거친 숨긴 cmd 프로세스에서 실제 CLI와 특수 경로의 임시 CLI 실행이 통과했다. 실제 CLI 버전은 0.162.1이었다.
- Chrome에서 HTML의 세팅 설명·링크·배치를 확인했고 console warn/error는 0개였다.
- 스펙·품질 재리뷰가 통과했고 동명 CLI, 루트 경로, 세미콜론 문제를 해결했다. git diff --check가 exit 0으로 통과했다.
- 현재 바탕화면 바로가기의 파일 해시가 보존됐다. 현재 전역 지침·아이콘을 변경하거나 CLI·Terminal을 설치하지 않았다.
- 별도 PC의 실제 OneDrive, Terminal GUI 새 탭과 대화형 Codex 세션, 공식 아이콘 신규 다운로드·PNG 변환은 실행하지 않았다. 이 저장소 변경은 환경 세팅 절차의 문서와 예제를 제공하며, 실제 세팅 시 해당 확인을 수행하고 미검증이면 미완료로 보고하도록 명시했다.
