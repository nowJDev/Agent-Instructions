# 스킬 카탈로그 — 한 줄 목차

> 각 스킬의 한 줄 요약 모음. 상세는 각 분류의 `README.md#<항목>`, 분류·수치·출처는 [`README.md`](README.md).
> 형식: `- **스킬명** — 요약`

엑셀·PPT 등 **하려는 작업으로 찾을 때는 [분야별 선택 안내](BY-TASK.md)**를 사용한다. 아래 전체 항목은 기존 출처별 분류로 유지한다.

2026-11-12 전수 대조로 **설명·원본 주소 294개**를 등록했다. 기존 설명 144개, 직접·시스템 보완 16개, 현재 선택 플러그인 패키지·전문 가이드 108개, 자체 제작 원본 26개다. 같은 이름의 다른 구현과 과거 배포 설명을 포함하므로 고유 실행 스킬 수가 아니다. [조사 증거](../references/skill-inventory-2026-11-12.json)는 유효 직접 패키지 244개·세션 노출 181개와 루트 SKILL이 없는 제외 후보 2개를 별도 기록한다.

---

## 기존 일반 설명 항목 (122)

이 절과 기존 OFF 절은 다른 배포 경로의 설명을 포함한다. 기존 일반 122개와 OFF 22개, 합계 144개·26그룹이며 고유 스킬 수나 현재 PC의 설치·노출 수를 뜻하지 않는다. ON/OFF는 작성 당시 Claude Code 환경의 기록이고 실제 발견·의존성 내부 스킬·명시 호출 정책의 경계는 [인덱스](README.md)를 따른다. 기존 `frontend-design`·`skill-creator`의 Codex 전역본은 2026-11-12 설치에서 `anthropic-` 이름으로 이전했으며 아래 원래 이름은 다른 배포 경로의 설명으로 유지한다. `firecrawl-cli`와 `skill-gen`도 과거 배포 설명으로 보존하며 현재 Codex의 `firecrawl` 이름과 `skill-gen` 퇴역은 [해당 안내](firecrawl/)에서 구분한다.

