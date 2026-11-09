<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-14-repository-review 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-14-repository-review.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-14-repository-review.md).

<!-- 추가 전체 리뷰의 수정 범위와 회귀 검증 계획을 기록한다. -->
<a id="plan--추가-전체-리뷰와-실행-계약-수정-계획"></a>
### 추가 전체 리뷰와 실행 계약 수정 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 독립된 검토·수정 영역은 저장소의 `rules/02`에 따라 별도 담당자에게 맡기고 전체 변경을 통합 검토한다.

<a id="plan--목표와-승인-범위"></a>
#### 목표와 승인 범위.

사용자는 저장소 추가 전체 리뷰와 발견 사항 수정을 선택했고, README의 `0. TL;DR`도 이해하기 쉬운 제목으로 바꾸도록 요청했다. 이후 검증한 변경 단위마다 바로 커밋하고 푸시는 마지막에 한 번에 하도록 지정했다. 기준선은 `a6a6602`이며 기존 회귀는 31개 통과다. `fix/review-20261014`에서 확인된 결함과 그 회귀·연관 문서만 수정한다. 실제 전역 설치본·개인 설정·외부 서비스는 변경하지 않는다.

표준 라이브러리와 기존 문서 구조를 유지한다. 작업 문서는 이 계획과 `docs/reviews/2026-10-14-repository-review.md`로 기록한다. 설정과 다운로드는 실패 시 사용자 원본을 보존하며, API 예시는 공식 계약을 근거로 수정한다.

<a id="plan--task-1-markdown-완료-검사"></a>
#### Task 1. Markdown 완료 검사.

Files: `Owned-Skills/design-driven-delivery/scripts/validate_workflow.py`, `Owned-Skills/design-driven-delivery/references/document-contracts.md`, `tests/test_workflow_markdown.py`.

- [x] 4칸 들여쓴 잘못된 fence, 문단·목록 경계를 가로지르는 inline 구분자, quoted fence와 escape 및 목록 내부 인용을 임시 프로젝트에서 RED로 재현했다. 미완료 누락은 잘못된 exit 0, 코드 예시 오탐은 잘못된 exit 1이었다.
- [x] fence 들여쓰기·컨테이너와 escaped opening을 구분하고 inline 예시 제거를 문서 블록 안으로 제한했다. 정상 multiline inline·목록 continuation·목록 내부 인용을 유지했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_workflow_markdown.py -v`의 Markdown 회귀 19개와 기존 회귀의 GREEN을 확인했다.

<a id="plan--task-2-설정-홈windows-실행다운로드"></a>
#### Task 2. 설정 홈·Windows 실행·다운로드.

Files: `GETTING_STARTED.md`, `references/windows-cli-shortcut.md`, `references/claude-code-cli-setup.md`, `tests/test_setup_profiles.py`, `tests/test_review_regressions.py`의 환경 격리와 `README.md`·`index.html`의 설정 홈 안내.

- [x] 사용자 지정 설정 홈, CMD의 `%`·`!` 재확장, jq HTTP 실패를 임시 fixture에서 RED로 확인했다.
- [x] 설정 홈을 일치시키고 `%` 포함 CLI 경로는 실행 전에 중단하며 `!`는 `/v:off`로 보호했다. jq는 HTTP 오류·실행 실패에서 원본을 보존하고 정상 fixture만 교체했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_setup_profiles.py -v`의 신규 7개 GREEN과 실패 전 원본 보존, 두 클라이언트·두 터미널의 실제 COM 생성·독립 검증을 확인했다.

<a id="plan--task-3-도구이식인증-안내"></a>
#### Task 3. 도구·이식·인증 안내.

