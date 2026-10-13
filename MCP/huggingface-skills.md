# huggingface-skills

> Hugging Face Hub 공식 원격 MCP 서버. OAuth 로그인을 거쳐 HF 생태계(모델·데이터셋·Spaces·Jobs 등) 작업을 연동한다.

## 📌 용도
Hugging Face의 공식 HTTP MCP 서버(`https://huggingface.co/mcp?login`)에 연결해 Hub 검색·문서 조회와 계정에서 선택한 Jobs·Spaces 등의 도구를 사용한다. OAuth는 클라이언트의 인증 절차로 진행하며 인증 화면이나 래퍼에서 보이는 항목을 서버의 전체 도구 목록으로 해석하지 않는다. `huggingface-skills`는 작업 절차를 안내하는 별도 스킬군이며 MCP 서버 연결의 필수 조건은 아니다.

## 🎯 트리거 조건 / 사용 맥락
- "hf", "huggingface", "Hugging Face", "허깅페이스" 언급
- 특정 작업에 쓸 최적 모델 추천/비교, 모델·데이터셋 다운로드/업로드
- HF Spaces(Gradio/Docker/Static, ZeroGPU) 앱 생성·배포·디버깅
- HF Jobs 클라우드 GPU로 학습/파인튜닝, 논문 조회 등
- 위 작업 전 HF 계정 연동이 필요할 때.

## 🛠️ 제공 도구 목록

| 대표 도구명 | 기능 | 주요 파라미터 |
|--------|------|----------------|
| hf_fs | Hub 리소스 탐색과 문서·Spaces 검색 등 | 설치·계정별 런타임 스키마 확인 |

[공식 서버 안내](https://huggingface.co/docs/hub/agents-mcp)를 참고한다. 추가 도구는 계정의 MCP 설정·선택한 Spaces와 클라이언트에 따라 달라진다. 실제 도구와 인자는 클라이언트의 도구 목록 또는 MCP `tools/list`에서 확인하며, 스킬이 없어도 노출된 도구를 직접 사용할 수 있다.

주요 스킬: `hf-cli`(Hub CLI 전반), `huggingface-best`(모델 추천), `huggingface-datasets`(데이터셋 뷰어 API), `huggingface-spaces`/`huggingface-zerogpu`(Spaces·ZeroGPU), `huggingface-llm-trainer`/`trl-training`(학습), `huggingface-papers`/`huggingface-paper-publisher`(논문) 등. 이 스킬들이 쓰는 CLI·API는 각자 필요한 인증을 확인하며 MCP OAuth 완료만으로 CLI 로그인까지 완료됐다고 보지 않는다.

## 💻 사용 예시

**예시 1 — 최초 연동**
1. [계정의 MCP 설정](https://huggingface.co/settings/mcp)에서 대상 클라이언트의 연결 안내를 확인한다.
2. 클라이언트의 OAuth 안내로 사용자가 Hugging Face 로그인·권한 승인을 진행한다.
3. 연결 완료 후 실제 도구 목록과 스키마를 확인한다.

**예시 2 — 작업용 모델 추천**
- 현재 노출된 Hub 검색 도구로 후보를 조회한다. `huggingface-skills:huggingface-best` 스킬이 설치돼 있으면 해당 절차로 작업별 벤치마크를 확인한다.

## 📦 출처 / 설치 상태
- 제공: **플러그인** `huggingface-skills@claude-plugins-official`
- 활성화: ON (`settings.json` → `enabledPlugins["huggingface-skills@claude-plugins-official"]: true`)
- 연결 방식: **http** — `https://huggingface.co/mcp?login` (원격 서버, OAuth 로그인 필요)
- 캐시에 여러 버전 공존: `huggingface-skills\1.0.3 / 1.0.4 / 1.0.5 / 1.0.8\.mcp.json` (현재 최신 1.0.8 기준 동일 URL)
- 설정/캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/.mcp.json`
- 세션 내 도구 식별자 접두사: `mcp__plugin_huggingface-skills_huggingface-skills__`
