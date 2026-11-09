<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-13-codex-windows-setup 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-10-13-codex-windows-setup-design.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/specs/2026-10-13-codex-windows-setup-design.md).

<!-- Windows Codex 세팅에 공식 아이콘 바로가기 생성과 검증을 포함하는 승인 설계를 기록한다. -->
<a id="spec--windows-codex-세팅-설계"></a>
### Windows Codex 세팅 설계.

2026-10-13 사용자가 문서 연결 방식의 설계를 승인하고 구현·전체 커밋·푸시를 요청했다.

<a id="spec--목표와-기준선"></a>
#### 목표와 기준선.

현재 Quick Start는 지침 적용만 안내하며 별도 바로가기 문서는 기존 bat 전환을 전제한다. Windows에서 “이 저장소대로 Codex 세팅해줘”라는 요청은 전역 지침 배치와 공식 아이콘 Codex.lnk 생성·갱신·검증까지 포함하도록 연결한다. 단순 “지침 적용”의 기존 의미는 보존한다.

<a id="spec--흐름과-책임"></a>
#### 흐름과 책임.

README.md와 GETTING_STARTED.md는 세팅 프롬프트와 완료 조건을 안내한다. AGENTS.md와 codex-global-AGENTS.md는 Windows Codex 세팅 요청을 해당 안내로 연결한다. references/codex-windows-shortcut.md는 실행 절차의 단일 출처다. index.html은 사람용 안내를 맞추고 CHANGELOG.md는 변경 이력을 기록한다.

1. 전역 지침을 배치한다. 기존 사용자 지침을 읽고 보존하며 충돌을 해결한다.
2. Codex CLI·Windows Terminal·작업 폴더를 확인한다.
3. 공식 아이콘을 재사용하거나 공식 출처에서 준비한다.
4. Windows API로 얻은 실제 바탕화면에 Codex.lnk를 생성한다. 기존 바로가기는 내용을 확인하고 갱신한다.
5. 실행 대상·인자·작업 폴더·아이콘과 실제 실행을 검증한다.

<a id="spec--오류와-경계"></a>
#### 오류와 경계.

CLI·Windows Terminal 누락, 아이콘 준비 실패, 바로가기 저장 실패, 실행 실패는 미완료로 보고한다. 필요한 준비 항목을 명시하며 실패를 건너뛰어 완료하지 않는다. 기본 작업 폴더는 실제 바탕화면 아래 Agent이며 사용자가 지정한 폴더가 있으면 그 폴더를 우선한다. 재실행은 동일 바로가기를 확인하고 갱신한다. 기존 bat와 무관한 파일은 삭제하지 않는다.

CLI·Windows Terminal 자동 설치, 타사 스킬·MCP 일괄 설치, 아이콘 바이너리 배포, 현재 PC 전역 지침 동기화는 범위 밖이다. 아이콘은 공식 출처를 확인하고 사용자 전역 assets에 보관하며 개인 설정·토큰은 커밋하지 않는다.

<a id="spec--검증과-완료-조건"></a>
#### 검증과 완료 조건.

문서 링크·Markdown 펜스·HTML 구조, PowerShell 구문, 생성·갱신·누락 전제·검증 실패를 확인한다. 임시 폴더에서 실제 Windows COM 바로가기 생성·읽기를 검증하며 바탕화면 바로가기는 변경하지 않는다. 실제 Codex CLI 버전 명령과 HTML 화면을 확인한다. Terminal GUI 새 탭·대화형 세션과 별도 PC 검증 여부는 결과에서 구분한다. 실제 환경 세팅의 완료 조건에는 새 세션 실행 확인을 포함한다. 전체 diff를 스펙 준수 후 품질 순으로 리뷰하고 git diff --check를 통과시킨다. 관련 변경을 한글 커밋으로 묶어 main에 반영하고 일반 push 후 원격·로컬 해시를 대조한다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-13-codex-windows-setup.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-13-codex-windows-setup.md).

<!-- Windows Codex 세팅 안내를 구현하고 검증·리뷰·커밋·푸시하는 계획을 기록한다. -->
<a id="plan--windows-codex-세팅-구현-계획"></a>
### Windows Codex 세팅 구현 계획.

