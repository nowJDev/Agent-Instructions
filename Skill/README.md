# 스킬 인덱스

2026-11-06의 [Codex 전용 업데이트](../references/codex-skill-update-2026-11-06.md)는 기존 후보 57개 중 48개 패키지를 갱신하고 9개를 동일 유지했다. 당시 Codex에서는 `firecrawl-cli`가 `firecrawl`로 바뀌고 `skill-gen`이 퇴역해 전역 설치는 102개였다. 당시 일반 설명 카탈로그 100개와 Claude 설치 상태는 그 날짜의 기록으로 보존한다. [출처 관리 132개 목록](../references/codex-skill-versions-2026-11-06.json)은 당시 새 CLI 발견 122개와 구분하며 원본 번들 버전을 실제 CLI·서버 버전으로 대신하지 않는다. Qodo 2개와 공식 경로에서 버전을 선택할 수 없는 네이티브 항목은 보류했다.

카탈로그 일반 설명 항목 **122개**를 출처별로 정리했습니다. 2026-11-11에 kordoc 1개, 2026-11-12에 Anthropic 원본 저장소의 설치 이름 19개와 Office·디자인 도구 3개를 추가했습니다. OFF 22개를 포함한 144개 항목에는 스킬·명령·메타 문서와 다른 배포 경로의 설명이 함께 있으므로 고유 스킬 수나 현재 호출 가능한 스킬 수와 구분합니다. 실제 PC의 설치·노출·인증 상태와도 구분합니다. 입력·절차·실패·검증까지 직접 작성한 범용 보강 23개와 기존 전달 스킬은 [Owned-Skills](../Owned-Skills/README.md)에 있습니다. 아래 이름과 중복되므로 카탈로그 수에 다시 더하지 않습니다.
카탈로그는 설명 단위를 선정한 목록이며 플러그인 내부 `references`·`node_modules`의 모든 `SKILL.md`를 집계하지 않습니다. 예를 들어 Huashu의 의존성 안 `playwright-trace`가 클라이언트에 별도로 발견될 수 있습니다. [2026-11-12 설치 검증의 enabled 발견 151개](../docs/history/2026-11-12-office-design-tools.md#review)는 이런 설치·클라이언트 발견 기준의 기록이며 설명 144개와 분모가 다릅니다. 명시 호출 전용 스킬은 암시적 선택 목록에 보이지 않을 수 있으므로 발견·노출·호출 정책도 구분합니다.

아래 빌트인·기존 플러그인의 ON/OFF와 캐시 경로는 작성 당시 Claude Code 환경의 기록입니다. Codex 등 현재 클라이언트에서는 실제 스킬 목록·원본 경로·도구 노출·인증을 별도로 확인합니다. 문서의 플러그인 활성 표시가 현재 설치나 사용 권한을 보장하지는 않습니다.

> 📋 **각 스킬의 한 줄 설명 목차**는 [`CATALOG.md`](CATALOG.md) 참조(일반 설명 122 + OFF 22, 스킬별 요약). 이 README는 분류·수치·출처를 다룬다.

## 분류

### 🔧 빌트인 스킬 (`_builtin/`, 13개)
Claude Code 내장 스킬. 별도 파일 없이 하네스에 내장.

| 스킬 | 한 줄 | 스킬 | 한 줄 |
|---|---|---|---|
| [code-review](_builtin/README.md#code-review) | diff 버그/품질 리뷰 | [simplify](_builtin/README.md#simplify) | 변경 코드 정리 |
| [verify](_builtin/README.md#verify) | 앱 실행해 동작 검증 | [run](_builtin/README.md#run) | 프로젝트 앱 실행 |
| [loop](_builtin/README.md#loop) | 주기적 반복 실행 | [schedule](_builtin/README.md#schedule) | cron 클라우드 에이전트 |
| [update-config](_builtin/README.md#update-config) | settings.json 설정 | [keybindings-help](_builtin/README.md#keybindings-help) | 단축키 커스터마이즈 |
| [fewer-permission-prompts](_builtin/README.md#fewer-permission-prompts) | allowlist 자동 추가 | [claude-api](_builtin/README.md#claude-api) | Claude API 레퍼런스 |
| [init](_builtin/README.md#init) | CLAUDE.md 초기화 | [review](_builtin/README.md#review) | PR 리뷰 |
| [security-review](_builtin/README.md#security-review) | 보안 취약점 리뷰 | | |

### 👤 개인 글로벌 스킬 (`_personal/`, 5개)
`~/.claude/skills/` 또는 하네스 등록형 개인 스킬.

| 스킬 | 한 줄 |
|---|---|
| [claude-news](_personal/README.md#claude-news) | Claude Code/Anthropic 소식 한국어 요약 |
| [delete-session](_personal/README.md#delete-session) | 세션 jsonl 삭제 |
| [handover](_personal/README.md#handover) | 세션 인수인계 md 작성 |
| [deep-research](_personal/README.md#deep-research) | 멀티소스 교차검증 리서치 리포트 |
| [design-driven-delivery](_personal/README.md#design-driven-delivery) | 설계부터 검증·통합까지 상태 변경 작업 통제 |

### 🧩 플러그인 스킬

| 플러그인 | 스킬 수 | 폴더 | 주제 |
|---|---|---|---|
| [superpowers](superpowers/) | 15 | `superpowers/` | 개발 워크플로우(브레인스토밍·TDD·디버깅·플랜) |
| [huggingface-skills](huggingface-skills/) | 18 | `huggingface-skills/` | HF Hub·모델학습·Spaces·데이터셋 |
| [firecrawl](firecrawl/) | 11 | `firecrawl/` | 웹 스크래핑·검색·크롤·모니터 |
| [figma](figma/) | 9 | `figma/` | Figma 디자인·다이어그램·코드커넥트·프로젝트플랜 |
| [plugin-dev](plugin-dev/) | 8 | `plugin-dev/` | Claude Code 플러그인 개발 |
| [chrome-devtools-mcp](chrome-devtools-mcp/) | 6 | `chrome-devtools-mcp/` | 브라우저 디버깅·성능·a11y |
| [ralph-loop](ralph-loop/) | 3 | `ralph-loop/` | Ralph Loop 자동 반복 |
| [claude-md-management](claude-md-management/) | 2 | `claude-md-management/` | CLAUDE.md 관리 |
| [qodo-skills](qodo-skills/) | 2 | `qodo-skills/` | Qodo 코딩 룰·PR 리졸버 |
| [agent-sdk-dev](agent-sdk-dev/) | 1 | `agent-sdk-dev/` | Agent SDK 앱 생성 |
| [pr-review-toolkit](pr-review-toolkit/) | 1 | `pr-review-toolkit/` | PR 종합 리뷰 |
| [feature-dev](feature-dev/) | 1 | `feature-dev/` | 기능 개발 가이드 |
| [claude-code-setup](claude-code-setup/) | 1 | `claude-code-setup/` | 자동화 추천 |
| [skill-creator](skill-creator/) | 1 | `skill-creator/` | 스킬 생성·최적화 |
| [frontend-design](frontend-design/) | 1 | `frontend-design/` | 프런트엔드 디자인 |
| [playground](playground/) | 1 | `playground/` | 인터랙티브 HTML 플레이그라운드 |
| [kordoc](kordoc/) | 1 | `kordoc/` | 한국 공문서 읽기·생성·채움·편집·검증 |
| [anthropic-skills](anthropic-skills/) | 19 | `anthropic-skills/` | Anthropic 원본을 `anthropic-` 이름으로 전역 설치하는 안내 |
| [office-design-tools](office-design-tools/) | 3 | `office-design-tools/` | PPT Master·OfficeCLI·Huashu Design의 단일 전역 설치 안내 |

`frontend-design`·`skill-creator` 그룹은 기존 Anthropic 플러그인 배포 경로의 설명으로 보존한다. 이번 Codex 설치에서는 해당 전역 실행본을 `anthropic-frontend-design`·`anthropic-skill-creator`로 이전한다. 자체 제작 `claude-api`와 OpenAI 내장 `skill-creator`는 별개로 보존한다. [이전·중복 처리와 호출 정책](anthropic-skills/README.md#설치와-중복-처리)을 따른다.

### ⛔ 비활성(OFF) 플러그인 스킬 (`_disabled/`, 22개)
작성 당시 Claude Code의 `settings.json`에서 `enabledPlugins = false`였던 항목이다. 활성화 뒤에도 해당 클라이언트의 설치·필수 실행 도구·인증·실제 노출을 확인해야 한다.

| 플러그인 | 구성 | 폴더 | 주제 |
|---|---|---|---|
| [vercel](_disabled/vercel/) | 스킬 7 + 명령 5 + 메타 문서 1 | `_disabled/vercel/` | 배포 커맨드(deploy·env·status…)는 사용자용 / benchmark·release·audit은 플러그인 내부 개발용 |
| [hookify](_disabled/hookify/) | 스킬 1 + 커맨드 4 | `_disabled/hookify/` | 자연어 규칙→훅 자동 생성 |
| [neon](_disabled/neon/) | 스킬 2 | `_disabled/neon/` | Neon Postgres·이그레스 최적화 ※원문 미vendoring → 메타데이터 기반 작성(문서는 완결) |
| [railway](_disabled/railway/) | 스킬 1 | `_disabled/railway/` | Railway 배포·DB 운영 |
| [semgrep](_disabled/semgrep/) | 커맨드 1 | `_disabled/semgrep/` | Semgrep 보안 스캔 설치(스킬 없음, MCP 제공) |

> ⚠️ **neon** 두 스킬은 캐시의 SKILL.md가 깨진 심볼릭 링크라 본문이 없어 매니페스트 메타데이터로만 작성됨. 본문 필요 시 `github.com/neondatabase/agent-skills` fetch 또는 플러그인 재설치 필요.
> ⚠️ **vercel** `_conventions.md`는 실제 슬래시 커맨드가 아닌 메타 문서(언더스코어 접두).

## ℹ️ 비노출 ON 플러그인 (의도된 제외)

다음은 작성 당시 Claude Code의 `enabledPlugins`에서 **ON이었지만** 해당 세션에 스킬/MCP로 노출되지 않아 카탈로그에서 제외한 항목입니다. 현재 클라이언트의 설치·노출 여부는 별도로 확인합니다.
- **LSP 4종** (`rust-analyzer`·`typescript`·`pyright`·`csharp`-lsp): 에디터 LSP 기능만 제공, 스킬/MCP 비노출.
- **atomic-agents**: 세션에 노출되는 스킬/MCP 컴포넌트 없음.
- **code-simplifier**: 전용 에이전트를 제공하며 동명 빌트인 simplify와 구분한다. pr-review-toolkit의 review-pr 명령은 위 카탈로그에 포함한다.

## 📦 출처·설치 매핑 (다른 AI로 이식 시 — 경로 A)

이 저장소는 **타사 Skill 실물을 담지 않는다**(재배포 회피). 직접 작성한 Skill만 [`../Owned-Skills/`](../Owned-Skills/)에 원본을 보관한다. 타사 Skill은 아래 **공개 원본에서 각자 설치**한다. 자세한 절차는 [`../PORTABILITY.md`](../PORTABILITY.md) §3 참조.

2026-11-06의 [설치 실물 출처 전수조사](../references/skill-provenance-2026-11-06.md)에는 스킬별 고정 원본 링크, 본문 일치·변환·미확인 판정과 삭제 이후 집계를 기록했다. 공개 설명 카탈로그와 실제 설치본의 출처는 구분한다.

### 자체 제작 원본.

| Skill | 공개 원본 | License |
|---|---|---|
| `design-driven-delivery` | [`Owned-Skills/design-driven-delivery`](../Owned-Skills/design-driven-delivery/SKILL.md) | 이 저장소의 MIT License |
| `daily-work-report` | [`Owned-Skills/daily-work-report`](../Owned-Skills/daily-work-report/SKILL.md) | 이 저장소의 MIT License |
| `coplay-funplay-unity-mcp-setup` | [`Owned-Skills/coplay-funplay-unity-mcp-setup`](../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md) | 이 저장소의 MIT License |
| 범용 보강 23개. | [이름별 패키지·설치 안내](../Owned-Skills/README.md), [공개 출처·채택 경계](../references/skill-strengthening.md). | 자체 작성 본문에 이 저장소의 MIT License 적용. |

### 외부 서드파티 repo (라이선스 명시 — 이식 가장 안전)
| 플러그인 | 공개 원본 | License |
|---|---|---|
| `superpowers` | `github.com/obra/superpowers` | MIT |
| `huggingface-skills` | `github.com/huggingface/skills` | Apache-2.0 |
| `qodo-skills` | `github.com/qodo-ai/qodo-skills` | MIT |
| `vercel` (OFF) | `github.com/vercel/vercel-plugin` | Apache-2.0 |
| `railway` (OFF) | `github.com/railwayapp/railway-skills` | MIT |
| `neon` (OFF) | `github.com/neondatabase/agent-skills` | Apache-2.0 |
| `atomic-agents`* | `github.com/BrainBlend-AI/atomic-agents` | MIT |
| `kordoc` | [chrisryugj/kordoc](https://github.com/chrisryugj/kordoc), [스킬 경로·버전·설치 안내](kordoc/README.md#kordoc) | MIT |
| `anthropic-skills` | [anthropics/skills](https://github.com/anthropics/skills), [고정 커밋·전역 설치 안내](anthropic-skills/README.md) | 원본 각 패키지의 라이선스·공통 고지를 보존한다. |
| `ppt-master`·`officecli`·`huashu-design` | [출처·고정 버전·전역 설치 안내](office-design-tools/README.md) | PPT Master MIT·OfficeCLI Apache-2.0·Huashu MIT 및 일부 스티커 PolyForm Shield 예외를 보존한다. |

\* atomic-agents는 세션 비노출(카탈로그 외)이나 출처 참고용 기재.

### 마켓플레이스 배포와 실제 원본.
마켓플레이스는 배포 경로이며 제작자 원본과 구분한다. 개별 플러그인 매니페스트에 repo·license가 없더라도 공개 원본 파일은 별도로 확인할 수 있다. 아래 제작자 원본과 스킬별 고정 커밋은 [전수조사 기록](../references/skill-provenance-2026-11-06.md)을 따른다.

| 계열 | 확인한 공개 원본 |
|---|---|
| Firecrawl. | [firecrawl/firecrawl-claude-plugin](https://github.com/firecrawl/firecrawl-claude-plugin). |
| Figma. | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide). |
| Chrome DevTools. | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp). |
| Unity. | [Unity-Technologies/skills](https://github.com/Unity-Technologies/skills). |
| Codex 내장. | [openai/codex](https://github.com/openai/codex/tree/main/codex-rs/skills/src/assets/samples). |
| OpenAI curated. | [openai/skills](https://github.com/openai/skills). |
| Ponytail. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail). |

- **Anthropic 제작(12)**: `plugin-dev`·`ralph-loop`·`claude-md-management`·`agent-sdk-dev`·`pr-review-toolkit`·`feature-dev`·`claude-code-setup`·`skill-creator`·`frontend-design`·`playground`·`code-simplifier`·`hookify`
- **외부사 번들(5)**: `firecrawl`(Firecrawl)·`figma`(Figma)·`context7`(Upstash)·`playwright`(Microsoft)·`semgrep`(Semgrep)
- `chrome-devtools-mcp`: MCP 실행 설정뿐 아니라 위 공개 저장소의 실제 스킬 원본 6개도 확인했다.

> ⚠️ **License 미기재 주의**: 위 번들 항목은 plugin.json에 license 필드가 없다. 외부사 제작분(Figma·Microsoft·Upstash·Semgrep·Firecrawl)을 다른 곳에 재배포·이식할 때는 **각 제작사 약관을 별도 확인**할 것. 안전한 길은 "재배포하지 말고 마켓플레이스에서 각자 설치"다.

### Superpowers 버전과 설치 채널

이 카탈로그의 기준은 [v7.0.2](https://github.com/obra/superpowers/tree/v7.0.2), 커밋 `22f0b463e7a5e579904dd6211a520321035526f7`의 15개 스킬이다. 이 저장소에는 요약만 두고 타사 실행 원본·설정·세션 자료는 넣지 않는다. 아래는 배포 경로 안내이며 특정 PC의 설치 완료나 새 세션 로드 성공을 뜻하지 않는다.

| 대상 | 설치·확인 방법 |
|---|---|
| Claude Code | 제작자 [superpowers-marketplace](https://github.com/obra/superpowers-marketplace)를 등록하고 `superpowers@superpowers-marketplace`를 사용한다. 실제 `plugin.json`의 버전과 설치 등록·활성 상태를 확인한다. |
| Codex 패키지 설치 | 확인한 원본의 `skills/<name>` 15개 패키지를 각각 `~/.agents/skills/<name>`에 리소스까지 보존해 배치한다. 기존 동명 항목·개인 추가 파일을 먼저 확인·백업하고 새로 복제한 파일을 원본과 비교한다. |
| 다른 배포 채널 | Anthropic 공식 마켓플레이스와 OpenAI 플러그인 마켓플레이스는 제작자 원본과 배포 시점이 다를 수 있다. 채널명만으로 최신 버전이라고 판단하지 않는다. |

Claude Code에서 제작자 채널을 선택할 때의 명령은 다음과 같다. 기존 설치가 있으면 같은 이름의 활성 출처를 먼저 확인해 중복을 피한다.

```text
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

2026-11-05 확인 당시 [Anthropic 공식 채널](https://github.com/anthropics/claude-plugins-official/blob/main/.claude-plugin/marketplace.json)은 7.0.0 원본을, [OpenAI 채널](https://github.com/openai/plugins/blob/main/plugins/superpowers/.codex-plugin/plugin.json)은 6.3.0을 배포했다. 재설치·업데이트 때에는 각 채널이 지정한 원본 커밋과 실제 매니페스트를 다시 확인한다. 이 날짜의 수치를 앞으로도 고정된 상태로 취급하지 않는다.

설치 후에는 새 세션에서 15개 스킬의 발견 여부, 실제 읽은 `SKILL.md`와 버전 근거, `diagnosing-superpowers`와 새 리뷰 템플릿·스크립트 참조를 확인한다. Claude 플러그인과 Codex 패키지 복사본은 별도로 갱신한다. 같은 클라이언트에 동명 스킬을 두 방식으로 중복 설치하지 않는다. 기존 사용자 지침·커스텀 스킬·MCP·권한·모델 설정은 보존한다.

### 설치 방법
- **받는 AI가 Claude Code**: 일반 번들은 `/plugin marketplace add anthropics/claude-plugins-official` 후 필요한 플러그인을 설치한다. Superpowers는 위 버전·채널 안내에 따라 제작자 마켓플레이스를 사용한다.
- **받는 AI가 Agent Skills 지원**: 해당 원본 repo에서 **스킬 루트 디렉터리 전체**를 배치하고, `SKILL.md`의 `scripts/`·`references/`·`assets/`·예제 및 상대경로 의존 리소스를 보존한다. 별도 플러그인의 커맨드·훅 등 Claude 전용 구성만 제외하며, 설치 후 참조 파일과 실행 환경을 확인한다. [패키지 구조](https://agentskills.io/specification#directory-structure)를 따른다.
- **미지원 AI**: [`../PORTABILITY.md`](../PORTABILITY.md) 경로 B(참조 활용)·C(MCP 래핑).

## 분류별 문서 구성.

144개 설명은 26개 그룹 폴더의 README.md에 모았다. [CATALOG](CATALOG.md)의 항목을 누르면 해당 분류의 절로 이동한다. 각 항목의 용도·사용 조건·예제·실패 처리·출처·설치 확인 경계는 유지한다.

기존 개별 Markdown 주소는 같은 폴더 README.md의 파일명 앵커로 바뀌었다. 예를 들어 _personal/claude-news.md는 [개인 스킬의 claude-news 절](_personal/README.md#claude-news)에서 찾는다. [고정된 이전 버전](https://github.com/nowJDev/Agent-Instructions/tree/a559c66d71aee886e717ff91bffce6270accdb17/Skill)에서 옛 배치를 확인할 수 있다. 기존 그룹에 항목을 추가할 때는 새 파일 대신 해당 README의 절과 CATALOG 링크를 갱신한다.
