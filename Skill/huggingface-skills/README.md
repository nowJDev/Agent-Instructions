<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# huggingface-skills 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. 활성 표시는 작성 당시 환경의 기록이다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [hf-cli](#hf-cli).
- [huggingface-best](#huggingface-best).
- [huggingface-community-evals](#huggingface-community-evals).
- [huggingface-datasets](#huggingface-datasets).
- [huggingface-gradio](#huggingface-gradio).
- [huggingface-llm-trainer](#huggingface-llm-trainer).
- [huggingface-local-models](#huggingface-local-models).
- [huggingface-lora-space-builder](#huggingface-lora-space-builder).
- [huggingface-paper-publisher](#huggingface-paper-publisher).
- [huggingface-papers](#huggingface-papers).
- [huggingface-spaces](#huggingface-spaces).
- [huggingface-tool-builder](#huggingface-tool-builder).
- [huggingface-trackio](#huggingface-trackio).
- [huggingface-vision-trainer](#huggingface-vision-trainer).
- [huggingface-zerogpu](#huggingface-zerogpu).
- [train-sentence-transformers](#train-sentence-transformers).
- [transformers-js](#transformers-js).
- [trl-training](#trl-training).

## hf-cli

> Hugging Face Hub의 공식 CLI 도구 `hf`로 모델·데이터셋·스페이스·버킷·repo·논문·잡(Jobs) 등을 다운로드/업로드/관리하는 스킬.

<a id="hf-cli---용도"></a>
### 📌 용도
Hugging Face Hub와 상호작용하는 통합 명령줄 도구 `hf`의 사용을 담당한다. 인증, 로컬 캐시 관리, 버킷(클라우드 스토리지) 관리, HF 인프라에서의 잡 실행/스케줄링, repo·discussion·PR 관리, 모델/데이터셋/스페이스 탐색, 학술 논문 읽기/검색, 컬렉션 관리, 데이터셋 SQL 쿼리, 스페이스 설정, 웹훅 설정, Inference Endpoint 배포/관리까지 폭넓게 커버한다. 이 도구는 deprecated된 `huggingface-cli`를 대체한다. 학습 체크포인트, 데이터 파이프라인, 에이전트 트레이스 같은 클라우드 스토리지 작업에도 사용된다. 사용자가 명시적으로 CLI 명령을 요구하지 않아도 HF 생태계나 AI/ML 관련 작업이면 사용된다.

<a id="hf-cli---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 사용자가 'hf', 'huggingface', 'Hugging Face', 'huggingface-cli', 'hugging face cli'를 언급할 때. 모델/데이터셋/스페이스 다운로드·업로드, 인증(로그인/whoami), 캐시 관리, 버킷 생성/동기화, HF Jobs 실행·스케줄, repo/discussion/PR 관리, 논문 검색·읽기, 컬렉션 관리, 데이터셋 쿼리, 스페이스 구성, 웹훅, Inference Endpoint 배포 등 HF 생태계 전반 또는 AI/ML 일반 작업.
- **언제 쓰지 않는가**: 명령어 자체보다 더 전문화된 다른 스킬(예: 학습은 huggingface-llm-trainer, 데이터셋 뷰어 API는 huggingface-datasets, 모델 추천은 huggingface-best)이 직접 다루는 작업은 그 스킬로 위임. 단 CLI 명령 실행 자체는 본 스킬.

<a id="hf-cli---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 설치
curl -LsSf https://hf.co/cli/install.sh | bash -s

# 인증
hf auth login                 # 토큰으로 로그인
hf auth whoami                # 현재 로그인 계정 확인

# 다운로드 / 업로드
hf download org/model --type model --include "*.safetensors"
hf upload org/model ./local --commit-message "add weights"
hf upload-large-folder org/model ./big --type model   # 재개 가능 업로드

# 잡 실행
hf jobs run IMAGE COMMAND --flavor a10g-small --timeout 1h
hf jobs uv run script.py --flavor t4-small            # UV 스크립트 실행
hf jobs scheduled run "0 * * * *" IMAGE COMMAND       # cron 스케줄

# 데이터셋 SQL
hf datasets sql "SELECT * FROM 'https://...parquet' LIMIT 10"

# 리포 마운트 (별도 도구 hf-mount)
hf-mount start repo openai-community/gpt2 /tmp/gpt2
```

<a id="hf-cli---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
주요 서브커맨드 그룹:
- **최상위**: `cp`, `download`, `env`, `sync`, `update`, `upload`, `upload-large-folder`, `version`
- **`hf auth`**: list, login, logout, switch, token, whoami
- **`hf buckets`**: cp, create, delete, info, list, move, remove, sync (클라우드 스토리지, `--region [us|eu]`)
- **`hf cache`**: list, prune, rm, verify
- **`hf collections`**: create/add-item/update/delete 등
- **`hf datasets`**: card, info, leaderboard, list, parquet, sql
- **`hf discussions`**: close, comment, create, diff, info, list, merge, rename, reopen
- **`hf endpoints`**: catalog deploy/list, deploy, describe, list, pause, resume, scale-to-zero, update, delete
- **`hf extensions`**: exec, install, list, remove, search
- **`hf jobs`**: cancel, hardware, inspect, labels, logs, ps, run, stats, uv run, `scheduled` 서브그룹
- **`hf models`**: card, info, list
- **`hf papers`**: info, list, read, search
- **`hf repos`**: branch, cp, create, delete, delete-files, duplicate, list, move, settings, tag
- **`hf skills`**: add, list, preview, update
- **`hf spaces`**: card, dev-mode, hardware, hot-reload, info, list, logs, pause, restart, search, secrets, settings, ssh, variables, volumes
- **`hf webhooks`**: create, delete, disable, enable, info, list, update

공통 옵션: `--format [auto|human|agent|json|quiet]`(또는 `--json`), `-q/--quiet`, `--revision`, `--token`(가급적 `HF_TOKEN` 환경변수 권장), `--type [model|dataset|space]`.

Jobs/Spaces 하드웨어 플레이버: `cpu-basic`, `t4-small`, `a10g-small`, `a100-large`, `h200`, `rtx-pro-6000` 등.

<a id="hf-cli---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/hf-cli/SKILL.md`

## huggingface-best

> 특정 작업에 가장 좋은/추천 AI 모델을 HF 공식 벤치마크 리더보드로 찾아 비교표로 제시하는 스킬.

<a id="huggingface-best---용도"></a>
### 📌 용도
사용자의 작업(코딩, 수학/추론, 채팅, OCR, RAG/검색, 음성 인식, 이미지 분류, 멀티모달, 에이전트 등)과 디바이스 제약을 파싱하여, Hugging Face의 공식 벤치마크 리더보드를 조회한다. 모델 크기 데이터로 결과를 보강하고, 사용자의 디바이스에 맞는 모델만 필터링한 뒤 벤치마크 점수가 포함된 비교표를 반환한다. 디바이스가 명시되지 않으면 크기 필터링을 생략하고 최고 성능 모델을 반환한다. 모델 추천이나 비교가 필요할 때, 사용자가 HuggingFace나 벤치마크를 명시하지 않아도 항상 사용한다.

<a id="huggingface-best---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "best model for X", "what model should I use for", "top models for [task]", "which model runs on my laptop/machine/device", "recommend a model for", "what LLM should I use for", "compare models for", "what's state of the art for" 등 특정 용도의 AI 모델 선택/비교 질문. HuggingFace나 벤치마크를 명시하지 않아도 트리거됨.
- **언제 쓰지 않는가**: 모델 선택/추천/비교가 아닌, 이미 정해진 모델의 학습·배포·실행 작업(해당 전용 스킬 사용).

<a id="huggingface-best---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# Step 2: 공식 벤치마크 데이터셋 목록 조회
curl -s -H "Authorization: Bearer $(cat ~/.cache/huggingface/token)" \
  "https://huggingface.co/api/datasets?filter=benchmark:official&limit=500" \
  | jq '[.[] | {id, tags, description}]'

# Step 3: 리더보드에서 상위 모델 가져오기
curl -s -H "Authorization: Bearer $(cat ~/.cache/huggingface/token)" \
  "https://huggingface.co/api/datasets/<namespace>/<repo>/leaderboard" \
  | jq '[.[:15] | .[] | {rank, modelId, value, verified}]'

# Step 4: 모델 메타데이터 보강
hf models info org/model1 --json | jq '{safetensors, tags, cardData}'
```

디바이스 → 파라미터 예산 변환:
- fp16 최대 파라미터(B) ≈ 메모리(GB) ÷ 2
- Q4 최대 파라미터(B) ≈ 메모리(GB) × 2
- 예: 16GB → 8B fp16 / 32B Q4, 24GB VRAM → 12B fp16 / 48B Q4

<a id="huggingface-best---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
6단계 워크플로우: (1) 요청 파싱(task/device) → (2) 관련 공식 벤치마크 데이터셋 선택 → (3) 리더보드 상위 모델 수집 → (4) `safetensors.total`로 파라미터·라이선스 보강 → (5) 디바이스 예산 기준 필터·랭킹 → (6) 비교표 출력.

출력 비교표 컬럼: `# / Model(링크) / Params / [Benchmark...] / License / On device`. On device 값은 `Yes (fp16)`, `Q4 only`, `Too large`, `API only`. 최상위 추천은 ⭐ 표시. 평가 안 된 벤치마크는 `—`.

에러 처리: 리더보드 404/401 → 스킵 후 표기, `safetensors` 없으면 모델명에서 크기 파싱(7b/13b/70b 등), 벤치마크 미발견 시 `hub_repo_search`로 트렌딩/인기 기반 폴백.

후속: 표 제시 후 "Run locally" 또는 "Run on HF Jobs" 안내.

<a id="huggingface-best---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-best/SKILL.md`

## huggingface-community-evals

> 로컬 하드웨어에서 inspect-ai와 lighteval로 HF Hub 모델 평가(eval)를 실행하는 스킬.

<a id="huggingface-community-evals---용도"></a>
### 📌 용도
Hugging Face Hub의 모델을 로컬 하드웨어에서 평가(evaluation)하는 작업을 담당한다. `inspect-ai`와 `lighteval` 두 평가 프레임워크를 로컬 추론으로 실행하며, 백엔드로 `vllm` / Hugging Face Transformers / `accelerate` 중 어떤 것을 쓸지 선택하도록 돕는다. 스모크 테스트(소량 샘플로 빠른 검증), 태스크 선택, 백엔드 폴백 전략을 포함한다. HF Jobs 오케스트레이션, model-card PR, `.eval_results` 발행, community-evals 자동화는 다루지 않는다.

<a id="huggingface-community-evals---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: HF Hub 모델을 로컬 GPU/하드웨어에서 평가할 때. 백엔드 선택(vLLM vs Transformers vs accelerate), inspect-ai 또는 lighteval 사용, 로컬 GPU eval 실행.
- **언제 쓰지 않는가**: HF Jobs에서 원격 실행(→ `hugging-face-jobs` 스킬로 핸드오프), model-card/`model-index` 편집, README 테이블 추출, Artificial Analysis 임포트, `.eval_results` 생성/발행, PR 생성, community-evals 자동화(→ `~/code/community-evals`로 핸드오프).

<a id="huggingface-community-evals---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 사전 검증
uv --version
printenv HF_TOKEN >/dev/null
nvidia-smi

# Option A: inspect-ai + Inference Providers (로컬 설정 최소)
uv run scripts/inspect_eval_uv.py --model meta-llama/Llama-3.2-1B --task mmlu --limit 20

# Option B: inspect-ai 로컬 GPU (vllm)
uv run scripts/inspect_vllm_uv.py --model meta-llama/Llama-3.2-1B --task gsm8k --limit 20
# Transformers 폴백
uv run scripts/inspect_vllm_uv.py --model microsoft/phi-2 --task mmlu --backend hf --trust-remote-code --limit 20

# Option C: lighteval 로컬 GPU (vllm)
uv run scripts/lighteval_vllm_uv.py --model meta-llama/Llama-3.2-3B-Instruct \
  --tasks "leaderboard|mmlu|5,leaderboard|gsm8k|5" --max-samples 20 --use-chat-template
# accelerate 폴백
uv run scripts/lighteval_vllm_uv.py --model microsoft/phi-2 --tasks "leaderboard|mmlu|5" \
  --backend accelerate --trust-remote-code --max-samples 20
```

<a id="huggingface-community-evals---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
제공 스크립트:
- `scripts/inspect_eval_uv.py` — Inference Providers 경유 inspect-ai eval
- `scripts/inspect_vllm_uv.py` — 로컬 GPU inspect-ai (vllm/Transformers)
- `scripts/lighteval_vllm_uv.py` — 로컬 GPU lighteval (vllm/accelerate)
- `examples/USAGE_EXAMPLES.md` — 추가 명령 패턴

태스크: inspect-ai는 `mmlu`, `gsm8k`, `hellaswag`, `arc_challenge`, `truthfulqa`, `winogrande`, `humaneval`. lighteval은 `suite|task|num_fewshot` 형식(예: `leaderboard|mmlu|5`), 콤마로 다중 지정.

주요 플래그: `--limit`(inspect 스모크), `--max-samples`(lighteval 스모크), `--backend [vllm|hf|accelerate]`, `--trust-remote-code`, `--use-chat-template`, `--batch-size`, `--gpu-memory-utilization`.

하드웨어 가이드: <3B 소비자 GPU/Apple Silicon, 3B~13B 강력 로컬 GPU, 13B+ 고메모리 GPU 또는 Jobs 핸드오프. OOM 시 batch-size/gpu-memory-utilization 축소 또는 모델 축소.

<a id="huggingface-community-evals---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-community-evals/SKILL.md`

## huggingface-datasets

> Hugging Face Dataset Viewer API로 데이터셋 메타데이터·행 페이지네이션·검색·필터·parquet URL을 읽는 스킬.

<a id="huggingface-datasets---용도"></a>
### 📌 용도
Hugging Face Dataset Viewer API를 사용한 읽기 전용 데이터셋 탐색/추출 워크플로우를 담당한다. subset/split 메타데이터를 가져오고, 행을 페이지네이션하고, 텍스트 검색과 필터(predicate)를 적용하고, parquet URL을 다운로드하고, 크기/통계를 읽는다. 데이터셋 가용성 검증(`/is-valid`)부터 시작해 config·split 해석, 미리보기, 페이지네이션, 검색/필터, parquet/size/statistics 조회까지의 코어 워크플로우를 제공한다. 데이터셋 생성/업로드(Hub UI, `@huggingface/hub` CLI), 에이전트 트레이스(JSONL) 업로드도 다룬다.

<a id="huggingface-datasets---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: HF 데이터셋의 subset/split 메타데이터 조회, 행 페이지네이션, 텍스트 검색, 필터 적용, parquet URL 다운로드, 크기/통계 읽기 등 Dataset Viewer API 워크플로우. 데이터셋 생성/업로드, 에이전트 세션 트레이스(Claude Code/Codex/Pi)를 데이터셋으로 올리는 작업.
- **언제 쓰지 않는가**: CLI 기반 parquet URL 탐색이나 SQL은 `hf-cli` 스킬의 `hf datasets parquet`/`hf datasets sql` 사용. 데이터셋으로 모델을 학습하는 작업은 학습 전용 스킬.

<a id="huggingface-datasets---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 행 페이지네이션 (offset 0-based, length 최대 100)
curl "https://datasets-server.huggingface.co/rows?dataset=stanfordnlp/imdb&config=plain_text&split=train&offset=0&length=100"
curl "https://datasets-server.huggingface.co/rows?dataset=stanfordnlp/imdb&config=plain_text&split=train&offset=100&length=100"
```

업로드 전에는 사용자가 승인한 **해당 프로젝트·세션 파일만** 별도 폴더 `./approved-traces`에 준비한다. 원본 전체를 복사하지 말고 토큰·개인정보·비공개 코드 등 민감정보를 제거한 뒤, 파일 목록과 내용을 확인받는다. 아래 예시는 이 준비를 마친 뒤 실행한다. 일반 데이터셋도 같은 방식으로 승인된 데이터 폴더와 원격 경로를 지정한다.

```python
# 승인된 파일만 준비한 폴더를 실제 비공개 데이터셋에 업로드한다.
from pathlib import Path
from huggingface_hub import HfApi

api = HfApi()  # HF_TOKEN 환경변수 또는 기존 CLI 로그인 사용.
repo_id = "namespace/repo"  # 사용자가 지정한 저장소로 변경.
prepared_folder = Path("./approved-traces")
api.create_repo(repo_id=repo_id, repo_type="dataset", private=True, exist_ok=True)
if api.repo_info(repo_id=repo_id, repo_type="dataset").private is not True:
    raise RuntimeError("비공개 저장소가 확인되지 않아 업로드를 중단합니다.")
api.upload_folder(repo_id=repo_id, repo_type="dataset", folder_path=prepared_folder,
                  path_in_repo="codex/project-name")
```

`private=True`나 CLI의 `--private`는 기존 공개 저장소를 비공개로 바꾸지 않는다. 실제 공개 여부를 조회해서 비공개인 경우에만 업로드하고, 조회 실패도 그대로 중단한다. 공개 저장소의 가시성은 자동 변경하지 않는다. 원격 경로 `codex/project-name`은 저장 위치일 뿐 **프로젝트 필터가 아니다**. [공식 API 계약](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.HfApi.create_repo)을 참고한다.

<a id="huggingface-datasets---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
Base URL: `https://datasets-server.huggingface.co` (GET, 쿼리 파라미터 URL 인코딩, gated/private는 `Authorization: Bearer <HF_TOKEN>`).

엔드포인트:
- `/is-valid?dataset=<ns/repo>` — 가용성 검증
- `/splits?dataset=` — subset·split 목록
- `/first-rows?dataset=&config=&split=` — 첫 행 미리보기
- `/rows?dataset=&config=&split=&offset=&length=` — 행 페이지네이션(length 최대 100)
- `/search?...&query=<text>` — 문자열 컬럼 텍스트 검색
- `/filter?...&where=<predicate>&orderby=<sort>` — predicate 필터
- `/parquet?dataset=` — parquet shard 목록
- `/size?dataset=` — 크기 총계
- `/statistics?dataset=&config=&split=` — 컬럼 통계
- `/croissant?dataset=` — Croissant 메타데이터

페이지네이션 응답 필드 `num_rows_total`, `num_rows_per_page`, `partial`로 연속 처리. 모든 검색/필터는 읽기 전용·부작용 없음.

에이전트 트레이스: Claude Code(`~/.claude/projects`), Codex(`~/.codex/sessions`), Pi(`~/.pi/agent/sessions`)의 `.jsonl`에는 여러 프로젝트의 프롬프트·경로·시크릿·PII가 포함될 수 있다. 이 전역 폴더를 직접 업로드하지 않는다. 승인된 프로젝트·세션만 선택해 민감정보를 제거하고 별도 폴더를 준비한 뒤 위 비공개 확인 절차를 따른다. Hub는 지원되는 트레이스 형식을 감지해 `Traces` 태깅과 트레이스 뷰어를 활성화한다.

<a id="huggingface-datasets---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-datasets/SKILL.md`

## huggingface-gradio

> Python으로 Gradio 웹 UI와 ML 데모를 만드는 스킬 (Interface/Blocks/ChatInterface, 컴포넌트, 이벤트 리스너).

<a id="huggingface-gradio---용도"></a>
### 📌 용도
Gradio는 인터랙티브 웹 UI와 ML 데모를 만드는 Python 라이브러리다. 이 스킬은 핵심 API, 패턴, 예제를 커버한다. 고수준 `Interface`(함수를 입출력 컴포넌트로 감쌈), 저수준 `Blocks`(명시적 레이아웃·이벤트 와이어링), `ChatInterface`(챗봇 UI 래퍼) 세 가지 코어 패턴을 제공한다. Textbox, Number, Slider, Image, Audio, Video, Chatbot 등 주요 컴포넌트의 시그니처, 이벤트 리스너 패턴, `gr.HTML` 기반 커스텀 컴포넌트, 그리고 `gradio` CLI(`info`/`predict`)를 통한 프로그래매틱 Spaces 호출까지 다룬다.

<a id="huggingface-gradio---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: Gradio 앱/데모 생성·편집, 컴포넌트·이벤트 리스너·레이아웃·챗봇 작성. Python으로 ML 데모 웹 UI를 만들 때.
- **언제 쓰지 않는가**: Gradio가 아닌 다른 프레임워크(예: Streamlit, 일반 React 프런트엔드). LoRA용 Space 빌드는 huggingface-lora-space-builder, ZeroGPU 코드 제약은 huggingface-zerogpu, Space 배포/디버깅은 huggingface-spaces가 더 적합.

<a id="huggingface-gradio---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```python
import gradio as gr

# Interface (고수준)
gr.Interface(fn=lambda name: f"Hello {name}!", inputs="text", outputs="text").launch()

# Blocks (저수준)
with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Greeting")
    btn = gr.Button("Greet")
    btn.click(fn=lambda n: f"Hello {n}!", inputs=name, outputs=output)
demo.launch()

# ChatInterface (챗봇)
gr.ChatInterface(fn=lambda message, history: f"You said: {message}").launch()
```

```bash
# Prediction CLI - 엔드포인트/파라미터 발견
gradio info gradio/calculator

# 예측 전송
gradio predict gradio/calculator /predict '{"num1": 5, "operation": "multiply", "num2": 3}'
gradio predict black-forest-labs/FLUX.2-dev /infer '{"prompt": "A majestic dragon"}'
# 파일 업로드는 meta 키 필요
gradio predict gradio/image_mod /predict '{"image": {"path": "/path/to/image.png", "meta": {"_type": "gradio.FileData"}}}'
```

<a id="huggingface-gradio---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
주요 컴포넌트: `Textbox`, `Number`, `Slider`, `Checkbox`, `Dropdown`, `Radio`, `Image`, `Audio`, `Video`, `File`, `Chatbot`, `Button`, `Markdown`, `HTML` 등. 각 컴포넌트의 전체 시그니처(value/type/label/interactive/visible 등)가 SKILL.md에 수록됨.

이벤트 리스너 공통 시그니처: `component.event_name(fn, inputs, outputs, api_name, show_progress, queue, concurrency_limit, ...)`. 컴포넌트별 지원 이벤트(예: Button→click, Textbox→change/input/submit, Chatbot→change/select/like/retry/edit, Audio→stream/play/pause 등) 정리됨.

커스텀 컴포넌트: `gr.HTML`로 `html_template`(`${}` JS, `{{}}` Handlebars), `css_template`(스코프 스타일), `js_on_load`(인터랙션). `props.value`로 값 갱신, `trigger('event_name')`로 이벤트 발화. 서브클래싱 + `api_info()`로 API/MCP 지원.

Prediction CLI: `gradio info <space>`(엔드포인트/파라미터 JSON), `gradio predict <space> <endpoint> <json>`(예측). 둘 다 private Space는 `--token`.

참고 가이드 링크(Quickstart, Blocks, Streaming, Sharing 등)와 `examples.md`(완전 동작 앱).

<a id="huggingface-gradio---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-gradio/SKILL.md`

## huggingface-llm-trainer

> TRL/Unsloth와 Hugging Face Jobs 클라우드 GPU로 언어·비전 모델을 학습/파인튜닝하는 스킬 (SFT/DPO/GRPO/Reward + GGUF 변환).

<a id="huggingface-llm-trainer---용도"></a>
### 📌 용도
TRL(Transformer Reinforcement Learning) 또는 Unsloth를 사용해 완전 관리형 Hugging Face 인프라(클라우드 GPU)에서 언어·비전 모델을 학습한다. 로컬 GPU 설정 없이 학습하며 결과는 자동으로 Hub에 저장된다. SFT(지도 파인튜닝), DPO(선호 데이터 정렬), GRPO(온라인 RL), Reward Modeling 학습 방법과, 로컬 배포용 GGUF 변환을 커버한다. TRL Jobs 패키지, PEP 723 형식 UV 스크립트, 데이터셋 준비/검증, 하드웨어 선택, 비용 추정, Trackio 모니터링, Hub 인증, 모델 선택/리더보드, 모델 영속화 가이드를 포함한다. 학습 환경은 ephemeral이므로 Hub push가 필수다.

<a id="huggingface-llm-trainer---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 로컬 인프라 없이 클라우드 GPU에서 LM 파인튜닝, TRL 방법(SFT/DPO/GRPO) 학습, Hugging Face Jobs 인프라에서 학습 잡 실행, GGUF 변환(Ollama/LM Studio/llama.cpp용), 모델을 Hub에 영속 저장. 사용자가 "train a model", "fine-tune" 또는 로컬 GPU 없이 HF Jobs에서 학습을 언급할 때.
- **언제 쓰지 않는가**: 로컬 GPU에서 직접 평가(huggingface-community-evals), 비전 전용 학습 작업은 huggingface-vision-trainer, sentence-transformers는 train-sentence-transformers, CLI 명령만 다룰 땐 trl-training이 더 적합. 제한 GPU 메모리/속도/대형 모델(>13B)/VLM은 Unsloth(`references/unsloth.md`) 사용.

<a id="huggingface-llm-trainer---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```python
# Approach 1 (기본): hf_jobs() MCP + 인라인 UV 스크립트 (PEP 723)
hf_jobs("uv", {
    "script": """
# /// script
# dependencies = ["trl>=0.12.0", "peft>=0.7.0", "trackio"]
# ///
from datasets import load_dataset
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig
import trackio

dataset = load_dataset("trl-lib/Capybara", split="train")
split = dataset.train_test_split(test_size=0.1, seed=42)
trainer = SFTTrainer(
    model="Qwen/Qwen2.5-0.5B",
    train_dataset=split["train"], eval_dataset=split["test"],
    peft_config=LoraConfig(r=16, lora_alpha=32),
    args=SFTConfig(output_dir="my-model", push_to_hub=True,
        hub_model_id="username/my-model", num_train_epochs=3,
        report_to="trackio", project="proj", run_name="run"),
)
trainer.train(); trainer.push_to_hub()
""",
    "flavor": "a10g-large", "timeout": "2h", "secrets": {"HF_TOKEN": "$HF_TOKEN"}
})
```

```bash
# Approach 3: HF Jobs CLI (플래그는 스크립트 URL 앞에, --secrets 복수형)
hf jobs uv run --flavor a10g-large --timeout 2h --secrets HF_TOKEN \
  "https://huggingface.co/user/repo/resolve/main/train.py"
hf jobs ps; hf jobs logs <job-id>; hf jobs inspect <job-id>; hf jobs cancel <job-id>

# Approach 4: trl-jobs 패키지 (터미널 직접 작업 시)
uvx trl-jobs sft --model_name Qwen/Qwen2.5-0.5B --dataset_name trl-lib/Capybara

# 비용 추정 / 데이터셋 검증
uv run scripts/estimate_cost.py --model meta-llama/Llama-2-7b-hf --dataset trl-lib/Capybara --hardware a10g-large --dataset-size 16000 --epochs 3
```

<a id="huggingface-llm-trainer---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
핵심 디렉티브: ① 항상 `hf_jobs("uv", {...})` MCP 도구로 인라인 스크립트 제출(로컬 파일 경로 불가, 인라인/URL만), ② 항상 Trackio 포함, ③ 제출 후 job ID·모니터링 URL·예상시간 보고, ④ 비동기이므로 폴링 금지·사용자 요청 시 상태 확인.

학습 방법 4가지 접근: (1) UV 스크립트 인라인(기본), (2) TRL 공식 유지보수 스크립트 URL+`script_args`, (3) `hf jobs uv run` CLI, (4) `uvx trl-jobs` 패키지.

시퀀스 길이: TRL config는 `max_length`(NOT `max_seq_length`), 기본 1024, 비전 모델은 `max_length=None`.

하드웨어: <1B t4-small, 1-3B t4-medium/l4x1, 3-7B a10g-small/large, 7-13B a10g-large/a100-large(LoRA), 13B+ a100-large/a10g-largex2(LoRA). >7B는 LoRA/PEFT 사용.

필수 설정: `push_to_hub=True` + `hub_model_id="username/model"` + `secrets={"HF_TOKEN": "$HF_TOKEN"}`. timeout 기본 30분은 너무 짧음 — 최소 1-2시간, 20-30% 버퍼 추가.

데이터셋 검증: GPU 학습 전 `dataset_inspector.py`(CPU ~$0.01)로 형식 검증, 특히 DPO(prompt/chosen/rejected). 출력 마커 ✓READY/✗NEEDS MAPPING/✗INCOMPATIBLE.

GGUF 변환: 학습 후 4/5/8-bit 양자화로 llama.cpp/Ollama/LM Studio용 변환(`references/gguf_conversion.md`).

스크립트: `scripts/train_{sft,dpo,grpo}_example.py`, `unsloth_sft_example.py`, `estimate_cost.py`, `convert_to_gguf.py`, `hf_benchmarks.py`. 실패 모드: OOM(batch size↓, gradient_checkpointing, 하드웨어↑), 데이터셋 형식, timeout, Hub push 실패.

<a id="huggingface-llm-trainer---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-llm-trainer/SKILL.md`

## huggingface-local-models

> llama.cpp + GGUF로 CPU/Mac Metal/CUDA/ROCm에서 모델을 로컬 실행하기 위한 모델 선택·실행 스킬.

<a id="huggingface-local-models---용도"></a>
### 📌 용도
Hugging Face Hub에서 llama.cpp 호환 GGUF repo를 검색하고, 알맞은 양자화(quant)를 고르고, `llama-cli` 또는 `llama-server`로 모델을 실행하는 작업을 담당한다. GGUF 찾기, quant 선택, 서버 실행, 정확한 GGUF 파일 조회, 변환, OpenAI 호환 로컬 서빙을 커버한다. 기본 워크플로우는 `apps=llama.cpp` 필터로 Hub 검색 → `?local-app=llama.cpp` 페이지에서 권장 snippet/quant 확인 → tree API로 정확한 `.gguf` 파일명 확인 → `-hf <repo>:<QUANT>`로 실행 → 커스텀 파일명이면 `--hf-repo`+`--hf-file` 폴백 → GGUF가 없을 때만 Transformers 가중치에서 변환. CPU, Mac Metal, CUDA, ROCm 가속을 지원한다.

<a id="huggingface-local-models---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: llama.cpp와 GGUF로 모델을 로컬 실행할 때. GGUF repo 검색, quant 선택, 로컬 서버 실행, 정확한 GGUF 파일 조회, GGUF 변환, OpenAI 호환 로컬 서빙.
- **언제 쓰지 않는가**: 클라우드 GPU 학습(huggingface-llm-trainer), 모델 추천/벤치마크 비교(huggingface-best), 브라우저/JS 추론(transformers-js). 모델 선택보다 학습/배포가 목적인 경우.

<a id="huggingface-local-models---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 설치
brew install llama.cpp          # 또는 winget install llama.cpp
git clone https://github.com/ggml-org/llama.cpp && cd llama.cpp && make

# gated repo 인증
hf auth login

# Hub 검색 (브라우저 URL)
# https://huggingface.co/models?apps=llama.cpp&sort=trending
# https://huggingface.co/models?search=<term>&apps=llama.cpp&num_parameters=min:0,max:24B&sort=trending

# Hub에서 직접 실행
llama-cli    -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_M
llama-server -hf unsloth/Qwen3.6-35B-A3B-GGUF:UD-Q4_K_M

# 정확한 GGUF 파일 지정 (커스텀 파일명)
llama-server --hf-repo unsloth/Qwen3.6-35B-A3B-GGUF \
    --hf-file Qwen3.6-35B-A3B-UD-Q4_K_M.gguf -c 4096

# GGUF가 없을 때만 변환
hf download <repo-without-gguf> --local-dir ./model-src
python convert_hf_to_gguf.py ./model-src --outfile model-f16.gguf --outtype f16
llama-quantize model-f16.gguf model-q4_k_m.gguf Q4_K_M

# OpenAI 호환 서버 스모크 테스트
curl http://localhost:8080/v1/chat/completions \
  -H "Content-Type: application/json" -H "Authorization: Bearer no-key" \
  -d '{"messages":[{"role":"user","content":"Write a limerick about exception handling"}]}'
```

<a id="huggingface-local-models---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
정확한 파일명 확인: `https://huggingface.co/api/models/<repo>/tree/main?recursive=true`.

Quant 선택 가이드:
- HF `?local-app=llama.cpp` 페이지가 호환으로 표시한 정확한 quant 우선.
- repo-native 라벨(예: `UD-Q4_K_M`)을 정규화하지 말고 그대로 사용.
- 기본값 `Q4_K_M`. 코드/기술 워크로드는 메모리 여유 시 `Q5_K_M`/`Q6_K`.
- 빠듯한 RAM/VRAM은 `Q3_K_M`, `Q4_K_S`, repo별 `IQ`/`UD-*` 변형.
- `mmproj-*.gguf`는 projector 가중치이지 메인 체크포인트가 아님.

참조 파일: `references/hub-discovery.md`(URL-우선 워크플로우·tree API·명령 재구성), `references/quantization.md`(포맷 테이블·스케일링·imatrix), `references/hardware.md`(Metal/CUDA/ROCm/CPU 빌드·가속).

리소스: llama.cpp GitHub, HF GGUF+llama.cpp 문서, Local Apps/Local Agents 문서, GGUF 변환 Space(`ggml-org/gguf-my-repo`).

<a id="huggingface-local-models---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-local-models/SKILL.md`

## huggingface-lora-space-builder

> 사용자가 제공한 LoRA를 위한 Gradio 데모를 Hugging Face Spaces(ZeroGPU, 기본 private)에 빌드·발행하는 스킬.

<a id="huggingface-lora-space-builder---용도"></a>
### 📌 용도
사용자가 제공한 LoRA로 추론을 실행하는 Gradio 데모를 Hugging Face Spaces에 빌드하고 발행한다. Qwen-Image, Qwen-Image-Edit, LTX-Video, Wan, FLUX, SDXL 등 diffusion 베이스 모델의 LoRA를 대상으로 한다. 알맞은 베이스 파이프라인과 `diffusers` 추론 레시피 선택, LoRA의 작업·입력(Union/멀티태스크 컨트롤, 편집, 비디오, 이미지 등)에 맞춘 UI 설계, 모델카드 권장사항(트리거 워드, 스텝, 가이던스, LoRA scale, 예시 입력) 준수, ZeroGPU 하드웨어에 기본 private Space로 배포를 커버한다. 출력은 로컬 스크립트가 아니라 브라우저에서 바로 시험할 수 있는 실제 발행된 Space다. 핵심은 "이 LoRA만을 위한 손수 만든 데모"이지 범용 템플릿이 아니다.

<a id="huggingface-lora-space-builder---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: LoRA를 위한 Space/데모/Gradio 앱/플레이그라운드를 만들거나(create/generate/ship/publish) 발행해 달라고 할 때. Qwen-Image(-Edit), LTX-Video, Wan, FLUX, SDXL 등 diffusion 베이스의 LoRA. 학습했거나 Hub에 호스팅한 LoRA를 공유하고 싶다고 묘사할 때.
- **언제 쓰지 않는가**: 일반 Gradio 앱 작성(huggingface-gradio), ZeroGPU 코드 제약 일반(huggingface-zerogpu), 비-LoRA Space 배포/디버깅(huggingface-spaces). LoRA 없이 베이스 모델만 데모하는 경우.

<a id="huggingface-lora-space-builder---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
6단계 워크플로우: ① LoRA 정보 수집 → ② 베이스 파이프라인 선택 → ③ 이 LoRA만의 UI 설계 → ④ app.py/requirements.txt/README.md 함께 작성 후 한 번에 승인 → ⑤ Space 발행(private) → ⑥ 스모크 테스트.

```python
# Phase 1: 인증 + repo 읽기
from huggingface_hub import HfApi, get_token, ModelCard
cached_token = get_token()  # HF_TOKEN env 또는 캐시된 CLI 로그인
api = HfApi(token=cached_token)
files = api.list_repo_files(repo_id)        # .safetensors, README 등 확인
card = ModelCard.load(repo_id)              # data dict + text(README)

# Phase 2: 베이스 모델 카드의 diffusers snippet에서 파이프라인 클래스 검증(필수)
base_card = ModelCard.load(base_model_id)   # 임포트된 클래스가 진실의 원천

# Phase 5: Space 발행 (private, ZeroGPU)
from huggingface_hub import HfApi, SpaceHardware
api = HfApi(token=hf_token)
repo_id = f"{api.whoami()['name']}/{space_name}"
api.create_repo(repo_id=repo_id, repo_type="space", space_sdk="gradio",
    space_hardware=SpaceHardware.ZERO_A10G, private=True, exist_ok=True)
if api.repo_info(repo_id=repo_id, repo_type="space").private is not True:
    raise RuntimeError("비공개 Space가 확인되지 않아 파일과 secret 전송을 중단합니다.")
for path in ["app.py", "requirements.txt", "README.md"]:
    api.upload_file(path_or_fileobj=path, path_in_repo=path, repo_id=repo_id, repo_type="space")
api.add_space_secret(repo_id=repo_id, key="HF_TOKEN", value=HF_TOKEN)  # private LoRA 런타임용
```

`private=True`는 기존 공개 Space의 가시성을 바꾸지 않는다. 파일 업로드와 런타임 secret 전송 전에 실제 비공개 여부를 조회하며, 공개·불명확한 결과나 조회 실패 시 중단한다. 기존 공개 Space를 자동으로 비공개로 바꾸지 않고 사용자가 배포 대상을 다시 선택하도록 한다. [공식 API 계약](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.HfApi.create_repo)을 참고한다.

```bash
# Phase 6: 스모크 테스트 (gradio CLI)
gradio info {repo_id} --token $HF_TOKEN
gradio predict {repo_id} /predict '{"prompt": "...", "aspect_ratio": "1:1"}' --token $HF_TOKEN
```

<a id="huggingface-lora-space-builder---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
참조 파일: `references/base-models/qwen-image.md`(Qwen-Image/Edit), `references/base-models/ltx.md`(LTX 패밀리), `references/tasks.md`(T2I/I2I/T2V/I2V/V2V 베이스 UI), `references/adapting-to-the-lora.md`(이 LoRA만의 필요 분석 — 가장 중요), `references/creative-mode.md`(gr.HTML 커스텀 JS), `references/zerogpu-and-publishing.md`(ZeroGPU 규칙·발행).

처리 5작업: `text-to-image`, `image-to-image`, `text-to-video`, `image-to-video`, `video-to-video`.

파이프라인 클래스 검증(필수): 베이스 모델 카드의 diffusers snippet이 진실의 원천. 예) Qwen-Image-Edit는 `QwenImageEditPipeline`, 2509/2511은 `QwenImageEditPlusPipeline`(클래스·기본 파라미터·입력 형태 다름). LTX-Video는 `LTXPipeline` 등, LTX-2는 `LTX2Pipeline`.

ZeroGPU 규칙: 모델은 module-level에서 `cuda`에 배치(lazy 로딩 금지), 추론 함수는 `@spaces.GPU(duration=...)`, `torch.compile` 금지.

requirements.txt: app.py 임포트 + 베이스 모델 reference의 "Required dependencies" + LoRA 카드 pip + diffusers/transformers/accelerate/peft/safetensors. `gradio`·`torch`·`spaces`·`huggingface_hub`는 넣지 않음(런타임 제공, README의 `sdk_version`로 gradio 제어). `xformers`/`flash-attn`은 반사적 추가 금지.

README YAML: `sdk: gradio`, `sdk_version`(현재 버전), `hardware: zero-a10g`(실제는 RTX Pro 6000 Blackwell, PRO/Team/Enterprise 필요), `models:`(base+lora), `short_description`(~60자, 초과 시 validate-yaml 400).

발행/빌드 실패 처리: validate-yaml 400(short_description 단축), zero-a10g 403(PRO 아님 → space_hardware 빼고 생성, CPU 폴백), weight_name 불일치, gated 베이스 모델 토큰 누락, diffusers 버전(git 설치) 등.

<a id="huggingface-lora-space-builder---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-lora-space-builder/SKILL.md`

## huggingface-paper-publisher

> Hugging Face Hub에 연구 논문을 발행·관리하는 스킬 (페이지 생성, 모델/데이터셋 연결, 저자권 주장, 연구 아티클 생성).

<a id="huggingface-paper-publisher---용도"></a>
### 📌 용도
AI 엔지니어와 연구자가 Hugging Face Hub에서 연구 논문을 발행·관리·연결하도록 돕는다. 논문 작성부터 발행까지의 워크플로우를 간소화하며, arXiv 연동, 모델/데이터셋 연결, 저자권 관리를 포함한다. 주요 기능은 (1) 논문 페이지 관리(arXiv에서 인덱싱, 저자권 주장, 가시성 제어, 논문 발견), (2) 모델/데이터셋 아티팩트에 논문 연결(Hub가 자동으로 `arxiv:<ID>` 태그 생성), (3) 마크다운 기반 전문 연구 아티클 생성(standard/modern/arxiv/ml-report 템플릿), (4) 메타데이터 관리(YAML frontmatter, BibTeX 인용). `scripts/paper_manager.py`를 `uv run`으로 실행한다.

<a id="huggingface-paper-publisher---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: HF Hub에 연구 논문 발행/관리, 논문 페이지 생성, 논문을 모델/데이터셋에 연결, 저자권 주장, 마크다운 기반 연구 아티클 생성.
- **언제 쓰지 않는가**: 기존 논문을 읽기/요약/분석하는 작업(huggingface-papers). 논문 발행이 아니라 단순히 arXiv/HF paper URL을 읽어달라는 경우.

<a id="huggingface-paper-publisher---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
전제: `uv run`으로 스크립트 실행, `HF_TOKEN`(Write 권한) 설정. 경로는 SKILL.md 디렉토리 기준.

```bash
# arXiv에서 논문 인덱싱 / 존재 확인
uv run scripts/paper_manager.py index --arxiv-id "2301.12345"
uv run scripts/paper_manager.py check --arxiv-id "2301.12345"

# 모델/데이터셋/스페이스에 논문 연결 (자동 arxiv 태그 생성)
uv run scripts/paper_manager.py link --repo-id "username/model-name" --repo-type "model" --arxiv-id "2301.12345"
uv run scripts/paper_manager.py link --repo-id "username/model-name" --repo-type "model" --arxiv-ids "2301.12345,2302.67890"
uv run scripts/paper_manager.py link --repo-id "username/model-name" --repo-type "model" --arxiv-id "2301.12345" --citation "$(cat citation.txt)" --create-pr

# 저자권 주장 / 상태 확인
uv run scripts/paper_manager.py claim --arxiv-id "2301.12345" --email "your.email@institution.edu"
uv run scripts/paper_manager.py check-authorship --arxiv-id "2301.12345"

# 가시성 관리
uv run scripts/paper_manager.py list-my-papers
uv run scripts/paper_manager.py toggle-visibility --arxiv-id "2301.12345" --show true

# 연구 아티클 생성 / HTML 변환
uv run scripts/paper_manager.py create --template "modern" --title "..." --authors "Jane Doe, John Smith" --abstract "$(cat abstract.txt)" --output "paper.md"
uv run scripts/paper_manager.py convert --input "paper.md" --output "paper.html" --style "modern"

# 검색 / 정보 / 인용
uv run scripts/paper_manager.py search --query "transformer attention"
uv run scripts/paper_manager.py info --arxiv-id "2301.12345" --format "json"
uv run scripts/paper_manager.py citation --arxiv-id "2301.12345" --format "bibtex"
uv run scripts/paper_manager.py validate --repo-id "username/model-name" --repo-type "model"
```

<a id="huggingface-paper-publisher---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
스크립트: `scripts/paper_manager.py`. PEP 723 인라인 의존성(huggingface_hub>=0.26.0, pyyaml, requests, markdown, python-dotenv).

서브커맨드: `index`, `check`, `link`, `claim`, `check-authorship`, `list-my-papers`, `toggle-visibility`, `create`, `convert`, `search`, `info`, `citation`, `validate`.

연구 아티클 템플릿: `standard`(전통적), `modern`(Distill풍 웹 친화), `arxiv`, `ml-report`. modern은 동적 목차·반응형·코드 하이라이트·LaTeX 수식 지원.

연결 원리: README에 arXiv 링크 추가 → Hub가 ID 추출 → `arxiv:<ID>` 태그 자동 생성 → 클릭 시 Paper Page → 해당 논문 인용 모델/데이터셋 표시.

Python API: `from scripts.paper_manager import PaperManager; pm = PaperManager(hf_token=...); pm.index_paper(...); pm.link_paper(...)`.

에러: Paper Not Found(미인덱싱), Permission Denied(토큰 권한), Invalid YAML, Authorship Failed(이메일 불일치), Already Claimed, Rate Limiting. tfrere의 research-article-template Space와 보완 관계.

<a id="huggingface-paper-publisher---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-paper-publisher/SKILL.md`

## huggingface-papers

> HF paper page를 마크다운으로 읽고, papers API로 저자·연결된 모델/데이터셋/스페이스 등 구조화 메타데이터를 조회하는 스킬.

<a id="huggingface-papers---용도"></a>
### 📌 용도
Hugging Face Paper Pages(hf.co/papers, arXiv 기반)의 논문을 마크다운으로 가져와 읽고, papers API로 저자명·HF 사용자명·연결된 모델/데이터셋/스페이스·GitHub repo·프로젝트 페이지·요약(abstract)·AI 생성 요약·업보트 같은 구조화 메타데이터를 조회한다. 사용자가 HF paper page URL, arXiv URL/ID를 공유하거나, AI 연구 논문을 요약·설명·분석해 달라고 할 때 사용한다. 마크다운 콘텐츠는 arxiv.org/html 버전에 의존하며, 없으면 HF paper page HTML로 폴백한다. 공개 paper page는 인증 불필요, 쓰기(claim/index/links) 엔드포인트만 토큰 필요.

<a id="huggingface-papers---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: HF paper page URL(`https://huggingface.co/papers/2602.08025`), `.md` URL, arXiv URL(`abs`/`pdf`), arXiv ID(`2602.08025`, 버전 접미사 포함)를 공유할 때. AI 연구 논문을 요약·설명·분석해 달라고 할 때.
- **언제 쓰지 않는가**: 논문을 새로 발행/생성하거나 연구 아티클을 만드는 작업(huggingface-paper-publisher). 단순 읽기/분석이 아니라 모델/데이터셋에 논문을 연결·게시하는 워크플로우.

<a id="huggingface-papers---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
Paper ID 파싱: 어떤 입력이든 arXiv ID로 추출 (예: `.../papers/2602.08025.md` → `2602.08025`, `2602.08025v1` → 버전 유지).

```bash
# 마크다운으로 논문 읽기 (권장: .md 엔드포인트)
curl -s "https://huggingface.co/papers/{PAPER_ID}.md"
curl -s -H "Accept: text/markdown" "https://huggingface.co/papers/{PAPER_ID}"

# 구조화 메타데이터 (JSON)
curl -s "https://huggingface.co/api/papers/{PAPER_ID}"

# 논문에 연결된 모델/데이터셋/스페이스 찾기
curl "https://huggingface.co/api/models?filter=arxiv:{PAPER_ID}"
curl "https://huggingface.co/api/datasets?filter=arxiv:{PAPER_ID}"
curl "https://huggingface.co/api/spaces?filter=arxiv:{PAPER_ID}"

# Daily Papers / 목록 / 검색
curl -s -H "Authorization: Bearer $HF_TOKEN" "https://huggingface.co/api/daily_papers?p=0&limit=20&sort=trending"
curl -s -H "Authorization: Bearer $HF_TOKEN" "https://huggingface.co/api/papers?cursor={CURSOR}&limit=20"
curl -s -H "Authorization: Bearer $HF_TOKEN" "https://huggingface.co/api/papers/search?q=vision+language&limit=20"
```

<a id="huggingface-papers---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
API base: `https://huggingface.co`.

읽기 엔드포인트:
- `GET /papers/{ID}.md` — 마크다운 본문 (권장)
- `GET /api/papers/{ID}` — 구조화 JSON (authors, summary, AI summary, projectPage, githubRepo, upvotes 등)
- `GET /api/models|datasets|spaces?filter=arxiv:{ID}` — 연결된 아티팩트
- `GET /api/daily_papers` — `p`, `limit`(1~100), `date`(RFC3339), `week`(ISO), `month`, `submitter`, `sort`(publishedAt|trending)
- `GET /api/papers` — `cursor`, `limit`
- `GET /api/papers/search` — `q`(max 250), `limit`(1~120). 제목·저자·본문 하이브리드 시맨틱+전문 검색

쓰기 엔드포인트(`Authorization: Bearer $HF_TOKEN` 필요):
- `POST /api/settings/papers/claim` — 저자권 주장 (`paperId`, `claimAuthorId`, `targetUserId`)
- `POST /api/papers/index` — arXiv ID 인덱싱 (패턴 `^\d{4}\.\d{4,5}$`)
- `POST /api/papers/{paperId}/links` — projectPage/githubRepo/organizationId 갱신

에러: 404(아직 미인덱싱), Paper ID 미발견(버전 접미사 확인). 폴백: HF paper page → arXiv abs/pdf.

<a id="huggingface-papers---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-papers/SKILL.md`

## huggingface-spaces

> Hugging Face Spaces 앱(Gradio/Docker/Static, ZeroGPU·전용 하드웨어)을 빌드·배포·디버깅·유지보수하는 스킬.

<a id="huggingface-spaces---용도"></a>
### 📌 용도
Hugging Face Spaces에서 머신러닝 애플리케이션을 만들고, 빌드하고, 디버깅하고, 유지보수하는 작업을 담당한다. 각 Space는 git repo이며 Gradio/Docker/Static SDK를 가질 수 있다. ZeroGPU와 전용 하드웨어, 모델 로딩, 디버깅, 버킷(영속 스토리지), 인퍼런스 프로바이더, 커뮤니티 그랜트를 커버한다. 코드를 ZeroGPU로 포팅하거나, 빌드/실행이 안 되는 Space를 고치거나, `hf spaces …`·`@spaces.GPU`·Space README frontmatter·`spaces` Python 패키지를 다루는 작업에 사용한다. 핵심 원칙은 "로컬이 아니라 라이브 Space에서 반복(iterate)"하는 것이다.

<a id="huggingface-spaces---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: HF에 앱 생성/호스팅, 코드를 ZeroGPU로 포팅, 빌드/실행 안 되는 Space 수정, `hf spaces` 명령·`@spaces.GPU`·Space README frontmatter·`spaces` Python 패키지 작업.
- **언제 쓰지 않는가**: LoRA 전용 Space 빌드(huggingface-lora-space-builder), ZeroGPU 코드 제약 디테일만(huggingface-zerogpu — 단 본 스킬도 references/zerogpu.md로 다룸), Gradio 앱 자체 작성(huggingface-gradio).

<a id="huggingface-spaces---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 0. 준비
which hf || pip install -U huggingface_hub
hf auth whoami           # canPay, isPro 플래그가 하드웨어 선택 좌우

# 2. 기존 데모 먼저 검색
hf spaces search "<model name or task>" --sdk gradio --limit 10

# 4. Space 생성
hf repos create <ns>/<name> --type space --space-sdk <gradio|docker|static> \
    --flavor zero-a10g|cpu-basic|<paid> --secrets KEY=val --env KEY=val \
    --public|--private|--protected --exist-ok

# 7. 검증 (RUNNING만 믿지 말 것)
hf spaces info <ns>/<name> --expand runtime
hf spaces logs <ns>/<name> --tail 200
hf spaces logs <ns>/<name> --follow

# 8. 영속 스토리지 (버킷)
hf buckets create <ns>/<bucket-name>
hf spaces volumes set <ns>/<space> -v hf://buckets/<ns>/<bucket-name>:/data

# 9. 디버깅
hf spaces logs <id> --build --follow    # 빌드 에러
hf spaces logs <id> --follow            # 런타임 에러 (첫 에러를 찾을 것)
```

```python
# 최소 ZeroGPU Gradio 앱
import spaces           # torch/diffusers/transformers보다 먼저!
import torch, gradio as gr
from diffusers import DiffusionPipeline
pipe = DiffusionPipeline.from_pretrained("<repo>", torch_dtype=torch.bfloat16).to("cuda")

@spaces.GPU(duration=60)
def generate(prompt):
    return pipe(prompt).images[0]
gr.Interface(fn=generate, inputs=gr.Text(), outputs=gr.Image()).launch()
```

<a id="huggingface-spaces---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
SDK 3종: Gradio(대부분, ZeroGPU 지원), Docker(임의 컨테이너, ZeroGPU 미지원), Static(브라우저 ML/프로젝트 페이지, 하드웨어 불필요).

하드웨어: 무료 — `cpu-basic`(2vCPU/16GB), `zero-a10g`(ZeroGPU, RTX PRO 6000 Blackwell sm_120, large 48GB/xlarge 96GB, Gradio 전용·PyTorch 우선·PRO/Team/Enterprise 필요). 전용 GPU(T4/L4/A10G/L40S/A100/H200, 시간당 과금, `canPay=True`). 비-PRO는 cpu-basic 생성 후 커뮤니티 그랜트 신청.

README frontmatter: `title`, `emoji`, `colorFrom`/`colorTo`(지정 8색만), `sdk`, `sdk_version`(최신 안정, 5.x는 5.50.0), `app_file`, `short_description`(≤60자), `python_version`("3.10.13"/"3.12.12"), `startup_duration_timeout`. 주의: `hardware:`는 README에서 무시됨 — `--flavor` 또는 `hf spaces settings --hardware`로만 설정.

ZeroGPU 3규칙: ① `import spaces`를 torch보다 먼저(`torch.cuda.*` 몽키패치), ② 모델은 module scope에서 `.to("cuda")` 즉시 로드, ③ Gradio가 바인딩하는 함수에 `@spaces.GPU(duration=...)`.

requirements.txt: `gradio`/`spaces`/`huggingface_hub` 미기재(플랫폼 관리), `torchvision`/`torchaudio` 등은 기재. torch는 `2.8.0`/`2.9.1`/`2.10.0`/`2.11.0`만, 기본 unpinned. CUDA-extension wheel(flash_attn/xformers 등)은 Blackwell prebuilt wheel 사용.

검증 4단계: A.Alive(stage/hardware), B.로그 클린(폴백·dtype 다운그레이드 없는지), C.API 응답(`gradio_client`로 `view_api`→`predict`), D.출력+로그 동시 확인(HTTP 200≠정답).

참조: `references/zerogpu.md`, `debugging.md`, `known-errors.md`, `requirements.md`, `gradio.md`, `buckets.md`, `grants.md`, `inference-providers.md`. 동반 스킬 `hf-cli`(`hf skills add hf-cli`).

<a id="huggingface-spaces---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-spaces/SKILL.md`

## huggingface-tool-builder

> Hugging Face API 데이터를 fetch·가공·결합하는 재사용 가능한 CLI 스크립트/유틸리티를 만드는 스킬.

<a id="huggingface-tool-builder---용도"></a>
### 📌 용도
Hugging Face API를 사용해 데이터를 fetch·enrich·process하는 재사용 가능한 명령줄 스크립트와 유틸리티를 만든다. API 직접 호출과 `hf` CLI 도구 둘 다 사용하며, 체이닝·파이핑·중간 처리가 도움이 될 때 특히 유용하다. 작업이 반복/자동화되거나 여러 API 호출을 연결/결합해야 할 때 적합하다. 모델/데이터셋 카드는 repo에서 직접 접근한다. 결과의 형태(shape)를 먼저 조사한 뒤 최종 설계를 확정하고, 합성성이 유리한 곳에 파이핑/체이닝을 활용하되 가능한 한 단순한 해법을 선호한다.

<a id="huggingface-tool-builder---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: HF API 데이터를 쓰는 도구/스크립트를 만들거나, API 호출을 연결/결합하는 작업, 반복·자동화될 작업. 데이터를 fetch/enrich/process하는 재사용 스크립트가 필요할 때.
- **언제 쓰지 않는가**: 일회성 단일 명령 실행(hf-cli로 충분), 학습/평가/배포 같은 특정 워크플로우(전용 스킬). Dataset Viewer API 단순 조회는 huggingface-datasets.

<a id="huggingface-tool-builder---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# HF_TOKEN을 Authorization 헤더로 (높은 rate limit + 권한)
curl -H "Authorization: Bearer ${HF_TOKEN}" https://huggingface.co/api/models

# OpenAPI 스펙 탐색 (직접 읽지 말고 jq로 추출 — 파일이 너무 큼)
curl -s "https://huggingface.co/.well-known/openapi.json" | jq '.paths | keys | sort'
curl -s "https://huggingface.co/.well-known/openapi.json" | jq '.paths["/api/models"]'

# 합성성 — 파이핑 예시
references/baseline_hf_api.sh 25 | jq -r '.[].id' | references/hf_enrich_models.sh \
  | jq -s 'sort_by(.downloads) | reverse | .[:10]'
references/baseline_hf_api.sh 50 | jq '[.[] | {id, downloads}] | sort_by(.downloads) | reverse | .[:10]'
printf '%s\n' openai/gpt-oss-120b meta-llama/Meta-Llama-3.1-8B \
  | references/hf_model_card_frontmatter.sh | jq -s 'map({id, license, has_extra_gated_prompt})'
```

<a id="huggingface-tool-builder---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
스크립트 작성 규칙:
- 모든 스크립트는 `--help`로 입출력 설명 제공.
- 비파괴적 스크립트는 인계 전 테스트.
- 셸 스크립트 선호, 복잡도/필요 시 Python 또는 TSX.
- `HF_TOKEN` 환경변수를 Authorization 헤더로 사용.
- 최종 설계 전 API 결과 shape 조사, 합성성 유리한 곳에 파이핑/체이닝, 가능한 단순하게.
- 완성 후 사용 예시 공유.

주요 엔드포인트: `/api/datasets`, `/api/models`, `/api/spaces`, `/api/collections`, `/api/daily_papers`, `/api/notifications`, `/api/settings`, `/api/whoami-v2`, `/api/trending`, `/oauth/userinfo`. (전체 ~160개는 OpenAPI 스펙을 jq로 조회)

참조 예제 스크립트(skill 디렉토리 기준):
- `references/hf_model_papers_auth.sh` — trending → 모델 메타데이터 → 모델카드 파싱 체이닝 + auth 위생
- `references/find_models_by_paper.sh` — `--token` 옵션, arXiv 접두 검색 retry 경로
- `references/hf_model_card_frontmatter.sh` — `hf` CLI로 카드 다운로드, YAML frontmatter 추출, NDJSON 출력
- `references/baseline_hf_api.{sh,py,tsx}` — 초간단 raw JSON 베이스라인 (3개 언어)
- `references/hf_enrich_models.sh` — stdin의 모델 ID → 메타데이터 → 라인당 1 JSON (스트리밍 파이프)

`hf` CLI 서브커맨드 그룹: auth, buckets, cache, collections, datasets, discussions, download, endpoints, env, extensions, jobs, models, papers, repos, skills, spaces, sync, upload, webhooks 등 (deprecated `huggingface-cli` 대체).

<a id="huggingface-tool-builder---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-tool-builder/SKILL.md`

## huggingface-trackio

> Trackio로 ML 학습 실험의 메트릭을 로깅·시각화하고, 알림 발화·메트릭 조회까지 다루는 스킬.

<a id="huggingface-trackio---용도"></a>
### 📌 용도
Trackio는 ML 학습 메트릭을 로깅하고 시각화하는 실험 추적 라이브러리다. Hugging Face Spaces로 동기화되어 실시간 모니터링 대시보드를 제공한다. 세 가지 인터페이스를 다룬다: (1) 학습 중 메트릭 로깅(Python API), (2) 학습 진단을 위한 알림 발화(Python API), (3) 학습 중/후 메트릭·알림 조회(CLI). 원격/클라우드 학습 시 `space_id`를 넘기면 인스턴스 종료 후에도 메트릭이 Space 대시보드에 영속된다. 알림은 LLM 에이전트의 자율 실험 반복을 위한 핵심 메커니즘으로, 진단 조건(loss spike, NaN gradient, 낮은 정확도, stall)을 코드에 삽입하고 터미널 출력/DB/대시보드/웹훅(Slack·Discord)으로 전달된다.

<a id="huggingface-trackio---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 학습 중 메트릭 로깅(Python API), 학습 진단 알림 발화, 로깅된 메트릭/알림 조회·분석(CLI). 실시간 대시보드 시각화, 웹훅 알림, HF Space 동기화, 자동화용 JSON 출력.
- **언제 쓰지 않는가**: 학습 자체 오케스트레이션(huggingface-llm-trainer/vision-trainer가 Trackio를 내부적으로 호출). 단순 모델 추론/배포.

<a id="huggingface-trackio---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```python
# 최소 로깅 설정
import trackio
trackio.init(project="my-project", space_id="username/trackio")
trackio.log({"loss": 0.1, "accuracy": 0.9})
trackio.log({"loss": 0.09, "accuracy": 0.91})
trackio.finish()

# 자율 실험 워크플로우 (알림 삽입)
trackio.init(project="my-project", config={"lr": 1e-4})
for step in range(num_steps):
    loss = train_step()
    trackio.log({"loss": loss, "step": step})
    if step > 100 and loss > 5.0:
        trackio.alert(title="Loss divergence", text=f"Loss {loss:.4f} high after {step} steps",
                      level=trackio.AlertLevel.ERROR)
    if step > 0 and abs(loss) < 1e-8:
        trackio.alert(title="Vanishing loss", text="Loss near zero — gradient collapse?",
                      level=trackio.AlertLevel.WARN)
trackio.finish()
```

```bash
# CLI 조회 (--json으로 자동화용 출력)
trackio list projects --json
trackio list runs --project my-project
trackio list metrics
trackio get metric --project my-project --run my-run --metric loss --json
trackio list alerts --project my-project --json --since "2025-01-01T00:00:00"
trackio show              # 대시보드 실행
trackio sync              # HF Space로 동기화
```

<a id="huggingface-trackio---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
Python API(로깅): `trackio.init(project, space_id, config)`, `trackio.log({...})`, `trackio.finish()`. TRL 통합은 `report_to="trackio"`. 원격 학습은 `space_id`로 Space 동기화·영속.

Python API(알림): `trackio.alert(title, text, level)`. 레벨 3종 `AlertLevel.INFO`/`WARN`/`ERROR`. 터미널 출력+DB 저장+대시보드 표시+선택적 웹훅.

CLI(조회): `trackio list projects|runs|metrics|alerts`, `trackio get project|run|metric`, `trackio show`(대시보드), `trackio sync`(Space 동기화). `--json` 플래그로 프로그래매틱 출력, `--since <timestamp>`로 신규 알림 폴링.

자율 ML 실험 워크플로우: ① 진단 알림 삽입 → ② 백그라운드 학습 실행 → ③ `trackio list alerts --json --since`로 폴링 → ④ `trackio get metric`으로 값 검사 → ⑤ 알림·메트릭 기반으로 중단·하이퍼파라미터 조정·재실행.

참조: `references/logging_metrics.md`(설정·TRL 통합·옵션), `references/alerts.md`(알림 API·웹훅·자율 워크플로우), `references/retrieving_metrics.md`(CLI 명령·JSON 포맷).

<a id="huggingface-trackio---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-trackio/SKILL.md`

## huggingface-vision-trainer

> HF Transformers + HF Jobs 클라우드 GPU로 객체탐지·이미지분류·SAM/SAM2 분할 비전 모델을 학습/파인튜닝하는 스킬.

<a id="huggingface-vision-trainer---용도"></a>
### 📌 용도
객체 탐지(D-FINE, RT-DETR v2, DETR, YOLOS), 이미지 분류(timm: MobileNetV3, MobileViT, ResNet, ViT/DINOv3 및 임의 Transformers 분류기), SAM/SAM2 분할 모델을 관리형 클라우드 GPU(HF Jobs)에서 학습한다. 로컬 GPU 설정 없이 학습하며 결과는 자동으로 Hub에 저장된다. COCO 형식 데이터셋 준비, Albumentations 증강, mAP/mAR 평가, accuracy 메트릭, bbox/point 프롬프트 SAM 분할, DiceCE loss, 하드웨어 선택, 비용 추정, Trackio 모니터링, Hub 영속화를 커버한다. 학습 스크립트는 `HfArgumentParser`를 쓰므로 모든 설정은 Python 변수 편집이 아니라 `script_args`로 전달한다.

<a id="huggingface-vision-trainer---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 객체 탐지, 이미지 분류, SAM/SAM2, segmentation, image matting, DETR/D-FINE/RT-DETR/ViT/timm/MobileNet/ResNet, bounding box 모델 학습 또는 비전 모델을 HF Jobs에서 파인튜닝.
- **언제 쓰지 않는가**: 텍스트/언어 모델 학습(huggingface-llm-trainer/trl-training), Jobs 인프라 비-학습 질문(hugging-face-jobs 스킬: secrets/하드웨어/토큰 등), sentence-transformers(train-sentence-transformers).

<a id="huggingface-vision-trainer---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
워크플로우: ① 전제 검증 → ② 데이터셋 검증(`dataset_inspector.py`) → ③ AskUserQuestion으로 데이터 크기·검증 분할·하드웨어 질문 → ④ 학습 스크립트 준비 → ⑤ `submitted_jobs/`에 저장·제출·보고.

```python
# 객체 탐지 (Python API — hf_jobs MCP 미가용 시)
from huggingface_hub import HfApi, get_token
api = HfApi()
OD_SCRIPT_ARGS = [
    "--model_name_or_path", "ustc-community/dfine-small-coco",
    "--dataset_name", "cppe-5", "--image_square_size", "640",
    "--output_dir", "dfine_finetuned", "--num_train_epochs", "30",
    "--per_device_train_batch_size", "8", "--learning_rate", "5e-5",
    "--eval_strategy", "epoch", "--save_strategy", "epoch",
    "--load_best_model_at_end", "--metric_for_best_model", "eval_map",
    "--greater_is_better", "True",         # Optional[bool]은 값 명시 필수
    "--no_remove_unused_columns",          # 필수: image 컬럼 보존
    "--no_eval_do_concat_batches",         # 필수: 이미지별 박스 수 다름
    "--push_to_hub", "--hub_model_id", "username/model-name",
    "--do_train", "--do_eval",
]
job_info = api.run_uv_job(
    script="scripts/object_detection_training.py",   # MCP는 코드/URL, run_uv_job은 파일 경로
    script_args=OD_SCRIPT_ARGS, flavor="t4-small", timeout=14400,
    env={"PYTHONUNBUFFERED": "1"},
    secrets={"HF_TOKEN": get_token()},     # run_uv_job은 get_token(), MCP는 "$HF_TOKEN"
)
print(f"Job ID: {job_info.id}")            # .id (NOT .job_id/.name)
```

```python
# hf_jobs MCP 도구 (선호) — script는 코드 문자열, timeout은 "4h", secrets는 "$HF_TOKEN"
hf_jobs("uv", {"script": training_script_content, "flavor": "a10g-large",
               "timeout": "4h", "secrets": {"HF_TOKEN": "$HF_TOKEN"}})
```

<a id="huggingface-vision-trainer---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
스크립트: `scripts/object_detection_training.py`, `image_classification_training.py`, `sam_segmentation_training.py`, `dataset_inspector.py`, `estimate_cost.py`.

제출 방법 차이: `hf_jobs()` MCP(script=코드/URL, timeout="4h", secrets="$HF_TOKEN") vs `HfApi().run_uv_job()`(script=파일 경로, timeout=초, secrets=get_token()). 둘 다 PEP 723 인라인 메타데이터 필요. `image`/`command` 파라미터 사용 금지(run_job용).

토큰 주입: 커스텀 스크립트는 `Trainer(...)` 생성 전 `training_args.hub_token = os.environ["HF_TOKEN"]` 주입 필수.

필수 플래그(OD): `--no_remove_unused_columns`, `--no_eval_do_concat_batches`, `--push_to_hub`, `--metric_for_best_model eval_map`, `--greater_is_better True`. (IC) `eval_accuracy`. (SAM) `--remove_unused_columns False`, `--prompt_type bbox|point`, `--dataloader_pin_memory False`.

데이터셋 요구: OD는 `objects.bbox`+`objects.category`(xywh/xyxy 자동 감지, 문자열 카테고리 자동 리매핑). IC는 `image`+`label`. SAM은 `image`+`mask`+프롬프트(`prompt` JSON 또는 `bbox`/`point` 컬럼, xyxy). 검증 결과: ✓READY / ✗NEEDS FORMATTING.

추천 모델: OD `ustc-community/dfine-small-coco`(10.4M, 시작점), IC `timm/mobilenetv3_small_100.lamb_in1k`(2.5M), SAM `facebook/sam2.1-hiera-small`(46M). 모두 <100M는 `t4-small`($0.40/hr) 충분.

타임아웃: 기본 30분 부족 — OD 최소 2-4시간, +30% 버퍼. 빠른테스트 1h, 개발 2-3h, 프로덕션 4-6h, 대형 6-12h.

Trackio: OD 스크립트는 자동 활성(`trackio.init/finish`), IC/SAM은 `--report_to trackio`. 대시보드 `https://huggingface.co/spaces/{username}/trackio`.

실패 모드: OOM(batch size↓), 데이터셋 형식, Hub push 401(토큰/hub_token/권한), timeout, KeyError 'test'(validation 폴백), 단일 클래스 0-d 텐서, 낮은 mAP. 참조: `references/timm_trainer.md`, `finetune_sam2_trainer.md`, `reliability_principles.md` 등.

<a id="huggingface-vision-trainer---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-vision-trainer/SKILL.md`

## huggingface-zerogpu

> Gradio Spaces의 ZeroGPU 하드웨어 코드 제약(`@spaces.GPU`, 프로세스 격리, duration/quota, CUDA 빌드)을 다루는 스킬.

<a id="huggingface-zerogpu---용도"></a>
### 📌 용도
Hugging Face Spaces의 ZeroGPU 하드웨어에서 ML 데모를 만들 때의 규칙과 패턴을 다룬다. `@spaces.GPU` 데코레이터, duration·quota 튜닝, 프로세스 격리(pickle), CUDA 가용성 모델, 동시성 안전성, CUDA 빌드 제약을 커버한다. ZeroGPU는 Gradio SDK Space 전용이며(Docker/Static은 스케줄 불가), PyTorch 우선이다. `import spaces`가 `torch.cuda.*`를 몽키패치해 module scope에서 `device="cuda"`가 동작하지만 실제 GPU는 `@spaces.GPU` 함수 안에서만 붙는다. `torch.compile`은 미지원이며 AoTI를 사용한다. backing GPU는 예고 없이 바뀌므로 정확한 VRAM/티어는 ZeroGPU 공식 문서를 확인한다.

<a id="huggingface-zerogpu---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `@spaces.GPU`를 쓰는 코드 작성/리뷰, ZeroGPU Space의 `python_version`/`requirements.txt` 구성, ZeroGPU 코드 제약(pickle 프로세스 격리, gr.State 시맨틱, no torch.compile, CUDA wheel-only 빌드, large/xlarge 사이징, dynamic duration). 사용자가 ZeroGPU·`@spaces.GPU`·`spaces` 패키지를 언급하거나 `PicklingError`/`illegal duration`/`flash-attn` wheel 빌드 실패를 겪을 때. `import spaces`/`@spaces.GPU` 코드만 보여도 트리거.
- **언제 쓰지 않는가**: 일반 Gradio 코딩(huggingface-gradio), Space 전반 빌드/배포/디버깅(huggingface-spaces), LoRA Space 빌드(huggingface-lora-space-builder). Docker/Static Space나 dedicated GPU.

<a id="huggingface-zerogpu---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```python
# 기본 패턴
import spaces           # torch보다 먼저
import torch
from transformers import pipeline
pipe = pipeline("text-generation", model="...", device="cuda")  # module scope

@spaces.GPU(duration=120)              # 현실적 worst-case로
def generate(prompt: str) -> str:
    return pipe(prompt, max_new_tokens=100)[0]["generated_text"]

# 디바이스 선택 관용구 (하드코딩 금지)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = AutoModel.from_pretrained("...").to(device)

# 가변 워크로드용 dynamic duration
def estimate_duration(prompt, steps):
    return int(steps * 3.5)
@spaces.GPU(duration=estimate_duration)
def generate(prompt, steps):
    return pipe(prompt, num_inference_steps=steps).images[0]

# 프로세스 경계: CUDA 텐서 직접 반환 금지 → CPU로
# return tensor.cpu()  또는  tensor.cpu().numpy()
```

```bash
# ZeroGPU 예제 캐싱 동작 로컬 재현
GRADIO_CACHE_EXAMPLES=true GRADIO_CACHE_MODE=lazy python app.py

# uv로 requirements 내보내기 (spaces 제외)
uv export --no-hashes --no-dev --no-emit-package spaces -o requirements.txt
```

<a id="huggingface-zerogpu---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
하드웨어 size: `large`(기본, 반쪽 GPU, 1x quota), `xlarge`(전체, 2x quota — 요청도 N×2로 계산).

핵심 규칙: ① 모델은 module scope에서 `.to("cuda")` 즉시 로드, ② GPU 함수에 `@spaces.GPU`(off-ZeroGPU에서는 no-op), ③ `duration`은 worst-case(기본 60s, 작을수록 큐 우선·quota 통과), ④ `torch.compile` 금지→AoTI(torch 2.8+), ⑤ `xlarge` 절약 사용.

duration/quota 3검사: tier-max(`illegal duration`), quota pre-check(`quota exceeded`, requested vs remaining), 노드 큐 우선순위. 작은 duration이 모두 유리.

프로세스 격리: `@spaces.GPU` 함수는 별도 프로세스, 인자/반환은 pickle. picklable만 가능(파일핸들/lock/lambda/closure는 `PicklingError`). CUDA 텐서 직접 반환 금지(`torch.cuda._lazy_init` 차단)→`.cpu()`. `gr.State`는 yield마다 pickle 복사(참조 시맨틱 아님), CUDA 텐서는 yield 전 CPU로.

동시성: 핸들러는 기본 병렬. ① mutable global 금지, ② 고정 출력 경로 금지(`tempfile`), ③ read-only global은 안전.

호출 단위: 핫루프 안에서 `@spaces.GPU` 호출 금지 — 루프 소유 외부 함수를 데코레이트.

CUDA 빌드: 빌드 단계 `nvcc` 없음(base `python:3.13`) — bare `flash-attn` 등 sdist 불가, prebuilt wheel만. 런타임은 `/cuda-image`에 `nvcc` 있음(AoTI용).

의존성: README frontmatter `python_version: "3.12"` 핀 사실상 필수. `spaces`는 requirements.txt에 넣지 않음(플랫폼 핀). 직접 URL wheel 설치 시 `torch==X.Y.Z`를 wheel 태그에 맞춰 핀.

로컬 개발: `import spaces`를 try/except no-op으로 감싸지 말 것(off-ZeroGPU에서 이미 no-op, `SPACES_ZERO_GPU` env로 게이트). 그냥 의존성에 추가하고 무조건 import.

참조: `references/concurrency.md`, `how-zerogpu-works.md`, `how-quota-works.md`, `cuda-and-deps.md`.

<a id="huggingface-zerogpu---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-zerogpu/SKILL.md`

## train-sentence-transformers

> sentence-transformers 모델(SentenceTransformer/CrossEncoder/SparseEncoder)을 학습/파인튜닝하는 라우터형 스킬.

<a id="train-sentence-transformers---용도"></a>
### 📌 용도
sentence-transformers 모델을 세 가지 타입에 걸쳐 학습/파인튜닝한다: `SentenceTransformer`(bi-encoder; dense 또는 static 임베딩; 검색·유사도·클러스터링·분류·패러프레이즈 마이닝·중복제거·멀티모달), `CrossEncoder`(reranker; 쌍 점수화, 2단계 검색/쌍 분류), `SparseEncoder`(SPLADE; 학습형 sparse 검색, inverted-index 백엔드). loss 선택, hard-negative 마이닝, evaluator, distillation, LoRA, Matryoshka, Hub 발행을 커버한다. **이 SKILL.md는 매뉴얼이 아니라 라우터**로, 작업에 맞는 references와 예제 스크립트를 어디서 로드할지 알려준다. 학습 스크립트는 이 파일만으로 합성하지 말고 타입별 프로덕션 템플릿(`scripts/train_<type>_example.py`)을 복사해 시작해야 한다(autocast helper, model-card 클래스, logger silencing, seed, TF32 등 핵심 scaffolding 포함).

<a id="train-sentence-transformers---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 임의의 sentence-transformers 학습 작업. "embedding model"/"vector search"/"similarity"→SentenceTransformer, "rerank"/"ranker"/"two-stage"→CrossEncoder, "SPLADE"/"sparse"/"inverted index"→SparseEncoder.
- **언제 쓰지 않는가**: 일반 LM 학습(huggingface-llm-trainer/trl-training), 비전 모델(huggingface-vision-trainer). sentence-transformers가 아닌 임베딩 라이브러리.

<a id="train-sentence-transformers---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# 전제
pip install "sentence-transformers[train]>=5.0"   # 멀티모달은 [train,image]/[audio]/[video]
pip install trackio                                # 선택 tracker (wandb/tensorboard/mlflow 가능)
hf auth login                                      # 또는 HF_TOKEN write scope (Hub push용)
```

워크플로우: ① 모델 타입 식별(모호하면 질문) → ② 타입별 §2 필수 reading 로드 → ③ `scripts/train_<type>_example.py` 복사 → ④ MODEL_NAME/DATASET_NAME/RUN_NAME/loss/evaluator 교체(loss↔data shape, metric_for_best_model 키 교차검증) → ⑤ 스모크 테스트(`max_steps=1`) → ⑥ 실행 → ⑦ `logs/experiments.md` 추가·반복 제안.

<a id="train-sentence-transformers---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
모델 타입 3종: `SentenceTransformer`(bi-encoder, 고정차원 dense), `CrossEncoder`(쌍 joint 점수화), `SparseEncoder`(SPLADE, 어휘 sparse 벡터).

타입별 필수 reading + 템플릿:
- SentenceTransformer: `references/losses_sentence_transformer.md`, `evaluators_sentence_transformer.md`, `model_architectures.md`, `scripts/train_sentence_transformer_example.py`
- CrossEncoder: `references/losses_cross_encoder.md`(non-BCE는 `activation_fn=Identity()` 필수), `evaluators_cross_encoder.md`, `scripts/train_cross_encoder_example.py`
- SparseEncoder: `references/losses_sparse_encoder.md`(`SpladeLoss` 래퍼·FLOPS 정규화), `evaluators_sparse_encoder.md`, `scripts/train_sparse_encoder_example.py`

교차 reading(항상): `references/training_args.md`(precision: fp32 로드+autocast bf16/fp16, `torch_dtype=bfloat16` 금지; save_steps는 eval_steps 배수), `dataset_formats.md`(컬럼 매칭·hard-negative 마이닝), `base_model_selection.md`(ModernBERT max_seq_length=8192 함정, datasets>=4 script-loader 거부), `troubleshooting.md`.

적용 시 로드: `hardware_guide.md`(>24GB/멀티GPU/HF Jobs), `hf_jobs_execution.md`, `prompts_and_instructions.md`(E5/BGE/GTE/Qwen3-Embedding 등 프롬프트 튜닝 베이스).

variant 스크립트: matryoshka, multi_dataset, with_lora, distillation, make_multilingual, static_embedding(ST); distillation, listwise(CE); distillation(SE); `mine_hard_negatives.py`.

산출 스크립트 제약(비협상): `trainer.train()` 전 `baseline_eval` 캡처, 종료 라인 `VERDICT: WIN|MARGINAL|REGRESSION | score=... | baseline=... | delta=...`, httpx/httpcore/huggingface_hub 등 WARNING 무음, `logs/{RUN_NAME}.log` tee, `model.push_to_hub(...)` try/except, 긴 실행 전 스모크 테스트. CE는 `EarlyStoppingCallback(patience>=3)`, SE는 verdict에 `query/corpus_active_dims` 로깅.

기본값: 로컬 실행(맞지 않을 때만 HF Jobs), 단일 run, 종료 시 public Hub push(try-except), HF Jobs는 in-trainer push도(`push_to_hub=True`+`hub_strategy="every_save"`).

<a id="train-sentence-transformers---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/train-sentence-transformers/SKILL.md`

## transformers-js

> Transformers.js로 최신 ML 모델을 JavaScript/TypeScript에서 직접 실행하는 스킬 (브라우저·Node.js·Bun·Deno, WebGPU/WASM).

<a id="transformers-js---용도"></a>
### 📌 용도
Transformers.js를 사용해 최신 머신러닝 모델을 Python 서버 없이 JavaScript에서 직접 실행한다. 브라우저와 서버사이드 런타임(Node.js, Bun, Deno)에서 WebGPU/WASM으로 Hugging Face Hub의 사전학습 모델을 구동한다. NLP(텍스트 분류·번역·요약·생성), 컴퓨터 비전(이미지 분류·객체 탐지·분할·깊이 추정), 오디오(음성 인식·오디오 분류·TTS), 멀티모달(이미지 캡셔닝·문서 QA·zero-shot) 작업을 지원한다. 핵심은 `pipeline` API(전처리+추론+후처리 묶음)이며, 모든 파이프라인은 사용 후 `pipe.dispose()`로 메모리를 해제해야 한다.

<a id="transformers-js---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: JavaScript에서 텍스트 분석/생성/번역 ML 모델 실행, 이미지 분류/객체탐지/분할, 음성 인식/오디오 처리, 멀티모달 AI 앱(텍스트→이미지, 이미지→텍스트), 백엔드 없이 브라우저 클라이언트사이드 모델 실행.
- **언제 쓰지 않는가**: Python 기반 추론/학습(transformers, huggingface-llm-trainer 등), 로컬 GGUF/llama.cpp(huggingface-local-models). 서버에 Python ML 백엔드를 두는 경우.

<a id="transformers-js---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
npm install @huggingface/transformers
```

```javascript
// CDN (브라우저)
import { pipeline } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers';

// Pipeline API
import { pipeline } from '@huggingface/transformers';
const pipe = await pipeline('sentiment-analysis');
const result = await pipe('I love transformers!');
// [{ label: 'POSITIVE', score: 0.9998 }]
await pipe.dispose();   // 필수: 메모리 해제

// 커스텀 모델 + 디바이스 + 양자화
const gen = await pipeline('text-generation', 'onnx-community/gemma-3-270m-it-ONNX',
  { device: 'webgpu', dtype: 'q4' });   // dtype: fp32|fp16|q8|q4
const out = await gen('Once upon a time', { max_new_tokens: 100, temperature: 0.7 });

// 임베딩 (mean pooling + normalize)
const ext = await pipeline('feature-extraction', 'onnx-community/all-MiniLM-L6-v2-ONNX');
const emb = await ext('Text to embed', { pooling: 'mean', normalize: true });

// 진행률 콜백
const clf = await pipeline('sentiment-analysis', null, { progress_callback: onProgress });
```

```javascript
// env 전역 설정
import { env } from '@huggingface/transformers';
env.allowRemoteModels = true; env.useFSCache = true; env.cacheDir = './.cache';
```

**비공개·gated 모델 인증**: 서버(Node.js)의 실행 환경에 `HF_TOKEN`을 주입하면 라이브러리가 Hugging Face Hub 요청에 인증 헤더를 붙인다. 전역 `env.fetch`로 모든 URL에 토큰을 붙이지 않는다. 브라우저 코드·번들에 비밀 토큰을 넣지 않으며, 공개 모델은 토큰 없이 사용한다. [공식 서버 인증 안내](https://huggingface.co/docs/transformers.js/guides/private)를 따른다.

<a id="transformers-js---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
핵심 개념: ① pipeline API(가장 쉬움), ② 모델 선택(2번째 인자), ③ device(`webgpu` 또는 기본 WASM/CPU), ④ 양자화 dtype(`fp32`/`fp16`/`q8`/`q4`).

지원 태스크(태스크 ID): text-classification(sentiment-analysis), token-classification(ner), question-answering, fill-mask, summarization, translation, text-generation, zero-shot-classification, image-classification, image-segmentation, object-detection, depth-estimation, zero-shot-image/object-detection, automatic-speech-recognition, audio-classification, text-to-speech, image-to-text, document-question-answering, feature-extraction, sentence-similarity.

모델 찾기: `https://huggingface.co/models?library=transformers.js&sort=trending`, `pipeline_tag`로 필터. ONNX 파일(onnx 폴더) 확인 필수.

고급: `ModelRegistry`(파일 목록·캐시 상태·dtype 검사·캐시 정리), `@huggingface/tokenizers`(토크나이저 전용 경량 패키지), `AutoTokenizer`/`AutoModel`(저수준 제어), 배치 처리.

메모리 관리(중요): `pipe.dispose()` 필수 — 앱 종료/언마운트, 다른 모델 로드 전, 배치 후. 모델은 100MB~수GB 점유.

런타임: WebGPU(Chrome/Edge 113+, fp16 폴백), WASM(가장 호환). 모델 자동 캐싱(브라우저 Cache API/Node FS).

참조: `references/PIPELINE_OPTIONS.md`, `CONFIGURATION.md`, `MODEL_REGISTRY.md`, `CACHE.md`, `TEXT_GENERATION.md`(스트리밍·chat), `MODEL_ARCHITECTURES.md`, `EXAMPLES.md`.

베스트 프랙티스: 항상 dispose, pipeline 우선, 버전 핀(`revision`), try-catch, 파이프라인 재사용, 서버 SIGTERM/SIGINT 시 dispose.

<a id="transformers-js---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/transformers-js/SKILL.md`

## trl-training

> TRL(Transformers Reinforcement Learning) CLI 명령으로 LM을 학습/파인튜닝하는 스킬 (SFT/DPO/GRPO/KTO/RLOO/Reward).

<a id="trl-training---용도"></a>
### 📌 용도
TRL 라이브러리의 CLI 명령으로 트랜스포머 언어 모델을 학습/파인튜닝한다. SFT(지도 파인튜닝), DPO(선호 데이터 정렬), GRPO(여러 샘플 출력을 상대 보상으로 랭킹·최적화), RLOO(생성 기반 보상 온라인 RL), Reward Model 학습(RLHF용)을 지원한다. Hugging Face Transformers와 Accelerate 위에 구축되어 HF 생태계와 매끄럽게 통합된다. YAML 설정 파일로 재현 가능한 학습을 지원하고, Accelerate로 멀티 GPU/멀티 노드(FSDP, DeepSpeed ZeRO) 분산 학습을 한다. LoRA(`--use_peft`)로 효율적 학습이 가능하다.

<a id="trl-training---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: TRL CLI 명령(`trl sft`/`dpo`/`grpo`/`kto`/`rloo`/`reward`)으로 LM 학습/파인튜닝. SFT/DPO/GRPO/RLOO/Reward Model 학습.
- **언제 쓰지 않는가**: 클라우드 GPU/HF Jobs 기반 학습이나 인라인 UV 스크립트(huggingface-llm-trainer가 hf_jobs MCP로 다룸), 비전 모델(huggingface-vision-trainer), sentence-transformers(train-sentence-transformers). 본 스킬은 로컬/터미널 TRL CLI 중심.

<a id="trl-training---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```bash
# SFT (지도 파인튜닝)
trl sft --model_name_or_path Qwen/Qwen2-0.5B --dataset_name trl-lib/Capybara \
  --learning_rate 2.0e-5 --num_train_epochs 1 --packing \
  --per_device_train_batch_size 2 --gradient_accumulation_steps 8 \
  --eos_token '<|im_end|>' --eval_strategy steps --eval_steps 100 \
  --output_dir Qwen2-0.5B-SFT --push_to_hub
# LoRA: --use_peft --lora_r 32 --lora_alpha 16 (learning_rate는 2.0e-4)

# DPO (선호 정렬)
trl dpo --dataset_name trl-lib/ultrafeedback_binarized --model_name_or_path Qwen/Qwen2-0.5B-Instruct \
  --learning_rate 5.0e-7 --max_steps 1000 --per_device_train_batch_size 2 \
  --gradient_accumulation_steps 8 --eval_strategy steps --eval_steps 50 \
  --output_dir Qwen2-0.5B-DPO --no_remove_unused_columns

# GRPO (보상 함수/LLM-as-judge)
trl grpo --model_name_or_path Qwen/Qwen2.5-0.5B --dataset_name trl-lib/gsm8k \
  --reward_funcs accuracy_reward --output_dir Qwen2-0.5B-GRPO --push_to_hub

# RLOO (온라인 RL)
trl rloo --model_name_or_path Qwen/Qwen2.5-0.5B --dataset_name trl-lib/tldr \
  --reward_model_name_or_path sentiment-analysis:nlptown/bert-base-multilingual-uncased-sentiment \
  --output_dir Qwen2-0.5B-RLOO --push_to_hub

# Reward Model
trl reward --model_name_or_path Qwen/Qwen2-0.5B-Instruct --dataset_name trl-lib/ultrafeedback_binarized \
  --output_dir Qwen2-0.5B-Reward --per_device_train_batch_size 8 --num_train_epochs 1 \
  --learning_rate 1.0e-5 --eval_strategy steps --eval_steps 50 --max_length 2048
# LoRA: --use_peft --lora_task_type SEQ_CLS --lora_r 32 --lora_alpha 16
```

```bash
# YAML 설정 + 오버라이드
trl sft --config sft_config.yaml
trl sft --config sft_config.yaml --learning_rate 1.0e-5

# 분산 학습 (Accelerate)
trl sft --config sft_config.yaml --num_processes 4
trl sft --config sft_config.yaml --accelerate_config zero2     # fsdp2, zero3 등
```

<a id="trl-training---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
코어 명령: `trl sft`, `trl dpo`, `trl grpo`, `trl kto`, `trl rloo`, `trl reward`.

학습 방법: SFT(명령/대화 데이터셋), DPO(chosen/rejected 선호), GRPO(상대 보상 랭킹), RLOO(생성 기반 보상), Reward Model(텍스트 품질 점수).

설정 파일: YAML로 모든 CLI 인자 지정, `--config`로 실행, CLI 플래그로 오버라이드.

분산 학습: `--num_processes`(멀티 GPU), 사전 정의 config `single_gpu`/`multi_gpu`/`fsdp1`/`fsdp2`/`zero1`/`zero2`/`zero3`, `--accelerate_config`, 커스텀은 `accelerate config` + `--config_file`.

주요 옵션: `--use_peft`(LoRA), `--lora_r`/`--lora_alpha`/`--lora_task_type`, `--packing`(짧은 시퀀스), `--gradient_checkpointing`, `--tf32`/`--bf16`, `--push_to_hub`, `--report_to trackio|wandb|tensorboard`, `--reward_funcs`(GRPO), `--reward_model_name_or_path`(RLOO).

트러블슈팅: CUDA OOM(batch size↓/grad accum↑, use_peft, gradient_checkpointing), 데이터셋 로딩(형식·`--dataset_config`), 모델 로딩(`hf auth login` for gated), 느린 학습(packing, bf16, tf32, 멀티GPU), 생성 이슈(GRPO/RLOO의 temperature/top_p/reward 함수).

베스트 프랙티스: 선호 정렬 전 SFT 먼저, LoRA로 효율, `--report_to`로 모니터링, 작은 데이터셋 선검증, YAML config 재현성, Accelerate 활용.

<a id="trl-training---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/trl-training/SKILL.md`