For agentic workers: REQUIRED SUB-SKILL: subagent-driven-development. 단계는 체크박스로 관리한다.

<a id="plan--goal"></a>
#### Goal.

승인 설계에 따라 Windows Codex 세팅 요청에 공식 아이콘 바로가기 생성·검증을 포함한다. 사용자의 구현 요청은 설계에 따른 실행과 전체 커밋·푸시를 승인한다.

<a id="plan--architecture"></a>
#### Architecture.

기존 안내와 PowerShell 예제를 재사용한다. 실행 절차는 references/codex-windows-shortcut.md에 두고 다른 문서는 연결한다. 독립 설치 프로그램이나 의존성을 추가하지 않는다.

<a id="plan--tech-stack"></a>
#### Tech Stack.

Markdown, HTML, Windows PowerShell, WScript.Shell COM, Git. 문서 변경은 정합성 검사로 검증하며 PowerShell 예제는 임시 경로에서 실제 동작을 확인한다.

<a id="plan--task-1-세팅-동선과-바로가기-절차-연결"></a>
#### Task 1. 세팅 동선과 바로가기 절차 연결.

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

<a id="plan--task-2-검증리뷰"></a>
#### Task 2. 검증·리뷰.

Files: Verify Task 1 files and this plan; Create docs/reviews/2026-10-13-codex-windows-setup-review.md.

- [x] 상대 링크·앵커·코드 펜스·HTML 구조와 문서 간 완료 조건을 검사한다. 누락은 0개여야 한다.
- [x] 모든 PowerShell 예제를 Parser.ParseInput으로 검사한다. 파서 오류는 0개여야 한다.
- [x] 임시 폴더에서 생성·갱신·누락 전제·검증 실패를 검사한다. COM에서 읽은 TargetPath·Arguments·WorkingDirectory·IconLocation을 기대값과 대조한다. `codex --version` 실행도 확인한다.
- [x] HTML을 브라우저에서 열고 세팅 설명과 링크를 확인한다.
- [x] 스펙 리뷰 후 품질 리뷰를 수행하고 발견 사항을 해결한다.
- [x] `git diff --check`를 실행한다. exit 0이어야 한다.
- [x] 이 계획과 리뷰 기록에 실제 결과·제한을 반영한다.

<a id="plan--커밋통합-절차"></a>
#### 커밋·통합 절차.

검증을 마친 관련 10개 문서만 스테이징하고 한글 제목·빈 줄·bullet 본문을 파일로 작성해 `git commit --file`로 커밋한다. 원본 main 작업 트리가 깨끗한지 확인하고 작업 브랜치를 main에 fast-forward한 뒤 `git push origin main`으로 일반 push한다. `git ls-remote origin refs/heads/main`과 `git rev-parse HEAD`를 비교하고 작업 트리 상태를 확인한다. 커밋·푸시의 실행 결과는 이후 Git 이력과 원격 브랜치에서 확인한다.

<a id="plan--검증-증거"></a>
#### 검증 증거.

- 대상 문서 7개를 UTF-8로 검사했고 로컬 링크·앵커 81개, 코드 펜스, HTML id 검사에서 누락은 0개였다.
- PowerShell 예제 4개의 Parser.ParseInput 오류는 0개였다.
- 임시 경로에서 실제 WScript.Shell COM 생성·갱신과 실패 처리 18건이 통과했다. 사용자 지정 폴더, 드라이브 루트, OneDrive를 모의한 경로, 공백·쉼표·작은따옴표·한글·세미콜론을 확인했다.
- 작업 폴더의 동명 codex.cmd가 실행되는 문제를 수정 전 실패·수정 후 통과로 확인했다. CLI Source 전체 경로로 실행을 고정했다.
- Windows CommandLineToArgvW와 Terminal의 인자 재구성·세미콜론 역변환을 거친 숨긴 cmd 프로세스에서 실제 CLI와 특수 경로의 임시 CLI 실행이 통과했다. 실제 CLI 버전은 0.162.1이었다.
- Chrome에서 HTML의 세팅 설명·링크·배치를 확인했고 console warn/error는 0개였다.
- 스펙·품질 재리뷰가 통과했고 동명 CLI, 루트 경로, 세미콜론 문제를 해결했다. git diff --check가 exit 0으로 통과했다.
- 현재 바탕화면 바로가기의 파일 해시가 보존됐다. 현재 전역 지침·아이콘을 변경하거나 CLI·Terminal을 설치하지 않았다.
- 별도 PC의 실제 OneDrive, Terminal GUI 새 탭과 대화형 Codex 세션, 공식 아이콘 신규 다운로드·PNG 변환은 실행하지 않았다. 이 저장소 변경은 환경 세팅 절차의 문서와 예제를 제공하며, 실제 세팅 시 해당 확인을 수행하고 미검증이면 미완료로 보고하도록 명시했다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-13-codex-windows-setup-review.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-13-codex-windows-setup-review.md).

