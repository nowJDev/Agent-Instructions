<!-- 추가 전체 리뷰의 수정 범위와 회귀 검증 계획을 기록한다. -->
# 추가 전체 리뷰와 실행 계약 수정 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 독립된 검토·수정 영역은 저장소의 `rules/02`에 따라 별도 담당자에게 맡기고 전체 변경을 통합 검토한다.

## 목표와 승인 범위.

사용자는 저장소 추가 전체 리뷰와 발견 사항 수정을 선택했고, README의 `0. TL;DR`도 이해하기 쉬운 제목으로 바꾸도록 요청했다. 이후 검증한 변경 단위마다 바로 커밋하고 푸시는 마지막에 한 번에 하도록 지정했다. 기준선은 `a6a6602`이며 기존 회귀는 31개 통과다. `fix/review-20261014`에서 확인된 결함과 그 회귀·연관 문서만 수정한다. 실제 전역 설치본·개인 설정·외부 서비스는 변경하지 않는다.

표준 라이브러리와 기존 문서 구조를 유지한다. 작업 문서는 이 계획과 `docs/reviews/2026-10-14-repository-review.md`로 기록한다. 설정과 다운로드는 실패 시 사용자 원본을 보존하며, API 예시는 공식 계약을 근거로 수정한다.

## Task 1. Markdown 완료 검사.

Files: `Owned-Skills/design-driven-delivery/scripts/validate_workflow.py`, `Owned-Skills/design-driven-delivery/references/document-contracts.md`, `tests/test_workflow_markdown.py`.

- [x] 4칸 들여쓴 잘못된 fence, 문단·목록 경계를 가로지르는 inline 구분자, quoted fence와 escape 및 목록 내부 인용을 임시 프로젝트에서 RED로 재현했다. 미완료 누락은 잘못된 exit 0, 코드 예시 오탐은 잘못된 exit 1이었다.
- [x] fence 들여쓰기·컨테이너와 escaped opening을 구분하고 inline 예시 제거를 문서 블록 안으로 제한했다. 정상 multiline inline·목록 continuation·목록 내부 인용을 유지했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_workflow_markdown.py -v`의 Markdown 회귀 19개와 기존 회귀의 GREEN을 확인했다.

## Task 2. 설정 홈·Windows 실행·다운로드.

Files: `GETTING_STARTED.md`, `references/windows-cli-shortcut.md`, `references/claude-code-cli-setup.md`, `tests/test_setup_profiles.py`, `tests/test_review_regressions.py`의 환경 격리와 `README.md`·`index.html`의 설정 홈 안내.

- [x] 사용자 지정 설정 홈, CMD의 `%`·`!` 재확장, jq HTTP 실패를 임시 fixture에서 RED로 확인했다.
- [x] 설정 홈을 일치시키고 `%` 포함 CLI 경로는 실행 전에 중단하며 `!`는 `/v:off`로 보호했다. jq는 HTTP 오류·실행 실패에서 원본을 보존하고 정상 fixture만 교체했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_setup_profiles.py -v`의 신규 7개 GREEN과 실패 전 원본 보존, 두 클라이언트·두 터미널의 실제 COM 생성·독립 검증을 확인했다.

## Task 3. 도구·이식·인증 안내.

Files: `MCP/{playwright,README,_disabled/vercel}.md`, `PORTABILITY.md`, `Skill/README.md`, `Skill/_builtin/schedule.md`, `Skill/_disabled/hookify/writing-rules.md`, `Skill/chrome-devtools-mcp/{chrome-devtools,chrome-devtools-cli,debug-optimize-lcp}.md`, `Skill/claude-md-management/revise-claude-md.md`, `Skill/firecrawl/{firecrawl-interact,skill-gen}.md`, `Skill/huggingface-skills/transformers-js.md`, `Skill/plugin-dev/{command-development,create-plugin}.md`, `Skill/qodo-skills/qodo-pr-resolver.md`, `index.html`의 지침 로딩 FAQ.

- [x] 배포된 Playwright·Chrome·Firecrawl, Vercel 권한·명칭, 위치 인자·예약·YAML·지침 로딩을 공식 계약으로 확인했다.
- [x] 실행 예시와 권한을 맞추고 스킬 리소스 보존·공식 서버 인증·외부 리뷰 자료의 기술 검증을 안내했다. 잘못된 명령 별칭·로컬 파일명·중첩 fence도 수정했다.
- [x] 공식 원본·버전 근거와 연관 예시를 확인했다. 독립 리뷰의 Chrome CLI `evaluate_script` 인자·Vercel 도구명 발견도 공식 원본으로 대조한 뒤 반영했다.

## Task 4. README와 종료 검증.

Files: `README.md`, `CHANGELOG.md`, `docs/reviews/2026-10-14-repository-review.md`, 이 계획.

- [x] README의 제목을 `0. 핵심 안내`로 바꾸고 기존 제목을 참조하는 내부 링크가 없음을 확인한다.
- [x] 전체 57개 통과, 실패·스킵 0개를 확인했다. Python 문법, UTF-8·BOM·LF, Markdown·로컬 링크·앵커와 `git diff --check`를 검사했다.
- [x] 각 담당자의 전체 변경과 독립 리뷰 발견을 확인하고 수정했다. 검증·제한은 `docs/reviews/2026-10-14-repository-review.md`에 기록했다.
- [x] 제목·완료 검사·설치·카탈로그를 별도 한글 커밋으로 저장하고 각 커밋의 파일 목록을 확인했다. 로컬 HTML 브라우저 검증은 URL 보안 정책으로 차단돼 제외했고 실제 설치·인증·GUI의 미검증 범위를 기록했다.