### _builtin (13)
- [**claude-api**](_builtin/README.md#claude-api) — Claude API / Anthropic SDK 레퍼런스 빌트인 스킬. model id·가격·파라미터·스트리밍·tool use·MCP·캐싱·토큰 카운팅·모델 마이그레이션을 다룬다. **Claude/Anthropic 관련 작업 시 파일을 열기 전에 먼저 읽는 트리거 스킬**.
- [**code-review**](_builtin/README.md#code-review) — 현재 diff를 **정확성(버그) + 재사용/단순화/효율성** 관점에서 리뷰하는 빌트인 스킬. effort 레벨로 깊이를 조절하고, PR 코멘트나 워킹트리 적용까지 가능.
- [**fewer-permission-prompts**](_builtin/README.md#fewer-permission-prompts) — 트랜스크립트에서 자주 쓴 **read-only Bash·MCP 호출**을 스캔해, 프로젝트 `settings.json`에 우선순위 allowlist를 추가함으로써 권한 프롬프트를 줄이는 빌트인 스킬.
- [**init**](_builtin/README.md#init) — 코드베이스를 분석해 **CLAUDE.md를 생성/초기화**하는 빌트인 명령.
- [**keybindings-help**](_builtin/README.md#keybindings-help) — `~/.claude/keybindings.json`을 편집해 Claude Code의 키보드 단축키를 커스터마이즈하는 빌트인 스킬.
- [**loop**](_builtin/README.md#loop) — 프롬프트나 슬래시 명령을 **주기적으로 반복 실행**하는 빌트인 스킬. 인터벌을 주면 그 간격으로, 생략하면 모델이 스스로 페이스를 정해 반복한다.
- [**review**](_builtin/README.md#review) — PR / 코드 리뷰를 수행하는 빌트인 명령.
- [**run**](_builtin/README.md#run) — 프로젝트 앱을 **실제로 띄워서** 변경이 동작하는지 확인하는 빌트인 스킬. 프로젝트 타입(CLI/server/TUI/Electron/browser/library)별 구동 패턴을 안다.
- [**schedule**](_builtin/README.md#schedule) — **cron 스케줄로 도는 클라우드 에이전트(routines)**를 생성·수정·목록·실행하는 빌트인 스킬. 1회성 예약 실행도 지원.
- [**security-review**](_builtin/README.md#security-review) — **보안 취약점 관점**에서 코드를 리뷰하는 빌트인 명령.
- [**simplify**](_builtin/README.md#simplify) — 변경된 코드를 **재사용·단순화·효율성·altitude(추상화 수준)** 관점에서 정리하고 그 수정을 직접 적용하는 빌트인 스킬. **품질 전용**이며 버그는 찾지 않는다.
- [**update-config**](_builtin/README.md#update-config) — `settings.json` / `settings.local.json`을 직접 편집해 Claude Code 하네스(harness)를 설정하는 빌트인 스킬. 권한·환경변수·hook·자동 동작을 다룬다.
- [**verify**](_builtin/README.md#verify) — 코드 변경이 **실제로 의도대로 동작하는지** 앱을 직접 실행해 동작을 관찰하며 검증하는 빌트인 스킬.

### _personal (5)
- [**claude-news**](_personal/README.md#claude-news) — Claude Code 릴리스 노트 + Anthropic 모델/제품 소식을 **한국어로 요약**하는 개인 글로벌 스킬. 새 기능과 주요 변경을 카테고리별로 정리해 보여준다.
- [**deep-research**](_personal/README.md#deep-research) — 멀티소스 웹 검색 + 소스 fetch + **교차검증(adversarial verify)** + 인용 포함 리포트 합성을 수행하는 개인 글로벌 딥리서치 스킬.
- [**design-driven-delivery**](_personal/README.md#design-driven-delivery) — 모든 요청을 읽기 전용·진단·상태 변경·모니터링으로 분류하고, 상태 변경을 설계·계획·구현·검증·리뷰·문서화·통합 순서로 통제하는 자체 제작 최상위 전달 스킬.
- [**delete-session**](_personal/README.md#delete-session) — 현재 프로젝트의 **세션 목록을 보여주고**, 선택한 세션의 `jsonl` 파일을 삭제해 resume 리스트에서 제거하는 개인 글로벌 스킬.
- [**handover**](_personal/README.md#handover) — 현재 세션 전체 내용을 **다음 세션 인수인계용 md 파일**로 정리·저장하는 개인 글로벌 스킬.

### superpowers (15)
- [**brainstorming**](superpowers/README.md#brainstorming) — 새 작업의 목적·범위와 접근법을 확인하고, 규모에 맞는 승인 설계로 정리하는 대화형 스킬.
- [**diagnosing-superpowers**](superpowers/README.md#diagnosing-superpowers) — Superpowers 세션의 반복 작업·계획 이탈·비용·실패를 대화 기록의 파일·줄 근거로 보고하는 스킬.
- [**dispatching-parallel-agents**](superpowers/README.md#dispatching-parallel-agents) — 공유 상태와 순차 의존성이 없는 독립 작업을 각각의 에이전트에게 병렬 위임하는 스킬.
- [**executing-plans**](superpowers/README.md#executing-plans) — 현재 세션에서 계획을 직접 구현하고 진행 원장과 태스크별 검증·최종 브랜치 리뷰를 유지하는 스킬.
- [**finishing-a-development-branch**](superpowers/README.md#finishing-a-development-branch) — 전체 테스트를 확인한 뒤 병합·PR·유지 중 승인된 통합을 수행하고 소유한 작업 공간을 정리하는 스킬.
- [**receiving-code-review**](superpowers/README.md#receiving-code-review) — 리뷰 피드백을 코드·요구사항·검증 근거와 대조한 뒤 항목별로 반영하거나 기술적으로 반박하는 스킬.
- [**requesting-code-review**](superpowers/README.md#requesting-code-review) — 정확한 변경 범위와 요구사항을 전달해 작업 산출물의 독립 코드 리뷰를 요청하는 스킬.
- [**subagent-driven-development**](superpowers/README.md#subagent-driven-development) — 태스크마다 새 구현자와 스펙·품질을 함께 보는 리뷰어를 배치하고 최종 전체 브랜치 리뷰를 수행하는 스킬.
- [**systematic-debugging**](superpowers/README.md#systematic-debugging) — 수정안을 내기 전에 재현·증거·패턴 비교로 근본 원인을 찾는 네 단계 디버깅 스킬.
- [**test-driven-development**](superpowers/README.md#test-driven-development) — 실패 테스트를 먼저 확인하고 최소 구현과 전체 회귀를 거쳐 동작을 보장하는 TDD 스킬.
- [**using-git-worktrees**](superpowers/README.md#using-git-worktrees) — 기존 격리를 확인하고 네이티브 도구를 우선해 작업 공간을 준비하는 스킬.
- [**using-superpowers**](superpowers/README.md#using-superpowers) — 응답과 탐색 전에 관련 스킬을 확인하고 현재 플랫폼의 도구로 적용하게 하는 진입 스킬.
- [**verification-before-completion**](superpowers/README.md#verification-before-completion) — 완료·수정·통과를 주장하기 전에 실제 검증 명령과 전체 결과를 확인하는 스킬.
- [**writing-plans**](superpowers/README.md#writing-plans) — 승인 스펙을 정확한 인터페이스·테스트·검증 결과가 있는 실행 가능한 태스크로 나누는 스킬.
- [**writing-skills**](superpowers/README.md#writing-skills) — 재사용 스킬의 설명·형태·실제 준수를 기준선과 비교해 검증하는 스킬 작성 절차.

### huggingface-skills (18)
- [**hf-cli**](huggingface-skills/README.md#hf-cli) — Hugging Face Hub의 공식 CLI 도구 `hf`로 모델·데이터셋·스페이스·버킷·repo·논문·잡(Jobs) 등을 다운로드/업로드/관리하는 스킬.
- [**huggingface-best**](huggingface-skills/README.md#huggingface-best) — 특정 작업에 가장 좋은/추천 AI 모델을 HF 공식 벤치마크 리더보드로 찾아 비교표로 제시하는 스킬.
- [**huggingface-community-evals**](huggingface-skills/README.md#huggingface-community-evals) — 로컬 하드웨어에서 inspect-ai와 lighteval로 HF Hub 모델 평가(eval)를 실행하는 스킬.
- [**huggingface-datasets**](huggingface-skills/README.md#huggingface-datasets) — Hugging Face Dataset Viewer API로 데이터셋 메타데이터·행 페이지네이션·검색·필터·parquet URL을 읽는 스킬.
- [**huggingface-gradio**](huggingface-skills/README.md#huggingface-gradio) — Python으로 Gradio 웹 UI와 ML 데모를 만드는 스킬 (Interface/Blocks/ChatInterface, 컴포넌트, 이벤트 리스너).
- [**huggingface-llm-trainer**](huggingface-skills/README.md#huggingface-llm-trainer) — TRL/Unsloth와 Hugging Face Jobs 클라우드 GPU로 언어·비전 모델을 학습/파인튜닝하는 스킬 (SFT/DPO/GRPO/Reward + GGUF 변환).
- [**huggingface-local-models**](huggingface-skills/README.md#huggingface-local-models) — llama.cpp + GGUF로 CPU/Mac Metal/CUDA/ROCm에서 모델을 로컬 실행하기 위한 모델 선택·실행 스킬.
- [**huggingface-lora-space-builder**](huggingface-skills/README.md#huggingface-lora-space-builder) — 사용자가 제공한 LoRA를 위한 Gradio 데모를 Hugging Face Spaces(ZeroGPU, 기본 private)에 빌드·발행하는 스킬.
- [**huggingface-paper-publisher**](huggingface-skills/README.md#huggingface-paper-publisher) — Hugging Face Hub에 연구 논문을 발행·관리하는 스킬 (페이지 생성, 모델/데이터셋 연결, 저자권 주장, 연구 아티클 생성).
- [**huggingface-papers**](huggingface-skills/README.md#huggingface-papers) — HF paper page를 마크다운으로 읽고, papers API로 저자·연결된 모델/데이터셋/스페이스 등 구조화 메타데이터를 조회하는 스킬.
- [**huggingface-spaces**](huggingface-skills/README.md#huggingface-spaces) — Hugging Face Spaces 앱(Gradio/Docker/Static, ZeroGPU·전용 하드웨어)을 빌드·배포·디버깅·유지보수하는 스킬.
- [**huggingface-tool-builder**](huggingface-skills/README.md#huggingface-tool-builder) — Hugging Face API 데이터를 fetch·가공·결합하는 재사용 가능한 CLI 스크립트/유틸리티를 만드는 스킬.
- [**huggingface-trackio**](huggingface-skills/README.md#huggingface-trackio) — Trackio로 ML 학습 실험의 메트릭을 로깅·시각화하고, 알림 발화·메트릭 조회까지 다루는 스킬.
- [**huggingface-vision-trainer**](huggingface-skills/README.md#huggingface-vision-trainer) — HF Transformers + HF Jobs 클라우드 GPU로 객체탐지·이미지분류·SAM/SAM2 분할 비전 모델을 학습/파인튜닝하는 스킬.
- [**huggingface-zerogpu**](huggingface-skills/README.md#huggingface-zerogpu) — Gradio Spaces의 ZeroGPU 하드웨어 코드 제약(`@spaces.GPU`, 프로세스 격리, duration/quota, CUDA 빌드)을 다루는 스킬.
- [**train-sentence-transformers**](huggingface-skills/README.md#train-sentence-transformers) — sentence-transformers 모델(SentenceTransformer/CrossEncoder/SparseEncoder)을 학습/파인튜닝하는 라우터형 스킬.
- [**transformers-js**](huggingface-skills/README.md#transformers-js) — Transformers.js로 최신 ML 모델을 JavaScript/TypeScript에서 직접 실행하는 스킬 (브라우저·Node.js·Bun·Deno, WebGPU/WASM).
- [**trl-training**](huggingface-skills/README.md#trl-training) — TRL(Transformers Reinforcement Learning) CLI 명령으로 LM을 학습/파인튜닝하는 스킬 (SFT/DPO/GRPO/KTO/RLOO/Reward).

### firecrawl (11)
- [**firecrawl-agent**](firecrawl/README.md#firecrawl-agent) — AI가 복잡한 사이트를 자율 탐색해 구조화된 JSON 데이터를 추출하는 스킬.
- [**firecrawl-cli**](firecrawl/README.md#firecrawl-cli) — Firecrawl CLI로 웹을 검색·스크래핑·상호작용하는 최상위 워크플로우 스킬. LLM에 최적화된 클린 마크다운 반환.
- [**firecrawl-crawl**](firecrawl/README.md#firecrawl-crawl) — 웹사이트 전체 또는 섹션의 여러 페이지를 링크를 따라가며 대량 추출하는 스킬.
- [**firecrawl-download**](firecrawl/README.md#firecrawl-download) — 웹사이트 전체를 로컬 파일(마크다운/스크린샷/다중 포맷)로 다운로드하는 스킬. (실험적)
- [**firecrawl-interact**](firecrawl/README.md#firecrawl-interact) — 스크래프한 페이지의 라이브 브라우저 세션을 자연어/코드로 제어하는 스킬 — 클릭, 폼 입력, 내비게이션, 로그인.
- [**firecrawl-map**](firecrawl/README.md#firecrawl-map) — 웹사이트의 모든 URL을 발견·나열하는 스킬. 검색 필터로 특정 페이지 위치 파악.
- [**firecrawl-monitor**](firecrawl/README.md#firecrawl-monitor) — 웹사이트 콘텐츠 변경을 감지해 웹훅/이메일로 알려주는 스킬 — cron·스크래퍼·diff 스크립트 불필요.
- [**firecrawl-parse**](firecrawl/README.md#firecrawl-parse) — 로컬 파일(PDF/DOCX/XLSX/HTML 등)을 클린 마크다운으로 변환해 디스크에 저장하는 스킬.
- [**firecrawl-scrape**](firecrawl/README.md#firecrawl-scrape) — 임의의 URL(JS 렌더링 SPA 포함)에서 클린 마크다운을 추출하는 스킬. WebFetch 대체.
- [**firecrawl-search**](firecrawl/README.md#firecrawl-search) — 전체 페이지 콘텐츠 추출까지 지원하는 웹 검색 스킬. 스니펫이 아닌 실제 결과 + 풀페이지 마크다운.
- [**skill-gen**](firecrawl/README.md#skill-gen) — Firecrawl로 문서 URL을 스크래핑해 완전한 Agent Skill을 자동 생성하는 슬래시 명령어.

### figma (9)
- [**figma-code-connect**](figma/README.md#figma-code-connect) — Figma 컴포넌트를 코드 스니펫에 매핑하는 Code Connect 템플릿 파일(`.figma.ts`)을 생성·유지하는 스킬.
- [**figma-create-new-file**](figma/README.md#figma-create-new-file) — 새 빈 Figma 파일(design/figjam/slides)을 생성하는 스킬. `create_new_file` 호출의 필수 선행 스킬.
- [**figma-generate-design**](figma/README.md#figma-generate-design) — 코드/설명으로부터 디자인 시스템을 재사용해 Figma에 화면·뷰·다중 섹션 레이아웃을 구축/업데이트하는 스킬.
- [**figma-generate-diagram**](figma/README.md#figma-generate-diagram) — Mermaid.js 구문으로 편집 가능한 FigJam 다이어그램을 생성하는 스킬. `generate_diagram` 호출의 필수 선행 스킬.
- [**figma-generate-library**](figma/README.md#figma-generate-library) — 코드베이스로부터 Figma에 프로페셔널급 디자인 시스템(변수/토큰, 컴포넌트 라이브러리, 테마)을 구축/업데이트하는 스킬.
- [**figma-generate-project-plan**](figma/README.md#figma-generate-project-plan) — PRD(+선택적 코드베이스 컨텍스트)를 **FigJam 프로젝트 플랜 보드**로 변환하는 인터랙티브 워크플로 스킬. 섹션 후보 제안 → 사용자 선택 → 섹션별 콘텐츠·블록 확정 → FigJam 생성까지 단계마다 확인을 거친다.
- [**figma-use-figjam**](figma/README.md#figma-use-figjam) — FigJam 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 FigJam 특화 스킬. `figma-use`와 함께 사용.
- [**figma-use-slides**](figma/README.md#figma-use-slides) — Slides 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 Slides 특화 스킬. `figma-use`와 함께 사용.
- [**figma-use**](figma/README.md#figma-use) — Figma Plugin API로 JavaScript를 실행해 노드를 생성/편집/조회하는 기반 스킬. 모든 `use_figma` 호출의 필수 선행 스킬.

### plugin-dev (8)
- [**agent-development**](plugin-dev/README.md#agent-development) — Claude Code 플러그인용 서브에이전트의 구조·시스템 프롬프트·트리거 조건 설계를 안내하는 스킬
- [**command-development**](plugin-dev/README.md#command-development) — Claude Code 슬래시 명령의 구조·YAML frontmatter·동적 인자·사용자 인터랙션 패턴을 안내하는 스킬
- [**create-plugin**](plugin-dev/README.md#create-plugin) — 컴포넌트 설계·구현·검증을 아우르는, 가이드형 엔드투엔드 Claude Code 플러그인 생성 워크플로 (슬래시 명령)
- [**hook-development**](plugin-dev/README.md#hook-development) — Claude Code 플러그인의 이벤트 기반 훅을 생성·구현하는 스킬 (프롬프트 기반 훅 API 중심)
- [**mcp-integration**](plugin-dev/README.md#mcp-integration) — Claude Code 플러그인에 Model Context Protocol(MCP) 서버를 통합해 외부 도구·서비스를 연동하는 스킬
- [**plugin-settings**](plugin-dev/README.md#plugin-settings) — `.claude/plugin-name.local.md` 패턴으로 플러그인별 설정·상태를 YAML frontmatter와 마크다운으로 저장하는 스킬
- [**plugin-structure**](plugin-dev/README.md#plugin-structure) — Claude Code 플러그인의 디렉터리 레이아웃·매니페스트·컴포넌트 구성·자동 발견을 안내하는 스킬
- [**skill-development**](plugin-dev/README.md#skill-development) — Claude Code 플러그인용 스킬의 구조·점진적 공개·작성 스타일 베스트 프랙티스를 안내하는 스킬

### chrome-devtools-mcp (6)
- [**a11y-debugging**](chrome-devtools-mcp/README.md#a11y-debugging) — Chrome DevTools MCP를 활용해 web.dev 가이드라인 기반으로 웹 페이지의 접근성(a11y)을 디버깅·감사하는 스킬
- [**chrome-devtools-cli**](chrome-devtools-mcp/README.md#chrome-devtools-cli) — 터미널에서 셸 스크립트/명령으로 Chrome DevTools를 제어해 브라우저 작업을 자동화하는 스킬
- [**chrome-devtools**](chrome-devtools-mcp/README.md#chrome-devtools) — Chrome DevTools를 MCP로 활용해 효율적으로 디버깅, 트러블슈팅, 브라우저 자동화를 수행하는 핵심 스킬
- [**debug-optimize-lcp**](chrome-devtools-mcp/README.md#debug-optimize-lcp) — Chrome DevTools MCP로 Largest Contentful Paint(LCP)를 디버깅하고 최적화하는 스킬
- [**memory-leak-debugging**](chrome-devtools-mcp/README.md#memory-leak-debugging) — JavaScript/Node.js 애플리케이션의 메모리 누수를 진단·해결하는 스킬
- [**troubleshooting**](chrome-devtools-mcp/README.md#troubleshooting) — Chrome DevTools MCP의 연결·타겟 문제를 단계별로 진단·해결하는 트러블슈팅 마법사 스킬

### ralph-loop (3)
- [**cancel-ralph**](ralph-loop/README.md#cancel-ralph) — 활성화된 Ralph 루프의 상태 파일을 제거해 루프를 취소하는 명령어.
- [**help**](ralph-loop/README.md#help) — Ralph Loop 플러그인의 개념·명령어·핵심 메커니즘을 사용자에게 설명하는 도움말 명령어.
- [**ralph-loop**](ralph-loop/README.md#ralph-loop) — 같은 프롬프트를 Stop 훅으로 반복 주입해 현재 세션 안에서 자기참조 반복 개발 루프(Ralph Wiggum 기법)를 시작하는 명령어.

### claude-md-management (2)
- [**claude-md-improver**](claude-md-management/README.md#claude-md-improver) — 저장소의 CLAUDE.md 파일들을 감사·평가하고 타겟 개선을 수행하는 스킬
- [**revise-claude-md**](claude-md-management/README.md#revise-claude-md) — 현재 세션에서 얻은 학습 내용을 CLAUDE.md에 반영해 업데이트하는 슬래시 명령

### qodo-skills (2)
- [**qodo-get-rules**](qodo-skills/README.md#qodo-get-rules) — 현재 코딩 작업에 가장 관련 있는 Qodo 코딩 규칙을, 시맨틱 검색 쿼리를 생성해 `POST /rules/search`로 가져와 심각도별로 적용하는 스킬.
- [**qodo-pr-resolver**](qodo-skills/README.md#qodo-pr-resolver) — 현재 브랜치 PR/MR의 Qodo 리뷰 이슈를 가져와 심각도별로 보여주고, 대화형/일괄로 수정한 뒤 인라인 코멘트에 답글·요약을 다는 스킬. GitHub·GitLab·Bitbucket·Azure DevOps·Gerrit 지원.

### agent-sdk-dev (1)
- [**new-sdk-app**](agent-sdk-dev/README.md#new-sdk-app) — Claude Agent SDK 애플리케이션(Python / TypeScript)을 대화형으로 새로 만들고, 최신 SDK 설치·검증까지 끝내는 슬래시 명령어.

### pr-review-toolkit (1)
- [**review-pr**](pr-review-toolkit/README.md#review-pr) — 변경된 코드(git diff)를 여러 전문 에이전트로 나눠 종합 PR 리뷰를 수행하고, 심각도별 액션 플랜으로 정리해주는 슬래시 명령어.

### feature-dev (1)
- [**feature-dev**](feature-dev/README.md#feature-dev) — 코드베이스를 깊이 이해하고, 모호한 부분을 먼저 질문하고, 여러 아키텍처를 설계한 뒤 구현하는 7단계 가이드형 기능 개발 명령어.

### claude-code-setup (1)
- [**claude-automation-recommender**](claude-code-setup/README.md#claude-automation-recommender) — 코드베이스를 분석해 맞춤형 Claude Code 자동화(훅·서브에이전트·스킬·플러그인·MCP 서버)를 추천하는 스킬

### skill-creator (1)
- [**skill-creator**](skill-creator/README.md#skill-creator) — 새 스킬을 만들고, 기존 스킬을 수정·개선하며, eval로 성능을 측정·최적화하는 메타 스킬

### frontend-design (1)
- [**frontend-design**](frontend-design/README.md#frontend-design) — 일반적인 "AI 슬롭" 미감을 피하고, 독창적이고 프로덕션급의 프론트엔드 인터페이스를 만드는 스킬

### playground (1)
- [**playground**](playground/README.md#playground) — 컨트롤·라이브 프리뷰·프롬프트 출력을 갖춘 자기완결형 단일 HTML 인터랙티브 탐색기를 만드는 스킬

### kordoc (1)
- [**kordoc**](kordoc/README.md#kordoc) — HWP·HWPX·HWPML과 한국 공문서를 읽고, 생성·채움·편집·비교·검증·미리보기하는 스킬.

### anthropic-skills (19)
- [**anthropic-academy-guide**](anthropic-skills/README.md#anthropic-academy-guide) — Claude 사용 목적에 맞는 Academy 과정·튜토리얼을 찾는 스킬.
- [**anthropic-algorithmic-art**](anthropic-skills/README.md#anthropic-algorithmic-art) — 코드와 조절 가능한 매개변수로 알고리즘 아트를 만드는 스킬.
- [**anthropic-brand-guidelines**](anthropic-skills/README.md#anthropic-brand-guidelines) — Anthropic의 브랜드 색상·타이포그래피를 적용하는 명시 호출 전용 스킬.
- [**anthropic-canvas-design**](anthropic-skills/README.md#anthropic-canvas-design) — 포스터 등 정적인 시각 작품을 제작하는 스킬.
- [**anthropic-claude-api**](anthropic-skills/README.md#anthropic-claude-api) — 공식 Claude API·SDK 원본 자료를 참고하는 명시 호출 전용 스킬.
- [**anthropic-discernment-nudge**](anthropic-skills/README.md#anthropic-discernment-nudge) — 답변의 사실·추론·누락을 점검하는 후속 질문을 제안하는 명시 호출 전용 스킬.
- [**anthropic-doc-coauthoring**](anthropic-skills/README.md#anthropic-doc-coauthoring) — 초안·구조·독자 관점 검토를 거쳐 문서를 공동 작성하는 스킬.
- [**anthropic-docx**](anthropic-skills/README.md#anthropic-docx) — Word 문서 생성·편집을 안내하는 명시 호출 전용 스킬.
- [**anthropic-frontend-design**](anthropic-skills/README.md#anthropic-frontend-design) — 의도적인 시각 방향을 가진 프런트엔드 UI를 만드는 스킬.
- [**anthropic-internal-comms**](anthropic-skills/README.md#anthropic-internal-comms) — 상태 보고·사내 공지 등 내부 커뮤니케이션 문서를 작성하는 스킬.
- [**anthropic-mcp-builder**](anthropic-skills/README.md#anthropic-mcp-builder) — 외부 서비스를 연결하는 MCP 서버를 설계·구현하는 스킬.
- [**anthropic-pdf**](anthropic-skills/README.md#anthropic-pdf) — PDF 읽기·작성·변환을 안내하는 명시 호출 전용 스킬.
- [**anthropic-pptx**](anthropic-skills/README.md#anthropic-pptx) — PowerPoint 슬라이드 생성·편집을 안내하는 명시 호출 전용 스킬.
- [**anthropic-skill-creator**](anthropic-skills/README.md#anthropic-skill-creator) — 스킬 작성·수정·평가를 안내하는 명시 호출 전용 스킬.
- [**anthropic-slack-gif-creator**](anthropic-skills/README.md#anthropic-slack-gif-creator) — Slack에 사용할 애니메이션 GIF를 만드는 스킬.
- [**anthropic-theme-factory**](anthropic-skills/README.md#anthropic-theme-factory) — 문서·슬라이드·웹 산출물에 일관된 시각 테마를 적용하는 스킬.
- [**anthropic-web-artifacts-builder**](anthropic-skills/README.md#anthropic-web-artifacts-builder) — 여러 UI 요소가 필요한 웹 산출물을 구성하는 명시 호출 전용 스킬.
- [**anthropic-webapp-testing**](anthropic-skills/README.md#anthropic-webapp-testing) — 로컬 웹 앱의 브라우저 동작과 화면을 검증하는 명시 호출 전용 스킬.
- [**anthropic-xlsx**](anthropic-skills/README.md#anthropic-xlsx) — 스프레드시트 작성·편집을 안내하는 명시 호출 전용 스킬.

### office-design-tools (3)
- [**ppt-master**](office-design-tools/README.md#ppt-master) — SVG에서 편집 가능한 PowerPoint를 만드는 명시 호출 전용 스킬.
- [**officecli**](office-design-tools/README.md#officecli) — Office 없는 DOCX·XLSX·PPTX CLI와 명시 호출 전용 연동 스킬.
- [**huashu-design**](office-design-tools/README.md#huashu-design) — HTML 기반 웹·앱·PPTX 디자인을 만드는 명시 호출 전용 스킬.

## ⛔ OFF 플러그인 (`_disabled/`, 22) — 켜야 사용

### vercel (13)
- [**_conventions**](_disabled/vercel/README.md#_conventions) — 이 플러그인의 모든 슬래시 커맨드가 따르는 일관된 구조를 정의하는 메타 문서. 사용자가 직접 호출하는 커맨드가 아님.
- [**benchmark-agents**](_disabled/vercel/README.md#benchmark-agents) — vercel-plugin의 스킬 주입을 고난도 AI 시스템 시나리오로 스트레스 테스트하는 내부 벤치마크 스킬.
- [**benchmark-e2e**](_disabled/vercel/README.md#benchmark-e2e) — vercel-plugin을 현실적 프로젝트로 돌려 스킬 주입·dev 서버 기동·검증·개선 리포트를 한 번에 생성하는 내부 E2E 벤치마크 스킬.
- [**benchmark-sandbox**](_disabled/vercel/README.md#benchmark-sandbox) — 로컬 WezTerm 대신 Vercel Sandbox(원격 microVM)에서 eval 시나리오를 돌리는 내부 벤치마크 스킬.
- [**benchmark-testing**](_disabled/vercel/README.md#benchmark-testing) — 현실적·기술명 비공개 프롬프트로 vercel-plugin 스킬 주입을 시험할 격리 테스트 프로젝트를 만드는 내부 벤치마크 스킬.
- [**bootstrap**](_disabled/vercel/README.md#bootstrap) — Vercel 연동 리소스로 저장소를 부트스트랩 — 사전 점검, 통합 프로비저닝, env 키 검증 후 db/dev 시작 명령을 안전하게 실행.
- [**deploy**](_disabled/vercel/README.md#deploy) — 현재 프로젝트를 Vercel에 배포 — 사전 안전 점검, 프로덕션 명시 확인, 배포 후 검증 포함. 인자로 "prod"/"production" 전달 시 프로덕션 배포.
- [**env**](_disabled/vercel/README.md#env) — Vercel 환경 변수 관리 — list, pull, add, remove, diff. Vercel과 로컬 개발 환경 간 env 변수 동기화. 시크릿 값은 절대 출력하지 않음.
- [**marketplace**](_disabled/vercel/README.md#marketplace) — Vercel Marketplace 통합 발견·설치 — 데이터베이스, CMS, 인증, 결제, 옵저버빌리티 등 서비스를 가이드 셋업과 로컬 검증으로 추가.
- [**plugin-audit**](_disabled/vercel/README.md#plugin-audit) — 실제 Claude Code 세션 로그를 분석해 vercel-plugin 스킬 주입 성능과 패턴 커버리지 갭을 진단하는 내부 감사 스킬.
- [**release**](_disabled/vercel/README.md#release) — vercel-plugin을 릴리스 — 게이트 실행, 버전 범프, 아티팩트 생성, 커밋, 푸시까지 처리하는 내부 릴리스 스킬.
- [**status**](_disabled/vercel/README.md#status) — 현재 Vercel 프로젝트의 상태 진단(Doctor) — 최근 배포, 링크 정보, env 개요, 도메인, 빌드 상태, 옵저버빌리티 점검. 읽기 전용.
- [**vercel-plugin-eval**](_disabled/vercel/README.md#vercel-plugin-eval) — 실제 Claude Code 세션을 띄워 vercel-plugin의 훅 발화·스킬 주입·dedup 정확성·커버리지를 검증하는 내부 eval 스킬.

### hookify (5)
- [**configure**](_disabled/hookify/README.md#configure) — 기존 hookify 규칙을 인터랙티브하게 활성/비활성 토글하는 커맨드.
- [**help**](_disabled/hookify/README.md#help) — hookify 플러그인의 동작 원리와 사용법을 설명하는 도움말 커맨드.
- [**hookify**](_disabled/hookify/README.md#hookify) — 대화 분석이나 명시적 지시로부터 원치 않는 행동을 막는 hookify 규칙을 생성하는 커맨드.
- [**list**](_disabled/hookify/README.md#list) — 프로젝트에 설정된 모든 hookify 규칙을 표와 미리보기로 나열하는 커맨드.
- [**writing-rules**](_disabled/hookify/README.md#writing-rules) — hookify 규칙 파일(`.claude/hookify.*.local.md`)의 작성 문법과 패턴을 안내하는 스킬.

### neon (2)
- [**neon-postgres-egress-optimizer**](_disabled/neon/README.md#neon-postgres-egress-optimizer) — Neon Postgres의 데이터 송신(egress) 비용/트래픽을 최적화하는 에이전트 스킬 (neon 플러그인 동봉).
- [**neon-postgres**](_disabled/neon/README.md#neon-postgres) — Neon 서버리스 Postgres 프로젝트와 데이터베이스를 관리하는 에이전트 스킬 (Neon MCP 서버와 연계).

### railway (1)
- [**use-railway**](_disabled/railway/README.md#use-railway) — Railway 인프라(계정 가입/로그인, 프로젝트·서비스·DB·버킷 생성, 배포, 환경/변수, 도메인, 장애 진단, 메트릭, 에이전트 도구 설정)를 CLI/MCP로 운영하는 스킬.

### semgrep (1)
- [**setup-semgrep-plugin**](_disabled/semgrep/README.md#setup-semgrep-plugin) — Semgrep 설치·인증·버전 호환성 확인을 통해 Semgrep 플러그인을 셋업하는 커맨드.

## 조사에서 보완한 직접 패키지 (16)

- [**firecrawl**](codex-local/README.md#user-firecrawl) — 웹 검색·페이지 읽기·크롤링·상호작용을 작업에 맞는 Firecrawl 경로로 연결한다.
- [**paseo**](codex-local/README.md#user-paseo) — Paseo의 호스트·프로젝트·작업 공간·에이전트·스케줄을 관리한다.
- [**paseo-advisor**](codex-local/README.md#user-paseo-advisor) — 현재 작업에 대한 한 에이전트의 조언과 독립 의견을 구한다.
- [**paseo-committee**](codex-local/README.md#user-paseo-committee) — 두 에이전트의 위원회로 원인과 어려운 계획을 검토한다.
- [**paseo-handoff**](codex-local/README.md#user-paseo-handoff) — 현재 작업의 문맥을 다른 에이전트에게 인계한다.
- [**paseo-help**](codex-local/README.md#user-paseo-help) — Paseo의 사용법·설정·연결·로그 문제를 설명한다.
- [**paseo-plugin**](codex-local/README.md#user-paseo-plugin) — Paseo의 신뢰된 로컬 플러그인을 제작·관리한다.
- [**source-command-delete-session**](codex-local/README.md#user-source-command-delete-session) — 현재 프로젝트의 세션 목록과 선택한 종료 세션의 제거를 다룬다.
- [**source-command-handover**](codex-local/README.md#user-source-command-handover) — 현재 세션을 다음 작업자가 이어갈 인수인계 문서로 정리한다.
- [**unity-cli**](codex-local/README.md#user-unity-cli) — CLI로 Unity Editor와 프로젝트·장면·빌드·테스트 작업을 제어한다.
- [**migrate-to-codex**](codex-local/README.md#codex-user-migrate-to-codex) — 다른 도구의 지침·스킬·에이전트·MCP 설정을 Codex 형식으로 이전한다.
- [**imagegen**](codex-local/README.md#codex-system-imagegen) — 이미지 생성·편집·참조 변형으로 비트맵 시각 자산을 만든다.
- [**openai-docs**](codex-local/README.md#codex-system-openai-docs) — Codex·OpenAI API·ChatGPT Work의 사용법과 설정 자료를 확인한다.
- [**review-agent**](codex-local/README.md#codex-system-review-agent) — 위임된 코드 변경을 읽기 전용으로 검토하고 재현 가능한 결함을 보고한다.
- [**skill-creator**](codex-local/README.md#codex-system-skill-creator) — 범위가 명확한 Codex 스킬과 필요한 지원 리소스를 작성·갱신한다.
- [**skill-installer**](codex-local/README.md#codex-system-skill-installer) — 선정된 목록이나 저장소에서 Codex 스킬을 설치한다.

## 현재 제공 플러그인 패키지·전문 가이드 (108)

### spreadsheets

- [**spreadsheets:excel-live-control**](codex-plugins/README.md#spreadsheets-excel-live-control) — 연결 세션에서 열려 있는 Microsoft Excel 통합문서를 제어한다.
- [**spreadsheets:Spreadsheets**](codex-plugins/README.md#spreadsheets-spreadsheets) — XLSX·XLS·CSV·TSV 파일과 Google Sheets 대상 스프레드시트를 작성·편집·분석한다.

### documents

- [**documents:documents**](codex-plugins/README.md#documents-documents) — DOCX·Word·Google Docs 대상 문서를 작성·편집하고 렌더링으로 확인한다.

### pdf

- [**pdf:pdf**](codex-plugins/README.md#pdf-pdf) — PDF를 읽고 작성·렌더링·검증하며 양식 작업을 지원한다.

### presentations

- [**presentations:Presentations**](codex-plugins/README.md#presentations-presentations) — 발표자료를 읽고 작성·편집하며 PPTX·Google Slides 등 출력 경로를 안내한다.

### template-creator

- [**template-creator:template-creator**](codex-plugins/README.md#template-creator-template-creator) — 개인용 산출물 템플릿을 재사용 가능한 Codex 스킬로 작성·갱신한다.

### computer-use

- [**computer-use:computer-use**](codex-plugins/README.md#computer-use-computer-use) — 사용자 컴퓨터의 Windows 앱을 화면 기반으로 조작한다.

### visualize

- [**visualize:visualize**](codex-plugins/README.md#visualize-visualize) — 대화 안에서 시각화와 상호작용 도구를 만든다.

### spotify

- [**app-68de829bf7648191acd70a907364c67c:browse-collections**](codex-plugins/README.md#spotify-browse-collections) — URI가 있는 Spotify 재생목록·앨범·팟캐스트의 내용을 조회한다.
- [**app-68de829bf7648191acd70a907364c67c:build-playlists**](codex-plugins/README.md#spotify-build-playlists) — 사용자 요청에 따라 Spotify 재생목록을 생성·편집한다.
- [**app-68de829bf7648191acd70a907364c67c:manage-library**](codex-plugins/README.md#spotify-manage-library) — Spotify 콘텐츠 저장·좋아요·팔로우 등 라이브러리를 관리한다.
- [**app-68de829bf7648191acd70a907364c67c:now-playing**](codex-plugins/README.md#spotify-now-playing) — 현재 Spotify에서 재생 중인 콘텐츠를 확인한다.
- [**app-68de829bf7648191acd70a907364c67c:search-spotify**](codex-plugins/README.md#spotify-search-spotify) — Spotify 음악·팟캐스트·오디오북을 찾고 추천한다.

### data-analytics

- [**data-analytics:analyze-data-quality**](codex-plugins/README.md#data-analytics-analyze-data-quality) — 구조화 데이터의 누락·중복·조인·최신성 등 품질 위험을 조사한다.
- [**data-analytics:answers-follow-up**](codex-plugins/README.md#data-analytics-answers-follow-up) — 분석 답변 다음에 유용한 후속 작업을 선택지로 제안한다.
- [**data-analytics:build-dashboard**](codex-plugins/README.md#data-analytics-build-dashboard) — 데이터 출처에 근거한 탐색·모니터링용 상호작용 대시보드를 만든다.
- [**data-analytics:build-report**](codex-plugins/README.md#data-analytics-build-report) — 검토 가능한 근거를 갖춘 분석 보고서를 작성한다.
- [**data-analytics:convert-to-doc**](codex-plugins/README.md#data-analytics-convert-to-doc) — 기존 Data 산출물을 DOCX·Google Docs 문서로 변환한다. 현재 세션 직접 비노출.
- [**data-analytics:convert-to-slides**](codex-plugins/README.md#data-analytics-convert-to-slides) — 기존 Data 산출물을 PowerPoint·Google Slides 발표자료로 변환한다. 현재 세션 직접 비노출.
- [**data-analytics:customize-data-plugin**](codex-plugins/README.md#data-analytics-customize-data-plugin) — 개인·팀의 데이터 작업 관례와 문맥을 재사용 스킬로 정리한다.
- [**data-analytics:design-kpis**](codex-plugins/README.md#data-analytics-design-kpis) — KPI 정의·목표·가드레일·측정 계획을 설계한다.
- [**data-analytics:index**](codex-plugins/README.md#data-analytics-index) — 데이터·지표·분석 요청을 알맞은 Data 작업 흐름으로 연결한다.
- [**data-analytics:jupyter-notebooks**](codex-plugins/README.md#data-analytics-jupyter-notebooks) — 요청한 SQL·Python 노트북을 생성·편집·검증·내보낸다.
- [**data-analytics:kpi-reporting**](codex-plugins/README.md#data-analytics-kpi-reporting) — KPI 성과·목표 대비 결과와 정기 운영 보고를 작성한다.
- [**data-analytics:market-sizing**](codex-plugins/README.md#data-analytics-market-sizing) — 가정과 불확실성을 밝혀 시장·세그먼트·기회 규모를 추정한다.
- [**data-analytics:metric-diagnostics**](codex-plugins/README.md#data-analytics-metric-diagnostics) — 지표 변화·이상·차이의 원인과 기여 요인을 진단한다.
- [**data-analytics:onboarding**](codex-plugins/README.md#data-analytics-onboarding) — Data 연결·첫 작업·사용 시작을 안내한다.
- [**data-analytics:product-business-analysis**](codex-plugins/README.md#data-analytics-product-business-analysis) — 제품·사업 의사결정에 필요한 데이터 분석을 수행한다.
- [**data-analytics:publish-artifact-to-sites**](codex-plugins/README.md#data-analytics-publish-artifact-to-sites) — 기존 Data HTML 보고서·대시보드를 Sites에 게시한다.
- [**data-analytics:report-to-pdf**](codex-plugins/README.md#data-analytics-report-to-pdf) — 기존 Data 보고서·대시보드를 PDF로 변환한다. 현재 세션 직접 비노출.
- [**data-analytics:schedule-refresh-jobs**](codex-plugins/README.md#data-analytics-schedule-refresh-jobs) — 기존 Data 산출물의 반복 갱신 클라우드 작업을 설정한다. 현재 세션 직접 비노출.
- [**data-analytics:share-artifact-summary**](codex-plugins/README.md#data-analytics-share-artifact-summary) — Data 보고서·대시보드·차트의 요약을 제공하거나 공유한다. 현재 세션 직접 비노출.
- [**data-analytics:validate-data**](codex-plugins/README.md#data-analytics-validate-data) — 분석 방법·계산·시각화·결론과 보고서 완성도를 검증한다.
- [**data-analytics:visualize-data**](codex-plugins/README.md#data-analytics-visualize-data) — 분석 산출물에 들어갈 정량 차트·그림을 제작·검증한다.

### notion

- [**notion:notion-build-my-engineering-wiki**](codex-plugins/README.md#notion-notion-build-my-engineering-wiki) — 기술 자료와 프로젝트 문맥을 Notion 엔지니어링 위키로 정리한다.
- [**notion:notion-create-my-team-handbook**](codex-plugins/README.md#notion-notion-create-my-team-handbook) — 흩어진 절차·문서를 Notion 팀 핸드북으로 구성한다.
- [**notion:notion-database-designer**](codex-plugins/README.md#notion-notion-database-designer) — 반복 업무와 메모를 Notion 데이터베이스 추적기로 설계한다.
- [**notion:notion-knowledge-capture**](codex-plugins/README.md#notion-notion-knowledge-capture) — 대화·메모를 Notion 지식 문서·FAQ·결정 기록으로 저장한다.
- [**notion:notion-meeting-prep**](codex-plugins/README.md#notion-notion-meeting-prep) — Notion 문맥과 조사 근거로 회의 안건·사전 자료를 준비한다.
- [**notion:notion-organize-my-semester**](codex-plugins/README.md#notion-notion-organize-my-semester) — 수업·과제·일정을 Notion 학기 관리 공간으로 정리한다.
- [**notion:notion-plan-marketing-campaigns**](codex-plugins/README.md#notion-notion-plan-marketing-campaigns) — 캠페인 개요·콘텐츠·제작 업무를 Notion에서 정리한다.
- [**notion:notion-research-documentation**](codex-plugins/README.md#notion-notion-research-documentation) — 여러 Notion 자료를 조사해 출처가 있는 설명·비교·보고서를 만든다.
- [**notion:notion-set-up-my-project**](codex-plugins/README.md#notion-notion-set-up-my-project) — Notion에 프로젝트 문서·업무·회의를 위한 초기 홈을 만든다.
- [**notion:notion-setup**](codex-plugins/README.md#notion-notion-setup) — Notion에서 선호·문맥을 보존하고 작업을 이어갈 초기 구성을 준비한다.
- [**notion:notion-spec-to-implementation**](codex-plugins/README.md#notion-notion-spec-to-implementation) — Notion 제품·기술 사양을 구현 계획과 연결된 업무로 바꾼다.
- [**notion:notion-weekly-project-digest**](codex-plugins/README.md#notion-notion-weekly-project-digest) — Notion 업무·결정·장애 근거를 비교해 주간 프로젝트 소식을 작성한다.

### pages

- [**pages:maintain-space**](codex-plugins/README.md#pages-maintain-space) — 새 근거를 기존 ChatGPT Pages·Space 내용에 반영해 유지한다.
- [**pages:manage-schedules**](codex-plugins/README.md#pages-manage-schedules) — Space 페이지와 예약을 검토하고 반복 자동화를 관리한다.
- [**pages:organize-space**](codex-plugins/README.md#pages-organize-space) — 기존 ChatGPT Pages·Space의 구조와 배치를 정리한다.
- [**pages:write-page**](codex-plugins/README.md#pages-write-page) — 요청한 ChatGPT Page·Space 내용을 작성·편집한다.

### sites

- [**sites:sites**](codex-plugins/README.md#sites-sites) — 랜딩 페이지·대시보드·포털·내부 도구 등 웹사이트를 제작·수정한다.
- [**sites:sites-remix**](codex-plugins/README.md#sites-sites-remix) — 지정된 기존 Sites 사이트를 바탕으로 새 사이트를 만든다.

### work-pets

- [**work-pets:create-pet**](codex-plugins/README.md#work-pets-create-pet) — ChatGPT Work용 애니메이션 펫을 제작·검증·미리보기·업로드한다.
- [**work-pets:pets**](codex-plugins/README.md#work-pets-pets) — ChatGPT Work의 애니메이션 펫을 조회·선택·다운로드·삭제한다.
- [**work-pets:update-pet**](codex-plugins/README.md#work-pets-update-pet) — ChatGPT Work 펫의 이름·설명·스프라이트 등 기존 구성을 갱신한다.

### investment-banking

- [**investment-banking:buyer-investor-list**](codex-plugins/README.md#investment-banking-buyer-investor-list) — 매수자·투자자·스폰서·대출자 후보를 근거에 따라 분류·우선순위화한다. 현재 세션 직접 비노출.
- [**investment-banking:capital-markets-issuance**](codex-plugins/README.md#investment-banking-capital-markets-issuance) — 증자·채권·차환·자금 조달과 발행 대안을 분석한다. 현재 세션 직접 비노출.
- [**investment-banking:cim-builder**](codex-plugins/README.md#investment-banking-cim-builder) — 거래 마케팅용 CIM·티저·경영진 발표 서사를 작성한다. 현재 세션 직접 비노출.
- [**investment-banking:cim-teardown**](codex-plugins/README.md#investment-banking-cim-teardown) — CIM·티저·실사 자료의 주장과 근거를 검토한다. 현재 세션 직접 비노출.
- [**investment-banking:company-tearsheet**](codex-plugins/README.md#investment-banking-company-tearsheet) — 기업의 신원·사업·재무·시장 사실을 출처와 함께 요약한다. 현재 세션 직접 비노출.
- [**investment-banking:comps-valuation**](codex-plugins/README.md#investment-banking-comps-valuation) — 비교 기업·거래와 배수에 근거한 가치평가를 수행한다. 현재 세션 직접 비노출.
- [**investment-banking:covenant-package-analyzer**](codex-plugins/README.md#investment-banking-covenant-package-analyzer) — 채무약정 정의·제약·여유·변경 가능성을 분석한다. 현재 세션 직접 비노출.
- [**investment-banking:dcf-model-builder**](codex-plugins/README.md#investment-banking-dcf-model-builder) — 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다. 현재 세션 직접 비노출.
- [**investment-banking:deal-process-tracker**](codex-plugins/README.md#investment-banking-deal-process-tracker) — NDA·입찰·실사·마감 등 거래 진행 상태를 추적한다. 현재 세션 직접 비노출.
- [**investment-banking:distressed-recovery-waterfall**](codex-plugins/README.md#investment-banking-distressed-recovery-waterfall) — 부실 자본구조·채권자 순위·회수금 배분을 분석한다. 현재 세션 직접 비노출.
- [**investment-banking:financials-normalizer**](codex-plugins/README.md#investment-banking-financials-normalizer) — 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다. 현재 세션 직접 비노출.
- [**investment-banking:ib-deck-qc**](codex-plugins/README.md#investment-banking-ib-deck-qc) — 거래 자문 발표자료의 출처·모델·일관성과 배포 준비 상태를 점검한다. 현재 세션 직접 비노출.
- [**investment-banking:investment-banking**](codex-plugins/README.md#investment-banking-investment-banking) — 거래·자금 조달·실사·가치평가 등 투자은행 작업을 전문 스킬로 연결한다.
- [**investment-banking:lbo-model-build**](codex-plugins/README.md#investment-banking-lbo-model-build) — 인수 자금 조달·차입·수익률·회수 민감도를 포함한 LBO 모델을 작성한다. 현재 세션 직접 비노출.
- [**investment-banking:meeting-prep**](codex-plugins/README.md#investment-banking-meeting-prep) — 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다. 현재 세션 직접 비노출.
- [**investment-banking:memo-builder**](codex-plugins/README.md#investment-banking-memo-builder) — 분석 담당 스킬의 결과를 의사결정 메모로 종합한다. 현재 세션 직접 비노출.
- [**investment-banking:merger-model-builder**](codex-plugins/README.md#investment-banking-merger-model-builder) — 합병의 주당이익·구매회계·시너지·교환비율과 통합 재무를 모델링한다. 현재 세션 직접 비노출.
- [**investment-banking:model-audit-tieout**](codex-plugins/README.md#investment-banking-model-audit-tieout) — 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다. 현재 세션 직접 비노출.
- [**investment-banking:pitch-deck-builder**](codex-plugins/README.md#investment-banking-pitch-deck-builder) — 거래·이사회·위원회용 피치덱의 이야기·페이지 계획·근거를 구성한다. 현재 세션 직접 비노출.
- [**investment-banking:private-credit-underwriting**](codex-plugins/README.md#investment-banking-private-credit-underwriting) — 차입자 신용·담보·부채 수용력·하방 시나리오를 심사한다. 현재 세션 직접 비노출.
- [**investment-banking:scenario-sensitivity-generator**](codex-plugins/README.md#investment-banking-scenario-sensitivity-generator) — 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다. 현재 세션 직접 비노출.
- [**investment-banking:three-statement-model-builder**](codex-plugins/README.md#investment-banking-three-statement-model-builder) — 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다. 현재 세션 직접 비노출.
- [**investment-banking:user-context**](codex-plugins/README.md#investment-banking-user-context) — 해당 금융 플러그인의 저장 선호·자료 설정·문맥을 관리한다. 현재 세션 직접 비노출.

### public-equity-investing

- [**public-equity-investing:catalyst-calendar**](codex-plugins/README.md#public-equity-investing-catalyst-calendar) — 주가 촉매의 일정·확인 상태·투자 영향을 관리한다. 현재 세션 직접 비노출.
- [**public-equity-investing:company-tearsheet**](codex-plugins/README.md#public-equity-investing-company-tearsheet) — 기업의 신원·사업·재무·시장 사실을 출처와 함께 요약한다. 현재 세션 직접 비노출.
- [**public-equity-investing:comps-valuation**](codex-plugins/README.md#public-equity-investing-comps-valuation) — 비교 기업·거래와 배수에 근거한 가치평가를 수행한다. 현재 세션 직접 비노출.
- [**public-equity-investing:dcf-model-builder**](codex-plugins/README.md#public-equity-investing-dcf-model-builder) — 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다. 현재 세션 직접 비노출.
- [**public-equity-investing:deck-report-qc**](codex-plugins/README.md#public-equity-investing-deck-report-qc) — 투자 발표자료·보고서의 출처·모델·글쓰기 일관성을 점검한다. 현재 세션 직접 비노출.
- [**public-equity-investing:earnings-deep-dive**](codex-plugins/README.md#public-equity-investing-earnings-deep-dive) — 발표 실적·가이던스·경영진 발언이 투자 논지에 미치는 영향을 분석한다. 현재 세션 직접 비노출.
- [**public-equity-investing:earnings-preview**](codex-plugins/README.md#public-equity-investing-earnings-preview) — 실적 발표 전 기대·컨센서스·지표·시나리오를 정리한다. 현재 세션 직접 비노출.
- [**public-equity-investing:economic-impact-report**](codex-plugins/README.md#public-equity-investing-economic-impact-report) — 거시·정책·원자재·금리·환율 변화의 상장주식 영향을 분석한다. 현재 세션 직접 비노출.
- [**public-equity-investing:equity-model-update**](codex-plugins/README.md#public-equity-investing-equity-model-update) — 기존 주식 투자 모델의 실적·가이던스·가정·수식을 갱신한다. 현재 세션 직접 비노출.
- [**public-equity-investing:event-driven-analyzer**](codex-plugins/README.md#public-equity-investing-event-driven-analyzer) — 합병·규제·특수 상황의 확률·보상·시기·하방을 평가한다. 현재 세션 직접 비노출.
- [**public-equity-investing:financials-normalizer**](codex-plugins/README.md#public-equity-investing-financials-normalizer) — 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다. 현재 세션 직접 비노출.
- [**public-equity-investing:idea-generation**](codex-plugins/README.md#public-equity-investing-idea-generation) — 투자 유니버스·테마·관심 종목에서 조사 후보를 발굴한다. 현재 세션 직접 비노출.
- [**public-equity-investing:initiating-coverage**](codex-plugins/README.md#public-equity-investing-initiating-coverage) — 투자 논지·위험·목표주가·가치평가를 갖춘 최초 분석 보고서를 작성한다. 현재 세션 직접 비노출.
- [**public-equity-investing:long-short-pitch**](codex-plugins/README.md#public-equity-investing-long-short-pitch) — 롱·숏·페어 투자 논지와 촉매·위험·진입·청산 조건을 구성한다. 현재 세션 직접 비노출.
- [**public-equity-investing:meeting-prep**](codex-plugins/README.md#public-equity-investing-meeting-prep) — 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다. 현재 세션 직접 비노출.
- [**public-equity-investing:memo-builder**](codex-plugins/README.md#public-equity-investing-memo-builder) — 분석 담당 스킬의 결과를 의사결정 메모로 종합한다. 현재 세션 직접 비노출.
- [**public-equity-investing:model-audit-tieout**](codex-plugins/README.md#public-equity-investing-model-audit-tieout) — 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다. 현재 세션 직접 비노출.
- [**public-equity-investing:portfolio-risk-management**](codex-plugins/README.md#public-equity-investing-portfolio-risk-management) — 포지션 크기·추가·축소·헤지·위험 예산과 운용 조치를 분석한다. 현재 세션 직접 비노출.
- [**public-equity-investing:public-equity-investing**](codex-plugins/README.md#public-equity-investing-public-equity-investing) — 상장주식의 기업·실적·가치평가·포트폴리오 작업을 전문 스킬로 연결한다.
- [**public-equity-investing:scenario-sensitivity-generator**](codex-plugins/README.md#public-equity-investing-scenario-sensitivity-generator) — 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다. 현재 세션 직접 비노출.
- [**public-equity-investing:thesis-tracker**](codex-plugins/README.md#public-equity-investing-thesis-tracker) — 투자 논지·촉매·반증 조건과 검토 주기를 추적한다. 현재 세션 직접 비노출.
- [**public-equity-investing:three-statement-model-builder**](codex-plugins/README.md#public-equity-investing-three-statement-model-builder) — 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다. 현재 세션 직접 비노출.
- [**public-equity-investing:user-context**](codex-plugins/README.md#public-equity-investing-user-context) — 해당 금융 플러그인의 저장 선호·자료 설정·문맥을 관리한다. 현재 세션 직접 비노출.

### plugin-management

- [**plugin-management:plugin-management**](codex-plugins/README.md#plugin-management-plugin-management) — 관련 플러그인을 찾고 권한·의존성·연결·제거를 관리한다.

### ponytail

- [**ponytail:ponytail**](codex-plugins/README.md#ponytail-ponytail) — 요청을 완결하는 최소 변경과 간결한 보고 원칙을 적용한다.
- [**ponytail:ponytail-audit**](codex-plugins/README.md#ponytail-ponytail-audit) — 저장소 전체의 결함·보안·부하·테스트·불필요한 코드를 감사한다.
- [**ponytail:ponytail-debt**](codex-plugins/README.md#ponytail-ponytail-debt) — shortcut·ponytail 주석을 찾아 기술 부채 목록으로 보여준다.
- [**ponytail:ponytail-gain**](codex-plugins/README.md#ponytail-ponytail-gain) — Ponytail 벤치마크에 기록된 코드·비용·속도 절감 결과를 보여준다.
- [**ponytail:ponytail-help**](codex-plugins/README.md#ponytail-ponytail-help) — Ponytail 수준·스킬·명령의 사용법을 안내한다.
- [**ponytail:ponytail-review**](codex-plugins/README.md#ponytail-ponytail-review) — 코드 변경의 정확성·안전·부하·테스트·필요성을 검토한다.

## 자체 제작 실행 원본 (26)

동명 내장·플러그인 설명과 별도로 보존하는 자체 제작 원본이다. 실행 기능·권한의 자동 제공을 뜻하지 않는다.

- [**cancel-ralph · 자체 제작**](../Owned-Skills/cancel-ralph/SKILL.md) — 사용자가 요청한 현재 Ralph 반복 작업을 취소한다.
- [**claude-api · 자체 제작**](../Owned-Skills/claude-api/SKILL.md) — Claude API·SDK·Agent SDK의 구현과 공식 사용 조건을 확인한다.
- [**claude-news · 자체 제작**](../Owned-Skills/claude-news/SKILL.md) — Claude Code 릴리스와 Anthropic 제품의 최근 변경을 확인한다.
- [**code-review · 자체 제작**](../Owned-Skills/code-review/SKILL.md) — 코드 변경의 정확성·상태·실패 경로·보안과 검증 근거를 검토한다.
- [**coplay-funplay-unity-mcp-setup · 자체 제작**](../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md) — Coplay·Funplay Unity MCP의 설치·초기 연결·재연결을 수행한다.
- [**daily-work-report · 자체 제작**](../Owned-Skills/daily-work-report/SKILL.md) — 지정한 로컬 자료와 업무명·템플릿을 근거로 한국어 일일 업무보고를 작성한다.
- [**deep-research · 자체 제작**](../Owned-Skills/deep-research/SKILL.md) — 여러 소스를 비교·교차 검증하고 출처·불확실성을 포함해 조사한다.
- [**delete-session · 자체 제작**](../Owned-Skills/delete-session/SKILL.md) — 현재 프로젝트의 세션 목록을 확인하고 승인된 종료 세션을 보관·제거한다.
- [**design-driven-delivery · 자체 제작**](../Owned-Skills/design-driven-delivery/SKILL.md) — 요청을 분류하고 상태 변경을 설계부터 검증·통합까지 조율한다.
- [**feature-dev · 자체 제작**](../Owned-Skills/feature-dev/SKILL.md) — 기존 코드베이스의 기능을 조사·설계·구현하고 실제 동작을 검증한다.
- [**fewer-permission-prompts · 자체 제작**](../Owned-Skills/fewer-permission-prompts/SKILL.md) — 반복되는 읽기 전용 승인에서 좁은 허용 규칙 후보를 찾는다.
- [**figma-generate-project-plan · 자체 제작**](../Owned-Skills/figma-generate-project-plan/SKILL.md) — PRD를 FigJam 프로젝트 계획으로 정리하고 실제 도구 조건에 맞춰 반영한다.
- [**handover · 자체 제작**](../Owned-Skills/handover/SKILL.md) — 다음 세션이 작업을 이어갈 수 있도록 근거와 재개 방법을 문서로 남긴다.
- [**help · 자체 제작**](../Owned-Skills/help/SKILL.md) — Ralph Loop의 개념·옵션·완료 신호와 취소 방법을 설명한다.
- [**init · 자체 제작**](../Owned-Skills/init/SKILL.md) — 코드베이스를 근거로 프로젝트 AGENTS.md·CLAUDE.md 초기 지침을 작성한다.
- [**keybindings-help · 자체 제작**](../Owned-Skills/keybindings-help/SKILL.md) — Claude Code 터미널 단축키 재할당·해제·설정 오류를 다룬다.
- [**loop · 자체 제작**](../Owned-Skills/loop/SKILL.md) — 현재 세션에서 승인된 작업이나 상태 조회를 일정 간격으로 반복한다.
- [**new-sdk-app · 자체 제작**](../Owned-Skills/new-sdk-app/SKILL.md) — Python 또는 TypeScript의 Claude Agent SDK 앱을 준비하고 실행을 검증한다.
- [**ralph-loop · 자체 제작**](../Owned-Skills/ralph-loop/SKILL.md) — 명시적으로 요청한 Ralph 방식의 검증 가능한 개발 작업을 제한된 세션에서 반복한다.
- [**review · 자체 제작**](../Owned-Skills/review/SKILL.md) — 검토 대상을 정하고 코드·PR 리뷰의 적절한 절차로 연결한다.
- [**review-pr · 자체 제작**](../Owned-Skills/review-pr/SKILL.md) — PR의 테스트·오류 처리·주석·타입 등 여러 관점을 종합 검토한다.
- [**run · 자체 제작**](../Owned-Skills/run/SKILL.md) — 프로젝트의 앱·CLI·서버를 실제 실행하고 준비 상태를 확인한다.
- [**security-review · 자체 제작**](../Owned-Skills/security-review/SKILL.md) — 실제 공격 경로와 증거를 바탕으로 보안 문제를 조사한다.
- [**simplify · 자체 제작**](../Owned-Skills/simplify/SKILL.md) — 기존 동작·오류·부작용을 보존하며 요청한 코드를 단순화한다.
- [**update-config · 자체 제작**](../Owned-Skills/update-config/SKILL.md) — 지정한 클라이언트의 환경·권한·hook·동작 설정을 변경하거나 진단한다.
- [**verify · 자체 제작**](../Owned-Skills/verify/SKILL.md) — 변경 기능의 정상·실패 사용자 흐름과 실제 실행 증거를 확인한다.
