<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# _disabled/hookify 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. 활성 표시는 작성 당시 환경의 기록이다. [전체 항목 목차](../../CATALOG.md)에서 다른 분류를 찾는다.

- [configure](#configure).
- [help](#help).
- [hookify](#hookify).
- [list](#list).
- [writing-rules](#writing-rules).

## configure

> 기존 hookify 규칙을 인터랙티브하게 활성/비활성 토글하는 커맨드.

<a id="configure---용도"></a>
### 📌 용도
이미 만들어진 hookify 규칙들을 대화형 인터페이스로 켜거나 끈다. 규칙 파일을 찾아 현재 상태(enabled)를 읽고, 사용자가 토글할 규칙을 선택하면 해당 파일의 `enabled` 값을 뒤집는다. 규칙을 삭제하지 않고 상태만 전환한다. 실행 시 먼저 `hookify:writing-rules` 스킬을 로드한다.

<a id="configure---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 기존 hookify 규칙을 일시적으로 켜거나 끄고 싶을 때.
- **언제 쓰지 않는가**: 새 규칙 생성(→ `/hookify`), 규칙 목록만 보기(→ `/hookify:list`), 규칙 영구 삭제(→ `.local.md` 파일 직접 삭제).

<a id="configure---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/hookify:configure
```
- 인자 없음. 실행 시 규칙 목록을 제시하고 AskUserQuestion으로 토글 대상을 multiSelect로 선택받는다.

<a id="configure---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
allowed-tools: `Glob`, `Read`, `Edit`, `AskUserQuestion`, `Skill`.

절차:
1. **규칙 찾기**: Glob 패턴 `.claude/hookify.*.local.md`. 없으면 "`/hookify`로 먼저 규칙을 만들라" 안내.
2. **현재 상태 읽기**: 각 파일에서 프론트매터 `name`, `enabled` 추출.
3. **토글 대상 선택**: AskUserQuestion(multiSelect). 옵션 라벨 형식 `{rule-name} (currently {enabled|disabled})`, 설명은 규칙 메시지/패턴 요약.
4. **선택 파싱**: 선택된 규칙마다 현재 상태를 반대로 토글.
5. **파일 수정**: Read로 읽고 Edit로 `enabled: true` ↔ `enabled: false` 교체(따옴표 유무 모두 처리).
6. **변경 확인**: Enabled/Disabled/Unchanged로 구분해 보여주고 즉시 반영(재시작 불필요)임을 알림.

엣지 케이스: 규칙 없음 → `/hookify`로 생성 안내 / 아무것도 선택 안 함 → 변경 없음 안내 / 파일 읽기·쓰기 오류 → 구체적 오류 표시 후 수동 편집 대안 제시.

<a id="configure---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: hookify@claude-plugins-official
- 활성화: ⛔ **OFF** (settings.json enabledPlugins = false) — 켜야 사용 가능
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/hookify/unknown/commands/configure.md`

## help

> hookify 플러그인의 동작 원리와 사용법을 설명하는 도움말 커맨드.

<a id="help---용도"></a>
### 📌 용도
hookify 플러그인이 어떻게 작동하는지, 규칙을 어떻게 만들고 쓰는지 설명한다. hookify는 `hooks.json`을 직접 편집하지 않고도, 감시할 패턴을 정의한 간단한 마크다운 설정 파일(`.claude/hookify.*.local.md`)로 커스텀 훅을 만들 수 있게 해준다. 이 커맨드는 훅 시스템·설정 파일·규칙 생성 방법·패턴 문법·문제 해결·시작 가이드를 한 화면에 정리해 보여준다.

<a id="help---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: hookify 플러그인의 개념·동작·사용법을 알고 싶을 때.
- **언제 쓰지 않는가**: 실제 규칙 생성(→ `/hookify`), 목록 조회(→ `/hookify:list`), 활성/비활성 토글(→ `/hookify:configure`)일 때.

<a id="help---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/hookify:help
```
- 인자 없음. 출력에 포함되는 다른 커맨드 안내:
  - `/hookify` — 대화 분석 또는 명시적 지시로 훅 생성
  - `/hookify:help` — 이 도움말
  - `/hookify:list` — 설정된 훅 목록
  - `/hookify:configure` — 기존 훅 활성/비활성 토글

<a id="help---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
allowed-tools: `Read`.

설명하는 핵심 내용:
- **훅 시스템**: hookify는 PreToolUse / PostToolUse / Stop / UserPromptSubmit 이벤트에서 동작하는 범용 훅을 설치하고, `.claude/hookify.*.local.md` 설정을 읽어 현재 작업과 매치되는 규칙이 있는지 검사한다.
- **설정 파일 필드**: `name`, `enabled`, `event`(bash/file/stop/prompt/all), `pattern`(정규식). 메시지 본문이 트리거 시 Claude에게 보이는 내용.
- **규칙 생성 3가지 방법**: `/hookify <지시>` / 수동 파일 생성 / 인자 없는 `/hookify`(대화 분석).
- **패턴 문법**: Python regex (`\s`, `\.`, `|`, `+`, `*`, `\d`, `[abc]` 등).
- **중요 사항**: 재시작 불필요(즉시 반영), block/warn 선택(`action` 필드), 규칙 파일은 git-ignore 권장, `enabled: false` 또는 파일 삭제로 비활성화.
- **문제 해결**: 훅 미트리거 시 위치·enabled·정규식 점검(`python3 -c "import re; ..."`), import 오류 시 `python3 --version` 확인, 패턴 미매치 시 이스케이프 점검.

<a id="help---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: hookify@claude-plugins-official
- 활성화: ⛔ **OFF** (settings.json enabledPlugins = false) — 켜야 사용 가능
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/hookify/unknown/commands/help.md`

## hookify

> 대화 분석이나 명시적 지시로부터 원치 않는 행동을 막는 hookify 규칙을 생성하는 커맨드.

<a id="hookify---용도"></a>
### 📌 용도
사용자가 겪은 문제 행동을 분석하여, 이를 방지하는 hookify 규칙 파일을 만든다. 인자로 받은 명시적 지시 또는 최근 대화 분석을 통해 막을 행동을 찾아내고, 사용자 확인을 거쳐 `.claude/hookify.{rule-name}.local.md` 파일을 생성한다. 실행 시 먼저 `hookify:writing-rules` 스킬을 로드해 규칙 형식을 이해한 뒤 진행한다.

<a id="hookify---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 원치 않는 행동(위험한 명령, 디버그 코드, 완료 전 누락 단계 등)을 막는 규칙을 만들고 싶을 때. 인자 있으면 명시적 지시 기반, 인자 없으면 대화 분석 기반.
- **언제 쓰지 않는가**: 기존 규칙의 활성/비활성 토글(→ `/hookify:configure`), 규칙 목록 확인(→ `/hookify:list`), 사용법 안내(→ `/hookify:help`)일 때.

<a id="hookify---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/hookify                                          # 인자 없음 → 대화 분석으로 문제 행동 탐지
/hookify Don't use console.log in production files
/hookify Don't use rm -rf without asking me first
```
- 인자(argument-hint): "Optional specific behavior to address" — 다룰 특정 행동을 선택적으로 지정.

<a id="hookify---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
allowed-tools: `Read`, `Write`, `AskUserQuestion`, `Task`, `Grep`, `TodoWrite`, `Skill`.

절차:
1. **행동 정보 수집**: `$ARGUMENTS`가 있으면 그 지시 + 최근 대화(마지막 10-15개 사용자 메시지) 분석. 비어 있으면 Task 도구로 conversation-analyzer 에이전트(general-purpose)를 띄워, 명시적 회피 요청·정정/되돌림·불만 반응·반복 문제를 찾아 category/tool/pattern/context/severity 구조로 반환받는다.
2. **사용자에게 제시**: AskUserQuestion으로 (1) 어떤 행동을 규칙화할지 multiSelect, (2) 각 행동을 block할지 warn할지, (3) 트리거 패턴 확인.
3. **규칙 파일 생성**: 확정된 행동마다 `.claude/hookify.{rule-name}.local.md` 작성. name은 kebab-case·동사 시작(block/warn/prevent/require). 단순 패턴 또는 conditions(다중 조건) 형식 사용. action은 `warn`(기본)/`block`.
4. **생성 및 확인**: 파일은 반드시 현재 작업 디렉터리의 `.claude/` 폴더에 생성(플러그인 디렉터리가 아님). 없으면 `mkdir -p .claude`. 생성 후 목록으로 검증하고 "재시작 없이 즉시 활성화"임을 알림. 진행 상황은 TodoWrite로 추적.

<a id="hookify---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: hookify@claude-plugins-official
- 활성화: ⛔ **OFF** (settings.json enabledPlugins = false) — 켜야 사용 가능
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/hookify/unknown/commands/hookify.md`

## list

> 프로젝트에 설정된 모든 hookify 규칙을 표와 미리보기로 나열하는 커맨드.

<a id="list---용도"></a>
### 📌 용도
현재 프로젝트의 `.claude/hookify.*.local.md` 규칙 파일을 모두 찾아, 각 규칙의 name·enabled·event·pattern과 메시지 미리보기를 표 형태로 보여준다. 어떤 규칙이 설정되어 있고 활성 상태인지 한눈에 확인할 때 사용한다. 실행 시 먼저 `hookify:writing-rules` 스킬을 로드한다.

<a id="list---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 설정된 hookify 규칙 전체를 조회하고 싶을 때.
- **언제 쓰지 않는가**: 규칙 생성(→ `/hookify`), 활성/비활성 변경(→ `/hookify:configure`), 사용법 안내(→ `/hookify:help`)일 때.

<a id="list---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/hookify:list
```
- 인자 없음.

<a id="list---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
allowed-tools: `Glob`, `Read`, `Skill`.

절차:
1. Glob 패턴 `.claude/hookify.*.local.md`로 규칙 파일 검색.
2. 각 파일을 Read하여 프론트매터 필드(name, enabled, event, pattern)와 메시지 미리보기(앞 100자) 추출.
3. 결과를 표로 제시 (Name / Enabled / Event / Pattern / File), 활성/비활성 개수 합계 표시.
4. 규칙별 간단 미리보기(Event, Pattern, Message, Status, File) 출력.
5. 푸터에 수정/비활성/활성/삭제/생성 방법 안내 및 "즉시 반영(재시작 불필요)" 명시.

규칙이 없으면: "No Hookify Rules Configured" 메시지와 함께 `/hookify`로 시작하는 방법, 수동 생성, `/hookify:help` 안내를 표시.

<a id="list---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: hookify@claude-plugins-official
- 활성화: ⛔ **OFF** (settings.json enabledPlugins = false) — 켜야 사용 가능
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/hookify/unknown/commands/list.md`

## writing-rules

> hookify 규칙 파일(`.claude/hookify.*.local.md`)의 작성 문법과 패턴을 안내하는 스킬.

<a id="writing-rules---용도"></a>
### 📌 용도
hookify 규칙은 YAML 프론트매터를 가진 마크다운 파일로, "감시할 패턴"과 "패턴이 매치될 때 Claude에게 보여줄 메시지"를 정의한다. 규칙은 `.claude/hookify.{rule-name}.local.md` 파일에 저장된다. 이 스킬은 규칙 파일의 구조, 프론트매터 필드, 이벤트 타입, 정규식 작성 요령, 파일 명명/정리 규칙, 생성·수정·비활성화 워크플로우를 제공한다.

규칙 파일 기본 구조:
```markdown
---
name: rule-identifier
enabled: true
event: bash|file|stop|prompt|all
pattern: regex-pattern-here
---

규칙이 트리거될 때 Claude에게 보여줄 메시지.
```

<a id="writing-rules---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 사용자가 "create a hookify rule", "write a hook rule", "configure hookify", "add a hookify rule"를 요청하거나 hookify 규칙 문법·패턴에 대한 안내가 필요할 때. `/hookify`, `/hookify:configure`, `/hookify:list` 커맨드가 실행 시 "먼저 이 스킬을 로드"하라고 명시한다.
- **언제 쓰지 않는가**: hookify 규칙 생성/문법과 무관한 일반 작업. (이 스킬 자체는 규칙 문법 참조용이므로, 단순 코드 작성·디버깅 등에는 사용하지 않는다.)

<a id="writing-rules---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
이 스킬은 슬래시 커맨드가 아니라 hookify 커맨드들이 내부적으로 로드하는 참조 스킬이다. 직접 호출보다는 `/hookify` 계열 커맨드 실행 시 자동으로 함께 로드된다.

최소 규칙 예시:
```markdown
---
name: my-rule
enabled: true
event: bash
pattern: dangerous_command
---

Warning message here
```

다중 조건 규칙 예시:
```markdown
---
name: warn-env-file-edits
enabled: true
event: file
conditions:
  - field: file_path
    operator: regex_match
    pattern: \.env$
  - field: new_text
    operator: contains
    pattern: API_KEY
---

You're adding an API key to a .env file. Ensure this file is in .gitignore!
```
(모든 condition이 매치되어야 규칙이 트리거됨.)

<a id="writing-rules---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
프론트매터 필드:
- **name** (필수): 규칙 고유 식별자. kebab-case, 동사로 시작 (warn, prevent, block, require, check).
- **enabled** (필수): `true`/`false`. 삭제 없이 토글 가능.
- **event** (필수): 트리거할 훅 이벤트.
  - `bash`: Bash 도구 명령
  - `file`: Edit/Write/MultiEdit 도구
  - `stop`: 에이전트가 멈추려 할 때 (완료 체크)
  - `prompt`: 사용자 프롬프트 제출 시
  - `all`: 모든 이벤트
- **action** (선택): 매치 시 동작. `warn`(메시지만 보여주고 허용, 기본값) / `block`(작업 차단 또는 세션 중단).
- **pattern** (단순 형식): 매치할 정규식 (Python regex 문법). bash는 command, file은 new_text에 매치.

다중 조건(conditions) 형식:
- `field`: 검사 대상 필드. bash → `command`; file → `file_path`, `new_text`, `old_text`, `content`; prompt → `user_prompt`.
- `operator`: `regex_match`, `contains`, `equals`, `not_contains`, `starts_with`, `ends_with`.
- `pattern`: 매치할 패턴/문자열.

정규식 메타문자: `\s`(공백), `\d`(숫자), `\w`(단어문자), `.`(임의문자), `+`(1+), `*`(0+), `?`(0/1), `|`(OR). YAML의 작은따옴표는 백슬래시를 그대로 보존하므로 `pattern: '\s'`를 사용한다. 큰따옴표는 escape를 해석하므로 `pattern: "\\s"`로 쓴다. 두 값 모두 Python에는 `\s` 하나로 전달되어 공백에 매치된다. 작은따옴표 안에서 백슬래시를 두 번 쓰면 의미가 달라진다. 따옴표 없는 값은 YAML 예약 문자·주석 구문과 충돌하는지 확인한다. [YAML scalar 규칙](https://yaml.org/spec/1.2.2/#73-flow-scalar-styles)을 따른다.

패턴 테스트: `python3 -c "import re; print(re.search(r'your_pattern', 'test text'))"`

파일 정리 규칙:
- 위치: `.claude/` 디렉터리
- 명명: `.claude/hookify.{descriptive-name}.local.md`
- gitignore: `.claude/*.local.md` 추가 권장
- 비활성화: 임시 → `enabled: false`; 영구 → 파일 삭제

규칙은 동적으로 읽히므로 **재시작 없이 다음 도구 사용 시 즉시 반영**된다. 예시 파일은 플러그인의 `${CLAUDE_PLUGIN_ROOT}/examples/` 참고 (dangerous-rm, console-log-warning, sensitive-files-warning 등).

<a id="writing-rules---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: hookify@claude-plugins-official
- 활성화: ⛔ **OFF** (settings.json enabledPlugins = false) — 켜야 사용 가능
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/hookify/unknown/skills/writing-rules/SKILL.md`
