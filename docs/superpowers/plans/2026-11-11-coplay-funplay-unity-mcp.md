<!-- Unity MCP 설치 문서의 변경 파일과 검증 순서를 기록한다. -->
# Unity MCP 설치 구현 계획.

> **For agentic workers:** 이 계획은 현재 세션에서 실행하며 문서 검증 뒤 전체 변경을 리뷰한다.

**Goal:** CoplayDev/unity-mcp 전역 서버를 준비하고 두 MCP의 프로젝트별 설치·연결 절차를 공개 카탈로그와 전역 스킬에 반영한다.

**Architecture:** 기존 MCP 목차·이식 표에 항목을 추가하고 `MCP/coplay-funplay-unity-mcp.md`에서 상세 절차를 관리한다. 개인 설정과 실행 패키지는 공개 저장소 밖에 둔다.

**Tech Stack:** Markdown, Codex MCP, Unity UPM, 기존 Python unittest.

**Spec:** [설계](../specs/2026-11-11-coplay-funplay-unity-mcp-design.md).

## 제약과 리뷰 초점.

개인 경로·설정·토큰은 공개 문서에 넣지 않는다. 기존 서버 등록·사용자 파일을 보존한다. CoplayDev/unity-mcp의 서버/Unity 패키지 버전 정합성, FunplayAI/funplay-unity-mcp의 프로젝트별 주소·포트 충돌, 닫힌 Unity의 연결 실패, 여러 Editor의 대상 구분, 미검증 항목의 완료 과장을 검토한다.

## 작업.

- [x] 기준선 `1900d96`의 깨끗한 상태와 격리 worktree를 확인했다.
- [x] 변경 전 전체 84개 unittest가 통과했다.
- [x] `MCP/README.md`, `PORTABILITY.md`, `MCP/coplay-funplay-unity-mcp.md`에 설치·등록·검증 안내를 작성했다.
- [x] 사용자 확정에 따라 프로젝트 설치를 연기하고 `Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md`와 목차를 추가했다.
- [x] `tests/test_owned_skill_packages.py`의 패키지 집합을 추가해 스킬 누락 RED와 작성 후 8개 검사 GREEN을 확인했다.
- [x] 변경 후 전체 84개 unittest와 `git diff --check`를 통과했다.
- [x] 전체 문서 diff를 자체 검토하고 검증 기록·현재 상태·체크리스트를 갱신했다.

전역 설정 등록·Unity 패키지 설치와 실제 연결 결과는 설치 담당의 증거를 기록한다. 문서 검증 결과로 Unity 동작 검증을 대신하지 않는다.
