<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-14-beginner-readme-and-audit-fixes 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-10-14-beginner-readme-and-audit-fixes.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/specs/2026-10-14-beginner-readme-and-audit-fixes.md).

<!-- 승인된 리뷰 수정과 입문자용 README의 목적과 경계를 기록한다. -->
<a id="spec--리뷰-발견-수정과-입문자용-readme-설계"></a>
### 리뷰 발견 수정과 입문자용 README 설계.

<a id="spec--승인과-기준선"></a>
#### 승인과 기준선.

기준선은 `3c4c082`다. 사용자는 직전 전체 리뷰의 네 가지 발견 사항을 수정하고, README 전체를 AI 입문자가 이해할 수준으로 변경하도록 실행을 요청했다. 직전 리뷰에서 제시한 최소 수정안을 실행 범위로 사용한다. 구조도는 이해에 도움이 됐다는 사용자 의견을 반영해 유지한다. 검증한 논리 단위로 한글 커밋을 작성하고 푸시는 보류한다.

<a id="spec--동작과-책임"></a>
#### 동작과 책임.

- 업로드 전 실제 저장소가 비공개인지 확인한다. 기존 공개 저장소는 자동 변경하지 않고 중단한다. 실패하거나 공개 여부를 확인하지 못해도 업로드하지 않는다.
- 세션 업로드는 사용자가 승인한 프로젝트·세션 파일만 별도 로컬 폴더에 준비하고 민감정보를 제거한 뒤 실행한다. 전역 세션 폴더와 원격 프로젝트 이름을 필터로 오해하는 안내를 제거한다.
- 완료 검사는 코드 예시를 제외한 명시적 목록·인용 안의 미완료 체크박스도 검사한다. 기존 코드 예시·컨테이너 경계 처리는 보존한다.
- Claude 로컬 지침의 검색·설명에 공식 파일명 `CLAUDE.local.md`를 사용한다.
- README는 목적, 복사해서 시작하기, 작업 흐름, 쉬운 용어, 필요한 문서 찾기 순서로 재작성한다. 설정 상세·전체 카탈로그는 기존 문서로 연결하고 기존 설치·인증·환경 차이 계약을 보존한다. README 제목 변경의 직접 참조도 갱신한다.
- 사용자의 추가 요청에 따라 사람용 `index.html`의 상세 내용을 `GUIDE.md`로 옮기고 README에서 연결한다. README는 시작 안내, GUIDE는 사람용 상세 설명, AGENTS와 rules는 AI 작업 규칙으로 구분한다. 기존 HTML의 설명은 현재 규칙에 맞추고 Markdown 체크리스트의 정적 성격을 설명한다. HTML 파일은 변환 검증 후 개별 삭제한다.

<a id="spec--비목표와-검증"></a>
#### 비목표와 검증.

실제 업로드·공개 여부 변경·전역 설치·개인 설정·로그인·외부 게시를 수행하지 않는다. 타사 스킬 원본을 개편하지 않는다. 테스트는 임시 프로젝트와 인증 없는 가짜 API로만 실행한다. 미완료 세 가지 상태와 목록·인용 순서, fenced·inline 예시의 정상 통과를 확인한다. 업로드 예시는 비공개·공개·조회 실패와 준비 폴더의 전송 범위를 검증한다. 전체 회귀, Python 예제 문법, 인코딩·링크·앵커·fence, README·GUIDE 문장과 그림을 검토한다. 미검증 범위와 검증 증거는 리뷰 문서에 기록한다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-14-beginner-readme-and-audit-fixes.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-14-beginner-readme-and-audit-fixes.md).

<!-- 리뷰 수정과 README 재작성의 실행 순서와 검증 기준을 기록한다. -->
<a id="plan--리뷰-수정과-입문자용-readme-실행-계획"></a>
### 리뷰 수정과 입문자용 README 실행 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 독립된 문서 영역은 `rules/02`에 따라 위임하고 전체 diff를 통합 검토한다.