Files: `MCP/{playwright,README,_disabled/vercel}.md`, `PORTABILITY.md`, `Skill/README.md`, `Skill/_builtin/schedule.md`, `Skill/_disabled/hookify/writing-rules.md`, `Skill/chrome-devtools-mcp/{chrome-devtools,chrome-devtools-cli,debug-optimize-lcp}.md`, `Skill/claude-md-management/revise-claude-md.md`, `Skill/firecrawl/{firecrawl-interact,skill-gen}.md`, `Skill/huggingface-skills/transformers-js.md`, `Skill/plugin-dev/{command-development,create-plugin}.md`, `Skill/qodo-skills/qodo-pr-resolver.md`, `index.html`의 지침 로딩 FAQ.

- [x] 배포된 Playwright·Chrome·Firecrawl, Vercel 권한·명칭, 위치 인자·예약·YAML·지침 로딩을 공식 계약으로 확인했다.
- [x] 실행 예시와 권한을 맞추고 스킬 리소스 보존·공식 서버 인증·외부 리뷰 자료의 기술 검증을 안내했다. 잘못된 명령 별칭·로컬 파일명·중첩 fence도 수정했다.
- [x] 공식 원본·버전 근거와 연관 예시를 확인했다. 독립 리뷰의 Chrome CLI `evaluate_script` 인자·Vercel 도구명 발견도 공식 원본으로 대조한 뒤 반영했다.

<a id="plan--task-4-readme와-종료-검증"></a>
#### Task 4. README와 종료 검증.

Files: `README.md`, `CHANGELOG.md`, `docs/reviews/2026-10-14-repository-review.md`, 이 계획.

- [x] README의 제목을 `0. 핵심 안내`로 바꾸고 기존 제목을 참조하는 내부 링크가 없음을 확인한다.
- [x] 전체 57개 통과, 실패·스킵 0개를 확인했다. Python 문법, UTF-8·BOM·LF, Markdown·로컬 링크·앵커와 `git diff --check`를 검사했다.
- [x] 각 담당자의 전체 변경과 독립 리뷰 발견을 확인하고 수정했다. 검증·제한은 `docs/reviews/2026-10-14-repository-review.md`에 기록했다.
- [x] 제목·완료 검사·설치·카탈로그를 별도 한글 커밋으로 저장하고 각 커밋의 파일 목록을 확인했다. 로컬 HTML 브라우저 검증은 URL 보안 정책으로 차단돼 제외했고 실제 설치·인증·GUI의 미검증 범위를 기록했다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-14-repository-review.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-14-repository-review.md).

<!-- 추가 전체 리뷰의 재현·수정·독립 검토와 검증 범위를 기록한다. -->
<a id="review--추가-전체-리뷰의-수정-검증"></a>
### 추가 전체 리뷰의 수정 검증.

