<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# _builtin 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. 활성 표시는 작성 당시 환경의 기록이다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [claude-api](#claude-api).
- [code-review](#code-review).
- [fewer-permission-prompts](#fewer-permission-prompts).
- [init](#init).
- [keybindings-help](#keybindings-help).
- [loop](#loop).
- [review](#review).
- [run](#run).
- [schedule](#schedule).
- [security-review](#security-review).
- [simplify](#simplify).
- [update-config](#update-config).
- [verify](#verify).

## claude-api

> Claude API / Anthropic SDK 레퍼런스 빌트인 스킬. model id·가격·파라미터·스트리밍·tool use·MCP·캐싱·토큰 카운팅·모델 마이그레이션을 다룬다. **Claude/Anthropic 관련 작업 시 파일을 열기 전에 먼저 읽는 트리거 스킬**.

<a id="claude-api---용도"></a>
### 📌 용도
Claude API와 Anthropic SDK를 다룰 때 **메모리에 의존하지 않고 정확한 최신 레퍼런스를 참조**하기 위한 스킬. 다음을 포함한다.
- **model id** (예: `claude-opus-4-...`, `us.anthropic.*` 등)
- **pricing**(가격), 모델 선택, 한도(limits)
- **파라미터**(params), **streaming**
- **tool use**, **MCP**, **agents**(멀티에이전트/RAG/LLM-judge/computer-use 등)
- **prompt caching**, **token counting**
- **모델 마이그레이션**(model migration)

핵심 행동 규칙: **대상 파일을 열기 전에 먼저 이 스킬을 읽는다.** "한 줄짜리처럼 보인다"는 이유로 건너뛰지 않는다. 가격·모델·캐싱 같은 LLM 관련 질문은 **절대 기억으로 답하지 말고** 이 레퍼런스를 근거로 답한다.

<a id="claude-api---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가** (대상 파일 Read 전에 먼저)
  - 프롬프트가 Claude/Anthropic을 어떤 형태로든 언급할 때: Claude, Anthropic, Opus, Sonnet, Haiku, `anthropic`, `@anthropic-ai`, `claude-*`, `us.anthropic.*`, `[1m]`
  - LLM에 대한 질문(가격/모델 선택/한도/캐싱) — 기억으로 답하지 말 것
  - 제공자가 명시되지 않은 **LLM-형태의 작업**: agent/MCP/tool 정의/멀티에이전트/RAG/LLM-judge/computer-use, 혹은 자연어에 대한 generate/summarize/extract/classify/rewrite/대화, refusals/cutoffs/streaming/tool-call/token 디버깅
- **언제 쓰지 않는가** (다른 제공자 작업이면 모든 트리거를 무시하고 SKIP)
  - 쿼리에 OpenAI/GPT/Gemini/Llama/Mistral/Cohere/Ollama가 명시됐을 때
  - 제공자 미명시 시, 프로젝트에 `openai|langchain_openai|google.generativeai|genai|mistralai|cohere|ollama` grep이 걸리면 → 이 경우 파일을 Read하기 **전에 먼저 grep**을 돌려 판단

<a id="claude-api---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "Opus랑 Sonnet 가격 차이 알려줘" → 기억 대신 이 레퍼런스 참조
- "tool use 정의 어떻게 짜?" → 스킬 읽고 답변
- "claude-3-5에서 최신 모델로 마이그레이션하려면?" → migration 레퍼런스 참조
- Anthropic SDK를 쓰는 코드 파일을 열기 직전 → 먼저 이 스킬 로드

<a id="claude-api---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 레퍼런스 항목: model ids / pricing / params / streaming / tool use / MCP / agents / caching / token counting / model migration
- 동작 규칙: **파일 열기 전 선행 로드**, LLM 질문은 기억 금지
- 선행 판별: 제공자 미명시 시 `grep -rE 'openai|langchain_openai|google.generativeai|genai|mistralai|cohere|ollama'`로 타 제공자 여부 먼저 확인

<a id="claude-api---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장)

## code-review

> 현재 diff를 **정확성(버그) + 재사용/단순화/효율성** 관점에서 리뷰하는 빌트인 스킬. effort 레벨로 깊이를 조절하고, PR 코멘트나 워킹트리 적용까지 가능.

<a id="code-review---용도"></a>
### 📌 용도
작업 중인 변경(diff)을 대상으로 코드 리뷰를 수행한다. 두 축으로 본다.
1. **Correctness 버그** — 실제로 잘못 동작할 수 있는 결함 탐지
2. **정리(cleanup)** — 재사용(reuse), 단순화(simplification), 효율성(efficiency) 관점의 개선점

effort 레벨로 탐색 범위와 확신도 트레이드오프를 조절한다. 낮을수록 "확신 높은 소수의 발견"만, 높을수록 "불확실한 것까지 포함한 넓은 커버리지"를 제공한다.

<a id="code-review---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "코드 리뷰해줘", "이 diff 봐줘", "버그 없는지 검토해줘"
  - PR 올리기 전/후 변경 검토
  - 변경에 숨은 결함이나 개선점을 찾고 싶을 때
- **언제 쓰지 않는가**
  - **버그를 찾지 않고 품질 정리만** 원하면 `simplify` (code-review와 역할 분리됨)
  - 앱을 실제 실행해 동작을 확인하려면 `verify` / `run`
  - 보안 취약점 전용 리뷰는 `security-review`

<a id="code-review---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/code-review` — 기본 레벨로 현재 diff 리뷰
- `/code-review high` — 넓은 커버리지(불확실한 발견 포함 가능)
- `/code-review max` / `/code-review ultra` — 최대 깊이 / 클라우드 멀티에이전트 심층 리뷰
- `/code-review high --comment` — 발견 사항을 PR 인라인 코멘트로 게시
- `/code-review high --fix` — 리뷰 후 발견 사항을 워킹트리에 직접 적용

<a id="code-review---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **effort 레벨**:
  - `low` / `medium` — 적은 수의 고확신 발견
  - `high` → `max` — 넓은 커버리지, 불확실한 발견 포함 가능
  - `ultra` — 클라우드에서 도는 **멀티에이전트 심층 리뷰**
- **플래그**:
  - `--comment` — 발견 사항을 PR **인라인 코멘트**로 게시
  - `--fix` — 리뷰 후 발견 사항을 **워킹트리에 적용**
- **리뷰 관점**: correctness 버그 + reuse / simplification / efficiency

<a id="code-review---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장)
- 참고: 이름이 비슷한 `pr-review-toolkit` 플러그인(ON)은 별개다 — 그쪽은 **에이전트 + `review-pr` 커맨드**를 제공하며, 이 `/code-review` 빌트인 스킬과 다르다.

## fewer-permission-prompts

> 트랜스크립트에서 자주 쓴 **read-only Bash·MCP 호출**을 스캔해, 프로젝트 `settings.json`에 우선순위 allowlist를 추가함으로써 권한 프롬프트를 줄이는 빌트인 스킬.

<a id="fewer-permission-prompts---용도"></a>
### 📌 용도
작업 중 반복적으로 뜨는 **권한 승인 프롬프트를 줄인다.** 과거 대화 트랜스크립트를 분석해 사용자가 자주 호출하는 **읽기 전용(안전한) Bash 명령과 MCP 도구 호출**을 찾아내고, 이를 프로젝트 `.claude/settings.json`의 권한 allowlist에 우선순위를 매겨 추가한다. 결과적으로 같은 명령을 다시 쓸 때 매번 확인 창이 뜨지 않는다.

핵심: **read-only(안전) 호출만** 대상으로 한다. 파일을 수정하거나 부작용이 있는 명령은 무분별하게 허용 목록에 넣지 않는다.

<a id="fewer-permission-prompts---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "권한 프롬프트가 너무 자주 떠, 좀 줄여줘"
  - "자주 쓰는 안전한 명령들 allowlist에 넣어줘"
  - 반복되는 승인 요청으로 작업 흐름이 끊길 때
- **언제 쓰지 않는가**
  - 특정 단일 권한만 추가/이동하려면 `update-config`가 더 직접적
  - 위험하거나 부작용 있는 명령을 허용하려는 경우 (이 스킬은 read-only만 다룸)

<a id="fewer-permission-prompts---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/fewer-permission-prompts` — 트랜스크립트 스캔 후 allowlist 제안·추가
- "내가 자주 쓰는 git status, ls 같은 거 그만 물어보게 해줘"

<a id="fewer-permission-prompts---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **스캔 대상**: 트랜스크립트 내 빈번한 read-only Bash 명령 + MCP 도구 호출
- **출력**: 프로젝트 `.claude/settings.json`의 권한 allow 목록에 **우선순위가 매겨진 항목** 추가
- **안전 필터**: 부작용 없는 read-only 호출로 한정

<a id="fewer-permission-prompts---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장). 수정 대상은 프로젝트 `.claude/settings.json`

## init

> 코드베이스를 분석해 **CLAUDE.md를 생성/초기화**하는 빌트인 명령.

<a id="init---용도"></a>
### 📌 용도
현재 프로젝트의 코드베이스를 훑어 구조·기술스택·빌드/테스트 방법·관례 등을 파악하고, 이를 바탕으로 프로젝트용 **CLAUDE.md(프로젝트 메모리)** 파일을 만들어 준다. 새 프로젝트에서 Claude Code를 처음 세팅할 때, 또는 기존 CLAUDE.md를 코드베이스 기준으로 초기화/재생성할 때 사용한다.

생성된 CLAUDE.md는 이후 모든 세션에서 Claude가 프로젝트 컨텍스트로 자동 참조한다.

<a id="init---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - 프로젝트에 Claude Code를 처음 도입할 때
  - "CLAUDE.md 만들어줘 / 초기화해줘"
  - 코드베이스 분석 기반 프로젝트 메모리가 필요할 때
- **언제 쓰지 않는가**
  - 기존 CLAUDE.md를 세션 학습 내용으로 **개선/감사**하려면 전용 도구(claude-md 관리 계열)가 더 적합
  - 글로벌(사용자) CLAUDE.md 작성과는 무관 (init은 프로젝트 대상)

<a id="init---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/init` — 현재 코드베이스 분석 후 CLAUDE.md 생성/초기화

<a id="init---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **분석 대상**: 현재 프로젝트 코드베이스 (구조·스택·빌드/테스트·관례)
- **출력**: 프로젝트 루트의 `CLAUDE.md`
- **동작**: 분석 → 요약 → 메모리 파일 생성/초기화

<a id="init---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 명령/스킬**
- 경로: 없음 (내장)

## keybindings-help

> `~/.claude/keybindings.json`을 편집해 Claude Code의 키보드 단축키를 커스터마이즈하는 빌트인 스킬.

<a id="keybindings-help---용도"></a>
### 📌 용도
Claude Code 터미널 UI의 **키 바인딩을 사용자 정의**한다. 기본 단축키를 다른 키로 재할당(rebind)하거나, 여러 키를 순차로 누르는 **chord(연속) 바인딩**을 추가하는 등 입력 동작을 바꾼다. 대상 파일은 `~/.claude/keybindings.json` 한 개다.

<a id="keybindings-help---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "단축키 바꿔줘 / 재할당해줘 / rebind 해줘"
  - "ctrl+s를 다른 동작에 연결해줘"
  - "chord 단축키(연속 키 입력) 추가해줘"
  - "제출(submit) 키를 바꾸고 싶어"
  - keybindings.json을 직접 손봐야 하는 모든 작업
- **언제 쓰지 않는가**
  - 권한/환경변수/hook 등 동작 설정은 `update-config`(settings.json) 담당
  - 에디터(VSCode 등) 자체의 단축키와는 무관 — 어디까지나 Claude Code TUI 한정

<a id="keybindings-help---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "ctrl+s를 rebind 해줘"
- "chord 단축키 하나 추가해줘 (예: ctrl+k 다음 ctrl+d)"
- "submit 키를 enter 대신 ctrl+enter로 바꿔줘"
- "기본 키맵을 내 취향대로 커스터마이즈하고 싶어"

<a id="keybindings-help---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **대상 파일**: `~/.claude/keybindings.json`
- **바인딩 유형**:
  - 단일 키 재할당 (rebind)
  - chord 바인딩 (키 시퀀스 → 동작)
- 액션과 키 조합의 매핑 구조를 편집

<a id="keybindings-help---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장). 수정 대상 파일은 `~/.claude/keybindings.json`

## loop

> 프롬프트나 슬래시 명령을 **주기적으로 반복 실행**하는 빌트인 스킬. 인터벌을 주면 그 간격으로, 생략하면 모델이 스스로 페이스를 정해 반복한다.

<a id="loop---용도"></a>
### 📌 용도
같은 작업을 **일정 간격으로 계속 실행**해야 할 때 쓴다. 상태 폴링, 주기적 점검, 반복 작업 자동화 등에 적합하다. 인터벌(예: `5m`)을 지정하면 그 주기로 반복하고, 인터벌을 생략하면 모델이 self-pace(스스로 적절한 간격 판단)로 반복한다.

`schedule`이 **클라우드에서 cron으로 도는 영구 routine**이라면, `loop`는 **현재 세션 안에서 도는 반복 실행**에 가깝다.

<a id="loop---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "5분마다 배포 상태 확인해줘"
  - "/babysit-prs 계속 돌려줘"
  - 상태 폴링, 주기적 반복 작업 설정
- **언제 쓰지 않는가**
  - **1회성 작업**에는 절대 쓰지 않는다 (반복이 아니면 그냥 직접 실행)
  - 세션과 무관하게 정해진 시각/cron으로 돌리려면 `schedule`

<a id="loop---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/loop 5m /foo` — 5분마다 `/foo` 슬래시 명령 실행
- `/loop 5m 배포 상태 확인` — 5분마다 해당 프롬프트 실행
- `/loop /check-deploy` — 인터벌 생략 → 모델이 self-pace로 반복
- "deploy를 5분마다 체크해줘" / "keep running /babysit-prs"

<a id="loop---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **인터벌**: `5m` 같은 시간 간격. **생략 시 모델 self-pace**
- **실행 대상**: 슬래시 명령(`/foo`) 또는 일반 프롬프트
- **용도 분류**: 폴링 / 주기적 반복 작업

<a id="loop---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장)

## review

> PR / 코드 리뷰를 수행하는 빌트인 명령.

<a id="review---용도"></a>
### 📌 용도
Pull Request나 코드 변경에 대한 리뷰를 수행하는 내장 명령이다. 변경 사항을 검토해 문제점·개선점을 짚어 준다. 일반적으로 GitHub PR 등 변경 단위를 대상으로 한 코드 리뷰 진입점 역할을 한다.

참고: 보다 세밀한 effort 제어(low~ultra), `--comment`/`--fix` 같은 옵션이 필요하면 `code-review` 스킬이 더 풍부한 기능을 제공한다. 보안 전용 관점은 `security-review`를 쓴다.

<a id="review---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "이 PR 리뷰해줘"
  - "코드 리뷰 돌려줘"
- **언제 쓰지 않는가**
  - effort 레벨·인라인 코멘트·자동 수정 등 세부 제어가 필요하면 `code-review`
  - 보안 취약점 중심 리뷰는 `security-review`
  - 동작 검증은 `verify` / `run`

<a id="review---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/review` — 현재 PR/변경에 대한 리뷰 수행

<a id="review---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **대상**: PR / 코드 변경
- **동작**: 변경 검토 후 리뷰 결과 제시
- (세부 옵션이 필요하면 `code-review` 참고)

<a id="review---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 명령/스킬**
- 경로: 없음 (내장)

## run

> 프로젝트 앱을 **실제로 띄워서** 변경이 동작하는지 확인하는 빌트인 스킬. 프로젝트 타입(CLI/server/TUI/Electron/browser/library)별 구동 패턴을 안다.

<a id="run---용도"></a>
### 📌 용도
"테스트만 통과"가 아니라 **진짜 앱에서 변경이 동작하는 것을 보기 위해** 프로젝트 앱을 실행·구동한다. 앱 실행, 시작, 스크린샷 요청이나 "이 변경이 실제 앱에서 되는지 확인" 같은 요청을 처리한다.

동작 순서: **먼저 프로젝트에 앱 구동을 다루는 프로젝트 전용 스킬이 있는지 찾고**, 없으면 프로젝트 타입별 빌트인 패턴으로 폴백한다.

`run`이 "어떻게 띄우는가"라면, `verify`는 "띄운 뒤 의도한 동작이 나오는가"를 검증한다 — 둘은 짝을 이룬다.

<a id="run---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "앱 실행해줘 / 시작해줘 / 스크린샷 찍어줘"
  - "이 변경이 실제 앱에서 동작하는지 확인해줘" (테스트 말고)
- **언제 쓰지 않는가**
  - 동작이 "의도대로"인지까지 판정해야 하면 `verify`
  - 코드 정적 검토는 `code-review` / `simplify`
  - 변경 없이 단순 코드 설명만 원할 때

<a id="run---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "앱 띄워서 보여줘"
- "서버 돌려서 새 엔드포인트 응답 확인해줘"
- "이 UI 변경 스크린샷 찍어줘"

<a id="run---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **선행 탐색**: 앱 구동을 이미 다루는 **프로젝트 스킬**이 있으면 그것을 우선 사용
- **폴백 패턴 (프로젝트 타입별)**:
  - **CLI** — 커맨드 직접 실행
  - **server** — 서버 기동 후 요청
  - **TUI** — 터미널 UI 구동
  - **Electron** — 데스크톱 앱 구동
  - **browser-driven** — 브라우저 자동화로 구동
  - **library** — 호출 예제/하네스로 구동

<a id="run---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장)

## schedule

> **cron 스케줄로 도는 클라우드 에이전트(routines)**를 생성·수정·목록·실행하는 빌트인 스킬. 1회성 예약 실행도 지원.

<a id="schedule---용도"></a>
### 📌 용도
정해진 일정에 따라 **클라우드에서 자동으로 실행되는 Claude Code 에이전트(routine)**를 관리한다. cron 표현식으로 주기를 정해 반복 실행하거나, 특정 시각에 단 한 번 실행하는 1회성 예약도 만들 수 있다. routine의 생성·수정·목록 조회·즉시 실행을 모두 다룬다.

`loop`이 현재 세션 안에서 반복한다면, `schedule`은 **세션과 독립적으로 클라우드에서 cron으로 도는 영구 자동화**다.

<a id="schedule---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "매일 아침 9시에 이거 실행되게 스케줄 걸어줘"
  - "Claude Code용 cron job 만들어줘"
  - "내 예약된 에이전트(routines) 목록 보여줘 / 수정해줘"
  - "오후 3시에 한 번만 실행해줘", "내일 X 확인하라고 알려줘" (1회성 예약)
- **언제 쓰지 않는가**
  - 현재 세션 안에서만 반복하면 되는 작업은 `loop`
  - 즉시 1회 실행하면 되는 작업은 그냥 직접 수행

<a id="schedule---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/schedule 매주 월요일 오전에 의존성 업데이트 점검` — 클라우드 routine 생성 절차를 시작한다.
- "내 routine 목록 보여줘"
- "X routine의 cron을 매시간으로 바꿔줘"
- "내일 오후 3시에 한 번만 배포 상태 확인해줘" (1회성)

<a id="schedule---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **관리 동작**: routine **생성 / 수정 / 목록(list) / 즉시 실행(run)**
- **스케줄 형식**: cron 표현식 (반복) 또는 1회성 예약 시각
- **실행 위치**: 클라우드 (세션과 독립)
- **클라우드 관리**: `/schedule`(별칭 `/routines`) 또는 계정의 Routines 화면을 사용한다. 저장 후 계정의 routine 목록에서 생성·일정·실행 상태를 확인한다. [공식 routines 안내](https://code.claude.com/docs/en/routines)를 따른다.
- **세션 작업과 구분**: `CronCreate`·`CronList`·`CronDelete`는 현재 세션의 예약 작업 도구이며 클라우드 routine을 생성하지 않는다. [세션 예약 도구](https://code.claude.com/docs/en/scheduled-tasks#manage-scheduled-tasks)는 `loop`나 세션 안의 일회성 알림에 사용한다.

<a id="schedule---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장)

## security-review

> **보안 취약점 관점**에서 코드를 리뷰하는 빌트인 명령.

<a id="security-review---용도"></a>
### 📌 용도
코드 변경(또는 코드베이스)을 **보안 관점**에서 검토한다. 인젝션, 인증/인가 결함, 비밀정보 노출, 안전하지 않은 입력 처리, 위험한 의존성 사용 등 **보안 취약점**에 초점을 맞춘 리뷰를 수행한다. 일반 correctness 리뷰(`code-review`)와 달리, 공격 표면과 보안 리스크에 특화돼 있다.

<a id="security-review---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "보안 취약점 있는지 검토해줘"
  - "이 변경 보안 리뷰 돌려줘"
  - 민감 데이터·인증·외부 입력을 다루는 코드 변경 시
- **언제 쓰지 않는가**
  - 일반 버그/정확성 리뷰는 `code-review`
  - 품질 정리(리팩터링)는 `simplify`
  - 동작 검증은 `verify` / `run`

<a id="security-review---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/security-review` — 현재 변경/코드를 보안 관점으로 리뷰

<a id="security-review---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **리뷰 관점**: 보안 취약점 (인젝션, 인증/인가, 비밀정보 노출, 안전하지 않은 입력 처리 등)
- **대상**: 코드 변경 또는 코드베이스
- **동작**: 보안 리스크 식별 후 보고

<a id="security-review---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 명령/스킬**
- 경로: 없음 (내장)

## simplify

> 변경된 코드를 **재사용·단순화·효율성·altitude(추상화 수준)** 관점에서 정리하고 그 수정을 직접 적용하는 빌트인 스킬. **품질 전용**이며 버그는 찾지 않는다.

<a id="simplify---용도"></a>
### 📌 용도
방금 변경한 코드의 **품질을 끌어올리는 리팩터링**을 수행하고 적용한다. 네 가지 관점을 본다.
- **reuse**: 이미 있는 함수/유틸로 대체 가능한 중복 제거
- **simplification**: 불필요하게 복잡한 로직을 단순하게
- **efficiency**: 비효율적인 처리 개선
- **altitude**: 코드의 추상화 수준을 적절히 맞춤 (너무 저수준/고수준이 섞이지 않게)

중요: **버그 헌팅은 하지 않는다.** correctness 결함 탐지가 필요하면 `code-review`를 써야 한다. simplify는 "동작은 맞다는 전제하의 품질 정리"에 특화돼 있다.

<a id="simplify---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "방금 짠 코드 좀 정리/단순화해줘"
  - "중복 줄이고 깔끔하게 리팩터링해줘"
  - 변경 직후 품질만 다듬고 싶을 때
- **언제 쓰지 않는가**
  - **버그를 찾고 싶으면** `code-review` (simplify는 버그 안 봄)
  - 동작 검증은 `verify` / `run`
  - 보안 검토는 `security-review`

<a id="simplify---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/simplify` — 변경된 코드를 4관점으로 정리하고 워킹트리에 적용
- "이번에 추가한 코드 reuse 관점에서 정리해줘"

<a id="simplify---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **리뷰·적용 관점**: reuse / simplification / efficiency / altitude
- **동작**: 발견한 정리 사항을 단순 제안에 그치지 않고 **직접 적용**
- **범위**: 변경된(changed) 코드 한정
- **명시적 비범위**: correctness 버그 탐지 없음 → `code-review` 사용

<a id="simplify---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장)
- 참고: 이름이 비슷한 `code-simplifier` 플러그인(ON)은 별개다 — 그쪽은 **에이전트**(`code-simplifier`)를 제공하며, 이 `/simplify` 빌트인 스킬과 다르다.

## update-config

> `settings.json` / `settings.local.json`을 직접 편집해 Claude Code 하네스(harness)를 설정하는 빌트인 스킬. 권한·환경변수·hook·자동 동작을 다룬다.

<a id="update-config---용도"></a>
### 📌 용도
Claude Code의 **동작 자체를 바꾸는 설정 파일**을 수정한다. Claude의 "기억/선호"로는 불가능한, 하네스 레벨의 영구 설정을 담당한다.

핵심 개념: **"앞으로 X 할 때마다 Y 해라" 같은 자동 동작은 Claude의 메모리로 충족할 수 없다.** 이런 자동화는 하네스가 실행하는 **hook**으로만 구현 가능하다. Claude는 매 턴 메모리를 "참고"할 뿐 강제 실행하지 않기 때문이다. 따라서 다음과 같은 요청은 전부 이 스킬이 처리한다.

- **권한(permissions)**: 특정 명령/도구를 자동 허용·거부·확인 목록에 추가. ("npm 명령 허용", "bq 권한을 글로벌 settings에 추가", "이 권한을 user settings로 옮겨라")
- **환경변수(env)**: Claude Code 프로세스에 주입할 환경변수 설정. ("DEBUG=true 설정")
- **hook**: 특정 이벤트(도구 사용 전후, 세션 시작/종료, Claude 응답 종료 등)에 자동 실행할 동작 등록. ("Claude가 응답을 끝내면 X를 표시해라", "커밋 전마다 린트 돌려라")
- **hook 트러블슈팅**: 등록한 hook이 안 먹을 때 원인 진단.
- **settings.json / settings.local.json 관련 모든 변경**.

<a id="update-config---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "앞으로 ~할 때마다 / 매번 / ~하기 전에·후에 ~해줘" 같은 **자동 반복 동작** 요청 (→ hook 필요)
  - "~ 허용해줘 / 권한 추가 / 권한을 다른 settings로 이동" 같은 권한 변경
  - "환경변수 X=Y로 설정" 같은 env 변경
  - hook이 동작하지 않을 때의 디버깅
  - settings.json / settings.local.json 파일을 손대야 하는 모든 작업
- **언제 쓰지 않는가**
  - theme, model 같은 **단순 설정**은 이 스킬 대신 `/config` 명령을 안내 (대화형 UI가 더 빠름)
  - 1회성 작업(자동 반복이 아닌 것)은 hook이 필요 없으므로 그냥 직접 수행
  - 프로젝트 코드 자체의 수정과는 무관

<a id="update-config---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "npm 명령은 매번 허용으로 해줘" → permissions.allow에 npm 패턴 추가
- "DEBUG=true 환경변수 설정해줘" → env에 키 추가
- "claude가 멈출 때(Stop) 알림을 띄워줘" → Stop hook 등록
- "이 bq 권한을 프로젝트가 아니라 글로벌(user) settings로 옮겨줘" → 권한 항목을 파일 간 이동
- "내가 만든 PreToolUse hook이 안 도는데 봐줘" → hook 설정 진단

<a id="update-config---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **대상 파일**:
  - `settings.json` (프로젝트 공유 설정)
  - `settings.local.json` (프로젝트 로컬·개인 설정, git 제외 권장)
  - user(글로벌) settings (`~/.claude/settings.json`)
- **주요 키 영역**: `permissions`(allow/deny/ask), `env`, `hooks`
- **hook 이벤트(예)**: PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification
- **권한 스코프 구분**: 프로젝트 settings ↔ user settings 간 이동 지원

<a id="update-config---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬** — 별도 SKILL.md 파일 없이 하네스에 내장
- 경로: 없음 (내장). 수정 대상은 `~/.claude/settings.json`, 프로젝트 `.claude/settings.json` / `.claude/settings.local.json`

## verify

> 코드 변경이 **실제로 의도대로 동작하는지** 앱을 직접 실행해 동작을 관찰하며 검증하는 빌트인 스킬.

<a id="verify---용도"></a>
### 📌 용도
정적 분석이나 테스트 통과만으로 끝내지 않고, **앱을 진짜로 띄워서 동작을 눈으로 확인**해 변경의 의도가 충족됐는지 검증한다. PR 검증, 버그 수정 확인, 기능 동작 확인, 푸시 전 로컬 변경 검증 등에서 "정말 되는지"를 보장하는 역할.

`run` 스킬이 "앱을 어떻게 띄우는가"에 집중한다면, `verify`는 "띄운 뒤 의도한 동작이 실제로 나타나는가"를 검증하는 데 초점이 있다.

<a id="verify---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "이 PR 검증해줘"
  - "이 수정(fix)이 진짜 되는지 확인해줘"
  - "이 변경을 수동으로 테스트해줘"
  - "이 기능이 동작하는지 봐줘"
  - "푸시하기 전에 로컬 변경 검증해줘"
- **언제 쓰지 않는가**
  - 단순히 앱을 실행/스크린샷만 원하면 `run`이 더 적합
  - 코드 품질 정리(중복/단순화)는 `simplify`, 버그 헌팅은 `code-review`
  - 변경 없이 단순 조회/설명 요청

<a id="verify---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "방금 고친 로그인 버그, 앱 띄워서 실제로 고쳐졌는지 확인해줘"
- "이 PR 머지 전에 동작 검증해줘"
- "새로 추가한 기능이 UI에서 의도대로 보이는지 확인해줘"

<a id="verify---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **검증 흐름**: 앱 실행 → 변경과 관련된 동작 재현 → 기대 동작과 실제 동작 비교 → 결과 보고
- 프로젝트를 실제로 구동해야 하므로 내부적으로 앱 실행 패턴(`run` 스킬과 유사한 프로젝트 타입별 구동)을 활용
- 통과/실패 및 관찰된 실제 동작을 근거로 결론 제시

<a id="verify---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **빌트인(내장) 스킬**
- 경로: 없음 (내장)
