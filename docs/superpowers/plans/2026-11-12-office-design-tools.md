# Office·디자인 도구 전역 설치 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 요청한 세 도구의 전역 설치·실제 실행 검증과 관리 저장소 커밋·push를 완료한다.

**Architecture:** 고정 원본을 사용자 전역에 단일 설치하고 런타임은 격리한다. 공개 저장소에는 설치 명세와 설명·검증만 둔다.

**Tech Stack:** Codex skill-installer, Python 3.12 venv, Node/npm, Windows x64 OfficeCLI, Git/GitHub Actions.

**Spec:** [설치 설계](../specs/2026-11-12-office-design-tools-design.md).

## Global Constraints

- 기존 전역 스킬·사용자 설정·MCP·권한과 다른 프로젝트 파일을 보존한다.
- 타사 원문·대형 자산·실행본·의존성·원문 로그·개인 자료는 공개 커밋에서 제외한다.
- 세 스킬의 원본 이름·본문·고지와 Huashu 별도 스티커 라이선스를 보존한다.
- 기존 도구를 재사용하고 별도의 범용 설치 프레임워크는 만들지 않는다.

## Review Focus

- 단일 SKILL.md 설치로 상대 리소스가 누락되지 않는가.
- OfficeCLI 자동 업데이트·다른 AI 설치가 고정 설치를 바꾸지 않는가.
- 기본 Python과 격리 venv를 혼동하지 않는가.
- 설치 발견·실제 샘플 수행·모든 기능 성공을 구분하는가.
- 기존 파일·환경변수·PATH를 덮어쓰거나 비공개 자료를 공개하지 않는가.

## Task 1: 전역 설치와 실행 증거.

- [x] 기존 설치·명령·보호 파일·환경과 고정 원본을 확인했다.
- [x] 표준 skill-installer로 세 패키지를 설치하고 전체 리소스·고지·명시 호출 정책을 확인했다.
- [x] OfficeCLI 해시 검증·사용자 PATH와 전용 업데이트 제한을 적용했다.
- [x] 별도 venv·필요한 Node 의존성을 준비하고 세 도구의 실제 샘플·실패 조건을 검사했다.
- [x] 새 Codex 사용자 프로세스 발견·중복·보호 파일 보존과 로컬 증거를 확인했다.

## Task 2: 공개 관리와 배포.

- [x] `references/office-design-tools.lock.json`과 `Skill/office-design-tools/README.md`에 원본·설치·호출·제약을 기록했다.
- [x] `Skill/README.md`, `Skill/CATALOG.md`, `tests/test_documentation.py`의 그룹과 설명 수를 함께 갱신했다. 단순 카탈로그 데이터 변경에는 새 동작 테스트를 만들지 않고 기존 구조·링크 검사를 실행했다.
- [x] `docs/reviews/2026-11-12-office-design-tools.md`, 현재 상태·체크리스트에 실제 결과를 기록했다.
- [x] 전체 103개 회귀·공개 정보 검사·독립 리뷰 후 커밋 `91c5763`의 main 통합·push·SHA 일치·두 OS CI 성공을 확인했다.
- [x] 소유 임시 worktree·브랜치·프로세스를 정리하고 증거를 보존했다.
