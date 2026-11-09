<!-- 승인된 문서 통합과 글로벌 적용·GitHub 반영을 실행 단위로 정리한다. -->
# 문서 통합과 글로벌 적용 구현 계획.

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox syntax for tracking.

**Goal:** 문서 270개를 예상 154개로 정리하고 사용자 글로벌 문서·지침 및 GitHub main에 검증한 결과를 반영한다.

**Architecture:** 카탈로그는 기존 23개 그룹 README로, 과거 문서는 14개 작업 기록으로 통합한다. 구조·내용 대조와 회귀를 통과한 동일 결과를 로컬 main, 기존 글로벌 복사본, 원격 main에 배포한다.

**Tech Stack:** Markdown, Python 3.12 표준 라이브러리 unittest, Git, Windows PowerShell·Git Bash.

**Spec:** [승인 설계](../specs/2026-11-09-document-consolidation-design.md).

## 승인과 전역 제약.

- 2026-11-09 사용자가 설계대로 실행, PC 글로벌 적용, 저장소 반영, 커밋·푸시를 명시 승인했다. 이후 메시지에서 PC 범위를 글로벌이라고 확인했다.
- 승인 범위 안의 구현·글로벌 배포·main 병합·일반 push를 수행한다. 이미 받은 승인을 반복해서 요청하지 않는다.
- 기준선은 a559c66이며 임시 브랜치 codex/document-consolidation을 사용한다. 원격 main 기준선 일치를 fetch로 확인했다.
- 121개 항목·37개 원문·Owned-Skills 62개 파일·기존 안전 테스트를 보존한다. 실제 설정·권한·인증·타사 설치본은 변경하지 않는다.
- 사용자 지침과 글로벌 개인 추가 파일은 비공개 백업 후 보존 병합한다. 보호 해시는 비공개 임시 공간에 기록한다.
- 중간 산출물은 Git에서 제외한 작업 공간에 둔다. 공개 문서에 개인 경로·복구 자료·설정 원문을 넣지 않는다.
- 이번 작업의 설계·계획·리뷰, history 목차, 문서 테스트를 포함한 예상 최종 수는154개다.

## Review Focus.

- 같은 help 이름·반복 하위 제목은 그룹과 항목 ID로 구분하고 기존 fragment를 정확한 새 절로 옮긴다.
- Hugging Face README의 서로 다른 Python 예제를 섞지 않고 해당 항목만 추출해 비공개·전송 경계를 그대로 검사한다.
- 코드 예제의 Markdown 링크·제목 모양 문자열은 실제 링크·항목으로 오인하지 않는다.
- 과거 로그인 대기·미검증·승인 원문을 보관 과정에서 완료로 바꾸지 않는다.
- 글로벌 복사본의 이전 버전 파일·개인 추가·사용자 수정은 구분하고 백업·동시 변경 확인 후 적용한다.

## Task 1. 카탈로그와 문서 계약.

**Files:** 새 tests/test_documentation.py, tests/test_upload_examples.py, Skill의23개 그룹 README, Skill/README.md, Skill/CATALOG.md.
**Interfaces:** 항목은 펜스 밖 H2 원래 파일명, 그룹 ID는 부모 상대경로다. 새 테스트의 catalog_sections(text)는 항목별 본문을 반환한다. Markdown 링크 추출은 기존 테스트 helper를 재사용한다.

- [x] test_catalog_layout의 23개 그룹·121개 식별자·목차 링크와 test_repository_links를 먼저 작성한다.
- [x] 누락·중복 항목, 중복·누락 앵커, fenced·inline 예시와 참조형 링크 반례를 추가한다.
- [x] 기존 배치에서 python -X utf8 -B -m unittest discover -s tests -p test_documentation.py -v를 실행해 그룹 README 부재에 따른 RED를 확인한다.
- [x] 임시 이전 도구에서 원문 전체를 읽고 H1을 항목 H2로, 하위 제목을 한 단계 내려 병합한다. 코드·출처·실패 경계는 보존한다.
- [x] 기존 fragment를 항목 접두사 명시 앵커로 매핑하고 old path→new path 정보를 임시 공간에 저장한다.
- [x] CATALOG121항목을 새 항목 절로 연결하고 상위 출처·설치 README를 갱신한다.
- [x] HF 테스트에서 catalog_sections로 항목을 먼저 선택한 뒤 기존 Python 블록 추출·가짜 API 검사를 그대로 수행한다.
- [x] 121개 원문·코드·출처 대조 후에만 파일별로 기존 문서를 삭제한다.

