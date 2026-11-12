<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# _personal 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. Claude 경로·하네스 등록·파일 미발견 표시는 작성 당시 환경의 기록이다. 현재 Codex의 동명 자체 제작 원본·설치·지원 범위는 [Owned-Skills](../../Owned-Skills/README.md)에서 확인하며, 아래 과거 경로를 현재 설치 근거로 사용하지 않는다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [claude-news](#claude-news).
- [deep-research](#deep-research).
- [delete-session](#delete-session).
- [design-driven-delivery](#design-driven-delivery).
- [handover](#handover).

## claude-news

> Claude Code 릴리스 노트 + Anthropic 모델/제품 소식을 **한국어로 요약**하는 개인 글로벌 스킬. 새 기능과 주요 변경을 카테고리별로 정리해 보여준다.

<a id="claude-news---용도"></a>
### 📌 용도
두 출처의 소식을 모아 한국어로 정리한다.
1. **Anthropic 공식 뉴스** (`https://www.anthropic.com/news`) — **모델 출시/제품 발표만** 필터링
2. **Claude Code 릴리스 노트** (GitHub `anthropics/claude-code`) — 새 기능·주요 변경 위주

개발자 실무와 무관한 항목(정치/정책 성명, 사업 투자, 채용/오피스 확장, 연구 논문)은 소식에서 제외한다. 릴리스 노트는 새 기능·주요 변경만 항목으로 보이고, 버그 수정·기타 개선은 건수만 집계한다.

<a id="claude-news---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "Claude 뉴스 / Claude Code 업데이트 알려줘"
  - 최근 릴리스·신기능·모델 소식을 한국어 요약으로 보고 싶을 때
  - `/claude-news`, `/claude-news 5`(개수), `/claude-news <버전>` 호출
- **언제 쓰지 않는가**
  - 특정 코드/프로젝트 질문 (그건 일반 도구나 RAG)
  - Anthropic 외 제공자 소식

<a id="claude-news---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/claude-news` — 기본 선택 로직(10일 이내 전부 표시, 5개 미만이면 보충)으로 소식+릴리스 요약
- `/claude-news 5` — 최근 릴리스 5개 가져오기 (숫자 인자)
- `/claude-news v2.x.xx` — 특정 버전 릴리스만
- 후속: "A1 자세히" / "3번 더 알려줘" / "MCP 관련만" — 번호로 특정 항목 심화 설명

<a id="claude-news---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 도구**: `WebFetch`(Anthropic 뉴스), `mcp__github__list_releases`(릴리스)
- **인자($ARGUMENTS)**: 숫자=개수 / 버전=특정 릴리스 / 생략=기본 선택 로직
- **기본 선택 로직**: 최근 10개부터 추가 페이지를 조회해 10일 이내 전부 표시 → 5개 미만이면 이전 유효 릴리스로 5개 채움 → 10일 이내=[NEW], 그 외=[최근]
- **분류 규칙**: Added=새 기능, 주요 Changed/Removed/Deprecated=주요 변경(항목), Fixed=버그 수정 N건, Improved/나머지=기타 개선 N건
- **번역 규칙**: 기술 용어(MCP, worktree, hook, slash command)는 원어 유지, Windows/Git Bash 항목은 **[Windows]** 태그
- **번호 체계**: 소식 A1·A2…, 릴리스 항목 1·2·3 연속
- **주의**: body 빈 릴리스 건너뜀, WebFetch 실패 시 소식 생략하고 릴리스만, GitHub API 실패 시 에러 안내·재시도

<a id="claude-news---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **개인 글로벌 스킬** (`~/.claude/skills`)
- 경로: `~/.claude/skills/claude-news/SKILL.md`

## deep-research

> 멀티소스 웹 검색 + 소스 fetch + **교차검증(adversarial verify)** + 인용 포함 리포트 합성을 수행하는 개인 글로벌 딥리서치 스킬.

<a id="deep-research---용도"></a>
### 📌 용도
어떤 주제든 **깊이 있고, 다출처(multi-source) 기반으로 팩트체크된 리서치 리포트**를 만든다. 동작 흐름:
1. **fan-out 웹 검색** — 질문을 여러 검색으로 분산 실행
2. **소스 fetch** — 검색으로 찾은 출처의 실제 내용을 가져옴
3. **adversarial verify** — 주장(claim)을 반대 관점에서 교차검증해 신뢰성 확인
4. **합성** — 검증된 내용을 **인용(citation)이 달린 리포트**로 종합

중요한 선행 단계: **질문이 충분히 구체적인지 먼저 판단한다.** 범위가 모호하면(예: 예산/용도/지역 없는 "어떤 차 살까") 바로 조사하지 않고 **2~3개 명확화 질문**으로 범위를 좁힌 뒤, 그 답을 녹여 정제된 질문으로 리서치를 시작한다.

<a id="deep-research---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - 어떤 주제에 대해 **깊고, 다출처로, 팩트체크된 리서치 리포트**를 원할 때
  - "이 주제 깊게 조사해서 출처까지 정리해줘"
- **언제 쓰지 않는가**
  - 단순 1회 검색이나 빠른 사실 확인 (일반 웹 검색이면 충분)
  - 질문이 너무 모호한 채로 들어오면 → **먼저 명확화 질문** (바로 조사 X)

<a id="deep-research---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/deep-research <정제된 질문>` — 명확화된 질문을 args로 넘겨 리서치 시작
- "2024~2025 전기차 보조금 정책 비교, 출처 포함 리포트로" → (필요 시 지역·차종 등 2~3개 질문 후) 리서치
- 모호한 입력 시: "예산은 얼마인지 / 용도는 무엇인지 / 지역은 어디인지" 같은 명확화 질문 먼저

<a id="deep-research---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **파이프라인**: fan-out 웹 검색 → 소스 fetch → adversarial 교차검증 → 인용 리포트 합성
- **선행 게이트**: 질문 구체성 점검 → 부족하면 2~3개 명확화 질문 → 답을 반영한 정제 질문으로 진행
- **인자(args)**: 정제된(명확화된) 리서치 질문을 전달
- **출력**: 출처 인용이 포함된 종합 리포트

<a id="deep-research---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **개인 글로벌 스킬** (`~/.claude/skills`)
- 경로: 표준 `~/.claude/skills/deep-research/SKILL.md` 미발견 — 하네스에 등록된 개인 스킬로 동작(별도 SKILL.md 파일 없이 제공). 시스템 제공 description 기준으로 문서화함.

## delete-session

> 현재 프로젝트의 **세션 목록을 보여주고**, 선택한 세션의 `jsonl` 파일을 삭제해 resume 리스트에서 제거하는 개인 글로벌 스킬.

<a id="delete-session---용도"></a>
### 📌 용도
현재 프로젝트에 쌓인 Claude Code 세션 기록을 정리한다. 프로젝트의 세션 목록을 표시한 뒤, 사용자가 고른 세션의 `.jsonl` 저장 파일을 삭제한다. 삭제된 세션은 이후 `--resume`(세션 이어가기) 목록에서 사라진다. 불필요하거나 잘못 시작된 세션, 더 이상 이어갈 필요 없는 세션을 깔끔하게 비울 때 쓴다.

<a id="delete-session---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "이 프로젝트 세션 목록 보여줘 / 정리해줘"
  - "필요 없는 세션 삭제해줘"
  - resume 목록을 비우거나 줄이고 싶을 때
- **언제 쓰지 않는가**
  - 세션 내용을 **인수인계 문서로 저장**하려면 `handover`
  - 현재 진행 중인 작업 자체와는 무관 (기록 관리용)
  - 다른 프로젝트의 세션 (현재 프로젝트 한정)

<a id="delete-session---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/delete-session` — 현재 프로젝트 세션 목록 표시 → 선택 → 해당 jsonl 삭제
- "오늘 잘못 만든 세션 지워줘"

<a id="delete-session---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **동작 흐름**: 세션 목록 표시 → 사용자 선택 → 선택 세션 `jsonl` 삭제
- **효과**: resume(이어가기) 리스트에서 제거
- **범위**: 현재 프로젝트의 세션 저장 디렉터리

<a id="delete-session---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **개인 글로벌 스킬** (`~/.claude/skills`)
- 경로: 표준 `~/.claude/skills/delete-session/SKILL.md` 미발견 — 하네스에 등록된 개인 스킬로 동작(별도 SKILL.md 파일 없이 제공). 시스템 제공 description 기준으로 문서화함.

## design-driven-delivery

> 상태 변경 요청을 분류하고 설계·계획·구현·검증·리뷰·문서화·통합 순서로 통제하는 자체 제작 최상위 프로젝트 전달 Skill이다.

<a id="design-driven-delivery---용도"></a>
### 📌 용도.

모든 사용자 요청을 읽기 전용, 진단, 상태 변경 또는 모니터링으로 먼저 분류한다. 기능 개발·버그 수정·리팩터링·코드·설정·문서·데이터·배포 변경에는 증거 기반 상태 머신을 적용하고, 기존 전문 Skill을 승인된 순서로 호출한다.

<a id="design-driven-delivery---트리거-조건"></a>
### 🎯 트리거 조건.

- **언제 호출되는가.**
  - 모든 사용자 메시지에서 변경 범위를 먼저 판정할 때.
  - 기능·버그·리팩터링·문서·설정·데이터·배포·커밋·병합·푸시 작업을 시작할 때.
- **언제 전체 워크플로를 실행하지 않는가.**
  - 단순 조회·설명·상태 보고.
  - 수정 요청이 없는 원인 진단·리뷰·감사.
  - 승인된 범위만 추적하는 모니터링.
- **Skill 유형.**
  - 최상위 라우터이자 증거 게이트다. 전문 Skill의 절차를 중복 구현하지 않는다.

<a id="design-driven-delivery---사용-예시"></a>
### 💻 사용 예시.

- `$design-driven-delivery로 이 기능을 설계부터 검증과 통합까지 진행해 주세요.`
- “이 오류를 진단하고 수정까지 진행해줘.”
- “전체 변경을 검증하고 코드 리뷰 후 커밋·푸시해줘.”
- “현재 상태만 설명해줘.”라고 요청하면 읽기 전용 흐름으로 종료한다.

<a id="design-driven-delivery---제공-절차와-도구"></a>
### 🛠️ 제공 절차와 도구.

- 상태 흐름은 `DISCOVERED → DISCUSSING → DESIGN_APPROVED → PLAN_APPROVED → IMPLEMENTING → VERIFIED → REVIEWED → DOCUMENTED → COMMITTED → INTEGRATED`다.
- 새 기능은 `brainstorming`, 승인 설계는 `writing-plans`, 구현은 Worktree·TDD·체계적 디버깅을 조율한다.
- 완료 전 `verification-before-completion`, 전체 변경에 `code-review`, 브랜치 통합에 `finishing-a-development-branch`를 호출한다.
- 기본 문서 구조를 비덮어쓰기 방식으로 초기화하는 `bootstrap_workflow.py`와 완료 증거를 검사하는 `validate_workflow.py`를 제공한다.
- 초기화는 기존 `docs/specs`·`docs/plans`도 유지한다. 검증의 `--spec`, `--plan`, `--review`로 현재 작업의 Markdown 문서를 지정한다. 경로는 프로젝트 상대경로이며 반복 가능하다. 미지정 종류는 전체 기본 경로를 검사한다. 상세 계약은 [문서 계약](../../Owned-Skills/design-driven-delivery/references/document-contracts.md)을 따른다.
- 프로젝트별 검증은 Unity, Web, Backend, Python·CLI, Data, Mobile·Desktop, Infrastructure Adapter에서 선택한다.

<a id="design-driven-delivery---출처와-설치-상태"></a>
### 📦 출처와 설치 상태.

- 분류: **자체 제작 개인 글로벌 Skill**.
- 공개 원본: [`Owned-Skills/design-driven-delivery`](../../Owned-Skills/design-driven-delivery/SKILL.md).
- Codex 사용자 설치 예시: `~/.agents/skills/design-driven-delivery`.
- UI 메타데이터는 `agents/openai.yaml`에 있으며 암시적 호출을 허용한다.
- 저장소의 MIT License가 직접 작성한 Skill 원본에 적용된다.

## handover

> 현재 세션 전체 내용을 **다음 세션 인수인계용 md 파일**로 정리·저장하는 개인 글로벌 스킬.

<a id="handover---용도"></a>
### 📌 용도
현재 진행한 작업 세션의 내용을 다음 세션이 이어받을 수 있도록 **인수인계(handover) 문서**로 정리해 md 파일로 저장한다. 작업 상태, 수정한 파일, 결정 사항, 남은 일 등 다음 세션이 컨텍스트 없이 시작하지 않도록 핵심을 보존하는 것이 목적이다.

`/compact`가 컨텍스트를 압축해 같은 세션을 이어간다면, `handover`는 **세션을 끊고 새 세션으로 넘길 때** 인수인계 문서를 남기는 용도다. (글로벌 CLAUDE.md의 Compact Instructions에 정의된 보존 항목 — 현재 작업 상태/수정 파일/실패한 접근/미해결 버그/사용자 지시/설계 결정 — 과 같은 정신으로 정리하면 좋다.)

<a id="handover---파일-생성-규칙"></a>
### 🗂️ 파일 생성 규칙

- **저장 폴더**: 사용자 홈 아래 `Desktop\Agent\handovers\`. 실행 환경의 사용자 홈을 확인해 절대 경로로 해석한다.
- **파일명**: `HANDOVER_{project-name}_{YYYYMMDD}_{topic-slug}.md`
- **프로젝트명 결정 순서**: 사용자가 명시한 이름 → Git 루트 폴더명 → 현재 작업 폴더명.
- 현재 작업 폴더가 홈·Desktop처럼 프로젝트를 특정할 수 없거나 여러 프로젝트가 섞여 있으면 추측하지 않고 사용자에게 확인한다.
- `project-name`의 공백은 `-`로 바꾸고 파일명에 사용할 수 없는 문자는 제거한다.
- `topic-slug`는 프로젝트명을 제외한 실제 작업 주제만 영문 kebab-case 2~5단어로 작성한다. 프로젝트명은 대소문자나 `-`·`_` 차이가 있어도 반복하지 않는다.
- 기존 handover 파일은 덮어쓰지 않는다. 같은 파일명이 있으면 `_2`, `_3` 접미사를 붙인다.
- 예시: `HANDOVER_AISafety_20260828_auth-middleware-refactor.md`.

<a id="handover---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**
  - "이 세션 인수인계 문서로 정리해줘"
  - "다음 세션에서 이어가게 핸드오버 만들어줘"
  - 긴 작업을 마치고 세션을 종료하기 직전, 컨텍스트를 파일로 남기고 싶을 때
- **언제 쓰지 않는가**
  - 같은 세션을 계속 이어갈 거면 `/compact`가 적합
  - 세션 기록(jsonl) 자체를 삭제·정리하려면 `delete-session`

<a id="handover---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/handover` — 현재 세션 전체를 인수인계용 md로 정리·저장
- "지금까지 한 거 핸드오버 파일로 만들어줘"

<a id="handover---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **입력**: 현재 세션의 전체 대화/작업 내용
- **출력**: 인수인계용 **md 파일** (다음 세션이 읽고 이어갈 수 있는 형태)
- **권장 보존 항목**: 현재 작업 상태 / 수정 파일 목록·이유 / 실패한 접근 / 미해결 버그 / 사용자 지시 / 설계 결정과 근거

<a id="handover---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 분류: **개인 글로벌 스킬** (`~/.claude/skills`)
- 경로: 표준 `~/.claude/skills/handover/SKILL.md` 미발견 — 하네스에 등록된 개인 스킬로 동작(별도 SKILL.md 파일 없이 제공). 시스템 제공 description 기준으로 문서화함.