기준선은 `a6a6602`다. 사용자는 추가 전체 리뷰와 발견 사항 수정, README 제목의 쉬운 한국어 변경을 요청했다. 검증한 논리 변경마다 바로 커밋하고 마지막에 한 번에 푸시하도록 지정했다. [실행 계획](#plan)의 범위로 저장소 원본만 수정했다.

<a id="review--검토-범위와-수정"></a>
#### 검토 범위와 수정.

루트 지침·README·사람용 안내, 자체 제작 Skill 패키지와 회귀, 설치·백업 참조, Skill·MCP 카탈로그를 영역별로 검토했다. 과거 수정의 해결 근거를 확인하고 이미 해결된 문제는 다시 결함으로 집계하지 않았다.

| 영역 | 확인한 문제 | 수정·검증 근거 |
|---|---|---|
| 완료 검사. | 4칸 들여쓴 잘못된 fence가 실제 미완료 작업을 숨겼다. | 컨테이너 기준의 fence 들여쓰기를 확인하고 실제 작업 목록을 유지한다. |
| 완료 검사. | Inline 구분자가 문단·heading·다른 목록·fence를 넘어 필수 필드를 숨겼다. | 블록별 검사로 나누며 같은 문단의 유효 multiline code는 유지한다. |
| 완료 검사. | 인용의 정상 fence는 예시로 제외하지 못했고 컨테이너 이탈을 구분하지 못했다. | 인용 깊이와 목록 들여쓰기를 추적해 정상 예시·실제 항목을 구분한다. |
| 완료 검사. | Escaped opening backtick을 코드로 오인했다. | 홀수·짝수 backslash와 코드 안의 닫힘 구분자를 회귀로 확인한다. |
| 완료 검사. | 독립 리뷰에서 목록 내부 인용의 유효 fence 오탐을 재현했다. | 명시적 list→quote와 quote→list→quote, 종료·컨테이너 이탈 뒤 실제 필드 검출을 추가했다. |
| 설정·설치. | 사용자 지정 설정 홈을 무시하고 기본 홈을 수정했다. | `CODEX_HOME`·`CLAUDE_CONFIG_DIR`을 백업·지침·복제본·설정·아이콘에서 공통 사용한다. |
| Windows 실행. | `%`·`!` 경로가 다른 CLI로 재확장될 수 있었다. | `%` 포함 Source는 실행 전에 중단하며 `!`는 `/v:off`로 보호한다. |
| 다운로드. | HTTP 오류·비실행 응답을 jq로 저장하고 기존 바이너리를 절단했다. | 동일 폴더 임시 파일에 `curl -fL`로 받고 실행 확인 후 교체한다. 실패 원본 보존과 정상 fixture 교체를 확인한다. |
| Playwright. | 이전 `ref`와 현재 필수 인자·도구 계약을 혼용했다. | 0.0.83의 `target`·drag·screenshot·network 계약을 맞추고 런타임 스키마 확인을 안내한다. |
| Chrome. | 필수 page ID·CLI 이름·enum과 MCP·CLI 인자 표현을 혼용했다. | 1.10.1 계약으로 맞췄다. 최종 독립 리뷰의 `evaluate_script` 발견은 함수 위치 인자와 `--pageId` 옵션으로 수정했다. |
| Vercel. | 현재 원격 도구를 읽기 전용으로 단정했다. | 조회·변경 도구와 승인 범위를 안내한다. 최종 독립 리뷰에서 배포 도구 이름을 `create_deployment`로 대조했다. |
| 명령·예약. | 위치 인자를 1부터 세고 클라우드 routines와 세션 Cron을 혼용했다. | `$0`부터 시작하는 인자와 각 예약의 실행 위치·관리 경로를 구분한다. |
| 스킬 이식. | SKILL.md만 복사하면 참조·실행 리소스가 사라졌다. | 스킬 루트와 상대경로 리소스를 함께 보존하도록 안내한다. |
| HF 인증. | Custom fetch가 모든 URL에 토큰을 붙였다. | 해당 코드를 제거하고 공식 Node 서버 환경 인증을 사용하도록 안내한다. 새 인증 구현은 추가하지 않는다. |
| 기타 도구. | 미정의 `cc` 별칭, Firecrawl 미지원 옵션, YAML 따옴표 escape 오류. | 공식 `claude` 명령, 배포 CLI 옵션과 YAML 실제 파싱·regex 결과를 확인한다. |
| 외부 리뷰. | Qodo prompt를 자동 실행 권한으로 취급했다. | 사용자 승인·프로젝트 지침·실제 코드와 테스트를 먼저 확인하도록 안내한다. |
| 지침 문서. | 잘못된 `.claude.local.md`, 중첩 fence와 오래된 자동 로딩 설명. | `CLAUDE.local.md`, 외부 4개 backtick fence와 버전·설정에 따른 로딩을 안내한다. |
| README. | 사용자가 TL;DR 제목을 이해하기 어렵다고 했다. | `0. 핵심 안내`로 변경했다. 구성도와 작업 흐름도는 기존 내용을 유지했다. |

<a id="review--회귀와-독립-검증"></a>
#### 회귀와 독립 검증.

최종 `python -X utf8 -B -m unittest discover -s tests -v`는 57개 통과, 실패·스킵 0개다. 기존 31개를 유지하고 Markdown 19개와 설치 7개를 추가했다. 부모의 직접 통합 실행은 21.590초이며 최종 독립 검토자의 직접 실행도 57개 통과했다.

재현은 임시 프로젝트·홈·설정·CLI fixture만 사용했다. Windows의 실제 WScript.Shell COM으로 Codex·Claude Code 각각 WT·CMD의 네 바로가기를 생성하고 별도 검증했다. jq는 localhost 응답으로 HTTP 오류·비실행 파일·정상 교체를 확인했다. 기존 fixture에도 설정 홈을 명시해 부모 환경변수에 따라 실홈을 수정하지 않게 했다.

실행 스크립트·설치와 전체 변경을 별도 검토자가 검증했다. 추가 발견인 목록 내부 인용 fence, Vercel 배포 도구 이름과 Chrome CLI 함수 인자는 수정 후 재현 회귀 또는 공식 배포 선언으로 확인했다. UTF-8·BOM 없음·LF, Python 파일·문서 예제 문법, JSON 예제, Markdown fence·로컬 링크·앵커와 `git diff --check`를 통과했다.

<a id="review--공식-근거"></a>
#### 공식 근거.

- Markdown 경계는 [CommonMark fence](https://spec.commonmark.org/0.31.2/#fenced-code-blocks)와 [블록 우선순위](https://spec.commonmark.org/0.31.2/#precedence)를 대조했다.
- 도구는 [Playwright 0.0.83](https://github.com/microsoft/playwright-mcp/blob/f183dad4a52965583e3cc1d59b88cdc279e2e57d/README.md#tools), [Chrome 1.10.1](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/e52c6b59b476c5e04d8dd9fd4bd017ba3b3d65df/docs/tool-reference.md), [Chrome CLI 선언](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/e52c6b59b476c5e04d8dd9fd4bd017ba3b3d65df/src/config/cli-options.ts), [Firecrawl 1.26.3](https://github.com/firecrawl/cli/blob/3136f724b3203c6a69bfb14d2f384271eb45822c/src/index.ts), [Vercel 배포 도구](https://vercel.com/docs/agent-resources/vercel-mcp/tools/deployments)를 확인했다.
- 설정·지침은 [Codex 설정 홈](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude 설정 홈](https://code.claude.com/docs/en/claude-directory), [Claude 지침 파일](https://code.claude.com/docs/en/memory), 다운로드는 [curl HTTP 실패 처리](https://curl.se/docs/manpage.html#-f)를 확인했다.
- 이식·인증은 [Agent Skills 패키지](https://agentskills.io/specification#directory-structure), [Transformers.js 서버 인증](https://huggingface.co/docs/transformers.js/guides/private), escape는 [YAML scalar](https://yaml.org/spec/1.2.2/#73-flow-scalar-styles)를 확인했다.

<a id="review--커밋과-제한"></a>
#### 커밋과 제한.

제목 변경은 `c7bf887`, 완료 검사는 `3659521`, 설치 계약은 `79f684a`, 카탈로그는 `4bd2414`에 각각 커밋했다. 계획·변경 이력과 이 리뷰 기록도 종료 검증 후 별도 커밋한다. main 통합과 마지막 한 번의 일반 push 결과는 최종 응답에서 확인한다.

완전한 CommonMark 파서는 아니다. HTML·들여쓴 코드 블록·lazy continuation 등 복합 문법은 [문서 계약](../../Owned-Skills/design-driven-delivery/references/document-contracts.md)의 수동 검증 범위를 따른다. `%`가 포함된 CLI 설치 경로는 실행 전에 명시적으로 중단한다.

실제 사용자 CLI 설치·로그인·WT GUI·상태줄·MCP 인증과 서비스 쓰기, Transformers.js 실제 fetch는 수행하지 않았다. 로컬 HTML 파일의 브라우저 검증은 URL 보안 정책으로 차단됐다. 현재 HTML 변경은 설정 홈·지침 로딩 설명 문구이며 인터랙션 코드는 수정하지 않았다. 저장소 원본을 갱신해도 설치된 전역 복제본은 자동 갱신되지 않는다.
