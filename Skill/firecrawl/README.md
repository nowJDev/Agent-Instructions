<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# firecrawl 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. ON/OFF·캐시 표시는 작성 당시 Claude Code 환경의 기록이며 현재 클라이언트의 설치·노출·인증 상태와 구분한다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [firecrawl-agent](#firecrawl-agent).
- [firecrawl-cli](#firecrawl-cli).
- [firecrawl-crawl](#firecrawl-crawl).
- [firecrawl-download](#firecrawl-download).
- [firecrawl-interact](#firecrawl-interact).
- [firecrawl-map](#firecrawl-map).
- [firecrawl-monitor](#firecrawl-monitor).
- [firecrawl-parse](#firecrawl-parse).
- [firecrawl-scrape](#firecrawl-scrape).
- [firecrawl-search](#firecrawl-search).
- [skill-gen](#skill-gen).

## firecrawl-agent

> AI가 복잡한 사이트를 자율 탐색해 구조화된 JSON 데이터를 추출하는 스킬.

<a id="firecrawl-agent---용도"></a>
### 📌 용도
AI 기반 자율 추출(autonomous extraction) 에이전트를 실행한다. 에이전트가 사이트를 스스로 돌아다니며 어디에 데이터가 있는지 파악하고, 구조화된 데이터를 반환한다. 실행에 보통 2~5분이 걸린다. 여러 페이지에 걸친 구조화 추출에서 단순 스크래핑보다 강력하다.

- 복잡한 다중 페이지 사이트에서 구조화된 데이터가 필요할 때
- 수동 스크래핑이라면 여러 페이지를 직접 돌아다녀야 하는 경우
- 데이터가 어디 있는지 AI가 알아서 찾아주길 원할 때

<a id="firecrawl-agent---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "구조화된 데이터 추출", "모든 제품 가져와", "가격 정보 뽑아줘", "JSON으로 추출", 또는 사용자가 웹 데이터용 JSON 스키마를 제공할 때. 가격 티어/제품 목록/디렉터리 항목 등을 스키마 기반 JSON으로 원할 때.
- **언제 쓰지 않는가**: 단일 페이지 단순 추출(→ `firecrawl-scrape`가 더 빠르고 저렴), 링크만 따라가는 비-AI 대량 추출(→ `firecrawl-crawl`), 수동 클릭/폼 제어가 필요한 경우(→ `firecrawl-interact`).

<a id="firecrawl-agent---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 구조화된 데이터 추출
firecrawl agent "extract all pricing tiers" --wait -o .firecrawl/pricing.json

# JSON 스키마로 구조화 출력
firecrawl agent "extract products" \
  --schema '{"type":"object","properties":{"name":{"type":"string"},"price":{"type":"number"}}}' \
  --wait -o .firecrawl/products.json

# 특정 페이지에 집중
firecrawl agent "get feature list" --urls "<url>" --wait -o .firecrawl/features.json
```

<a id="firecrawl-agent---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `--urls <urls>` | 에이전트 시작 URL |
| `--model <model>` | 모델 선택: `spark-1-mini` 또는 `spark-1-pro` |
| `--schema <json>` | 구조화 출력용 JSON 스키마 |
| `--schema-file <path>` | JSON 스키마 파일 경로 |
| `--max-credits <n>` | 이번 실행의 크레딧 상한 |
| `--wait` | 에이전트 완료까지 대기 |
| `--pretty` | JSON 보기 좋게 출력 |
| `-o, --output <path>` | 출력 파일 경로 |

**팁**: `--wait`를 항상 사용해 결과를 인라인으로 받는다(없으면 job ID만 반환). 예측 가능한 출력을 원하면 `--schema` 사용. agent 실행은 단순 스크래프보다 크레딧을 많이 소모하므로 `--max-credits`로 상한을 둔다.

<a id="firecrawl-agent---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl agent`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-agent/SKILL.md`

## firecrawl-cli

> Firecrawl CLI로 웹을 검색·스크래핑·상호작용하는 최상위 워크플로우 스킬. LLM에 최적화된 클린 마크다운 반환.

> 참고: 이 스킬의 frontmatter `name`은 `firecrawl`이지만, 플러그인 디렉터리/슬래시 명칭은 `firecrawl-cli`다.

이 절은 기존 Claude 플러그인 배포 이름을 보존한 설명이다. [2026-11-06 Codex 업데이트](../../references/codex-skill-update-2026-11-06.md)에서 전역 설치 이름은 `firecrawl`로 바뀌었다. 실행 전 현재 발견된 이름·원본 본문과 CLI의 설치·인증·`--help`를 확인한다.

<a id="firecrawl-cli---용도"></a>
### 📌 용도
웹 검색, 스크래핑, 페이지 상호작용을 모두 아우르는 Firecrawl CLI의 진입점/허브 스킬이다. 결과는 LLM 컨텍스트에 최적화된 클린 마크다운으로 반환한다. 개별 작업은 하위 스킬(search/scrape/map/crawl/agent/interact/download/parse/monitor)로 라우팅한다.

**워크플로우 에스컬레이션 패턴** (필요에 따라 단계 상승):
1. **search** — 특정 URL이 아직 없음. 페이지 발견, 질문 답변, 소스 탐색.
2. **scrape** — URL 보유. 내용 직접 추출(정적/JS 렌더링 모두).
3. **map + scrape** — 대형 사이트에서 특정 서브페이지를 찾을 때. `map --search`로 URL 찾고 스크래프.
4. **crawl** — 사이트 섹션 전체 대량 추출(예: 모든 `/docs/`).
5. **monitor** — 반복 점검/알림. 일회성 반복 스크래프 대신 `--page` + `--goal` 모니터 설정.
6. **interact** — 스크래프 후 페이지 상호작용(페이지네이션, 모달, 폼 제출, 다단계 내비게이션).

<a id="firecrawl-cli---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 웹 검색, 기사/주제 리서치, 온라인 조회, 웹페이지 스크래핑, URL에서 콘텐츠 가져오기, 문서 크롤링, 사이트 다운로드, 클릭/로그인이 필요한 상호작용. "fetch this page", "pull the content from", "get the page at https://", 외부 웹사이트 언급 등.
- **언제 쓰지 않는가**: 로컬 파일 작업, git 명령, 배포, 코드 편집 작업.

<a id="firecrawl-cli---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 상태/인증 확인
firecrawl --status

# 설치 검증
mkdir -p .firecrawl
firecrawl scrape "https://firecrawl.dev" -o .firecrawl/install-check.md

# 검색 + 스크래프
firecrawl search "query" --scrape --limit 3

# 모니터 생성(단일 페이지, 이메일 알림)
firecrawl monitor create --name "Blog" --schedule "every 5 minutes" \
  --goal "Alert when a new blog post is published." \
  --page https://example.com/blog --email alerts@example.com

# 병렬 스크래프(동시성 한도 내)
firecrawl scrape "<url-1>" -o .firecrawl/1.md &
firecrawl scrape "<url-2>" -o .firecrawl/2.md &
wait

# 크레딧 사용량
firecrawl credit-usage
```

<a id="firecrawl-cli---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`
- **명령 라우팅 표**: search / scrape / map / crawl / agent / interact / download / parse / monitor.
- **모니터 `--goal` 작성 규칙**: 사용자 의도를 `Alert when ...` 형식의 2~3문장으로 변환. 범위(top N, 가격, 역할, 회사, 지역 등) 명시. 의도별 예외만 `Ignore ...`로 추가(일반 노이즈는 judge가 자동 처리). 모호하면 범위를 넓게 유지.
- **JSON-mode change tracking**: 특정 구조화 필드(가격, 헤드라인, 재고)만 감시 시 `changeTracking` 포맷 + `modes: ["json"]` + JSON 스키마를 JSON 페이로드로 전달. 결과는 `plans[0].price` 같은 필드별 diff. `["json","git-diff"]`는 혼합 모드.
- **출력 규칙**: 결과는 `-o`로 `.firecrawl/`에 저장하고 `.gitignore`에 추가. URL은 항상 따옴표(`?`, `&` 보호). 전체 파일 통째로 읽지 말고 `grep`/`head`/증분 읽기. 단일 포맷은 raw, 복수 포맷(`--format markdown,links`)은 JSON.
- **search 후 피드백**: 검색은 2크레딧, `firecrawl search-feedback <id>`로 첫 피드백 시 1크레딧 환불. `FIRECRAWL_NO_SEARCH_FEEDBACK=1`이면 비활성.
- **연계 스킬**: 앱 통합은 `firecrawl-build`, 결과물 워크플로우(리서치/SEO/QA/리드/지식베이스/디자인시스템 추출)는 `firecrawl-workflows`.

<a id="firecrawl-cli---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(설치·인증 필요, `firecrawl --status`로 확인). 동시성/크레딧 한도 존재.
- 부속 룰 파일: `rules/install.md`(설치·인증), `rules/security.md`(출력·안전 읽기)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-cli/SKILL.md`

## firecrawl-crawl

> 웹사이트 전체 또는 섹션의 여러 페이지를 링크를 따라가며 대량 추출하는 스킬.

<a id="firecrawl-crawl---용도"></a>
### 📌 용도
링크를 따라가며 깊이/개수 제한 안에서 사이트의 여러 페이지 내용을 한꺼번에 추출한다. 경로 필터링과 동시 추출을 지원한다.

- 사이트의 많은 페이지가 필요할 때(예: 모든 `/docs/`)
- 사이트 섹션 전체를 추출하고 싶을 때
- 워크플로우 에스컬레이션 패턴 4단계: search → scrape → map → **crawl** → interact

<a id="firecrawl-crawl---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "crawl", "모든 페이지 가져와", "/docs 아래 전부 추출", "대량 추출(bulk extract)", 같은 사이트의 여러 페이지 콘텐츠가 필요할 때.
- **언제 쓰지 않는가**: 단일 페이지(→ `firecrawl-scrape`), 로컬 파일로 저장하고 싶을 때(→ `firecrawl-download`), 크롤 전 URL 목록만 보고 싶을 때(→ `firecrawl-map`), AI 자율 구조화 추출(→ `firecrawl-agent`).

<a id="firecrawl-crawl---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# docs 섹션 크롤
firecrawl crawl "<url>" --include-paths /docs --limit 50 --wait -o .firecrawl/crawl.json

# 깊이 제한 전체 크롤 + 진행 표시
firecrawl crawl "<url>" --max-depth 3 --wait --progress -o .firecrawl/crawl.json

# 실행 중 크롤 상태 확인
firecrawl crawl <job-id>
```

<a id="firecrawl-crawl---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `--wait` | 완료까지 대기 후 반환 |
| `--progress` | 대기 중 진행 표시 |
| `--limit <n>` | 최대 크롤 페이지 수 |
| `--max-depth <n>` | 따라갈 최대 링크 깊이 |
| `--include-paths <paths>` | 해당 경로 매칭 URL만 크롤 |
| `--exclude-paths <paths>` | 해당 경로 매칭 URL 제외 |
| `--delay <ms>` | 요청 간 지연 |
| `--max-concurrency <n>` | 최대 병렬 크롤 워커 |
| `--pretty` | JSON 보기 좋게 출력 |
| `-o, --output <path>` | 출력 파일 경로 |

**팁**: 결과가 즉시 필요하면 항상 `--wait`(없으면 비동기 폴링용 job ID). `--include-paths`로 범위를 좁혀 전체 사이트를 무분별하게 크롤하지 말 것. 크롤은 페이지당 크레딧을 소모하므로 대규모 크롤 전 `firecrawl credit-usage` 확인.

<a id="firecrawl-crawl---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl crawl`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-crawl/SKILL.md`

## firecrawl-download

> 웹사이트 전체를 로컬 파일(마크다운/스크린샷/다중 포맷)로 다운로드하는 스킬. (실험적)

<a id="firecrawl-download---용도"></a>
### 📌 용도
`map` + `scrape`를 결합한 편의 명령으로, 사이트 전체를 로컬 파일로 저장한다. 먼저 사이트를 매핑해 페이지를 발견한 뒤 각 페이지를 `.firecrawl/` 아래 중첩 디렉터리로 스크래프한다. 모든 scrape 옵션이 download에서도 동작한다. 자동화 흐름에서는 항상 `-y`로 확인 프롬프트를 건너뛴다.

- 사이트(또는 섹션) 전체를 로컬 파일로 저장하고 싶을 때
- 문서를 오프라인으로 접근해야 할 때
- 정리된 파일 구조로 대량 콘텐츠 추출

> **실험적(Experimental)** 명령이다.

<a id="firecrawl-download---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "사이트 다운로드", "로컬 파일로 저장", "오프라인 사본", "모든 docs 다운로드", "참고용으로 저장(save for reference)" 등.
- **언제 쓰지 않는가**: URL만 발견하면 되는 경우(→ `firecrawl-map`), 개별 페이지(→ `firecrawl-scrape`), 로컬 파일이 아닌 JSON 대량 추출(→ `firecrawl-crawl`).

<a id="firecrawl-download---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 대화형 마법사(포맷/스크린샷/경로 자동 선택)
firecrawl download https://docs.example.com

# 스크린샷 포함
firecrawl download https://docs.example.com --screenshot --limit 20 -y

# 다중 포맷(페이지마다 별도 파일)
firecrawl download https://docs.example.com --format markdown,links --screenshot --limit 20 -y
# 페이지별 생성: index.md + links.txt + screenshot.png

# 특정 섹션 필터
firecrawl download https://docs.example.com --include-paths "/features,/sdks"

# 번역 페이지 제외
firecrawl download https://docs.example.com --exclude-paths "/zh,/ja,/fr,/es,/pt-BR"
```

<a id="firecrawl-download---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

**Download 옵션**

| 옵션 | 설명 |
| --- | --- |
| `--limit <n>` | 최대 다운로드 페이지 수 |
| `--search <query>` | 검색어로 URL 필터 |
| `--include-paths <paths>` | 매칭 경로만 다운로드 |
| `--exclude-paths <paths>` | 매칭 경로 제외 |
| `--allow-subdomains` | 서브도메인 페이지 포함 |
| `-y` | 확인 프롬프트 건너뛰기(자동화 시 항상 사용) |

**Scrape 옵션(모두 download와 호환)**: `-f <formats>`, `-H`, `-S`, `--screenshot`, `--full-page-screenshot`, `--only-main-content`, `--include-tags`, `--exclude-tags`, `--wait-for`, `--max-age`, `--country`, `--languages`

<a id="firecrawl-download---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl download`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-download/SKILL.md`

## firecrawl-interact

> 스크래프한 페이지의 라이브 브라우저 세션을 자연어/코드로 제어하는 스킬 — 클릭, 폼 입력, 내비게이션, 로그인.

<a id="firecrawl-interact---용도"></a>
### 📌 용도
스크래프한 페이지를 라이브 브라우저 세션에서 조작한다. 먼저 페이지를 스크래프한 뒤, 자연어 프롬프트 또는 코드로 클릭·폼 입력·내비게이션·데이터 추출을 수행한다.

- 클릭, 폼 입력, 페이지네이션, 로그인 등 상호작용이 필요한 콘텐츠
- JavaScript 상호작용 뒤에 콘텐츠가 있어 `scrape`가 실패한 경우
- 다단계 플로우(체크아웃, 위저드 등) 내비게이션
- 워크플로우 에스컬레이션 패턴의 최후 수단: search → scrape → map → crawl → **interact**
- 웹 검색에는 절대 interact 사용 금지 — `search` 사용

<a id="firecrawl-interact---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "interact", "click", "fill out the form", "log in to", "sign in", "submit", "paginated", "next page", "infinite scroll", "navigate to", "open a session", "scrape failed". 인증 스크래핑(프로필) 포함.
- **언제 쓰지 않는가**: 단순 정적/SPA 페이지(먼저 `scrape` 시도), 웹 검색(→ `firecrawl-search`), AI 자율 구조화 추출(→ `firecrawl-agent`).

<a id="firecrawl-interact---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 1) 페이지 스크래프(scrape ID 자동 저장)
firecrawl scrape "<url>"

# 2) 자연어로 상호작용
firecrawl interact --prompt "Click the login button"
firecrawl interact --prompt "Fill in the email field with test@example.com"
firecrawl interact --prompt "Extract the pricing table"

# 3) 코드로 정밀 제어
firecrawl interact --code "agent-browser click @e5" --bash
firecrawl interact --code "agent-browser snapshot -i" --bash

# 4) 작업 종료 시 세션 정리
firecrawl interact stop
```

**프로필(인증 상태 유지)**:
```bash
# 세션1: 로그인 후 상태 저장
firecrawl scrape "https://app.example.com/login" --profile my-app
firecrawl interact --prompt "Fill in email with user@example.com and click login"

# 세션2: 인증된 상태로 재접속
firecrawl scrape "https://app.example.com/dashboard" --profile my-app
firecrawl interact --prompt "Extract the dashboard data"

# 읽기 전용 재접속(프로필 상태 미변경)
firecrawl scrape "https://app.example.com" --profile my-app --no-save-changes
```

<a id="firecrawl-interact---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `--prompt <text>` | 자연어 지시(이것 OR `--code`) |
| `--code <code>` | 브라우저 세션에서 실행할 코드 |
| `--bash` / `--python` / `--node` | 코드 언어 선택(서로 배타적, 기본 Node.js/Playwright) |
| `--timeout <seconds>` | 실행 타임아웃(기본 30, 최대 300) |
| `--scrape-id <id>` | 특정 스크래프 대상 지정(기본: 마지막 스크래프) |
| `-o, --output <path>` | 출력 파일 경로 |

**팁**: 반드시 먼저 `scrape` — interact는 이전 스크래프의 scrape ID가 필요. scrape ID는 자동 저장되어 이후 interact에는 `--scrape-id` 불필요. 작업 끝나면 `firecrawl interact stop`으로 리소스 해제. 병렬 작업 시 여러 페이지를 스크래프 후 각 `--scrape-id`로 상호작용.

옵션은 [공식 CLI 1.26.3 계약](https://github.com/firecrawl/cli/blob/3136f724b3203c6a69bfb14d2f384271eb45822c/src/index.ts)을 기준으로 하며, 실행 전 설치 버전의 `firecrawl interact --help`를 확인한다. `--language`는 이 배포 버전의 옵션이 아니다.

<a id="firecrawl-interact---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl interact`, 라이브 브라우저 세션)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-interact/SKILL.md`

## firecrawl-map

> 웹사이트의 모든 URL을 발견·나열하는 스킬. 검색 필터로 특정 페이지 위치 파악.

<a id="firecrawl-map---용도"></a>
### 📌 용도
사이트의 URL을 발견한다. `--search`로 대형 사이트 안에서 특정 페이지를 찾을 수 있다. 사이트는 알지만 정확한 페이지를 모를 때 필수적이다.

- 대형 사이트에서 특정 서브페이지를 찾아야 할 때
- 스크래프/크롤 전에 전체 URL 목록이 필요할 때
- 워크플로우 에스컬레이션 패턴 3단계: search → scrape → **map** → crawl → interact

<a id="firecrawl-map---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "map the site", "find the URL for", "what pages are on", "list all pages", 사이트 구조 파악, 도메인 내 위치 찾기.
- **언제 쓰지 않는가**: 이미 URL을 알고 내용만 필요할 때(→ `firecrawl-scrape`), 발견 후 바로 대량 추출(→ `firecrawl-crawl`), 로컬 다운로드(→ `firecrawl-download`).

<a id="firecrawl-map---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 대형 사이트에서 특정 페이지 찾기
firecrawl map "<url>" --search "authentication" -o .firecrawl/filtered.txt

# 모든 URL 가져오기
firecrawl map "<url>" --limit 500 --json -o .firecrawl/urls.json
```

**Map + scrape 패턴(흔한 조합)**: `map --search`로 올바른 URL을 찾고 그 URL을 `scrape`.
예: `map https://docs.example.com --search "auth"` → `/docs/api/authentication` 발견 → 해당 URL `scrape`.

<a id="firecrawl-map---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `--limit <n>` | 반환할 최대 URL 수 |
| `--search <query>` | 검색어로 URL 필터 |
| `--sitemap <include\|skip\|only>` | 사이트맵 처리 전략 |
| `--include-subdomains` | 서브도메인 URL 포함 |
| `--json` | JSON 출력 |
| `-o, --output <path>` | 출력 파일 경로 |

<a id="firecrawl-map---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl map`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-map/SKILL.md`

## firecrawl-monitor

> 웹사이트 콘텐츠 변경을 감지해 웹훅/이메일로 알려주는 스킬 — cron·스크래퍼·diff 스크립트 불필요.

<a id="firecrawl-monitor---용도"></a>
### 📌 용도
웹사이트 콘텐츠가 변경되면 감지해 웹훅 또는 이메일로 통지한다. 각 체크의 페이지마다 `same`/`new`/`changed`/`removed`/`error` 라벨이 붙고, 스냅샷 이력과 구조화된 필드별 diff를 제공해 다운스트림 도구에 바로 연동할 수 있다. AI judge가 포맷·타임스탬프·트래킹 파라미터 노이즈를 걸러 실제 콘텐츠 변경에만 알림을 발생시킨다.

**모니터를 쓰는 이유**
- **변경 감지 서비스화** — 페치·diff·판정·통지를 모두 서버 측에서 처리. cron/diff 라이브러리/SMTP/스냅샷 DB 불필요.
- **알림 우선** — 웹훅(`monitor.page`, `monitor.check.completed`)과 이메일 요약. 외부 수신자는 옵트인 확인 필요.
- **AI 노이즈 필터(`--goal`)** — 평문 목표를 주면 judge가 포맷/공백/케이스/세션ID/캐시버스터/트래킹 파라미터 등을 무시.
- **구조화 필드별 diff** — JSON 모드 시 `plans[0].price: "$19/mo" → "$24/mo"` 형태.
- **단순 페이지 상태 모델**, **인프라 없는 스냅샷 이력(`--retention-days`)**, **다중 페이지 감시**, **스케줄 글루 불필요**(자연어 스케줄 지원).

<a id="firecrawl-monitor---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "monitor", "watch", "track", "alert me when", "notify when X changes", "ping me if", "email me when", "send a webhook when". 경쟁사 가격 감시, 신규 채용/블로그 알림, docs/changelog/status 페이지 모니터링. 같은 URL을 두 번 이상 점검해야 하면 일회성 반복 스크래프 대신 권장.
- **언제 쓰지 않는가**: 페이지를 한 번만 읽으면 되는 경우(→ `firecrawl-scrape`). zero-data-retention 팀은 모니터링 불가.

<a id="firecrawl-monitor---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 단일 페이지, 자연어 스케줄, 이메일 알림
firecrawl monitor create --name "Blog" --schedule "every 30 minutes" \
  --goal "Alert when a new blog post is published." \
  --page https://example.com/blog --email alerts@example.com

# 여러 페이지 한 모니터로
firecrawl monitor create --name "Product pages" --schedule "every 30 minutes" \
  --goal "Alert when pricing, docs, or changelog content changes." \
  --scrape-urls https://example.com/pricing,https://example.com/docs

# 사이트 크롤 기반(발견된 모든 페이지 diff)
firecrawl monitor create --name "Docs site" --schedule "hourly" \
  --goal "Alert when any docs page is added, removed, or substantively changed." \
  --crawl-url https://docs.example.com

# 관리/검사
firecrawl monitor list --limit 20
firecrawl monitor run <monitorId>          # 즉시 체크 실행
firecrawl monitor checks <monitorId>
firecrawl monitor check <monitorId> <checkId> --page-status changed
firecrawl monitor update <monitorId> --state paused
firecrawl monitor delete <monitorId>
```
서브커맨드: `create | list | get | update | delete | run | checks | check`

<a id="firecrawl-monitor---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `--name <name>` | 모니터 이름(create 시 필수) |
| `--goal <text>` | 평문 변경 목표(AI judge 자동 활성) |
| `--schedule <text>` / `--cron <expr>` | 자연어/cron 스케줄. [공식 모니터 안내](https://docs.firecrawl.dev/features/monitoring) 확인 기준 최소 5분이며 서비스·설치 버전의 제한을 재확인한다. |
| `--timezone <tz>` | 스케줄 타임존(기본 UTC) |
| `--page <url>` / `--scrape-urls <list>` / `--crawl-url <url>` | 대상 페이지/URL 목록/크롤 루트 |
| `--webhook-url <url>` / `--webhook-events <list>` | 웹훅 대상/이벤트(`monitor.page`, `monitor.check.completed`) |
| `--email <list>` | 이메일 수신자(콤마 구분) |
| `--retention-days <n>` | 스냅샷 보존 기간 |
| `--state <state>` | `active`/`paused` (update 전용, `--status` 아님) |
| `--page-status <state>` | check 결과 필터(`same`/`new`/`changed`/`removed`/`error`) |

**핵심 주의**: 일시 중지는 `delete`가 아니라 `--state paused`(update). check 필터는 `--page-status`(전역 `--status`와 충돌 회피). 모니터 트리거 스크래프는 `maxAge`가 기본 0(매 체크 신선 스크래프). JSON-mode change tracking은 CLI 플래그로 불가 — JSON 페이로드(파일/stdin)로 `changeTracking` + `modes:["json"]` + 스키마 전달, `["json","git-diff"]`는 혼합 모드.

<a id="firecrawl-monitor---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl monitor`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-monitor/SKILL.md`

## firecrawl-parse

> 로컬 파일(PDF/DOCX/XLSX/HTML 등)을 클린 마크다운으로 변환해 디스크에 저장하는 스킬.

<a id="firecrawl-parse---용도"></a>
### 📌 용도
로컬 문서를 디스크상의 클린 마크다운으로 변환한다. 지원 포맷: **PDF, DOCX, DOC, ODT, RTF, XLSX, XLS, HTML/HTM/XHTML**. AI 요약 생성, 문서 내용 기반 질문 답변 같은 고급 옵션도 제공한다. 로컬 파일을 다룰 때는 `scrape`보다 이 스킬을 선호한다.

- 디스크에 파일이 있고(URL 아님) 그 텍스트를 마크다운으로 원할 때
- 사용자가 PDF/DOCX를 주며 내용/요약을 물을 때
- 소스가 URL이면 대신 `scrape` 사용

<a id="firecrawl-parse---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "이 PDF 파싱해줘", "이 문서 변환", "이 파일 읽어줘", "텍스트 추출", 또는 (URL이 아닌) 로컬 파일 경로가 제공될 때.
- **언제 쓰지 않는가**: 소스가 URL일 때(→ `firecrawl-scrape`).

<a id="firecrawl-parse---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
결과는 항상 `-o`로 `.firecrawl/`에 저장(파싱 문서는 수백 KB가 될 수 있어 stdout 스트리밍 시 컨텍스트 폭증). `.gitignore`에 추가.
```bash
mkdir -p .firecrawl

# 파일 → 마크다운
firecrawl parse ./paper.pdf -o .firecrawl/paper.md

# AI 요약
firecrawl parse ./paper.pdf -S -o .firecrawl/paper-summary.md

# 문서에 대한 질문
firecrawl parse ./paper.pdf -Q "What are the main conclusions?" \
  -o .firecrawl/paper-qa.md
```
이후 `head`/`grep`/`rg` 또는 증분 읽기 사용 — 통째로 로드 금지.

<a id="firecrawl-parse---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `-S, --summary` | AI 생성 요약 |
| `-Q, --query <prompt>` | 파싱 내용에 대한 질문 |
| `-o, --output <path>` | 출력 파일 경로 — **항상 사용** |
| `-f, --format <fmt>` | `markdown`(기본), `html`, `summary` |
| `--timeout <ms>` | 파싱 작업 타임아웃 |
| `--timing` | 요청 소요 시간 표시 |

**팁**: 공백 포함 경로는 따옴표(`"./My Doc.pdf"`). 최대 업로드 크기 **50 MB**/파일. 크레딧: PDF 페이지당 ~1, HTML은 1 고정. 재파싱 전 `.firecrawl/` 확인. 배치 처리 시 `firecrawl credit-usage`로 잔액 확인.

<a id="firecrawl-parse---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl parse`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-parse/SKILL.md`

## firecrawl-scrape

> 임의의 URL(JS 렌더링 SPA 포함)에서 클린 마크다운을 추출하는 스킬. WebFetch 대체.

<a id="firecrawl-scrape---용도"></a>
### 📌 용도
하나 이상의 URL을 스크래프한다. 클린한 LLM 최적화 마크다운을 반환하며, 여러 URL은 동시에 스크래프한다. 정적 페이지와 JS 렌더링 SPA를 모두 처리한다. 웹페이지 콘텐츠 추출에는 WebFetch 대신 이 스킬을 사용한다.

- 특정 URL이 있고 그 내용을 원할 때
- 페이지가 정적 또는 JS 렌더링(SPA)일 때
- 워크플로우 에스컬레이션 패턴 2단계: search → **scrape** → map → crawl → interact

<a id="firecrawl-scrape---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 사용자가 URL을 주며 내용을 원할 때, "scrape", "grab", "fetch", "pull", "get the page", "extract from this URL", "read this webpage".
- **언제 쓰지 않는가**: URL이 없어 먼저 찾아야 할 때(→ `firecrawl-search`), 클릭/폼 등 상호작용이 필요할 때(→ `firecrawl-interact`), 전체 사이트 로컬 다운로드(→ `firecrawl-download`), 로컬 파일(→ `firecrawl-parse`).

<a id="firecrawl-scrape---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 기본 마크다운 추출
firecrawl scrape "<url>" -o .firecrawl/page.md

# 본문만(nav/footer 제외)
firecrawl scrape "<url>" --only-main-content -o .firecrawl/page.md

# JS 렌더링 대기 후 스크래프
firecrawl scrape "<url>" --wait-for 3000 -o .firecrawl/page.md

# 여러 URL(각각 .firecrawl/에 저장)
firecrawl scrape https://example.com https://example.com/blog https://example.com/docs

# 마크다운 + 링크 함께
firecrawl scrape "<url>" --format markdown,links -o .firecrawl/page.json

# 페이지에 대한 질문
firecrawl scrape "https://example.com/pricing" --query "What is the enterprise plan price?"
```

<a id="firecrawl-scrape---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `-f, --format <formats>` | 출력 포맷: markdown, html, rawHtml, links, screenshot, json |
| `-Q, --query <prompt>` | 페이지 내용에 대한 질문(5 크레딧) |
| `-H` | 출력에 HTTP 헤더 포함 |
| `--only-main-content` | nav/footer/사이드바 제거, 본문만 |
| `--wait-for <ms>` | 스크래프 전 JS 렌더링 대기 |
| `--include-tags <tags>` / `--exclude-tags <tags>` | 특정 HTML 태그만/제외 |
| `--redact-pii` | 출력에서 개인식별정보 마스킹 |
| `-o, --output <path>` | 출력 파일 경로 |

**팁**: `--query`보다 일반 scrape 선호(파일로 저장 후 `grep`/`head`/직접 읽기로 전체 내용 추론 가능; `--query`는 5크레딧 추가). interact 전에 먼저 scrape 시도. 여러 URL은 동시 스크래프(`firecrawl --status`로 동시성 한도 확인). 단일 포맷은 raw, 복수 포맷은 JSON. URL은 항상 따옴표. 명명 규칙: `.firecrawl/{site}-{path}.md`.

<a id="firecrawl-scrape---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl scrape`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-scrape/SKILL.md`

## firecrawl-search

> 전체 페이지 콘텐츠 추출까지 지원하는 웹 검색 스킬. 스니펫이 아닌 실제 결과 + 풀페이지 마크다운.

<a id="firecrawl-search---용도"></a>
### 📌 용도
선택적 콘텐츠 스크래핑이 포함된 웹 검색이다. 검색 결과를 JSON으로 반환하며, 옵션으로 풀 페이지 콘텐츠를 함께 가져온다. Claude 내장 WebSearch를 넘어서는 실제 검색 결과(스니펫이 아닌 전체 마크다운)를 제공한다.

- 특정 URL이 아직 없을 때
- 페이지 발견, 질문 답변, 소스 탐색이 필요할 때
- 워크플로우 에스컬레이션 패턴 첫 단계: **search** → scrape → map → crawl → interact

<a id="firecrawl-search---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 웹 검색, 기사/주제 리서치, 조회, 최신 뉴스, 소스 발견. "search for", "find me", "look up", "what are people saying about", "find articles about".
- **언제 쓰지 않는가**: 이미 URL이 있을 때(→ `firecrawl-scrape`), 사이트 내 URL 발견(→ `firecrawl-map`), 사이트 대량 추출(→ `firecrawl-crawl`).

<a id="firecrawl-search---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 기본 검색
firecrawl search "your query" -o .firecrawl/result.json --json

# 검색 + 결과 풀페이지 스크래프
firecrawl search "your query" --scrape -o .firecrawl/scraped.json --json

# 지난 하루 뉴스
firecrawl search "your query" --sources news --tbs qdr:d -o .firecrawl/news.json --json
```

<a id="firecrawl-search---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- 사용 도구: `Bash(firecrawl *)`, `Bash(npx firecrawl *)`

| 옵션 | 설명 |
| --- | --- |
| `--limit <n>` | 최대 결과 수 |
| `--sources <web,images,news>` | 검색 소스 타입 |
| `--categories <github,research,pdf>` | 카테고리 필터 |
| `--tbs <qdr:h\|d\|w\|m\|y>` | 시간 기반 필터 |
| `--location` / `--country <code>` | 위치/국가 코드 |
| `--scrape` | 각 결과의 풀 페이지 콘텐츠도 스크래프 |
| `--scrape-formats` | 스크래프 시 포맷(기본 markdown) |
| `-o, --output <path>` / `--json` | 출력 경로 / JSON 출력 |

**팁**: `--scrape`는 풀 콘텐츠를 가져오므로 결과 URL을 재스크래프하지 말 것(크레딧 절약). 결과는 `.firecrawl/`에 저장. `jq -r '.data.web[].url'`로 URL 추출.

<a id="firecrawl-search--검색-후-피드백-1크레딧-환불"></a>
### 검색 후 피드백 (1크레딧 환불)
검색은 2크레딧. 결과를 실제로 사용/판단한 뒤 `firecrawl search-feedback <id>`로 구조화된 피드백을 보내면 검색당 첫 피드백 시 1크레딧 환불 + 검색 품질 개선에 기여. 백그라운드(`--silent &`)로 검색당 1회.

- **시간 창**: 검색 후 ~2분 이내(늦으면 거부).
- **`--missing-content`가 가장 중요**: 기대했지만 못 찾은 콘텐츠를 한 항목당 한 주제로. JSON 배열 `{topic, description?}` 선호.
- **실질 내용 필수**: `good`→`--valuable-sources` 1개 이상, `partial`→둘 중 하나, `bad`→`--missing-content` 또는 `--query-suggestions`(미충족 시 HTTP 400).
- **일일 환불 상한**: 팀·UTC일 기준 기본 100크레딧. `dailyCapReached: true`면 그날 호출 중단.
- **옵트아웃**: `FIRECRAWL_NO_SEARCH_FEEDBACK=1`(또는 `FIRECRAWL_DISABLE_SEARCH_FEEDBACK=1`)이면 조용히 스킵 — 우회 금지.

```bash
SEARCH_ID=$(jq -r '.id' .firecrawl/search-react-hooks.json)
firecrawl search-feedback "$SEARCH_ID" \
  --rating good \
  --valuable-sources '[{"url":"https://react.dev/reference/react/hooks","reason":"Most authoritative"}]' \
  --missing-content '[{"topic":"useDeferredValue","description":"No example with Suspense"}]' \
  --silent &
```

<a id="firecrawl-search---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl search`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/skills/firecrawl-search/SKILL.md`

## skill-gen

> Firecrawl로 문서 URL을 스크래핑해 완전한 Agent Skill을 자동 생성하는 슬래시 명령어.

과거 Claude 플러그인의 명령 설명이다. `skill-gen`은 [2026-11-06 Codex 업데이트](../../references/codex-skill-update-2026-11-06.md)에서 퇴역했으며 아래 예제가 현재 Codex에서 호출 가능함을 뜻하지 않는다. 새 스킬 작성은 현재 설치된 작성 도구와 [자체 제작 원본 안내](../../Owned-Skills/README.md)를 확인한다.

<a id="skill-gen---용도"></a>
### 📌 용도
임의의 라이브러리/도구/서비스 공식 문서 URL을 입력받아, 그 내용을 Firecrawl로 수집한 뒤 AI 에이전트가 사용할 수 있는 프로덕션 수준의 Agent Skill(SKILL.md + scripts/references/assets)을 처음부터 끝까지 만들어 주는 명령어다. 단순 요약이 아니라 "에이전트가 작업을 더 잘 수행하게 해 줄 비자명한 절차적 지식·도메인 세부사항·재사용 자산"을 식별해 스킬로 구조화하는 것이 목표다.

전체 흐름은 8단계로 구성된다.
1. **문서 스크래핑** — `firecrawl map`으로 관련 페이지를 발견하고, `firecrawl scrape`로 핵심 페이지(API 레퍼런스, 퀵스타트, 핵심 개념, 인증, 예제)를 가져온다. 대형 사이트는 `firecrawl crawl "<documentation-url>" --max-depth 2 --limit 15 --wait`로 수집한다. [공식 CLI 1.26.3 옵션](https://github.com/firecrawl/cli/blob/3136f724b3203c6a69bfb14d2f384271eb45822c/src/index.ts)은 `--max-depth`이며 설치 버전의 `firecrawl crawl --help`를 확인한다. 체인지로그/블로그/커뮤니티 페이지는 제외한다.
2. **스킬 범위 명확화** — 스킬 이름(kebab-case 제안), 2~3개 핵심 유스케이스(트리거 발화)를 사용자에게 1~2개 질문으로 확인.
3. **스킬 내용 설계** — 각 유스케이스를 처음부터 수행하는 방식을 분석해 재사용 리소스 유형(scripts/references/assets)을 결정.
4. **계획 승인** (필수, 파일 작성 전) — 디렉터리 트리, 각 파일 요약, SKILL.md frontmatter(name/description)를 제시하고 승인 대기.
5. **저장 위치 질문** (필수) — Project(`.claude/skills/`), Global(`~/.claude/skills/`), Custom 중 사용자 선택. 기본값 지정 금지.
6. **스킬 빌드** — 승인+위치 확정 후에만 파일 작성. 스크립트가 있으면 실행해 검증.
7. **검증** — frontmatter 체크(name kebab-case·디렉터리명 일치, description 비어있지 않음), SKILL.md 500줄 미만(`wc -l`), README/CHANGELOG 등 잡파일 없음, references 1단계 깊이. 각 항목 PASS/FAIL 보고.
8. **전달** — 빌드 요약, 줄 수 포함 디렉터리 트리, 검증 결과, 저장 위치 제시.

<a id="skill-gen---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/skill-gen <documentation-url>` 슬래시 명령어를 명시적으로 실행할 때. "이 문서로 스킬 만들어줘", "이 API 문서를 스킬화해줘" 같은 요청.
- **언제 쓰지 않는가**: 단순히 문서를 읽거나 요약만 원할 때(그건 `firecrawl-scrape`/`firecrawl-crawl`), 스킬 구조 일반론을 묻는 경우(별도 skill-creator/plugin-dev 영역).

<a id="skill-gen---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/skill-gen https://docs.stripe.com/api
/skill-gen https://docs.firecrawl.dev
```
- 인자(`$ARGUMENTS`): 문서 사이트의 시작 URL 하나. `argument-hint: <documentation-url>`.
- 내부적으로 `firecrawl map/scrape/crawl`를 호출하므로 firecrawl CLI 인증이 선행되어야 함.

<a id="skill-gen---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 도구**: `firecrawl` 스킬(map/scrape/crawl) — 문서 수집 단계에서만 사용.
- **산출물 형식 규칙(스킬 포맷 레퍼런스 내장)**:
  - frontmatter `name`(kebab-case, 최대 64자, 디렉터리명과 일치), `description`(최대 1024자, 트리거·컨텍스트 포함 — 활성화의 핵심 필드).
  - body 500줄 미만, 명령형 작성, "When to Use" 섹션은 body가 아니라 description에 둔다.
  - 리소스 유형: `scripts/`(반복 코드), `references/`(반복 참조 스키마·도메인 지식), `assets/`(반복 보일러플레이트).
  - Degrees of freedom(high/medium/low)와 progressive disclosure 패턴 3종 제공.
  - 금지: 보조 문서(README/CHANGELOG) 생성, 정보 중복, references 중첩 디렉터리.

<a id="skill-gen---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: firecrawl@claude-plugins-official
- 활성화: ON
- 관련 MCP: firecrawl은 CLI 기반(`firecrawl` 명령). 별도 MCP 서버 아님.
- 원본 유형: command (`commands/skill-gen.md`) — 슬래시 명령어
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/firecrawl/1.0.9/commands/skill-gen.md`
