<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# plugin-dev 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. ON/OFF·캐시 표시는 작성 당시 Claude Code 환경의 기록이며 현재 클라이언트의 설치·노출·인증 상태와 구분한다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [agent-development](#agent-development).
- [command-development](#command-development).
- [create-plugin](#create-plugin).
- [hook-development](#hook-development).
- [mcp-integration](#mcp-integration).
- [plugin-settings](#plugin-settings).
- [plugin-structure](#plugin-structure).
- [skill-development](#skill-development).

## agent-development

> Claude Code 플러그인용 서브에이전트의 구조·시스템 프롬프트·트리거 조건 설계를 안내하는 스킬

<a id="agent-development---용도"></a>
### 📌 용도
복잡한 다단계 작업을 독립적으로 처리하는 자율 서브에이전트를 만든다. 에이전트는 자율 작업을 위한 것이고, 명령은 사용자 시작 액션을 위한 것이다. YAML frontmatter를 가진 마크다운 파일 형식이며, description 필드와 예시로 트리거되고, 시스템 프롬프트가 동작을 정의한다.

<a id="agent-development---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "에이전트 생성/추가", "서브에이전트 작성", "agent frontmatter", "when to use description", "agent examples/tools/colors", "자율 에이전트" 요청 시. 에이전트 구조·시스템 프롬프트·트리거·베스트 프랙티스 가이드 필요 시.
- **언제 쓰지 않는가**: 슬래시 명령(→ command-development), 스킬(→ skill-development), 훅(→ hook-development) 작성.

<a id="agent-development---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "코드 리뷰 에이전트를 만들어줘"
- "이 에이전트의 description을 어떻게 써야 트리거가 잘 돼?"
- "에이전트에 어떤 tools를 줘야 해?"

<a id="agent-development---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**에이전트 파일 형식**(`agents/agent-name.md`):
```markdown
---
name: agent-identifier        # 필수: 소문자·숫자·하이픈, 3~50자, 영숫자로 시작/끝
description: Use this agent when [조건]. Typical triggers include [...]. See "When to invoke"...  # 필수, 가장 중요
model: inherit                # 필수: inherit(권장)/sonnet/opus/haiku
color: blue                   # 필수: blue/cyan/green/yellow/magenta/red
tools: ["Read", "Write"]      # 선택: 생략 시 전체 도구 (최소 권한 원칙)
---
You are [역할]...
## When to invoke
- **[시나리오].** [설명.]
```

**frontmatter 필드**:
- **description**(필수, 핵심): 에이전트 등록 시 컨텍스트에 로드되어 디스패치 결정에 사용. 트리거 조건 + 2~4개 시나리오 prose 요약 + body의 "When to invoke" 섹션 포인터 포함. 능동(자기 호출)·수동(사용자 요청) 트리거 모두 커버.
- **color 가이드**: blue/cyan(분석·리뷰), green(성공 작업), yellow(검증), red(보안), magenta(생성).
- **tools 세트**: 읽기 전용 `["Read","Grep","Glob"]`, 코드 생성 `["Read","Write","Grep"]`, 테스트 `["Read","Bash","Grep"]`.

**시스템 프롬프트**(마크다운 body): 2인칭("You are...")으로 작성. 책임/분석 프로세스/품질 기준/출력 형식/엣지 케이스 구조. 10,000자 이하(이상적 500~3,000자).

**생성 방법**: ① AI 보조 생성(Claude Code 추출 프롬프트 패턴, JSON 반환), ② 수동 생성. 검증은 `scripts/validate-agent.sh`, 트리거 테스트는 `scripts/test-agent-trigger.sh`.

**검증 규칙**: identifier 3~50자, description 10~5,000자(이상적 200~1,000자), 시스템 프롬프트 20~10,000자.

**참조 파일**: `references/system-prompt-design.md`, `references/triggering-examples.md`, `references/agent-creation-system-prompt.md`, `examples/agent-creation-prompt.md`, `examples/complete-agent-examples.md`

<a id="agent-development---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/skills/agent-development/SKILL.md`

## command-development

> Claude Code 슬래시 명령의 구조·YAML frontmatter·동적 인자·사용자 인터랙션 패턴을 안내하는 스킬

<a id="command-development---용도"></a>
### 📌 용도
자주 쓰는 프롬프트를 마크다운 파일로 정의한 슬래시 명령을 만든다. 재사용성·일관성·공유·효율성을 제공한다.

> **참고**: `.claude/commands/` 디렉터리는 legacy 형식이다. 새 스킬은 `.claude/skills/<name>/SKILL.md` 형식을 사용한다(둘은 동일하게 로드되며 파일 레이아웃만 다름). 권장 형식은 skill-development 참조.

**핵심**: 명령은 사용자가 아니라 **Claude를 위한 지시문**이다. `/command-name` 호출 시 명령 내용이 Claude의 지시가 되므로, 사용자에게 설명하는 글이 아니라 Claude에게 무엇을 하라고 지시하는 directive로 작성한다.

<a id="command-development---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "슬래시 명령 생성/추가", "커스텀 명령 작성", "command arguments 정의", "command frontmatter", "interactive command", "AskUserQuestion in command", file references 사용 요청 시.
- **언제 쓰지 않는가**: 자율 에이전트(→ agent-development), 스킬(→ skill-development), 이벤트 자동화(→ hook-development). 새 플러그인은 commands 대신 skills 권장.

<a id="command-development---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "PR 리뷰용 슬래시 명령을 만들어줘"
- "명령에 인자 두 개를 받게 하고 싶어"
- "git status를 가져와서 컨텍스트로 쓰는 명령"

<a id="command-development---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**파일 위치**: 프로젝트 `.claude/commands/`, 개인 `~/.claude/commands/`, 플러그인 `plugin-name/commands/`.

**YAML frontmatter 필드**:
- `description`: `/help`에 표시(60자 이하 권장)
- `allowed-tools`: 도구 제한 (`Read, Write, Edit`, `Bash(git:*)`)
- `model`: `haiku`/`sonnet`/`opus`
- `argument-hint`: 인자 문서화 (`[pr-number] [priority]`)
- `disable-model-invocation`: SlashCommand 도구의 프로그래밍 호출 차단

**동적 인자**:
- `$ARGUMENTS`: 모든 인자를 단일 문자열로
- `$0`, `$1`, `$2`: 0부터 시작하는 위치 인자(`$ARGUMENTS[0]`, `$ARGUMENTS[1]`, `$ARGUMENTS[2]`와 동일).
- 혼합: `Deploy $0 to $1 with options: $2`. `/deploy app staging --dry-run`이면 각각 `app`, `staging`, `--dry-run`으로 치환된다. [공식 인자 계약](https://code.claude.com/docs/en/skills#pass-arguments-to-skills)을 따른다.

**파일 참조 (@ 구문)**: `@$0`(첫 인자), `@src/old.js`, `@package.json` — Claude가 명령 처리 전 파일을 읽음.

**Bash 실행**: 인라인 백틱 `` !`git diff --name-only` ``으로 동적 컨텍스트 수집(상세 구문은 `references/plugin-features-reference.md`).

**플러그인 특화**: `${CLAUDE_PLUGIN_ROOT}`로 포터블 경로 참조(`!`bash ${CLAUDE_PLUGIN_ROOT}/scripts/x.sh``, `@${CLAUDE_PLUGIN_ROOT}/config/settings.json`).

**컴포넌트 통합**: 에이전트 실행(Task 도구), 스킬 활용(이름 언급으로 트리거), 훅 연계, 멀티 컴포넌트 워크플로.

**검증 패턴**: 인자 검증, 파일 존재 확인(`test -f`), 플러그인 리소스 검증, 에러 핸들링(`2>&1 || echo "FAILED"`).

**참조 파일**: `references/frontmatter-reference.md`, `references/plugin-features-reference.md`, `references/interactive-commands.md`, `examples/simple-commands.md`, `examples/plugin-commands.md`

<a id="command-development---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/skills/command-development/SKILL.md`

## create-plugin

> 컴포넌트 설계·구현·검증을 아우르는, 가이드형 엔드투엔드 Claude Code 플러그인 생성 워크플로 (슬래시 명령)

<a id="create-plugin---용도"></a>
### 📌 용도
초기 개념부터 테스트된 구현까지 완전하고 고품질의 Claude Code 플러그인을 단계별로 만든다. 요구사항 이해 → 컴포넌트 설계 → 세부 명확화 → 베스트 프랙티스 기반 구현 → 검증 → 테스트의 체계적 접근을 따른다.

**핵심 원칙**:
- **명확화 질문**: 목적·트리거·범위·컴포넌트의 모든 모호함을 구체적 질문으로 확인. 추측 금지, 답변 후 진행.
- **관련 스킬 로드**: 필요 시 Skill 도구로 plugin-dev 스킬(plugin-structure, hook-development 등) 로드.
- **전문 에이전트 활용**: agent-creator, plugin-validator, skill-reviewer.
- **점진적 공개(Progressive disclosure)**: references/examples를 갖춘 lean 스킬 생성.
- **TodoWrite로 진행 추적**.

이 명령은 `commands/` 디렉터리 형식(legacy)으로 작성된 슬래시 명령이다. 참고로 새 플러그인에서는 사용자 호출 명령도 `skills/<name>/SKILL.md`로 만드는 것이 권장된다.

<a id="create-plugin---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/plugin-dev:create-plugin` 슬래시 명령 실행 시. 플러그인을 처음부터 만들고 싶을 때.
- **언제 쓰지 않는가**: 개별 컴포넌트(스킬/에이전트/훅/MCP)만 만들 때는 해당 전용 스킬 직접 사용. 기존 플러그인 일부 수정.

<a id="create-plugin---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/plugin-dev:create-plugin
/plugin-dev:create-plugin 데이터베이스 마이그레이션 관리 플러그인
```
- argument-hint: `Optional plugin description` (선택적 플러그인 설명)

<a id="create-plugin---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**8단계 워크플로** (각 결정 지점에서 사용자 승인 대기):
1. **Discovery**: 플러그인 목적·대상 사용자 파악(7단계 todo 생성).
2. **Component Planning**(plugin-structure 스킬 로드 필수): 필요 컴포넌트(Skills/Agents/Hooks/MCP/Settings) 판단, 표로 제시.
3. **Detailed Design & 명확화 질문**(절대 건너뛰지 말 것): 각 컴포넌트의 미정 사항 질문, 답변 대기.
4. **Plugin Structure Creation**: kebab-case 이름, 위치 선택, 디렉터리 구조 + `plugin.json` 매니페스트 + README 생성, git 초기화.
5. **Component Implementation**: 타입별 스킬 로드 후 구현 (skill-development, agent-development, hook-development, mcp-integration, plugin-settings; legacy `commands/`만 command-development).
6. **Validation & Quality Check**: plugin-validator 에이전트, skill-reviewer, validate-agent.sh, validate-hook-schema.sh로 검증.
7. **Testing & Verification**: `claude --plugin-dir /path`로 로컬 테스트, 체크리스트 검증. 개인 별칭 없이 [공식 CLI 명령](https://code.claude.com/docs/en/discover-plugins)을 사용한다.
8. **Documentation & Next Steps**: README 완성, marketplace.json 엔트리, 요약.

**allowed-tools**: Read, Write, Grep, Glob, Bash, TodoWrite, AskUserQuestion, Skill, Task
**전문 에이전트**: agent-creator, plugin-validator, skill-reviewer

**품질 기준**: plugin-dev 자체 패턴 준수, 올바른 네이밍, 강한 트리거 조건, 동작 예시, ${CLAUDE_PLUGIN_ROOT} 사용, 보안 우선(HTTPS, 자격증명 하드코딩 금지).

<a id="create-plugin---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/commands/create-plugin.md`

## hook-development

> Claude Code 플러그인의 이벤트 기반 훅을 생성·구현하는 스킬 (프롬프트 기반 훅 API 중심)

<a id="hook-development---용도"></a>
### 📌 용도
Claude Code 이벤트에 반응해 실행되는 이벤트 기반 자동화 스크립트(훅)를 만든다. 도구 호출 검증, 정책 강제, 컨텍스트 추가, 외부 도구 통합에 사용한다.

**훅 유형**:
- **프롬프트 기반 훅(권장)**: LLM 기반 의사결정으로 컨텍스트 인식 검증. `{"type":"prompt","prompt":"...","timeout":30}`. 지원 이벤트: Stop, SubagentStop, UserPromptSubmit, PreToolUse. 자연어 추론, 유연성, 엣지 케이스 처리에 강점.
- **명령 훅**: 결정론적 검사용 bash 실행. `{"type":"command","command":"bash ${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh","timeout":60}`. 빠른 검증, 파일시스템 작업, 성능 중요 검사.

<a id="hook-development---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "훅 생성", "PreToolUse/PostToolUse/Stop 훅 추가", "도구 사용 검증", "프롬프트 기반 훅", "${CLAUDE_PLUGIN_ROOT}", "위험 명령 차단", 또는 훅 이벤트(PreToolUse, PostToolUse, Stop, SubagentStop, SessionStart, SessionEnd, UserPromptSubmit, PreCompact, Notification) 언급 시.
- **언제 쓰지 않는가**: 슬래시 명령(→ command-development), 에이전트(→ agent-development), 스킬(→ skill-development).

<a id="hook-development---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "파일 쓰기 전에 안전성 검증하는 훅을 만들어줘"
- ".env 파일 편집을 차단하는 PreToolUse 훅"
- "세션 시작 시 프로젝트 컨텍스트를 로드하는 훅"

<a id="hook-development---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**설정 형식**:
- 플러그인 `hooks/hooks.json`: 래퍼 형식 `{"description":"...","hooks":{"PreToolUse":[...]}}`
- 사용자 `~/.claude/settings.json`: `{"hooks":{"PreToolUse":[...]}}`. 이벤트는 최상위 `hooks` 아래에 둔다. [공식 hooks 설정](https://code.claude.com/docs/en/hooks)을 따른다.

**훅 이벤트**: PreToolUse(승인/거부/수정, `permissionDecision: allow|deny|ask`), PostToolUse(피드백, exit 2시 stderr가 Claude로), Stop(완결성 검증), SubagentStop, UserPromptSubmit(컨텍스트 추가), SessionStart(`$CLAUDE_ENV_FILE`로 env 영속), SessionEnd, PreCompact, Notification.

**Stop 응답**: 명령 훅은 `{"decision":"block","reason":"계속 작업할 이유"}`로 종료를 막고, 종료를 허용할 때 `decision`을 생략한다. 프롬프트 훅은 `{"ok":true}`로 허용하거나 `{"ok":false,"reason":"계속 작업할 이유"}`로 막는다. [명령 훅 계약](https://code.claude.com/docs/en/hooks#stop-decision-control)과 [프롬프트 훅 계약](https://code.claude.com/docs/en/hooks#response-schema)을 구분한다.

**입력**: 명령 훅은 stdin JSON의 `session_id`, `cwd`, `hook_event_name` 등 공통 필드와 이벤트별 필드를 읽는다. 도구 이벤트는 `tool_name`·`tool_input`, PostToolUse 결과는 `tool_response`, UserPromptSubmit 텍스트는 `prompt`다. 프롬프트 훅은 `$ARGUMENTS`로 전체 입력 JSON을 받는다. [공식 입력·치환 계약](https://code.claude.com/docs/en/hooks#prompt-hook-configuration)을 따른다.

**환경변수**: `$CLAUDE_PROJECT_DIR`, `$CLAUDE_PLUGIN_ROOT`(포터빌리티 필수), `$CLAUDE_ENV_FILE`(SessionStart), `$CLAUDE_CODE_REMOTE`.

**Exit 코드**: 0(성공·stdout 표시), 2(차단 에러·stderr가 Claude로), 기타(비차단 에러).

**매처**: 정확 `"Write"`, 다중 `"Read|Write|Edit"`, 와일드카드 `"*"`, 정규식 `"mcp__.*__delete.*"`(대소문자 구분).

**보안**: 입력 검증, 경로 traversal/민감 파일 차단, 모든 변수 따옴표, 타임아웃 설정(명령 60s/프롬프트 30s 기본).

**중요 제약**: 훅은 세션 시작 시 로드되어 핫스왑 불가 — 변경 후 Claude Code 재시작 필요. `/hooks`로 로드 확인, `claude --debug`로 디버깅.

**참조 파일**: `references/patterns.md`, `references/migration.md`, `references/advanced.md`; `examples/validate-write.sh`, `validate-bash.sh`, `load-context.sh`; `scripts/validate-hook-schema.sh`, `test-hook.sh`, `hook-linter.sh`

<a id="hook-development---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/skills/hook-development/SKILL.md`

## mcp-integration

> Claude Code 플러그인에 Model Context Protocol(MCP) 서버를 통합해 외부 도구·서비스를 연동하는 스킬

<a id="mcp-integration---용도"></a>
### 📌 용도
MCP를 통해 플러그인이 외부 서비스·API와 통합되어 구조화된 도구 접근을 제공하도록 한다. 외부 서비스(DB, API, 파일시스템) 연결, 단일 서비스에서 10개 이상의 관련 도구 제공, OAuth·복잡한 인증 처리, MCP 서버를 플러그인에 번들링해 자동 설정한다.

<a id="mcp-integration---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "MCP 서버 추가", "MCP 통합", "플러그인에 MCP 구성", ".mcp.json 사용", "Model Context Protocol 설정", "외부 서비스 연결", "${CLAUDE_PLUGIN_ROOT} with MCP", 또는 MCP 서버 유형(SSE, stdio, HTTP, WebSocket) 논의 시.
- **언제 쓰지 않는가**: 내부 컴포넌트(스킬·에이전트·훅·명령) 작성은 해당 전용 스킬.

<a id="mcp-integration---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "플러그인에 데이터베이스 MCP 서버를 추가해줘"
- "Asana SSE MCP 서버를 연동하고 싶어"
- "토큰 인증 HTTP MCP를 설정해줘"

<a id="mcp-integration---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**구성 방법**: ① 전용 `.mcp.json`(플러그인 루트, 권장), ② `plugin.json`의 `mcpServers` 필드 인라인(단순 단일 서버).

**서버 유형**:
| 유형 | 전송 | 적합 | 인증 |
| --- | --- | --- | --- |
| stdio | 프로세스 | 로컬 도구·커스텀 서버 | env 변수 |
| SSE | HTTP | 호스팅 서비스·클라우드 API | OAuth |
| HTTP | REST | API 백엔드·토큰 인증 | 토큰 |
| ws | WebSocket | 실시간·스트리밍 | 토큰 |

- **stdio**: `{"command":"npx","args":[...],"env":{...}}` — Claude Code가 프로세스 spawn/관리, stdin/stdout 통신.
- **SSE**: `{"type":"sse","url":"https://mcp.asana.com/sse"}` — OAuth 자동 처리, 첫 사용 시 브라우저 인증.
- **HTTP**: `{"type":"http","url":"...","headers":{"Authorization":"Bearer ${API_TOKEN}"}}`.
- **WebSocket**: `{"type":"ws","url":"wss://...","headers":{...}}`.

**환경변수 확장**: `${CLAUDE_PLUGIN_ROOT}`(포터빌리티 필수), 사용자 env(`${MY_API_KEY}`).

**도구 네이밍**: `mcp__plugin_<plugin-name>_<server-name>__<tool-name>`. 명령 frontmatter에서 특정 도구만 pre-allow(와일드카드 지양).

**라이프사이클**: 플러그인 로드 → MCP 구성 파싱 → 서버 시작/연결 → 도구 발견·등록 → `mcp__plugin_...` 사용 가능. `/mcp`로 서버 확인.

**보안**: HTTPS/WSS 사용, env 변수로 토큰(하드코딩·git 커밋 금지), 특정 도구만 pre-allow.

**통합 패턴**: ① 단순 도구 래퍼(명령 + 검증), ② 자율 에이전트, ③ 멀티 서버 플러그인.

**테스트**: `.mcp.json` 구성 → 로컬 설치 → `/mcp` 확인 → `claude --debug` 로그.

**참조 파일**: `references/server-types.md`, `references/authentication.md`, `references/tool-usage.md`; `examples/stdio-server.json`, `sse-server.json`, `http-server.json`

<a id="mcp-integration---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/skills/mcp-integration/SKILL.md`

## plugin-settings

> `.claude/plugin-name.local.md` 패턴으로 플러그인별 설정·상태를 YAML frontmatter와 마크다운으로 저장하는 스킬

<a id="plugin-settings---용도"></a>
### 📌 용도
플러그인이 사용자 구성 가능한 설정과 상태를 프로젝트 디렉터리의 `.claude/plugin-name.local.md` 파일에 저장하도록 한다. YAML frontmatter로 구조화된 설정을, 마크다운 본문으로 프롬프트·추가 컨텍스트를 담는다.

**특성**:
- 위치: 프로젝트 루트의 `.claude/plugin-name.local.md`
- 구조: YAML frontmatter + 마크다운 본문
- 용도: 프로젝트별 플러그인 구성·상태
- 사용처: 훅, 명령, 에이전트에서 읽기
- 라이프사이클: 사용자 관리(git 제외, `.gitignore`에 추가)

<a id="plugin-settings---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "플러그인 설정", "플러그인 구성 저장", "사용자 구성 가능 플러그인", ".local.md 파일", "플러그인 상태 파일", "YAML frontmatter 읽기", "프로젝트별 플러그인 설정", 플러그인 동작을 구성 가능하게 만들고 싶을 때.
- **언제 쓰지 않는가**: 훅/명령/에이전트 로직 자체 작성은 해당 전용 스킬.

<a id="plugin-settings---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "플러그인 설정을 .local.md로 저장하게 해줘"
- "프로젝트마다 다른 동작을 하도록 구성 파일을 읽게 하고 싶어"
- "훅을 켜고 끌 수 있는 설정 플래그를 추가해줘"

<a id="plugin-settings---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**기본 템플릿**:
```markdown
---
enabled: true
mode: standard
max_retries: 3
list_setting: ["item1", "item2"]
---
# Additional Context
프롬프트·지시·문서 등
```

**설정 읽기**:
- **훅(bash)**: frontmatter 파싱 `FRONTMATTER=$(sed -n '/^---$/,/^---$/{ /^---$/d; p; }' "$FILE")`, 필드 추출 `grep '^field:' | sed 's/field: *//'`, 본문 `awk '/^---$/{i++; next} i>=2'`.
- **명령/에이전트**: Read 도구로 읽고 frontmatter 파싱해 동작 커스터마이즈.

**공통 패턴**:
1. **조건부 활성 훅**: 설정 파일로 훅 활성화 제어(hooks.json 수정 없이, quick-exit 패턴).
2. **에이전트 상태 관리**: agent_name, coordinator_session 등 저장(multi-agent-swarm 사례).
3. **구성 기반 동작**: validation_level 등으로 case 분기(ralph-loop 사례).

**베스트 프랙티스**:
- 파일명: `.claude/plugin-name.local.md`(플러그인명 정확히 일치, `.local.md` 접미사)
- `.gitignore`에 `.claude/*.local.md` 추가
- 설정 파일 없을 때 sensible 기본값 제공
- 값 검증(숫자 범위 등)
- **변경 시 Claude Code 재시작 필요**(훅 핫스왑 불가)

**보안**: 사용자 입력 sanitize(따옴표 이스케이프), 파일 경로 traversal 검증, 권한(`chmod 600`, git 제외).

**참조 파일**: `references/parsing-techniques.md`, `references/real-world-examples.md`; `examples/read-settings-hook.sh`, `create-settings-command.md`, `example-settings.md`; `scripts/validate-settings.sh`, `parse-frontmatter.sh`

<a id="plugin-settings---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/skills/plugin-settings/SKILL.md`

## plugin-structure

> Claude Code 플러그인의 디렉터리 레이아웃·매니페스트·컴포넌트 구성·자동 발견을 안내하는 스킬

<a id="plugin-structure---용도"></a>
### 📌 용도
표준화된 디렉터리 구조와 자동 컴포넌트 발견을 따르는 잘 구성된 플러그인을 만든다. 관례적 디렉터리 레이아웃, `.claude-plugin/plugin.json` 매니페스트 기반 구성, 컴포넌트 기반 조직(commands, agents, skills, hooks), `${CLAUDE_PLUGIN_ROOT}` 포터블 경로, 명시적 vs 자동 발견 로딩을 다룬다.

<a id="plugin-structure---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "플러그인 생성/스캐폴드", "플러그인 구조 이해", "컴포넌트 구성", "plugin.json 설정", "${CLAUDE_PLUGIN_ROOT} 사용", "commands/agents/skills/hooks 추가", "자동 발견 구성" 요청 시.
- **언제 쓰지 않는가**: 개별 컴포넌트 작성 세부는 각 전용 스킬(skill-development 등).

<a id="plugin-structure---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "플러그인 디렉터리 구조를 잡아줘"
- "plugin.json에 어떤 필드가 필요해?"
- "스킬이 자동으로 발견되게 하려면 어디에 둬야 해?"

<a id="plugin-structure---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**디렉터리 구조**:
```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # 필수: 매니페스트
├── commands/                # 슬래시 명령 (.md)
├── agents/                  # 서브에이전트 (.md)
├── skills/
│   └── skill-name/SKILL.md  # 스킬별 필수
├── hooks/hooks.json         # 이벤트 핸들러
├── .mcp.json                # MCP 서버
└── scripts/                 # 헬퍼 스크립트
```

**핵심 규칙**:
1. `plugin.json`은 반드시 `.claude-plugin/`에.
2. 컴포넌트 디렉터리는 플러그인 루트(`.claude-plugin/` 내부 금지).
3. 사용하는 컴포넌트만 디렉터리 생성.
4. 모든 이름은 kebab-case.

**매니페스트(plugin.json)**:
- 필수: `name`(kebab-case, 고유)
- 권장: `version`(semver), `description`, `author`, `homepage`, `repository`, `license`, `keywords`
- 커스텀 경로: `commands`/`agents`/`hooks`/`mcpServers`(상대 경로, `./` 시작, 기본 디렉터리를 대체가 아닌 보완)

**컴포넌트 자동 발견**: commands/agents의 모든 `.md`, skills 하위의 모든 `SKILL.md`, hooks.json, .mcp.json을 스캔. 발견 타이밍: 설치 시 등록, 활성화 시 사용 가능, 재시작 불필요(변경은 다음 세션 반영).

**${CLAUDE_PLUGIN_ROOT}**: 모든 인트라 플러그인 경로 참조에 사용. 하드코딩 절대경로(`/Users/...`), 작업 디렉터리 상대경로(`./scripts/...`), 홈 단축(`~/...`) 사용 금지.

**네이밍**: 명령/에이전트/스킬 kebab-case, 스크립트 descriptive kebab-case, 설정은 표준명(hooks.json, .mcp.json, plugin.json).

**일반 패턴**: 최소 플러그인(단일 명령), 풀 피처 플러그인(전체 컴포넌트), 스킬 중심 플러그인.

**트러블슈팅**: 컴포넌트 미로드(위치·확장자·frontmatter 확인), 경로 해석 에러(${CLAUDE_PLUGIN_ROOT}), 자동 발견 실패(루트 위치 확인), 플러그인 충돌(고유 이름).

**참조 파일**: `references/`, `examples/` 디렉터리

<a id="plugin-structure---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/skills/plugin-structure/SKILL.md`

## skill-development

> Claude Code 플러그인용 스킬의 구조·점진적 공개·작성 스타일 베스트 프랙티스를 안내하는 스킬

<a id="skill-development---용도"></a>
### 📌 용도
효과적인 플러그인 스킬을 만든다. 스킬은 특정 도메인/작업을 위한 "온보딩 가이드"로, Claude를 범용 에이전트에서 절차적 지식을 갖춘 특화 에이전트로 변환한다. 특화 워크플로, 도구 통합, 도메인 전문성, 번들 리소스(스크립트·참조·에셋)를 제공한다.

<a id="skill-development---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "스킬 생성", "플러그인에 스킬 추가", "새 스킬 작성", "스킬 description 개선", "스킬 콘텐츠 구성" 요청 시. 스킬 구조·점진적 공개·베스트 프랙티스 가이드 필요 시.
- **언제 쓰지 않는가**: 명령(→ command-development), 에이전트(→ agent-development), 훅(→ hook-development). 독립 스킬 생성·평가는 별도의 skill-creator 스킬도 존재.

<a id="skill-development---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "API 문서화 스킬을 만들어줘"
- "이 스킬의 description이 트리거가 잘 되도록 개선해줘"
- "SKILL.md가 너무 길어졌는데 정리해줘"

<a id="skill-development---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**스킬 구조**:
```
skill-name/
├── SKILL.md (필수)
│   ├── YAML frontmatter (name, description 필수)
│   └── 마크다운 지시
└── 번들 리소스 (선택)
    ├── scripts/     - 실행 코드(결정론적/반복 작업)
    ├── references/  - 필요 시 컨텍스트로 로드되는 문서
    └── assets/      - 출력에 사용되는 파일(템플릿, 아이콘, 폰트)
```

**점진적 공개(3단계 로딩)**:
1. 메타데이터(name + description) — 항상 컨텍스트(~100단어)
2. SKILL.md 본문 — 스킬 트리거 시(<5k 단어)
3. 번들 리소스 — 필요 시(무제한, 스크립트는 로드 없이 실행)

**생성 프로세스**: ① 구체적 예시로 사용 패턴 이해 → ② 재사용 콘텐츠 계획(scripts/references/assets) → ③ 구조 생성(`mkdir -p skills/skill-name/{references,examples,scripts}`) → ④ SKILL.md 편집 → ⑤ 검증·테스트 → ⑥ 반복.

**작성 스타일(필수)**:
- 본문: **명령형/부정사형**(verb-first). "To do X, do Y" — "You should" 금지.
- description: **3인칭** + 구체적 트리거 구문. "This skill should be used when the user asks to '...'". 모호/2인칭 금지.

**lean 유지**: 본문 1,500~2,000단어 목표(<5k 최대). 상세 패턴 → `references/patterns.md`, 고급 → `references/advanced.md`, 마이그레이션 → `references/migration.md`, API → `references/api-reference.md`. 정보 중복 금지(SKILL.md 또는 references 중 한 곳).

**검증 체크리스트**: 구조(frontmatter name/description, 참조 파일 존재), description 품질(3인칭·구체적 트리거), 콘텐츠 품질(명령형·lean·references 분리), 점진적 공개, 테스트(트리거 동작).

**흔한 실수**: ① 약한 트리거 description, ② SKILL.md에 과다 콘텐츠, ③ 2인칭 작성, ④ 리소스 참조 누락.

**참조**: plugin-dev 자체 스킬(hook-development, agent-development, plugin-settings 등)을 모범 예시로 연구. skill-reviewer 에이전트로 검토.

<a id="skill-development---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: plugin-dev@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/plugin-dev/unknown/skills/skill-development/SKILL.md`
