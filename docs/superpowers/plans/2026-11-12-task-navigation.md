# 분야별 스킬 안내 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 분야별 선택 안내와 README 진입점을 추가하고 검증된 문서를 전역에 독립 복제한다.

**Architecture:** 기존 출처별 설명과 144개 카탈로그 링크를 보존하며 BY-TASK 한 파일을 추가한다. 검증된 저장소 파일을 백업 후 전역에 복사하고 전역 진입점의 개인 지침을 보존한다.

**Tech Stack:** UTF-8 Markdown, Python 표준 라이브러리·unittest, PowerShell, Git.

**Spec:** [승인 설계](../specs/2026-11-12-task-navigation-design.md).

## Global Constraints

- 기존 144개 상세 항목·26그룹과 설치 스킬·고정 명세·인증·권한을 보존한다.
- 명시 호출·과거 비활성·클라이언트 가용성의 경계를 유지한다.
- 전역은 독립 물리 복제하며 전역 밖 검증 백업과 개인 마무리 지침을 보존한다.
- 개인 경로·개인 문서·백업·실행 로그를 공개 저장소에 넣지 않는다.

## Review Focus

- 분야 안내의 목적지가 기존 카탈로그 또는 자체 제작 패키지인가.
- 명시 호출 전용 도구를 자동 선택 도구처럼 안내하지 않는가.
- 같은 도구를 여러 분야에서 같은 상세 주소로 찾을 수 있는가.
- 한영 README와 기존 카탈로그 진입점이 함께 유지되는가.
- 원본 저장소 없이도 전역의 상대 링크와 스킬 설치 경로가 완결하는가.

## Task 1: 분야 안내와 진입점.

**Files:** `Skill/BY-TASK.md`, `Skill/CATALOG.md`, `Skill/README.md`, `README.md`, `README.en.md`, `tests/test_documentation.py`.

**Interfaces:** 기존 카탈로그의 상세 링크와 Owned-Skills 원본 주소를 소비하고 12개 `task-*` 앵커를 제공한다.

- [x] 새 분야·기존 목적지·대표 작업·진입점·명시 호출·공유 도구를 검사하는 테스트를 추가하고 안내·진입점 부재의 RED를 확인했다.
- [x] 분야별 표와 기존 상세 링크, 한영 README·카탈로그 진입점을 구현했다.
- [x] 문서 대상 11개 테스트 GREEN과 엑셀·PPT·한글·디버깅의 대표 경로를 확인했다.

## Task 2: 독립 전역 복제와 전체 검증.

**Files:** 전역 문서 복제본·전역 AGENTS의 개인 병합, `CHANGELOG.md`, `docs/current-state.md`, `docs/design-progress-checklist.md`, `docs/reviews/2026-11-12-task-navigation.md`.

**Interfaces:** Task 1의 문서 집합을 전역 상대경로·해시 동일성과 자기완결 링크로 검증한다.

- [x] 전역 기존 165개 문서와 진입점을 비공개 위치에 백업하고 파일 집합·SHA를 대조했다.
- [x] 저장소 문서를 물리 복사하고 확인된 extra 8개는 백업 보존 후 개별 제거했다.
- [x] 전역 템플릿과 개인 마무리 절, 177개 파일의 동일성·148개 Markdown 링크·설치 경로 보존을 확인했다.
- [x] 저장소 전체 106개 회귀·원본 접근 차단 전역 106개 회귀·공개 정보·diff 검사와 독립 전체 리뷰를 마쳤다.

## Task 3: 통합·푸시·정리.

**Files:** 이번 변경 전체와 검증 기록.

**Interfaces:** 검증된 작업 브랜치를 main으로 통합하고 원격 SHA와 CI를 확인한다.

- [x] 관련 변경을 한글 메시지의 `d7bffa3`으로 커밋하고 승인된 main 통합·일반 push를 수행했다.
- [x] 원격 SHA·두 OS CI 성공·전역 동일성을 확인하고 소유 임시 worktree·브랜치를 정리했다. 최종 증거 문서도 다시 복제·검사한다.

## 실행 판단.

사용자의 명시적 구현·커밋·푸시 요청으로 이 계획을 연속 실행한다. 네이티브 worktree 도구는 현재 태스크의 홈 디렉터리를 저장소로 인식하지 못해 실패했으므로 사용자 영역의 별도 Git worktree를 사용한다. 로컬 기본 Python은 3.11.9이며 기준선 전체 103개 테스트는 실패·skip 없이 통과했다. CI는 기존 Python 3.12 구성을 유지한다.
