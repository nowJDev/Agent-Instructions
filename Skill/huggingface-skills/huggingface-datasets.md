# huggingface-datasets

> Hugging Face Dataset Viewer API로 데이터셋 메타데이터·행 페이지네이션·검색·필터·parquet URL을 읽는 스킬.

## 📌 용도
Hugging Face Dataset Viewer API를 사용한 읽기 전용 데이터셋 탐색/추출 워크플로우를 담당한다. subset/split 메타데이터를 가져오고, 행을 페이지네이션하고, 텍스트 검색과 필터(predicate)를 적용하고, parquet URL을 다운로드하고, 크기/통계를 읽는다. 데이터셋 가용성 검증(`/is-valid`)부터 시작해 config·split 해석, 미리보기, 페이지네이션, 검색/필터, parquet/size/statistics 조회까지의 코어 워크플로우를 제공한다. 데이터셋 생성/업로드(Hub UI, `@huggingface/hub` CLI), 에이전트 트레이스(JSONL) 업로드도 다룬다.

## 🎯 트리거 조건
- **언제 호출되는가**: HF 데이터셋의 subset/split 메타데이터 조회, 행 페이지네이션, 텍스트 검색, 필터 적용, parquet URL 다운로드, 크기/통계 읽기 등 Dataset Viewer API 워크플로우. 데이터셋 생성/업로드, 에이전트 세션 트레이스(Claude Code/Codex/Pi)를 데이터셋으로 올리는 작업.
- **언제 쓰지 않는가**: CLI 기반 parquet URL 탐색이나 SQL은 `hf-cli` 스킬의 `hf datasets parquet`/`hf datasets sql` 사용. 데이터셋으로 모델을 학습하는 작업은 학습 전용 스킬.

## 💻 사용 예시 / 명령어
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

## 🛠️ 제공 도구 / 주요 파라미터
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

## 📦 출처 / 설치 상태
- 플러그인: huggingface-skills@claude-plugins-official
- 활성화: ON
- 관련 MCP: [Hugging Face MCP](../../MCP/huggingface-skills.md). 인증과 실제 도구 확인은 해당 문서를 따른다.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/huggingface-skills/1.0.8/skills/huggingface-datasets/SKILL.md`
