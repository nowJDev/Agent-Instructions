# 전체 리뷰 발견 사항 수정 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 사용자 요청으로 아래 11건의 수정 실행을 승인받았다.

## 목표와 설계.

기준선은 `b9b443c`다. 전체 리뷰의 11건을 해결한다. Python 표준 라이브러리와 HTML 기본 체크박스를 사용하며 의존성을 추가하지 않는다. 실제 전역 설정·Notion 데이터·원격 저장소는 변경하지 않는다.

Notion 수정은 대상 블록 업데이트를 기본으로 한다. 훅은 matcher가 아닌 전체 설정 내용으로 중복을 제거한다. 백업은 정확한 새 디렉터리 하나에 선택된 원본만 복사한다. MCP·hooks 안내는 공식 클라이언트 스키마에 맞춘다.

작업 문서 경로는 초기화와 검사에서 같은 선택 함수를 사용한다. 기존 `docs/specs`·`docs/plans`가 있으면 유지하고, 없으면 기본 구조를 사용한다. 다른 승인 구조는 수동으로 유지한다. 완료 검증은 `--spec`, `--plan`, `--review`로 현재 문서를 지정할 수 있으며 경로는 프로젝트 내부의 Markdown 파일이어야 한다. 미지정 종류는 기존 전체 검사 동작을 유지한다. 파일 생성에는 배타적 생성 모드를 사용해 다른 작업자가 만든 파일을 보존한다.

## Task 1. 스크립트와 예제 회귀.

Files: `tests/test_review_regressions.py`, `Owned-Skills/design-driven-delivery/scripts/{bootstrap_workflow,validate_workflow,workflow_paths}.py`, `references/claude-code-cli-setup.md`.

- [x] 재현 테스트를 작성하고 `python -X utf8 -B -m unittest discover -s tests -v`에서 기존 구조 훼손·경쟁 생성·과거 문서 검사·훅 병합 실패를 확인한다.
- [x] 공유 경로 선택, `open("xb")`, 작업별 문서 선택, 내용 기준 훅 병합을 구현하고 같은 명령의 통과를 확인한다.
- [x] Bash 백업 예제를 임시 디렉터리에서 반복 실행해 과거 백업 유입과 오류 은폐가 없는지 확인한다.
- [x] 최종 리뷰에서 발견한 템플릿 읽기·복사 중단의 불완전 파일 잔존을 실패 테스트로 재현하고 정리·재시작 동작을 검증한다.

## Task 2. API·설정 안내 및 키보드 접근성.

Files: `rules/02_tool-boundaries.md`, `MCP/notion.md`, `Skill/plugin-dev/hook-development.md`, `PORTABILITY.md`, `GETTING_STARTED.md`, `index.html`, `Owned-Skills/design-driven-delivery/{SKILL.md,references/document-contracts.md}`, `Skill/_personal/design-driven-delivery.md`.

- [x] Notion 전체 삭제 기본값·데이터 소스 검색, 사용자 hooks 루트, Claude MCP 범위·프로젝트 설정 지원, VS Code `servers` 스키마를 공식 문서 근거와 함께 수정한다.
- [x] HTML 체크리스트에 기본 checkbox와 label을 쓰고 별도 클릭 토글 코드를 제거한다. Chrome에서 Tab·Space와 label 클릭을 확인한다.
- [x] 전체 문서 링크·UTF-8·코드 블록·차이 검사와 전체 회귀를 실행한다.

## Task 3. 리뷰와 전달.

- [x] 기준선 대비 전체 변경을 리뷰하고 검증 결과를 `docs/reviews/2026-10-13-review-fixes.md`에 기록한다.
- [x] 계획의 검증 상태와 한글 커밋 메시지·로컬 main 통합 절차를 준비한다. 검증된 변경은 커밋 후 로컬 main으로 fast-forward 통합하고 원격에는 push하지 않는다.

## 자동 검증 명령.

```powershell
python -X utf8 -B -m unittest discover -s tests -v
git diff --check
```

실패 경로는 누락·외부 경로·미완료 문서·기존 경로 충돌·경쟁 생성이며, 백업 실패 시 설치를 진행하지 않는다. 브라우저 검증이나 테스트가 실패하면 완료 표시와 커밋 전에 원인을 수정한다.