**Expected:** 구조 검사의 누락 실패가 해소되고 기존 HF4개 테스트의 공개·불명·오류·비공개 전송 경계가 유지된다. 전체 링크 GREEN은 Task2·3의 참조 갱신 후 확인한다.
**Commit:** Task2·3과 함께 통합 검증 후 하나의 논리 커밋으로 저장한다.

## Task 2. 과거 작업 기록 통합.

**Files:** docs/history/README.md 및 승인 설계6절의14개 기록. 이전 specs10개·plans14개·reviews13개 삭제.
**Interfaces:** #spec·#plan·#review 및 종류별 하위 앵커. 현재 작업의 spec·plan·review는 기존 위치에 유지한다.

- [x] test_history_layout으로14개 기록과37개 원본 경로 매핑을 검사하고 현재 배치에서 RED를 확인한다.
- [x] 승인된14개 작업 매핑으로 원문·당시 기준선·실패·미검증을 구분해 병합한다.
- [x] 같은 이름의 repository-review 두 파일을 임의 접미사 제거로 분리하지 않는지 확인한다.
- [x] 원문 경로와 고정 커밋, 후속·대체 작업을 기록하고 목차에37개 이전 주소의 대응을 둔다.
- [x] 모든 원문의 구조 변경 외 내용과 코드 블록 불변을 대조하고 일치한 파일만 개별 삭제한다.

**Expected:** 카탈로그와 기록 이전 목록이 정확히158개의 이전 파일을 포함하고 기록 원문 누락이 없다.
**Commit:** Task3 검증과 함께 저장한다.

## Task 3. 참조·진입 문서·정합성 갱신.

**Files:** README.md, GUIDE.md, GETTING_STARTED.md, PORTABILITY.md, AGENTS.md, codex-global-AGENTS.md, rules/01·02·03·04, references/claude-code-cli-setup.md, references의 이력 참조, CHANGELOG.md, docs/current-state.md, docs/design-progress-checklist.md, docs/ci.md, 이번 설계·계획·리뷰.
**Interfaces:** Task1·2의 경로·앵커 매핑을 사용한다. Owned-Skills와 JSON 내용은 변경하지 않는다.

- [x] 현재 문서 전체에서 내부 링크·참조형 링크·실제 경로 안내를 매핑하고 과거 코드 예제의 경로 인용과 구분한다.
- [x] 시작 안내·사람 설명·설치 절차·이식 기준의 책임에 맞게 반복 설치 정책을 줄인다.
- [x] 핵심 안전 규칙은 두 AGENTS에 유지하며 분류 README·앵커와 종료 기록 통합 규칙을 안내한다.
- [x] claude-news는 원본 기준과 일치시키고 pr-review-toolkit의 제외 문구를 실제 포함 기준으로 맞춘다.
- [x] Codex 시간 키·Firecrawl 최소 주기는 확인된 공식 근거로 통일하거나 미확인 수치 예제를 공식 링크로 대체한다.
- [x] 외부 dotfiles·sync.py 강제 전제와 구형 바로가기·무조건 덮어쓰기 설명을 사용자 파일 보존 원칙으로 정리한다. 테스트 중인 실행 코드 계약은 유지한다.
- [x] 현재 상태·체크리스트에는 현재 작업과 남은 확인만 남기고 이력은 history로 연결한다.
- [x] 문서 계약·HF 대상 테스트, 전체 회귀, 원문 대조·보호 해시·UTF8·펜스·금지 정보·git diff --check를 실행한다.
- [x] README부터 목차·그룹·보관 기록까지 Markdown 화면을 확인한다.
- [x] 전체 변경 독립 리뷰를 받고 중요 결함을 고친 뒤 대상·전체 검증을 다시 수행한다.
- [x] workflow 검사에 현재 spec·plan·review를 명시하고 완료 증거를 기록한다.
- [x] 검증 후 '문서 카탈로그와 작업 이력을 통합하고 검증 계약을 보강' 형식의 한글 제목과 bullet 본문으로 커밋한다.

