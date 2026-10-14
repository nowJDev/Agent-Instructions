<!-- 리뷰 수정과 README 재작성의 실행 순서와 검증 기준을 기록한다. -->
# 리뷰 수정과 입문자용 README 실행 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 독립된 문서 영역은 `rules/02`에 따라 위임하고 전체 diff를 통합 검토한다.

Goal: 승인된 네 가지 결함을 해결하고 README 전체를 AI 입문자용으로 재작성한다.
Architecture: 기존 카탈로그와 표준 라이브러리 기반 검증기를 유지한다. [설계](../specs/2026-10-14-beginner-readme-and-audit-fixes.md)의 범위만 수정한다.
Tech Stack: Markdown, Python unittest, Mermaid, Git, Windows PowerShell.

## Task 1. 완료 검사.

Files: `tests/test_workflow_markdown.py`, `Owned-Skills/design-driven-delivery/scripts/validate_workflow.py`, `Owned-Skills/design-driven-delivery/references/document-contracts.md`.

- [x] 미완료 세 상태와 컨테이너 6종의 18개 사례에서 기존 exit 0 누락을 RED로 확인했다.
- [x] 명시적 목록·인용 접두사를 검사하며 코드 예시를 제외한다. 독립 검토의 재귀 fence 오탐 3개도 RED 후 동일한 컨테이너 순서로 처리해 해결했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_workflow_markdown.py -v`의 Markdown 회귀 22개 GREEN, 문서 계약과 독립 리뷰를 확인했다. 검증한 코드·회귀·문서를 함께 커밋한다.

## Task 2. 업로드 경계와 지침 파일명.

Files: `Skill/huggingface-skills/huggingface-datasets.md`, `Skill/huggingface-skills/huggingface-lora-space-builder.md`, `Skill/claude-md-management/claude-md-improver.md`, 필요하면 문서 예제 회귀 테스트.

- [ ] 공식 `repo_info(...).private` 계약을 확인하고 비공개 조회 없이 진행하는 기존 예시를 인증 없는 fixture로 재현한다.
- [ ] 두 업로드 예시에 `if api.repo_info(repo_id=repo_id, repo_type=...).private is not True: raise RuntimeError(...)`를 업로드 앞에 배치한다. 조회 오류는 전파하고 기존 공개 저장소를 변경하지 않는다.
- [ ] 세션 업로드 원본은 승인·민감정보 제거를 마친 별도 폴더로 제한하고 전역 폴더 직접 업로드를 제거한다. 파일명은 `CLAUDE.local.md`로 수정한다.
- [ ] 가짜 API로 비공개 통과·공개 중단·조회 실패 중단·전송 범위를 확인하고 예제 문법과 파일명 검색을 검사한 뒤 커밋한다.

## Task 3. README 전체 재작성.

Files: `README.md`, `GUIDE.md`, 삭제할 `index.html`과 제목 변경의 직접 참조가 있는 `AGENTS.md`, `codex-global-AGENTS.md`, `PORTABILITY.md`, `rules/02_tool-boundaries.md`.

- [ ] 시작 프롬프트 두 종류와 쉬운 설명, 작업 흐름·구조도, 용어 설명, 문서 안내로 전체를 재작성한다. 긴 전체 도구 목록은 기존 목차로 연결한다.
- [ ] 지침 적용과 설치의 차이, 사용자 지정 대상·설정 홈·기존 설정 보존·인증·별도 확장 계약을 유지한다. 제목의 직접 참조를 갱신한다.
- [ ] 입문자 관점으로 전체 문장을 다시 읽고 로컬 링크·앵커·Mermaid 문법을 검사한 뒤 커밋한다.
- [ ] 추가 승인에 따라 `index.html` 상세 안내를 `GUIDE.md`로 변환하고 README에서 연결한다. 사람이 읽는 설명과 AI 지침 문서의 역할을 분리하며 HTML은 변환 검증 후 개별 삭제한다.

## Task 4. 종료 검증과 기록.

Files: `CHANGELOG.md`, `docs/reviews/2026-10-14-beginner-readme-and-audit-fixes.md`, 이 계획.

- [ ] 전체 `python -X utf8 -B -m unittest discover -s tests -v`, 예제 문법·UTF-8·BOM·LF·링크·앵커·fence와 `git diff --check`를 확인한다.
- [ ] 기준선부터 전체 diff를 독립 검토하고 중요한 발견을 해결한 뒤 관련 검증을 반복한다.
- [ ] 결과와 실제 외부 서비스·전역 설치·렌더링의 확인 범위를 기록한다. 검증한 변경을 한글 커밋으로 저장하고 푸시 없이 브랜치·작업 트리를 보존한다.
