<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-13-client-cli-setup 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-10-13-client-cli-setup-design.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/specs/2026-10-13-client-cli-setup-design.md).

<!-- 실행 중인 AI에 맞춰 최소 CLI 세팅을 선택하는 승인 설계를 기록한다. -->
<a id="spec--클라이언트별-최소-cli-세팅-설계"></a>
### 클라이언트별 최소 CLI 세팅 설계.

사용자는 “이거대로 세팅해줘” 요청을 현재 AI 클라이언트에 맞게 처리하는 설계를 승인했다. 기능 범위는 CLI를 사용할 수 있는 수준이다. 문서 기반 분기 방식을 구현하며 이전 커밋·푸시 요청을 이어서 적용한다.

<a id="spec--목표와-기준선"></a>
#### 목표와 기준선.

기준선은 dfac16764d14afce23fafd4a2a80fa6ad2ddabc1다. Codex 세팅은 기본 진입점과 별도 바로가기 예제가 있지만 CLI·Terminal 기설치를 전제한다. Claude Code 가이드는 외부 dotfiles와 확장 기능에 의존한다. 이를 공통 최소 세팅 진입점과 클라이언트별 준비 절차로 연결한다.

<a id="spec--선택과-흐름"></a>
#### 선택과 흐름.

사용자가 대상 클라이언트를 지정하면 우선한다. 지정하지 않으면 신뢰할 수 있는 실제 세션의 클라이언트 정보를 확인한다. 모델 이름이나 설치된 CLI 목록은 판별 근거가 아니다. 판별 불가면 한 번 질문하고 대상이 결정될 때까지 설치·설정 변경을 하지 않는다. Codex와 Claude Code가 함께 설치돼 있어도 선택한 하나만 처리한다.

1. 선택한 CLI의 설치 여부를 확인하고 있으면 재사용한다. 없으면 현재 공식 설치 절차를 따른다.
2. CLI 전체 경로와 버전 실행을 확인한다. 설치 직후 명령이 보이지 않으면 새 터미널·PATH 확인 후 다시 검증한다.
3. 기존 사용자 지침을 확인·보존하고 기본 작업 지침을 전역 AGENTS.md 또는 CLAUDE.md에 연결한다.
4. 실제 바탕화면·사용자 지정 작업 폴더·공식 제품 아이콘으로 선택한 CLI의 바로가기를 생성하거나 갱신한다.
5. Windows Terminal을 사용할 수 있으면 재사용하고 없으면 기본 cmd를 쓴다. CLI Source 전체 경로, UTF-8, 경로 인용, 기존 bat 보존과 속성 검증을 유지한다.
6. 실제 실행·새 세션 지침 로드와 로그인 여부를 확인한다. 로그인이 필요하면 사용자 인증 단계로 안내하고 미완료 항목으로 보고한다.

<a id="spec--책임과-범위"></a>
#### 책임과 범위.

GETTING_STARTED.md가 선택·설치·지침·완료 조건을 담당한다. references/windows-cli-shortcut.md에 두 클라이언트의 공통 Windows 생성·검증 예제를 둔다. 기존 codex-windows-shortcut.md 주소는 Codex 진입 안내로 유지한다. 기존 claude-code-cli-setup.md에는 최소 흐름을 우선 안내하고 외부 설정·확장 설치는 명시적 추가 요청으로 한정한다. README, 루트·전역 지침, PORTABILITY, HTML과 CHANGELOG의 안내를 맞춘다.

스킬·MCP·플러그인·Hooks·테마·상태줄·권한 변경·bypass 옵션을 기본 세팅에서 제외한다. 별도 통합 설치 프로그램이나 의존성을 추가하지 않는다. 현재 PC의 CLI 설치·로그인·전역 지침·바탕화면 변경은 이 저장소 구현 작업에 포함하지 않는다.

<a id="spec--실패와-검증"></a>
#### 실패와 검증.

설치 실패, 미지원 OS·클라이언트, 실행 파일·아이콘·작업 폴더 누락, 지침 충돌, 로그인 대기와 실행 실패를 개별 미완료로 보고한다. 기존 지침과 바로가기를 확인·보존하고 반복 실행 시 동일 파일만 갱신한다. 아이콘은 공식 출처를 확인해 사용자 영역에 준비하며 바이너리·인증 자료는 저장소에 넣지 않는다.

문서 링크·앵커·인코딩·펜스와 PowerShell 파서를 검사한다. 임시 경로에서 Codex·Claude Code와 WT·cmd 분기 4가지를 검증하고 기존 Codex의 생성·갱신·실패·루트·세미콜론·동명 CLI 회귀도 확인한다. 실제 CLI 버전 명령과 HTML 렌더링을 확인한다. 설치·로그인·실제 Terminal GUI·별도 PC 검증 여부는 결과에 명시한다. 스펙→품질 리뷰 후 관련 변경을 커밋·main에 반영·일반 push하고 원격 해시를 대조한다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-13-client-cli-setup.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-13-client-cli-setup.md).