**Expected:** 문서 구조·링크·앵커·기존 회귀 통과, Owned-Skills62개와 JSON 불변, 예상154개 파일, 중요 리뷰 발견 해결.
**Commit:** 실제 생성된 구현 커밋을 검증 기록에 남긴다. 완료 표시를 앞당기지 않는다.

## Task 4. 글로벌 적용과 main·GitHub 반영.

**Files:** 기존 사용자 설정 홈의 Agent-Instructions 문서 복사본과 활성 글로벌 지침. 저장소에는 사용자 경로·비공개 백업을 추가하지 않는다.
**Interfaces:** Task3의 검증된 Git 추적 목록, 기준선 목록, 배포 전 원본 해시·비공개 백업을 사용한다.

- [x] CODEX_HOME·CLAUDE_CONFIG_DIR 우선순위, 기존 지침 import·override·symlink와 실제 사용 중인 복사본을 확인한다. 존재하지 않는 클라이언트를 새로 설치하지 않는다.
- [x] 개인 추가 파일·기존 사용자 변경·설정 및 실제 설치 스킬의 보호 해시를 구분하고 백업한다.
- [x] 원래 로컬 main에 검증한 브랜치를 일반 병합하고 전체 회귀를 실행한다.
- [x] 원래 소유 목록의 obsolete 경로만 비교·백업 후 개별 제거하고 새 추적 파일을 배치한다. 사용자 추가 파일은 보존하고 사용자 수정은 보존 병합한다.
- [x] 전역 Codex AGENTS에는 공개 기본 지침의 변경만 적용하고 개인 추가 규칙을 보존한다. 다른 기존 글로벌 지침은 연결·참조가 바뀐 범위만 갱신한다.
- [x] 배포한 문서와 원본의 일치, 개인 추가·설정·실행 스킬 보호, 설치 위치 기준 링크와 이전 파일 부재를 검사한다.
- [x] 가능하면 실제 새 CLI 세션에서 글로벌 지침과 필요한 새 그룹 문서 로드를 확인한다. 인증·도구 부재로 확인하지 못한 범위는 완료로 표시하지 않는다.
- [x] 일반 git push origin main 후 git ls-remote와 로컬 SHA를 비교하고 GitHub CI를 확인한다.
- [x] 배포·통합 결과를 검증 기록에 반영하고 필요한 검증 후 후속 한글 커밋·일반 push로 문서를 맞춘다.
- [x] 병합된 임시 브랜치·worktree·본인이 만든 임시 파일은 미커밋·참조·복구 필요를 확인해 정리하고 비공개 복구 백업은 보존한다.

**Expected:** 로컬 main·원격 main SHA 일치, 글로벌 문서·기본 지침 반영, 개인 파일·설정·실행 원본 보존과 실제 로드 확인 범위 보고.
**Commit:** 인증이나 개인 경로 없이 결과·검증 범위만 기록한다.

## 자체 검토와 실행 기록.

설계1~12절을 Task1~4에 대응했다. 카탈로그·이력·루트 문서는 이전 경로 매핑을 공유하므로 같은 작업 트리에서 순서대로 구현한다. 독립적인 글로벌 사전 조사와 마지막 전체 리뷰만 위임한다. 사용자 실행·글로벌·커밋·푸시 승인을 그대로 적용한다.

실행 결과는 검증 기록에 남겼다. 구현 b040f65의 양OS CI, Windows80개, 글로벌156문서·개인 규칙·보호743해시와 새 CLI 읽기를 확인했다. 임시 브랜치·등록·내용은 정리했으며 빈 임시 폴더1개는 운영체제 잠금으로 남아 사용자 앱을 강제 종료하지 않았다.
