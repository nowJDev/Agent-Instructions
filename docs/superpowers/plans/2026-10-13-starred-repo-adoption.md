<!-- 승인된 스타 저장소 선별 반영을 파일별 작업과 검증으로 나눈다. -->
# 스타 저장소 선별 반영 구현 계획.

For agentic workers: REQUIRED SUB-SKILL: `executing-plans`. 승인 설계의 실행 요청에 따라 같은 세션에서 의존 작업을 순서대로 수행한다. 단계는 체크박스로 관리한다.

**Goal.** 기존 지침의 다섯 영역을 보완하고 검토 후보 26개의 채택 판단을 기록한다.

**Architecture.** 정식 규칙은 기존 문서에 두고 참고 문서에는 출처·중복·사용조건·검증 범위를 둔다. 추가 설치·스킬 원본 복제·전역 배포는 제외한다.

**Tech Stack.** Markdown, 기존 HTML, Git, Python 표준 라이브러리 기반 임시 문서 검사와 브라우저다. 실행 코드 변경이 없어 TDD 코드 테스트 대신 문서 검사를 적용한다.

## Task 1. 승인 설계와 후보 판단 기록.

Create: `docs/superpowers/specs/2026-10-13-starred-repo-adoption-design.md`, 이 계획, `references/starred-repo-adoption.md`.

- [x] 기준선·깨끗한 작업 트리·기존 worktree를 확인하고 `docs/starred-repo-adoption` 브랜치를 생성한다.
- [x] 승인 설계와 실행 계획을 기존 경로에 저장한다.
- [x] 26개 후보의 판정·반영 위치·중복·사용조건·원본 링크·검증 범위를 기록한다.
- [x] 표의 번호·저장소를 검토 목록과 대조하고 개인 계정·절대경로가 없는지 확인한다.

## Task 2. 기존 지침 보완.

Modify: `AGENTS.md`, `codex-global-AGENTS.md`, `Owned-Skills/design-driven-delivery/references/change-workflow.md`, `Owned-Skills/design-driven-delivery/references/document-contracts.md`, `rules/02_tool-boundaries.md`, `rules/04_garbage-collection.md`.

- [x] 출력 규칙에 결론·행동 우선, 사실·기술 용어·불확실성 보존을 한 줄로 추가한다.
- [x] DISCOVERED에서 기존 해결책·호출자·테스트·fixtures·설정·exports 영향을 확인하게 한다.
- [x] DISCUSSING에서 실제 정상·실패 사례, 기존 용어·결정 기록과 관찰 가능한 완료 기준을 구체화한다.
- [x] IMPLEMENTING에서 기존 코드→표준 기능→설치 의존성 순으로 충족 여부를 확인하게 한다.
- [x] 문서 계약에 정식 규칙의 단일 출처와 읽을 조건을 추가한다.
- [x] 도구 경계에 가용성 확인·대체·도입 시 지원 환경과 권한·데이터 전달·검증 기준을 추가한다.
- [x] 큰 성공 출력 요약과 원본 보존을 추가하고 기존 전체 읽기·실패 증거·상태 보존 경계와 대조한다.

## Task 3. 안내와 변경 이력 연결.

Modify: `README.md`, `index.html`, `CHANGELOG.md`.

- [x] README 의사결정 표에 참고 문서의 읽을 조건을 추가한다.
- [x] HTML 카탈로그 절에 선택 도구와 내부 원칙 반영의 구분 및 참고 링크를 안내한다.
- [x] 변경 이력을 기록하고 카탈로그 수와 스킬·MCP 파일이 그대로인지 확인한다.

## Task 4. 검증·리뷰·커밋.

Create: `docs/reviews/2026-10-13-starred-repo-adoption-review.md`.

- [x] 임시 Python 검사로 변경 문서 인코딩·펜스·링크·앵커·후보 26개·금지 경로·시크릿 패턴을 검사한다. 실패 시 원인을 수정하고 재실행한다.
- [x] 읽기 전용·재사용·모호함·문체·큰 출력·미설치 도구·포니테일 여부의 7개 지침 사례를 독립 리뷰한다. 실제 새 세션 검증과 구분한다.
- [x] 브라우저에서 HTML 링크와 표시를 확인한다.
- [x] 전체 diff를 요구사항 준수와 문서 품질 순으로 검토하고 발견 사항을 해결한다.
- [x] 리뷰 문서와 계획에 실제 검증 결과·미검증 범위를 기록한다.
- [x] 커밋 준비로 `git diff --check`·대상 범위를 확인하고 한글 제목·bullet 본문 메시지를 준비한다.
- [x] 로컬 반영 준비로 원본 main의 사용자 변경 없음과 반영 범위를 확인한다.

## 종료 작업.

위 체크박스는 커밋 전 구현·검증·반영 준비의 증거다. 최종 문서 검사 후 한 논리 커밋을 만들고 원본 작업 경로에 로컬 반영한다. 커밋과 반영 성공은 이후 `git show --stat`·`git status`로 확인해 최종 결과에 보고한다. 원격 푸시는 하지 않는다.

## 검증 명령.

작업 루트에서 `git diff --check`, `git diff --name-only`, `git diff --stat`를 실행한다. 임시 Python 검사는 저장소를 인자로 받아 검사하며 성공 시 각 항목의 PASS와 개수를 출력한다. 커밋 후 `git show --stat`와 `git status --short --branch`로 논리 단위와 작업 트리를 확인한다.

저장소 전체를 고정 경로로 검사하는 workflow 스크립트는 기존 `docs/current-state.md`·`docs/design-progress-checklist.md`가 없는 구조를 요구하므로 이번 작업의 완료 근거로 쓰지 않는다. 기존 문서 구조를 유지하며 이번 설계·계획·리뷰와 실제 검사 결과를 대조한다.