<!-- Windows Codex 세팅 안내 변경의 전체 리뷰와 검증 결과를 기록한다. -->
<a id="review--windows-codex-세팅-리뷰"></a>
### Windows Codex 세팅 리뷰.

기준선은 1de591f83b252ec5ab9212c4f314517036f29b3d다. 승인된 안내 문서 7개와 설계·계획을 검토했다. 별도 스펙 리뷰 후 품질 리뷰를 수행했고 발견 사항 수정과 재리뷰가 통과했다.

<a id="review--해결한-발견-사항"></a>
#### 해결한 발견 사항.

1. 확인한 CLI Source와 bare codex 호출이 달라 작업 폴더의 동명 파일이 실행될 수 있었다. 버전 검사와 생성·검증 인자 모두 확인된 CLI 전체 경로로 고정했다. 동명 cmd 파일의 실패 코드로 문제를 재현한 뒤 수정 후 통과를 확인했다.
2. 드라이브 루트의 끝 역슬래시가 WT의 닫는 따옴표를 이스케이프했다. WT 인자용 작업 폴더에 `\.`을 붙이고 COM WorkingDirectory는 원래 경로를 유지했다.
3. 경로 내 세미콜론이 WT 명령 분리자로 처리됐다. WT에 전달하는 작업 폴더·CLI 경로에 `\;` 이스케이프를 적용했다. 버전 검사는 WT를 거치지 않으므로 원래 Source를 사용한다.

인자 전달 검증은 [Microsoft Terminal 인자 파서](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/AppCommandlineArgs.cpp)와 [Commandline의 역변환](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/Commandline.cpp)을 확인한 뒤 Windows의 실제 argv 파싱과 숨긴 cmd 프로세스로 수행했다.

<a id="review--검증-결과"></a>
#### 검증 결과.

- UTF-8·코드 펜스·로컬 링크·Markdown 및 HTML 앵커 검사 통과, 대상 7개 문서의 링크·앵커 81개 누락 0개다.
- PowerShell 예제 4개 구문 오류 0개다.
- 실제 Windows COM 생성·갱신·실패 검사 18건이 통과했다. 실제 바탕화면 바로가기의 해시와 기존 bat를 보존했다.
- 사용자 지정 폴더, 드라이브 루트, 공백·쉼표·작은따옴표·한글·세미콜론과 동명 CLI 사례를 확인했다. 인자 재구성 후 실제 Codex CLI 0.162.1 및 임시 CLI 실행이 통과했다.
- Chrome의 새 안내 배치와 링크를 확인했고 console warn/error는 0개다.
- git diff --check 통과, 스펙·품질 재리뷰의 미해결 고확신 발견 사항은 없다.

<a id="review--검증-범위"></a>
#### 검증 범위.

별도 PC의 실제 OneDrive, Terminal GUI 새 탭·대화형 Codex 세션, 공식 아이콘 신규 다운로드·PNG 변환은 실행하지 않았다. 현재 전역 지침과 바탕화면은 변경하지 않았다. 실제 세팅 요청에서는 문서에 따라 새 세션·아이콘 출처를 확인하고 미검증 항목을 미완료로 보고한다.