<!-- 클라이언트별 최소 CLI 세팅 안내의 구현과 검증 계획을 기록한다. -->
<a id="plan--클라이언트별-최소-cli-세팅-구현-계획"></a>
### 클라이언트별 최소 CLI 세팅 구현 계획.

For agentic workers: REQUIRED SUB-SKILL: subagent-driven-development. 승인 설계에 따른 실행·검증·전체 커밋·푸시를 진행한다.

<a id="plan--goal"></a>
#### Goal.

“이거대로 세팅해줘”를 현재 Codex 또는 Claude Code의 최소 CLI 세팅 요청으로 연결한다.

<a id="plan--architecture"></a>
#### Architecture.

설치·선택·지침은 GETTING_STARTED.md, 공통 Windows 바로가기 실행은 references/windows-cli-shortcut.md에 둔다. 이전 Codex 문서 주소를 유지하며 Claude 확장 설치와 기본 설치를 구분한다. 새 설치기는 작성하지 않는다.

<a id="plan--tech-stack"></a>
#### Tech Stack.

Markdown, HTML, Windows PowerShell, WScript.Shell COM, Git. CLI 설치 명령은 공식 문서로 확인하며 검증 중 실제 설치나 로그인은 수행하지 않는다.

<a id="plan--task-1-공통-진입점과-두-클라이언트-안내"></a>
#### Task 1. 공통 진입점과 두 클라이언트 안내.

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

<a id="plan--task-2-검증리뷰"></a>
#### Task 2. 검증·리뷰.

Files: Verify Task 1 files and process documents. Create docs/reviews/2026-10-13-client-cli-setup-review.md.

- [x] 변경 전 검사로 공통 요청·Claude 공식 아이콘·cmd 대체 분기 누락을 확인한다.
- [x] UTF-8, 코드 펜스, 상대 링크·앵커와 HTML 구조를 검사한다. 누락 0개여야 한다.
- [x] 모든 새 PowerShell 예제의 Parser.ParseInput 오류가 0개인지 확인한다.
- [x] 임시 경로에서 두 클라이언트×WT·cmd 4분기의 실제 COM 생성·검증, 버전 실행, 기존 바로가기 갱신과 bat 보존을 확인한다.
- [x] 누락된 CLI·아이콘·폴더, 잘못된 속성, 동명 CLI, 공백·한글·쉼표·세미콜론·드라이브 루트 회귀를 확인한다.
- [x] HTML의 공통 요청과 결과 표를 브라우저에서 확인한다.
- [x] 스펙 리뷰 후 품질 리뷰를 수행하고 발견 사항을 해결한다.
- [x] `git diff --check` exit 0과 실제 검증 증거를 기록한다.

<a id="plan--커밋통합-절차"></a>
#### 커밋·통합 절차.

검증한 관련 문서만 한글 제목·빈 줄·bullet 본문으로 커밋한다. 깨끗한 원본 main에 fast-forward하고 origin/main에 일반 push한다. `git ls-remote origin refs/heads/main`과 로컬 HEAD를 비교한다. 커밋·푸시 결과는 이후 Git 이력과 원격 브랜치에서 확인한다.

<a id="plan--검증-증거"></a>
#### 검증 증거.

- 기준선에서 공통 요청 문구와 공통 바로가기 문서 누락을 확인한 뒤 구현 후 같은 문서 검사가 통과했다.
- 구현 문서 10개 UTF-8·BOM 없음·코드 펜스·로컬 링크 및 앵커 94개 누락 0개다. PowerShell 블록 8개 파서 오류 0개다.
- 두 클라이언트×WT·CMD 4분기에서 실제 Windows COM 생성·갱신·독립 검증을 통과했다. 기본·사용자·드라이브 루트 폴더와 동명 CLI를 포함한 숨긴 CLI 실행 24회, 실패 조건 37개가 통과했다. 검증 횟수는 최종 assert로 확인했다.
- 실제 CLI 버전은 Codex CLI 0.162.1과 Claude Code 2.1.181이다. 임시 작업 폴더의 동명 CLI는 실행되지 않았으며 기존 Desktop 바로가기 해시와 bat를 보존했다.
- Chrome에서 공통 요청과 두 클라이언트 결과 표를 확인했다. console warn/error는 0개다.
- 스펙 리뷰와 품질 리뷰가 순서대로 통과했다. 독립 품질 검사에서 구현·과정 문서 12개 UTF-8·BOM 없음, PowerShell 8개 구문 및 추가 내용의 시크릿 패턴 검사가 통과했다. `git diff --check` exit 0이다. [전체 리뷰](#review)에 결과를 기록한다.
- 실제 설치·로그인·전역 지침 수정·새 대화형 세션·Terminal GUI·별도 PC의 OneDrive·공식 아이콘 신규 다운로드와 PNG 변환은 실행하지 않았다. 아이콘 경로 검증에는 임시 ICO fixture를 사용했으며 Claude 공식 이미지의 확인 증거로 간주하지 않는다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-13-client-cli-setup-review.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-13-client-cli-setup-review.md).

