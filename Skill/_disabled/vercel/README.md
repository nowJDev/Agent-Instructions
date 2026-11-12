<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# _disabled/vercel 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. ON/OFF·캐시 표시는 작성 당시 Claude Code 환경의 기록이며 현재 클라이언트의 설치·노출·인증 상태와 구분한다. [전체 항목 목차](../../CATALOG.md)에서 다른 분류를 찾는다.

- [_conventions](#_conventions).
- [benchmark-agents](#benchmark-agents).
- [benchmark-e2e](#benchmark-e2e).
- [benchmark-sandbox](#benchmark-sandbox).
- [benchmark-testing](#benchmark-testing).
- [bootstrap](#bootstrap).
- [deploy](#deploy).
- [env](#env).
- [marketplace](#marketplace).
- [plugin-audit](#plugin-audit).
- [release](#release).
- [status](#status).
- [vercel-plugin-eval](#vercel-plugin-eval).

내부 개발용 항목은 benchmark 4개, plugin-audit, release, vercel-plugin-eval, _conventions다. 일반 배포 항목과 용도를 구분한다.

## _conventions

> 이 플러그인의 모든 슬래시 커맨드가 따르는 일관된 구조를 정의하는 메타 문서. 사용자가 직접 호출하는 커맨드가 아님.

<a id="_conventions---용도"></a>
### 📌 용도
**플러그인 내부 메타 문서**다. 파일명이 `_`로 시작하므로 `plugin.json` 열거에서 제외되며, 사용자에게 호출 가능한 슬래시 커맨드로 노출되지 않는다. 커맨드 파일을 작성·수정할 때 모든 커맨드가 일관된 구조를 갖도록 강제하는 작성 규약이다.

이 문서 자체는 사용자가 호출할 수 없지만, vercel 플러그인을 켰을 때 다른 커맨드(/deploy, /env, /marketplace, /status, /bootstrap)들이 왜 동일한 섹션 구조를 갖는지 설명한다.

<a id="_conventions---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 호출되지 않는다(slash command 아님). 플러그인 개발자가 새 커맨드를 작성/갱신할 때 참조하는 규약 문서.
- **언제 쓰지 않는가**: 일반 사용자 작업 전체.

<a id="_conventions---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
사용자 호출 명령 없음. 커맨드 파일 작성 시 아래 필수 섹션을 모두 포함해야 한다:
1. **Preflight** — 프로젝트 링크(`.vercel/project.json`)·CLI 존재·repo 상태·모노레포 스코프 점검
2. **Plan** — 실행할 명령/MCP 호출 명시, 파괴적/프로덕션 작업은 명시적 확인 요구
3. **Commands** — MCP-first·CLI-fallback, `--format=json` 선호, 시크릿 미출력, 파괴적 작업 확인
4. **Verification** — 실행 후 상태 재확인(`vercel ls`, `vercel env ls`), before/after 비교
5. **Summary** — 간결한 결과 블록(Action/Status/Details)
6. **Next Steps** — 논리적 후속 작업 제안

<a id="_conventions---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **파일 네이밍**: 커맨드는 `commands/`에 `.md`로 위치. `_` 접두 파일(이 문서 등)은 메타 문서로 plugin.json 열거에서 제외.
- **frontmatter**: 모든 커맨드 파일은 최소 `description` 필드를 가진 YAML frontmatter 필수.
- **검증**: `scripts/validate.ts`가 비-언더스코어 커맨드 파일마다 6개 필수 섹션(Preflight·Plan·Commands·Verification·Summary·Next Steps)을 강제.

<a id="_conventions---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/commands/_conventions.md`

## benchmark-agents

> vercel-plugin의 스킬 주입을 고난도 AI 시스템 시나리오로 스트레스 테스트하는 내부 벤치마크 스킬.

<a id="benchmark-agents---용도"></a>
### 📌 용도
**vercel 플러그인 자체 개발/벤치마크용 내부 스킬**이다. 일반 사용자의 Vercel 배포 작업과는 무관하며, 플러그인 개발자가 플러그인의 스킬 주입(skill injection) 품질을 검증할 때 쓴다.

Workflow DevKit, AI Gateway, MCP, Chat SDK, Queues, Flags, Sandbox, 멀티 에이전트 오케스트레이션 등 Vercel 플랫폼의 첨단 기능을 요구하는 복잡한 빌드 시나리오를 만들어, 실제 Claude Code 세션을 띄우고 플러그인이 올바른 스킬을 주입하는지, PostToolUse 검증이 잘못된 패턴을 잡아내는지 확인한다. setup → launch → monitor → verify → fix → release → repeat의 전체 eval 루프를 다룬다.

핵심 철학은 "eval은 스크립트가 아니라 대화 안에서 사람(에이전트)이 직접 실행한다"이다. `claude --print`, eval 스크립트, `Bun.spawn` 방식은 금지된다 — 훅(PreToolUse/PostToolUse/UserPromptSubmit)이 대화형 도구 호출 세션에서만 발화하기 때문이다. WezTerm 패널에서 대화형 Claude Code 세션을 띄우는 방식만 플러그인을 올바르게 작동시킨다.

<a id="benchmark-agents---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 플러그인 개발자가 고급 AI 에이전트 시나리오(멀티 시스템 빌드)로 스킬 주입을 평가하려 할 때. macOS + WezTerm + `~/dev/vercel-plugin-testing/` 로컬 환경 전제.
- **언제 쓰지 않는가**: 실제 프로덕트를 만들거나 Vercel에 배포하려는 일반 사용자 작업. 이 경우 commands(/deploy, /env 등)나 vercel MCP를 쓴다.

<a id="benchmark-agents---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 1. 테스트 디렉토리 생성 + 플러그인 설치 (타임스탬프 필수)
TS=$(date +%Y%m%d-%H%M)
SLUG="my-app-$TS"
mkdir -p ~/dev/vercel-plugin-testing/$SLUG
cd ~/dev/vercel-plugin-testing/$SLUG
npx add-plugin https://github.com/vercel/vercel-plugin -s project -y

# 2. WezTerm 패널에서 대화형 세션 띄우기
wezterm cli spawn --cwd .../$SLUG -- /bin/zsh -ic \
  "unset CLAUDECODE; VERCEL_PLUGIN_LOG_LEVEL=debug x '<PROMPT>' --settings .claude/settings.json; exec zsh"

# 3. 디버그 로그 찾기 (SessionStart 훅 발화까지 ~25초 대기)
find ~/.claude/debug -name "*.txt" -mmin -2 -exec grep -l "$SLUG" {} +
```

프롬프트 설계 규칙: **기술이 아니라 프로덕트를 묘사**하라(예: "각 단계를 스트리밍하는 멀티스텝 생성 파이프라인"). 항상 "Link the project to my vercel-labs team... Skip any planning and just build it. Get the dev server running."로 끝낸다.

<a id="benchmark-agents---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
| 구분 | 내용 |
|------|------|
| 모니터링 | 클레임 디렉토리(`/tmp/vercel-plugin-<session-id>-seen-skills.d`)로 주입된 스킬 추적, 디버그 로그에서 훅 발화/주입/PostToolUse VALIDATION 카운트 |
| 검증 포인트 | WDK 프로젝트 구조(`src/` 없어야 함), `withWorkflow`, 이미지 모델(`gemini-3.1-flash-image-preview`), gateway 사용 여부, AI Elements 설치 |
| 시나리오 | 12개 시나리오(doc-qa-agent, multi-agent-research 등), 3개 복잡도 티어 |
| 커버리지 리포트 | `.notes/COVERAGE.md`에 세션 인덱스/훅 매트릭스/스킬 주입 표/코드 품질 |
| 절대 금지 | `claude --print`, `--dangerously-skip-permissions`, `/tmp/` 사용, 수동 훅 설정, 디렉토리명 대문자 |

<a id="benchmark-agents---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.claude/skills/benchmark-agents/SKILL.md`

## benchmark-e2e

> vercel-plugin을 현실적 프로젝트로 돌려 스킬 주입·dev 서버 기동·검증·개선 리포트를 한 번에 생성하는 내부 E2E 벤치마크 스킬.

<a id="benchmark-e2e---용도"></a>
### 📌 용도
**vercel 플러그인 자체 개발/벤치마크용 내부 스킬**이다. 일반 사용자용이 아니라, 야간 자가 개선(overnight self-improvement) 루프를 위한 단일 커맨드 파이프라인을 제공한다.

프로젝트를 생성하고, 스킬 주입을 실행하며, dev 서버를 띄워 동작을 확인하고, 대화 로그를 분석해 실행 가능한 개선 리포트를 만든다. `bun run scripts/benchmark-e2e.ts` 한 줄로 runner → verify → analyze → report 4단계를 순차 실행한다.

(주의: 이 스킬의 runner는 `claude --print`를 사용한다고 명시되어 있는데, 이는 benchmark-agents/vercel-plugin-eval 등 대화형 스킬과 대비되는 자동화 지향 설계다. 이 스킬은 머신 판독용 `report.json`/`run-manifest.json`/`events.jsonl` 산출물을 통해 닫힌 피드백 루프를 만드는 데 초점이 있다.)

<a id="benchmark-e2e---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 플러그인 개발자가 9개(또는 quick 모드 3개) 현실 프로젝트에 대해 스킬 커버리지를 자동 측정하고, 야간 반복으로 개선 추세를 추적하려 할 때.
- **언제 쓰지 않는가**: 실제 Vercel 프로덕트 빌드/배포. 이 경우 commands나 vercel MCP를 쓴다.

<a id="benchmark-e2e---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 전체 스위트 (9개 프로젝트, ~2-3시간)
bun run scripts/benchmark-e2e.ts

# 빠른 모드 (앞 3개, ~30-45분)
bun run scripts/benchmark-e2e.ts --quick

# 야간 자동화 루프
while true; do bun run scripts/benchmark-e2e.ts; sleep 3600; done
```

| 플래그 | 설명 | 기본값 |
|--------|------|--------|
| `--quick` | 앞 3개 프로젝트만 | `false` |
| `--base <path>` | 기본 디렉토리 변경 | `~/dev/vercel-plugin-testing` |
| `--timeout <ms>` | 프로젝트당 타임아웃 | `900000` (15분) |

<a id="benchmark-e2e---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
| 단계 | 역할 |
|------|------|
| runner | 테스트 디렉토리 생성, 플러그인 설치, `VERCEL_PLUGIN_LOG_LEVEL=trace`로 실행 |
| verify | 패키지 매니저 감지, dev 서버 기동, 200 + 비어있지 않은 HTML 폴링 |
| analyze | `run-manifest.json`으로 JSONL 세션과 프로젝트 매칭, 메트릭 추출 |
| report | `report.md` + `report.json` (스코어카드, 추천 패턴) 생성 |

산출 계약: `run-manifest.json`(runId·프로젝트별 expectedSkills), `events.jsonl`(파이프라인 생명주기 NDJSON), `report.json`(verdict: pass/partial/fail, gaps, suggestedPatterns). 자가 개선 사이클은 Run → gaps 읽기 → suggestedPatterns로 frontmatter 패턴 추가 → 재실행 → verdict가 fail→partial→pass로 수렴하는지 diff.

프롬프트 표 9종: recipe-platform, trivia-game, code-review-bot, conference-tickets, content-aggregator, finance-tracker, multi-tenant-blog, status-page, dog-walking-saas.

<a id="benchmark-e2e---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.claude/skills/benchmark-e2e/SKILL.md`

## benchmark-sandbox

> 로컬 WezTerm 대신 Vercel Sandbox(원격 microVM)에서 eval 시나리오를 돌리는 내부 벤치마크 스킬.

<a id="benchmark-sandbox---용도"></a>
### 📌 용도
**vercel 플러그인 자체 개발/벤치마크용 내부 스킬**이다. benchmark-agents가 로컬 macOS 터미널 패널을 쓰는 반면, 이 스킬은 Vercel Sandbox(node24 기반 Firecracker microVM)에서 eval을 원격·병렬로 실행한다.

각 샌드박스는 Claude Code + Vercel CLI + agent-browser가 새로 설치되고, 로컬 vercel-plugin이 업로드되며, **3단계 파이프라인**을 돈다:
- **Phase 1 (BUILD)**: `--dangerously-skip-permissions --debug`로 앱 빌드
- **Phase 2 (VERIFY)**: 후속 세션이 `agent-browser`로 유저 스토리를 검증·수정 (20분 타임아웃)
- **Phase 3 (DEPLOY)**: 세 번째 세션이 vercel-labs에 링크 후 `vercel deploy`, 빌드 에러 최대 3회 수정

각 단계 후 haiku 모델(`claude -p --json-schema --model haiku`)로 구조화 JSON 스코어링을 한다. 스킬은 3단계 전체에 걸쳐 추적된다.

<a id="benchmark-sandbox---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 자동화된 병렬 커버리지 + 검증 + 배포 런이 필요할 때. 로컬 자원 한계를 넘어 동시 다수(최대 10개) 시나리오를 돌리고, 자동 agent-browser 검증과 영구 `*.vercel.app` URL이 필요할 때.
- **언제 쓰지 않는가**: 수동 eval/반복 루프(이 경우 benchmark-agents), 또는 일반 사용자의 실제 배포 작업.

<a id="benchmark-sandbox---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 기본 시나리오 + 전체 3단계 파이프라인
bun run .claude/skills/benchmark-sandbox/run-eval.ts

# 동적 시나리오 JSON 파일 사용 (권장)
bun run .claude/skills/benchmark-sandbox/run-eval.ts --scenarios-file /tmp/scenarios.json

# 야간 keep-alive (공개 URL 유지)
bun run .claude/skills/benchmark-sandbox/run-eval.ts --keep-alive --keep-hours 8

# 빌드만 (검증·배포 생략)
bun run .claude/skills/benchmark-sandbox/run-eval.ts --skip-verify --skip-deploy
```

<a id="benchmark-sandbox---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
| 플래그 | 기본값 | 설명 |
|--------|--------|------|
| `--concurrency N` | 5 | 병렬 샌드박스 수 (최대 10) |
| `--timeout MS` | 1800000 (30분) | 단계당 타임아웃 |
| `--keep-alive` / `--keep-hours N` | off / 8 | eval 후 샌드박스 유지 |
| `--skip-verify` / `--skip-deploy` | off | 검증/배포 단계 생략 |
| `--scenarios a,b,c` / `--scenarios-file path` | all / — | 슬러그 필터 / JSON 파일 로드 |

핵심 환경 사실: 홈은 `/home/vercel-sandbox`(NOT `/home/user`), SDK는 `@vercel/sandbox@1.8.0`(v2 beta는 404), 스냅샷은 파일+npm 글로벌 보존, 포트 노출은 `ports:[3000]` → `https://...vercel.run`. 파일 업로드는 `sandbox.writeFiles()`(heredoc 금지), 타임아웃은 `AbortSignal.timeout(ms)`. 산출물은 `~/dev/vercel-plugin-testing/sandbox-results/<run-id>/`에 result.json·source.tar.gz·report.md.

<a id="benchmark-sandbox---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.claude/skills/benchmark-sandbox/SKILL.md`

## benchmark-testing

> 현실적·기술명 비공개 프롬프트로 vercel-plugin 스킬 주입을 시험할 격리 테스트 프로젝트를 만드는 내부 벤치마크 스킬.

<a id="benchmark-testing---용도"></a>
### 📌 용도
**vercel 플러그인 자체 개발/벤치마크용 내부 스킬**이다. benchmark-agents의 간소화된 셋업 버전으로, 격리된 테스트 디렉토리를 만들고 플러그인을 설치한 뒤, 크래프팅된 프롬프트로 Claude Code를 WezTerm 패널에 띄우는 데 집중한다.

목표는 현실적이고 기술-중립적인(technology-agnostic) 프롬프트로 스킬 주입을 자극하는 것이다. 프롬프트에 특정 기술(Next.js, Stripe 등)을 절대 언급하지 않고 프로덕트와 기능만 묘사해, 플러그인이 자연어에서 올바른 스킬을 추론하는지 본다.

<a id="benchmark-testing---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 플러그인 개발자가 여러 현실 시나리오 테스트 프로젝트를 빠르게 셋업·기동하려 할 때. macOS + WezTerm 로컬 환경 전제.
- **언제 쓰지 않는가**: 일반 사용자의 실제 Vercel 빌드/배포(commands·MCP 사용), 모니터링·커버리지 리포트가 필요한 정밀 eval(benchmark-agents/vercel-plugin-eval 사용).

<a id="benchmark-testing---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 1. 테스트 디렉토리 생성
BASE=~/dev/vercel-plugin-testing
mkdir -p "$BASE"/{01-slug,02-slug,...}

# 2. 각 디렉토리에 플러그인 설치
for dir in "$BASE"/*/; do
  cd "$dir" && npx add-plugin https://github.com/vercel/vercel-plugin -s project -y 2>&1 | tail -1
done

# 3. WezTerm 패널에서 Claude Code 기동
wezterm cli spawn --cwd /absolute/path/to/test-dir -- /bin/zsh -ic \
  "unset CLAUDECODE; x 'YOUR PROMPT. Link the project to my vercel-labs team so we can deploy it later.' --settings .claude/settings.json; exec zsh"
```

<a id="benchmark-testing---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
필수 준수 사항:
- `--cwd <절대경로>`로 작업 디렉토리 지정
- `x` 앞에 `unset CLAUDECODE`로 중첩 세션 에러 방지
- `--settings .claude/settings.json` (NOT `--settings project`)
- 외부 `-ic` 문자열은 큰따옴표, 프롬프트는 작은따옴표
- 각 기동 사이 **10초** 대기
- `split-pane`은 ~4패널 후 공간 부족 → 항상 `spawn` 사용

프롬프트 가이드: 특정 기술명 금지, 프로덕트/기능 묘사, 여러 스킬 트리거를 자극하는 야심찬 멀티 기능, 항상 "Link the project to my vercel-labs team..." 추가. 예시 9종(recipe-platform, trivia-game, code-review-bot, conference-tickets 등)과 기대 스킬 표 제공.

<a id="benchmark-testing---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.claude/skills/benchmark-testing/SKILL.md`

## bootstrap

> Vercel 연동 리소스로 저장소를 부트스트랩 — 사전 점검, 통합 프로비저닝, env 키 검증 후 db/dev 시작 명령을 안전하게 실행.

<a id="bootstrap---용도"></a>
### 📌 용도
**사용자용 슬래시 커맨드**다. 신규이거나 부분 설정된 저장소를 결정론적 부트스트랩 플로우로 셋업한다. Vercel CLI 인증·링크 확인 → DB 등 리소스 프로비저닝(Vercel 관리형 Neon 우선) → 시크릿/env 셋업 → env 키 검증을 모두 통과한 뒤에야 `db:*`/`dev` 명령을 실행한다.

핵심 안전 규칙: Vercel 링크 완료 + env 키 검증 전에는 `db:push`/`db:migrate`/`db:seed`/`dev`를 실행하지 않으며, 시크릿 값을 터미널/로그/요약에 절대 출력하지 않는다.

<a id="bootstrap---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/bootstrap` 호출 시. Vercel과 연동된 새 프로젝트의 초기 환경(DB·인증·env)을 한 번에 셋업하고 싶을 때.
- **언제 쓰지 않는가**: 이미 셋업이 끝난 프로젝트의 단순 배포(`/deploy`)나 env 관리(`/env`)만 필요할 때.

<a id="bootstrap---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 사전 점검
vercel --version
vercel whoami
# .vercel/project.json 으로 링크 확인, 없으면:
vercel teams ls
vercel projects ls --scope <team>
vercel link --yes --scope <team> --project <project>

# 로컬 env 템플릿 (.env.example → .env.sample → .env.template 우선순위)
cp .env.example .env.local

# Postgres 프로비저닝 (Vercel 관리형 Neon 우선)
vercel integration guide neon
vercel integration add neon --scope <team>
vercel env ls
vercel env pull .env.local --yes

# AUTH_SECRET 생성 (값 출력 없이 Vercel에 저장)
AUTH_SECRET="$(node -e "console.log(require('node:crypto').randomBytes(32).toString('base64url'))")"
printf "%s" "$AUTH_SECRET" | vercel env add AUTH_SECRET development preview production
unset AUTH_SECRET
vercel env pull .env.local --yes

# 검증 후 앱 부트스트랩
npm run db:push
npm run db:seed
npm run dev
```

<a id="bootstrap---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
실행 순서: ① 사전 점검·링크 → ② 리소스 프로비저닝(Vercel 관리형 우선, 프로바이더 CLI는 폴백) → ③ 시크릿/env 셋업 → ④ env 키 검증(`comm`으로 템플릿 키 vs `.env.local` 키 비교, 이름만) → ⑤ db/dev 실행. 검증 단계마다 체크포인트 확인 후 실패 시 정확한 실패 단계와 해결책 보고. 최종 부트스트랩 요약(Linked Project, Resource Path, Env Keys, Secrets, Migration Status, Dev Result) 출력.

<a id="bootstrap---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/commands/bootstrap.md`

## deploy

> 현재 프로젝트를 Vercel에 배포 — 사전 안전 점검, 프로덕션 명시 확인, 배포 후 검증 포함. 인자로 "prod"/"production" 전달 시 프로덕션 배포.

<a id="deploy---용도"></a>
### 📌 용도
**사용자용 슬래시 커맨드**다. Vercel CLI로 현재 프로젝트를 배포한다. 기본은 프리뷰(preview) 배포이고, `$ARGUMENTS`에 "prod"/"production"이 있으면 프로덕션 배포다. 프로덕션은 실제 사용자에게 영향을 주므로 명시적 "yes" 확인 없이는 진행하지 않는다.

<a id="deploy---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/deploy`(프리뷰) 또는 `/deploy prod`(프로덕션) 호출 시. 코드를 Vercel에 올려 URL을 받고 싶을 때.
- **언제 쓰지 않는가**: env 변수만 관리하려 할 때(`/env`), 프로젝트 상태만 보려 할 때(`/status`), 초기 셋업이 안 된 신규 저장소(`/bootstrap` 먼저).

<a id="deploy---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 프리뷰 배포 (기본 — 격리된 고유 URL)
vercel
vercel deploy

# 프로덕션 배포 (명시적 확인 필요)
vercel --prod
vercel --prod --force      # 캐시 스킵 강제 재배포

# 배포 검사
vercel inspect <deployment-url>
vercel ls
vercel logs <deployment-url> --follow
git rev-parse --short HEAD   # 요약용 커밋 SHA
```

<a id="deploy---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
사전 점검: CLI 존재, `.vercel/project.json` 링크, 모노레포 감지(`turbo.json`/`pnpm-workspace.yaml`), `git status --porcelain` 미커밋 변경 경고, 프로덕션 전 옵저버빌리티 점검(drains 설정 여부, 에러 드레인 상태, 에러 모니터링).

검증: 배포 상태(READY/ERROR/BUILDING/QUEUED) 추출, 실패 시 빌드 로그 마지막 50줄에서 error/ERR!/FATAL 강조. 프로덕션은 READY 후 60초 대기 후 `vercel logs --level error --since 1h`로 런타임 에러 스캔. 배포 결과 블록(URL, Target, Status, Commit, Framework, Build Duration) 출력. 500/타임아웃 에러 해석 표 제공.

<a id="deploy---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/commands/deploy.md`

## env

> Vercel 환경 변수 관리 — list, pull, add, remove, diff. Vercel과 로컬 개발 환경 간 env 변수 동기화. 시크릿 값은 절대 출력하지 않음.

<a id="env---용도"></a>
### 📌 용도
**사용자용 슬래시 커맨드**다. 현재 Vercel 프로젝트의 환경 변수를 관리하되, 시크릿 누출을 막는 안전 가드를 둔다. **🔒 Never-Echo-Secrets 규칙**: env 변수 **값**은 출력/요약/대화에 절대 나타나지 않으며, 이름·환경·메타데이터(생성일·타입)만 표시한다.

<a id="env---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/env`, `/env pull`, `/env add <NAME>`, `/env rm <NAME>`, `/env diff` 등으로 env 변수를 조회·동기화·추가·삭제·비교할 때.
- **언제 쓰지 않는가**: 배포(`/deploy`)나 통합 설치(`/marketplace`)가 주 목적일 때. (단 이들 작업 후속으로 자주 함께 쓰임)

<a id="env---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# list / ls / (인자 없음) — 이름만 표시
vercel env ls
vercel env ls production

# pull — .env.local로 다운로드
vercel env pull .env.local
vercel env pull .env.local --environment=production
vercel env pull .env.local --yes

# add — 값은 대화형으로 입력(인자로 echo 금지)
vercel env add MY_SECRET
echo "secret-value" | vercel env add MY_SECRET production preview development
vercel env add MY_SECRET --sensitive

# rm / remove
vercel env rm MY_SECRET production
vercel env rm MY_SECRET

# diff — 로컬 vs Vercel 키 이름 비교(값 미열람)
grep -v '^#' .env.local | grep '=' | cut -d'=' -f1 | sort
```

<a id="env---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
| 인자 | 동작 | 파괴적? |
|------|------|---------|
| `list`/`ls`/(없음) | 환경별 변수 이름 목록 | No |
| `pull` | 로컬 `.env.local`로 다운로드 | No (로컬 파일 덮어씀) |
| `add <NAME>` | 새 변수 추가 | 프로덕션이면 Yes |
| `rm`/`remove <NAME>` | 변수 삭제 | **Yes** |
| `diff` | 로컬 vs Vercel 키 이름 비교 | No |

프로덕션 변경(add/rm)은 명시적 확인 필요. Git 브랜치 오버라이드(`--git-branch=staging`), 환경 스코핑(Production/Preview/Development) 설명. 주의: `vercel env pull`은 파일 전체를 덮어쓰므로 커스텀 변수는 백업·재추가 필요. mutation 후 `vercel env ls`로 검증.

<a id="env---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/commands/env.md`

## marketplace

> Vercel Marketplace 통합 발견·설치 — 데이터베이스, CMS, 인증, 결제, 옵저버빌리티 등 서비스를 가이드 셋업과 로컬 검증으로 추가.

<a id="marketplace---용도"></a>
### 📌 용도
**사용자용 슬래시 커맨드**다. Vercel Marketplace 카탈로그에서 통합(integration)을 발견·설치하고 가이드에 따라 코드를 적용한다. apply-guide 루프(Discover → Select → Guide → Install → env 검증 → 코드 적용 → drain 검증 → 로컬 헬스체크)를 따른다.

<a id="marketplace---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/marketplace` 또는 `/marketplace <name>` 호출 시. DB(Neon/PlanetScale/Supabase), 캐시(Upstash), 인증(Clerk/Auth0), CMS(Sanity/Contentful), 결제(Stripe), 모니터링(Datadog/Sentry/Axiom) 등을 프로젝트에 붙일 때.
- **언제 쓰지 않는가**: 이미 설치된 통합의 env 동기화만 필요할 때(`/env pull`), 단순 배포(`/deploy`).

<a id="marketplace---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 1. 카탈로그 검색
vercel integration discover
vercel integration discover --category databases
vercel integration list           # 이미 설치된 통합

# 3. 가이드 가져오기 (프레임워크별)
vercel integration guide <name> --framework <fw>

# 4. 설치 (env 변수·로그/트레이스 drain 자동 프로비저닝)
vercel integration add <name>
vercel integration open <name>    # 대시보드 폴백

# 5. env 검증 (이름만)
vercel env ls
vercel env pull .env.local --yes

# 6. SDK 설치 + 코드 스캐폴딩
npm install <sdk-package>
```

<a id="marketplace---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
옵저버빌리티 통합(Datadog/Sentry/Axiom/Honeycomb)은 drain 검증 단계가 추가된다. 데이터 타입 분리: **Logs/Traces**는 설치 시 네이티브 drain 자동 생성, **Speed Insights/Web Analytics**는 REST API/대시보드로 별도 수동 drain 필요. drain 생성·테스트(`curl POST /v1/drains/<id>/test`)와 페이로드 서명 검증(`x-vercel-signature` HMAC-SHA1)은 observability 스킬 참조. 로컬 헬스체크: DB는 `SELECT 1`, 인증은 리다이렉트, 캐시는 set/get 라운드트립. 결과 블록(Integration, Status, Package, Env Vars, Drain, Health Check, Files Changed) 출력.

<a id="marketplace---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/commands/marketplace.md`

## plugin-audit

> 실제 Claude Code 세션 로그를 분석해 vercel-plugin 스킬 주입 성능과 패턴 커버리지 갭을 진단하는 내부 감사 스킬.

<a id="plugin-audit---용도"></a>
### 📌 용도
**vercel 플러그인 자체 개발/감사용 내부 스킬**이다. 실제 프로젝트에서 vercel-plugin의 스킬 주입이 얼마나 잘 작동했는지 사후 감사한다.

Claude Code 대화 로그(JSONL)에서 도구 호출을 추출하고, 실제 입력에 대해 훅 매칭을 테스트하며, 패턴 커버리지 갭을 식별하고, 플러그인 캐시의 staleness(설치 버전 vs 개발 버전)를 확인한다. "플러그인 스킬 주입을 실제 프로젝트에서 감사/테스트/조사해줘"라는 요청에 사용한다.

<a id="plugin-audit---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 플러그인 개발자가 실제 세션에서 어떤 스킬이 주입되어야 했는데 안 됐는지, 어떤 패턴이 누락됐는지 진단할 때.
- **언제 쓰지 않는가**: 일반 사용자의 Vercel 작업, 또는 라이브 eval 세션 실행(이 경우 vercel-plugin-eval/benchmark-* 사용 — 이 스킬은 이미 존재하는 로그를 사후 분석).

<a id="plugin-audit---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 1. 대상 프로젝트의 대화 로그 찾기
ls -lt ~/.claude/projects/-Users-*-<project-name>/*.jsonl

# 5. 플러그인 캐시 staleness 확인
diff <(grep 'pattern' skills/<skill>/SKILL.md) \
     <(grep 'pattern' ~/.claude/plugins/cache/.../skills/<skill>/SKILL.md)
```

훅 매칭 테스트는 셸 아웃 대신 파이프라인 함수를 직접 import한다:
```js
import { loadSkills, matchSkills } from "./hooks/pretooluse-skill-inject.mjs";
import { createLogger } from "./hooks/logger.mjs";
// loadSkills() 1회 호출 후, 각 도구 호출마다 matchSkills(toolName, toolInput, compiledSkills)
```

<a id="plugin-audit---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
워크플로우 5단계:
1. **로그 위치 파악** — 프로젝트 절대경로의 슬래시를 하이픈으로 치환한 JSONL 경로
2. **도구 호출 추출** — `message.content[]`의 `type: "tool_use"` 블록에서 name·input 추출, 도구별(Bash/Read/Write/Edit) 그룹화
3. **훅 매칭 테스트** — exported 함수 직접 호출로 정확한 매치 결과
4. **갭 식별** — path 패턴 갭, bash 패턴 갭, dedup 마스킹, budget/cap 드롭(12KB 예산·3스킬 상한)
5. **캐시 staleness** — `installed_plugins.json`의 버전·git SHA 확인

리포트: 세션 요약, 매치 매트릭스(도구×스킬), 커버리지 갭(추천 패턴 추가안), dedup 타임라인, 캐시 상태(diff). 참조: `references/log-format.md`, `scripts/batch-match.mjs`.

<a id="plugin-audit---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.claude/skills/plugin-audit/SKILL.md`

## release

> vercel-plugin을 릴리스 — 게이트 실행, 버전 범프, 아티팩트 생성, 커밋, 푸시까지 처리하는 내부 릴리스 스킬.

<a id="release---용도"></a>
### 📌 용도
**vercel 플러그인 자체 개발/배포용 내부 스킬**이다. 일반 사용자의 앱 배포가 아니라, vercel-plugin 프로젝트 자체의 엔드투엔드 릴리스 워크플로우를 수행한다.

"release", "ship", "bump and push", "cut a release" 요청 시 사용한다. 사전 게이트를 통과시키고, 시맨틱 버전을 올리고, 생성 아티팩트를 재빌드한 뒤, 변경 전체를 커밋·푸시한다.

<a id="release---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 플러그인 개발자가 vercel-plugin의 새 버전을 릴리스하려 할 때.
- **언제 쓰지 않는가**: 사용자 앱을 Vercel에 배포할 때(이 경우 `/deploy` 커맨드 사용 — 이 스킬은 플러그인 패키지 자체의 릴리스).

<a id="release---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 1. 사전 게이트 (병렬 실행, 하나라도 실패하면 중단)
bun run typecheck          # tsc --noEmit on hooks/src
bun test                   # 전체 테스트
bun run validate           # 스킬 frontmatter + manifest 무결성

# 4. 생성 아티팩트 재빌드 (hooks tsup + manifest)
bun run build

# 5. 스테이지·커밋·푸시
git add -A
git commit -m "<summary>; bump to <new-version>"
git push
```

<a id="release---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
버전 범프 기준:
| 범프 | 시점 |
|------|------|
| patch | 버그 수정, 테스트/픽스처 갱신, 문서 (기본값) |
| minor | 새 스킬, 새 훅, 새 기능 |
| major | 훅 API 또는 스킬 맵의 파괴적 변경 |

- **버전 진실 소스**: `.plugin/plugin.json`의 `version` 필드 (동기화할 package.json 버전 없음)
- 커밋 메시지 컨벤션: 서술적 요약 + `; bump to X.Y.Z`
- pre-commit 훅이 typecheck·hooks 재컴파일을 자동 재실행. 실패 시 수정 후 **새 커밋** 생성(amend 금지)
- 체크리스트: typecheck/test/validate 통과 → plugin.json 버전 범프 → `bun run build` 성공 → 전체 변경 커밋 → main 푸시

<a id="release---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.claude/skills/release/SKILL.md`

## status

> 현재 Vercel 프로젝트의 상태 진단(Doctor) — 최근 배포, 링크 정보, env 개요, 도메인, 빌드 상태, 옵저버빌리티 점검. 읽기 전용.

<a id="status---용도"></a>
### 📌 용도
**사용자용 슬래시 커맨드**다. 프로젝트 종합 헬스체크(Doctor)를 수행한다. 배포 상태, 환경 변수 구성, 도메인, 빌드 상태, 옵저버빌리티 자세를 진단한다. 파괴적 작업이 전혀 없는 읽기 전용 커맨드이며, 가능하면 MCP 읽기를 우선하고 CLI를 폴백으로 쓴다.

<a id="status---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/status` 호출 시. 프로젝트의 최근 배포·env·도메인·옵저버빌리티 현황을 한눈에 점검할 때.
- **언제 쓰지 않는가**: 실제 배포(`/deploy`)나 env 변경(`/env`)이 목적일 때. (이 커맨드는 진단만 함)

중요: 프로젝트가 링크되지 않았으면 `vercel link` 안내 후 중단하며, **GitHub Actions(`gh run list`) 등 다른 CI로 폴백하지 않는다** — Vercel CLI가 유일한 권위 소스다.

<a id="status---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
vercel ls                          # 최근 배포 (--limit 미지원)
vercel inspect <latest-url>        # 빌드 시간, 함수 수, 리전, 프레임워크, Node 버전
vercel env ls                      # 환경별 카운트 (값 미출력)
vercel domains ls                  # 도메인 DNS/SSL 상태
# vercel.json 읽어 프레임워크·빌드·함수·rewrites·cron 요약

# 옵저버빌리티 진단
curl -s -H "Authorization: Bearer $VERCEL_TOKEN" \
  "https://api.vercel.com/v1/drains?teamId=$TEAM_ID" | jq '.drains | length'
vercel metrics schema --format=json
```

<a id="status---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
진단 항목: ① 최근 배포 5건(URL/state/target/생성시각) ② 최신 배포 검사 ③ 환경 변수 카운트(값 미출력) ④ 도메인 DNS/SSL ⑤ `vercel.json` 하이라이트 ⑥ 옵저버빌리티(drains 설정·에러 상태, `@vercel/analytics`·`@vercel/speed-insights` 설치 여부, drain 서명 시크릿 `DRAIN_SECRET` 점검). drain 서명 검증 코드(HMAC-SHA1, raw body 기준, timing-safe 비교) 예시 제공. 옵저버빌리티 결정 매트릭스와 Hobby 플랜 폴백 가이드 포함. 최종 "Vercel Doctor" 리포트 블록 출력.

<a id="status---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/commands/status.md`

## vercel-plugin-eval

> 실제 Claude Code 세션을 띄워 vercel-plugin의 훅 발화·스킬 주입·dedup 정확성·커버리지를 검증하는 내부 eval 스킬.

<a id="vercel-plugin-eval---용도"></a>
### 📌 용도
**vercel 플러그인 자체 개발/검증용 내부 스킬**이다. 실제 Claude Code 세션을 WezTerm으로 띄우고 디버그 로그를 실시간 모니터링하며, 8개 등록 훅이 모두 올바르게 발화하는지와 dedup(중복 제거)이 정확한지를 검증한다.

benchmark-agents가 "고급 AI 시스템 시나리오 + 코드 품질 검증"에 무게를 둔다면, 이 스킬은 **훅 발화 정확성과 dedup 정합성**(주입 횟수 == 클레임 수)에 초점을 맞춘 라이브 eval이다.

<a id="vercel-plugin-eval---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 플러그인 개발자가 모든 훅(SessionStart·PreToolUse·UserPromptSubmit·PostToolUse·SessionEnd)의 발화와 스킬 dedup을 라이브로 검증하고 커버리지 리포트를 만들 때. macOS + WezTerm 로컬 환경 전제.
- **언제 쓰지 않는가**: 일반 사용자의 실제 Vercel 작업, 또는 이미 끝난 세션의 사후 분석(plugin-audit 사용).

<a id="vercel-plugin-eval---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 1. 테스트 디렉토리 생성 + 플러그인 설치 (타임스탬프 필수)
TS=$(date +%Y%m%d-%H%M)
SLUG="my-eval-$TS"
mkdir -p ~/dev/vercel-plugin-testing/$SLUG
cd ~/dev/vercel-plugin-testing/$SLUG
npx add-plugin https://github.com/vercel/vercel-plugin -s project -y

# 2. WezTerm 세션 기동
wezterm cli spawn --cwd .../$SLUG -- /bin/zsh -ic \
  "unset CLAUDECODE; VERCEL_PLUGIN_LOG_LEVEL=debug x '<PROMPT>' --settings .claude/settings.json; exec zsh"

# 3. 디버그 로그 찾기 (~25초 대기)
find ~/.claude/debug -name "*.txt" -mmin -2 -exec grep -l "$SLUG" {} +
```

<a id="vercel-plugin-eval---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
모니터링 대상:
- **훅 발화(8개)**: SessionStart(3개), PreToolUse 주입, UserPromptSubmit, PostToolUse validate + shadcn font-fix, SessionEnd cleanup
- **dedup 정확성(핵심 메트릭)**: 클레임 디렉토리 파일 수 == 주입 수. `skillInjection:`은 로그에 주입당 3회 나오므로 3으로 나눔
- **PostToolUse validate 품질**: API 키 우회·구형 모델·잘못된 패턴 등 실제 catch(VALIDATION 그렙)

절대 금지: `claude --print`/`-p`, `--dangerously-skip-permissions`, `/tmp/` 사용, 수동 훅 설정, `CLAUDE_PLUGIN_ROOT` 수동 설정, `bash -c`(→ `/bin/zsh -ic`), claude 풀패스(→ `x` 별칭), eval 스크립트 작성.

시나리오 설계: 프로덕트/기능만 묘사. 트리거 어려운 스킬 목록 제공(ai-elements, v0-dev, vercel-firewall, marketplace, geist, json-render는 명시적 기술 언급 필요). 커버리지 리포트는 `.notes/COVERAGE.md`에 세션 인덱스·훅 매트릭스·44개 스킬 주입 표·dedup 통계.

<a id="vercel-plugin-eval---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: vercel@claude-plugins-official
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.claude/skills/vercel-plugin-eval/SKILL.md`
