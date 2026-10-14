<!-- Chrome DevTools MCP 안내와 전역 지침 반영 순서를 기록한다. -->
# Chrome DevTools MCP 문서 반영 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 독립 조사·리뷰는 `rules/02`에 따라 위임한다.

Goal: 승인된 MCP 사용 방침을 저장소와 Codex 전역 지침에 반영한다.
Architecture: [설계](../specs/2026-10-14-chrome-devtools-mcp.md)에 따라 기존 분류를 유지하고 상세 안내 한 문서를 연결한다.
Tech Stack: Markdown, Python unittest, Git, Windows PowerShell.

## Task 1. 카탈로그와 선택 규칙.

Files: `AGENTS.md`, `codex-global-AGENTS.md`, `MCP/README.md`, `MCP/chrome-devtools.md`, `PORTABILITY.md`, `rules/02_tool-boundaries.md`, `CHANGELOG.md`.

- [x] 사용자 지정 도구 우선·Chrome DevTools MCP 우선·Firecrawl 유지 규칙을 작성하고 상세 문서에서 자동 실행·별도 프로필·공식 출처·설치 상태를 안내한다.
- [x] `python -X utf8 -B -m unittest discover -s tests -v`, `git diff --check`와 UTF-8·BOM·상대링크 검사를 통과하고 전체 diff를 독립 리뷰한다. 문서 수정이므로 구현 RED·TDD는 해당하지 않는다.

## Task 2. 전역 반영과 통합.

Files: 이 계획과 `docs/reviews/2026-10-14-chrome-devtools-mcp.md`. 개인 경로는 저장소에 기록하지 않는다.

- [x] 실제 Codex 전역 지침의 사용자 고유 내용을 보존하고 변경 문서를 전역 복제본에 동기화한다. 파일 내용과 링크를 검증한다.
- [x] 검증·리뷰 결과를 기록하고 관련 파일만 한글 커밋한다. 로컬 main에 반영한 뒤 임시 브랜치·작업 폴더를 정리한다. 원격 푸시는 하지 않는다.