<!-- 클라이언트별 최소 CLI 세팅 안내의 전체 리뷰와 검증 결과를 기록한다. -->
<a id="review--클라이언트별-최소-cli-세팅-리뷰"></a>
### 클라이언트별 최소 CLI 세팅 리뷰.

기준선은 dfac16764d14afce23fafd4a2a80fa6ad2ddabc1다. 승인된 안내 문서 10개와 설계·계획을 전체 검토했다. 별도 스펙 리뷰 후 품질 리뷰가 통과했으며 미해결 고확신 발견 사항은 없다. 독립 설치 프로그램을 추가하지 않고 기존 Codex 바로가기 예제를 공통 문서로 옮겨 Claude Code와 CMD 분기를 반영했다.

<a id="review--확인해결한-사항"></a>
#### 확인·해결한 사항.

- 명시 대상 우선, 신뢰할 수 있는 현재 세션의 클라이언트 정보와 판별 불가 시 한 번 질문 규칙을 모든 진입점에 맞췄다. 둘 다 설치돼 있어도 선택한 하나만 설정한다.
- 기존 전역 지침 백업·보존 병합, Claude import 중복 방지, 공식 아이콘, 실제 실행·지침 로드·인증과 미완료 보고를 확인했다. 기존 Codex 주소를 유지하고 Claude 확장은 명시적 추가 요청의 선택 항목으로 제한했다.
- 신규 공통 문서 일부가 작성 중 한글 인코딩을 잃어 UTF-8로 복구한 뒤 전체 인코딩·실행 검사를 다시 통과했다. 검증 도구의 횟수 집계 범위 오류도 수정하고 최종 횟수를 assert로 확인했다.
- 설치 명령은 [Codex 공식 원문](https://learn.chatgpt.com/docs/codex/cli.md), [Claude 공식 설치 안내](https://code.claude.com/docs/en/setup), 상대 import와 `/context`는 [Claude 공식 memory 문서](https://code.claude.com/docs/en/memory)로 대조했다. 실제 설치는 실행하지 않았다.

<a id="review--검증-결과"></a>
#### 검증 결과.

- 구현 문서 10개 UTF-8·BOM 없음·코드 펜스·로컬 링크 및 앵커 94개 누락 0개다. 독립 품질 검사에서도 구현·과정 문서 12개 인코딩·펜스와 추가 내용의 시크릿 패턴 검사가 통과했다.
- GETTING_STARTED와 공통 바로가기의 PowerShell 블록 8개 파서 오류 0개다.
- Codex·Claude Code 각각 WT·CMD 4분기의 실제 Windows COM 생성·갱신·독립 속성 검증이 통과했다. 기본·사용자·드라이브 루트 작업 폴더와 실제 CLI·특수 경로 임시 CLI의 숨긴 실행 24회, 실패 조건 37개가 통과했다.
- CLI 버전은 Codex CLI 0.162.1과 Claude Code 2.1.181이다. 공백·쉼표·작은따옴표·한글·세미콜론·앰퍼샌드 경로와 동명 CLI를 확인했다. 확인된 Source 전체 경로가 실행되며 작업 폴더의 동명 CLI는 실행되지 않았다.
- 인자 검증은 Windows argv 파싱과 [Terminal 인자 파서](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/AppCommandlineArgs.cpp)·[역변환](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/Commandline.cpp)에 따른 숨긴 CMD 실행으로 수행했다. 실제 Terminal GUI 실행 증거와 구분한다.
- 기존 실제 Desktop 바로가기 해시와 임시 bat를 보존했다. Chrome에서 공통 요청과 두 클라이언트 결과 표를 확인했고 console warn/error는 0개다. 검증용 탭과 로컬 서버를 정리했다.
- 최종 관련 문서 13개의 인코딩·펜스·로컬 링크 및 앵커 95개 검사와 `git diff --check`가 통과했다. 스펙·품질 리뷰 PASS다.

<a id="review--검증-범위"></a>
#### 검증 범위.

현재 PC의 CLI 설치·로그인·전역 지침·실제 Desktop을 변경하지 않았다. 실제 설치·인증 후 새 세션 지침 로드·대화형 CLI 실행·Terminal GUI·별도 PC의 OneDrive·공식 아이콘 신규 다운로드·PNG 변환은 미검증이다. ICO는 임시 fixture로 경로·속성을 검증했으며 Claude 공식 이미지 확인 증거가 아니다.

실제 사용자 세팅에서는 문서에 따라 공식 아이콘 출처·바로가기 실행·지침 로드·사용자 인증을 확인하고 남은 항목을 미완료로 보고해야 한다. 이번 완료 범위는 저장소 안내 구현과 위 검증이다.
