# Anthropic 스킬 설치 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 승인된 19개 Anthropic 스킬을 이름 충돌·중복·개인 파일 손실 없이 전역 설치한다.

**Architecture:** 공개 저장소는 설치 명세·설치기·카탈로그를 관리하고 실행 패키지는 사용자 전역 한 곳에 둔다. 공식 ZIP을 고정 SHA256으로 검증해 준비한 뒤, 사전 검사·백업·게시·복구 순으로 적용한다.

**Tech Stack:** Python 3.11 이상 표준 라이브러리, Windows 기본 icacls, unittest, Git, Codex app-server.

**Spec:** [승인 설계](../specs/2026-11-12-anthropic-skills-design.md).

## Global Constraints

- 고정 커밋은 `2c5958ecac7cee2b583967a2c4981d0f4a75c579`이며 설치 이름은 `anthropic-<원본명>`이다.
- 타사 실물·로컬 상태·개인 절대 경로·백업은 공개 저장소에 넣지 않는다.
- 자체 제작 claude-api, OpenAI 내장 스킬, 기존 설정·개인 파일을 보존한다.
- 사용자의 설계 실행 요청으로 이 계획을 같은 세션에서 실행한다. 별도 중간 승인을 반복하지 않는다.

## Review Focus

- 압축 파일 경로 탈출·링크·중복 항목은 쓰기 전에 거부한다.
- 미관리 대상·개인 수정·추가 파일이 있으면 이전과 덮어쓰기를 중단한다.
- 모든 패키지 사전 검사를 끝낸 후에만 전역을 바꾸며 게시 실패 시 복구한다.
- 이름 변경이 패키지 내부의 명시 호출·리소스 참조를 깨뜨리지 않아야 한다.
- 동일 설치 재실행과 검사 모드는 활성 파일·백업·상태 파일을 변경하지 않아야 한다.

---

### Task 1: 설치기와 안전 회귀.

**Files:** `scripts/install_anthropic_skills.py`, `references/anthropic-skills.lock.json`, `tests/test_anthropic_skills.py`.

**Interfaces:** `install(manifest, archive, home, apply=False)`는 검사 결과를 반환하고 apply에서만 사용자 디렉터리를 바꾼다. CLI 기본 명세는 저장소 상대경로로 찾는다.

- [x] 합성 ZIP을 사용하는 동작 테스트를 작성하고 설치기 부재의 RED를 확인했다.
- [x] 고정 ZIP 검증·변환·사전 검사·백업·복구·재실행 무변경을 구현했다.
- [x] 설치기 19개 GREEN과 전체 103개 회귀를 확인했다.

### Task 2: 출처 카탈로그와 운영 문서.

**Files:** `Skill/anthropic-skills/README.md`, `Skill/README.md`, `Skill/CATALOG.md`, `tests/test_documentation.py`, `docs/current-state.md`, `docs/design-progress-checklist.md`, `docs/reviews/2026-11-12-anthropic-skills.md`.

**Interfaces:** 카탈로그는 명세의 19개 설치 이름을 설명하고 실제 설치 상태와 구분한다.

- [x] 공급자별 안내·명세·명령·이전 대응표·호출 정책을 연결했다.
- [x] 새 그룹의 카탈로그 링크 검증을 확장하고 전체 회귀를 통과했다.

### Task 3: 실제 배포와 통합.

**Files:** 사용자 전역 19개 패키지, 탐색 경로 밖 원본·상태·백업, 위 검증 기록.

**Interfaces:** 동일 설치기를 검사·적용·재검사하며 새 app-server의 skills/list로 결과를 확인한다.

- [x] 전체 원본 440파일과 보호 971파일 해시를 기록하고 기존 2개 스킬을 백업·이전했다.
- [x] 19개 실제 설치·469파일과 재실행 무변경·3개 cwd 새 프로세스의 147개 발견·본문을 검증했다.
- [x] 독립 전체 리뷰 결함 4개와 실제 Windows ACL 상속 문제를 반례로 수정하고 전체 회귀·diff를 확인했다.
- [x] 구현 커밋 `44e85c8`을 로컬 main에 통합하고 병합 후 103개 회귀를 통과한 뒤 소유 임시 worktree·브랜치를 정리했다.

## 실행 기록.

기준선은 `e6beb2b`이며 Windows 전체 회귀 84개가 통과했다. 내장 worktree 도구는 세션 cwd가 Git 저장소 밖이라 실패하여 Git worktree를 사용했다. 원본 다운로드는 제한된 네트워크를 사용하므로 승인된 설치 범위로 실행한다. 원격 push는 요청하지 않았다.

전수조사에서 선택이 겹친 3개를 추가해 명시 호출 10개·자동 선택 9개로 보강했다. 옛 공식 skill-creator의 라이선스 차이만 정확한 해시로 허용했다. 사용자가 새 패키지 19개와 상태 JSON의 ACL 상속 복원을 별도로 승인했고 현재 에이전트의 본문 읽기까지 검증했다. 전역 설명 복제본은 개인 목차·개인 파일 2개를 보존하면서 이번 문서·명세·설치기 8개만 동기화했다. 상세 실패 반례·검증은 [검증 기록](../../reviews/2026-11-12-anthropic-skills.md)에 있다.

Task 1과 Task 2는 구현 커밋 `44e85c8`에 함께 포함했다. Task 3의 실제 전역 설치·검증을 같은 커밋의 기록에 반영하고 로컬 main 병합 뒤 최종 상태를 별도 문서 커밋으로 확정한다. 원격 main은 `1900d96`이며 이번 작업은 push하지 않았다. 현재 프로세스와 실제 사용자 새 프로세스에서 본문 읽기·발견·검사 성공을 구분해 확인했다.