Goal: 승인된 네 가지 결함을 해결하고 README 전체를 AI 입문자용으로 재작성한다.
Architecture: 기존 카탈로그와 표준 라이브러리 기반 검증기를 유지한다. [설계](#spec)의 범위만 수정한다.
Tech Stack: Markdown, Python unittest, Mermaid, Git, Windows PowerShell.

<a id="plan--task-1-완료-검사"></a>
#### Task 1. 완료 검사.

Files: `tests/test_workflow_markdown.py`, `Owned-Skills/design-driven-delivery/scripts/validate_workflow.py`, `Owned-Skills/design-driven-delivery/references/document-contracts.md`.

- [x] 미완료 세 상태와 컨테이너 6종의 18개 사례에서 기존 exit 0 누락을 RED로 확인했다.
- [x] 명시적 목록·인용 접두사를 검사하며 코드 예시를 제외한다. 독립 검토의 재귀 fence 오탐 3개도 RED 후 동일한 컨테이너 순서로 처리해 해결했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_workflow_markdown.py -v`의 Markdown 회귀 22개 GREEN, 문서 계약과 독립 리뷰를 확인했다. 검증한 코드·회귀·문서를 함께 커밋한다.

<a id="plan--task-2-업로드-경계와-지침-파일명"></a>
#### Task 2. 업로드 경계와 지침 파일명.

Files: `Skill/huggingface-skills/huggingface-datasets.md`, `Skill/huggingface-skills/huggingface-lora-space-builder.md`, `Skill/claude-md-management/claude-md-improver.md`, 필요하면 문서 예제 회귀 테스트.

- [x] 공식 계약을 확인하고 기존 Space 예시의 비공개 확인 누락을 인증 없는 fixture의 실패 12건으로 재현했다.
- [x] 두 업로드 예시는 `repo_info(...).private is True` 확인 후 진행한다. 조회 오류는 전파하며 기존 공개 저장소를 변경하지 않는다.
- [x] 전역 세션 폴더 업로드 대신 승인·민감정보 제거를 마친 별도 폴더를 사용한다. `CLAUDE.local.md` 검색·설명과 전역 지침의 별도 조회를 수정했다.
- [x] 실제 문서 예제를 실행하는 회귀 4개와 전체 64개 테스트가 통과했다. 독립 검토의 비공개 guard·전송 폴더 변이 검사도 결함을 검출했다. 예제 문법·파일명 검색과 diff를 확인한 뒤 커밋한다.

<a id="plan--task-3-readme-전체-재작성"></a>
#### Task 3. README 전체 재작성.

Files: `README.md`, `GUIDE.md`, 삭제할 `index.html`과 제목 변경의 직접 참조가 있는 `AGENTS.md`, `codex-global-AGENTS.md`, `PORTABILITY.md`, `rules/02_tool-boundaries.md`.

- [x] 시작 프롬프트 두 종류와 쉬운 설명, 그림 두 개, 용어·문서 안내로 README 전체를 재작성했다. 긴 전체 목록과 설치 상세는 해당 문서로 연결한다.
- [x] 적용과 설치를 구분하고 설정 홈·기존 보존·인증·별도 확장 계약을 GUIDE와 GETTING_STARTED에서 유지한다. README의 설치 AI는 구체 절차를 반드시 읽도록 안내하며 직접 참조 4문서를 갱신했다.
- [x] 입문자 관점의 전체 읽기, 링크·앵커·그림의 소스 문법과 독립 리뷰를 확인했다. 실제 뷰어 렌더링은 검증 범위에서 제외하고 명시한다.
- [x] `index.html`의 상세 설명을 `GUIDE.md`로 변환해 README에서 연결했다. 정적 체크리스트와 AI 지침의 역할을 설명하며 원래 HTML은 개별 삭제했다. 과거 작업의 역사 참조는 보존한다.

<a id="plan--task-4-종료-검증과-기록"></a>
#### Task 4. 종료 검증과 기록.

Files: `CHANGELOG.md`, `docs/reviews/2026-10-14-beginner-readme-and-audit-fixes.md`, 이 계획.

- [x] 전체 64개 테스트 통과, 실패·스킵 0개를 확인했다. 예제 문법·UTF-8·BOM·LF·링크·앵커·fence와 git diff --check도 통과했다.
- [x] 코드·카탈로그·README·GUIDE와 연관 문서의 전체 변경을 독립 검토했다. 중첩 코드 예시 오탐 발견은 수정 후 대상 회귀와 추가 조건으로 재검증했다.
- [x] 논리 변경을 한글 커밋으로 저장했다. [검증 기록](#review)에 결과와 외부 서비스·전역 설치·뷰어 미검증 범위를 명시했다. 푸시는 실행하지 않고 로컬 작업을 보존한다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-14-beginner-readme-and-audit-fixes.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-14-beginner-readme-and-audit-fixes.md).

<!-- 네 가지 리뷰 발견 수정과 입문자 문서 개편의 검증 근거를 기록한다. -->
<a id="review--리뷰-수정과-입문자-문서-개편-검증"></a>
### 리뷰 수정과 입문자 문서 개편 검증.

<a id="review--범위와-승인"></a>
#### 범위와 승인.

기준선은 `3c4c082`다. 사용자는 읽기 전용 전체 리뷰에서 확인한 네 가지 결함의 수정과 README 전체의 쉬운 설명을 요청했다. 이후 사람용 HTML 상세 안내를 Markdown으로 바꾸고 README에서 연결하도록 추가 요청했다. [설계](#spec)와 [실행 계획](#plan)에 범위를 기록했다. 저장소 원본만 변경하고 논리 단위로 커밋했으며 푸시는 보류한다.

<a id="review--수정과-직접-검증"></a>
#### 수정과 직접 검증.

| 리뷰 발견 | 수정 | 증거 |
|---|---|---|
| 기존 공개 HF 저장소에서 private 생성 옵션이 무시됐다. | dataset·Space 예제는 실제 비공개 여부를 조회한 뒤 파일·secret을 전송한다. 공개·불명확한 결과·조회 오류는 중단한다. | 실제 문서 Python 예제를 가짜 SDK로 실행했다. guard 제거 변이는 assertion 8건으로 검출했다. |
| 프로젝트 이름을 붙여도 전역 세션 폴더 전체를 전송했다. | 승인된 프로젝트·세션만 선정하고 민감정보를 제거한 별도 폴더를 사용한다. 원격 경로가 필터가 아님을 명시한다. | 임시 승인 세션과 다른 프로젝트 세션을 분리해 업로드 원본을 확인했다. 전역 폴더로 되돌린 변이는 assertion 1건으로 검출했다. |
| 목록·인용 안의 미완료 체크 항목을 놓쳤다. | 코드 예시를 제외한 명시적 컨테이너 안의 세 상태를 검사한다. fence의 목록·인용 순서를 함께 추적한다. | 18개 누락 사례 RED 후 GREEN. 독립 리뷰의 중첩 fence 오탐 3개도 RED 후 회귀를 추가했다. |
| 로컬 지침 파일명이 잘못됐다. | 검색·설명에 CLAUDE.local.md를 사용하고 전역 지침의 별도 조회를 명시한다. | 실제 Git Bash find를 임시 정상·잘못된 파일 6개에 실행해 정상 4개만 선택했다. |

실제 업로드나 정보 유출을 발생시키지 않았다. 비공개 조회는 업로드 전 확인이며, 외부 관리자가 조회 후 공개 여부를 변경하는 동시 상황을 잠그는 기능은 아니다. 준비 폴더의 파일 승인과 민감정보 제거는 문서의 필수 준비 단계다.

<a id="review--문서-개편"></a>
#### 문서 개편.

README는 목적·복사할 요청 문장·작업 흐름·파일 역할·쉬운 용어·문서 찾기로 재작성했다. 그림 두 개와 시작 문장 두 종류를 유지했다. 사람이 읽는 자세한 설명은 GUIDE, AI가 따르는 규칙은 AGENTS와 rules로 연결한다. 설치를 수행하는 AI는 GETTING_STARTED와 공통 바로가기 절차를 반드시 읽도록 안내한다.

기존 index.html의 개요·설계 철학·구성·설치·사용·도구·규칙 관리·유지보수·공개 점검·한계·FAQ·라이선스를 GUIDE.md로 변환했다. 오래된 60줄 단정과 프로젝트 지식·실패 로그 안내는 현행 규칙에 맞췄다. Markdown 체크리스트가 정적이며 자동 검사·저장·설정 적용을 하지 않음을 명시했다. 변환 후 HTML은 개별 삭제하고 과거 계획·리뷰의 역사적 언급은 유지했다.

README 제목 변경의 직접 참조 4문서도 갱신했다. 사용자 지정 대상, 설정 홈, 기존 사용자 지침·설정 보존, CLI·아이콘·지침 로드·인증의 미완료 조건과 확장 별도 요청 계약을 유지했다.

<a id="review--자동독립-검증"></a>
#### 자동·독립 검증.

- 기준선 전체 테스트 57개 통과 후 새 회귀 7개를 추가했다.
- `python -X utf8 -B -m unittest discover -s tests -v`는 전체 64개 통과, 실패·스킵 0개다. 부모의 통합 실행은 23.631초다.
- Markdown 대상 회귀 22개와 업로드 예제 회귀 4개는 각각 통과했다. 테스트는 임시 파일·프로젝트·설정과 인증 없는 가짜 API를 사용했다.
- 독립 검토자는 parser의 1~4단계 목록·인용과 열린·닫힌 fence를 추가 720개 조건으로 검사했다. 업로드 guard·폴더의 변이 검증도 수행했다. 보고된 중첩 코드 예시 오탐은 해결하고 재검토했다.
- README·GUIDE·연관 지침을 전체 읽고 원래 HTML의 본문과 비교했다. 독립 문서 리뷰에서 중요 결함이 없었고 설치 상세를 GUIDE로 옮긴 마지막 변경도 재검토했다.
- 전체 문서의 UTF-8·BOM 없음·LF, Python 파일·예제 문법, JSON 예제, Markdown fence·로컬 링크·앵커 및 git diff --check를 검사했다.

공식 계약은 [HF create_repo](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.HfApi.create_repo), [HF repo_info](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.HfApi.repo_info), [Claude memory](https://code.claude.com/docs/en/memory), [CommonMark 컨테이너](https://spec.commonmark.org/0.31.2/#container-blocks)를 대조했다.

<a id="review--커밋과-확인-범위"></a>
#### 커밋과 확인 범위.

완료 검사는 `276be49`, 카탈로그는 `921e52c`, README·GUIDE 전환은 `346ffbd`에 커밋했다. 종료 기록은 별도 커밋한다. 최종 로컬 통합과 Git 상태는 사용자에게 별도로 보고한다. 이 작업에서는 원격 푸시를 실행하지 않는다.

실제 사용자 설치·전역 복제본 동기화·로그인·외부 업로드·Space 실행·브라우저 또는 Markdown 뷰어의 그림 렌더링은 수행하지 않았다. 그림은 기존 Mermaid 구조와 명시적 flowchart 문법을 소스에서 확인했다. 완료 검증기는 완전한 CommonMark 파서가 아니며 HTML·들여쓴 코드·lazy continuation은 기존 문서 계약의 수동 확인 범위다. 저장소 원본 변경이 전역 설치본을 자동 갱신하지 않는다.
