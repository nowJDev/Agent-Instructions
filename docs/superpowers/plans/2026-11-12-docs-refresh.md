# 문서 전체 정리 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 모든 문서를 점검하고 신규 설치 안내·현재 상태·과거 증거의 경계를 정리한다.

**Architecture:** 기존 진입점·카탈로그·history 구조를 유지하고 중복된 현재 서술을 줄인다. 실행 스킬·고정 원본·개인 환경은 보존한다.

**Tech Stack:** UTF-8 Markdown·JSON, Python unittest, Git/GitHub Actions.

**Spec:** [정리 설계](../specs/2026-11-12-docs-refresh-design.md).

## Global Constraints

- 과거 수치·실패·미검증을 현재 값이나 성공으로 덮어쓰지 않는다.
- Owned 실행 지침·템플릿·fixtures와 타사 고정 설치 명세를 보존한다.
- 보관 시 본문 사실·코드를 유지하고 제목·앵커·상대 링크만 변환한다.
- 전역 설치·설정·권한을 변경하지 않으며 개인 자료·원문 로그를 커밋하지 않는다.

## Review Focus

- 한·영 README의 기존 주소와 신규 안내가 함께 유지되는가.
- 설명 수·클라이언트 발견·설치 수를 혼동하지 않는가.
- 과거 ON/OFF·계정 연결·기능 지원을 현재 사실로 단정하지 않는가.
- 보관 원문·자체 제작 패키지 계약·내부 링크가 유지되는가.

## Task 1: 전수조사와 안내 정리.

- [x] 기준선 152개 Markdown의 전체 읽기 coverage와 파일 해시를 취합했다.
- [x] README 한영·GUIDE·운영/이식·변경 이력과 관련 참조를 갱신했다.
- [x] Skill·MCP의 분류·현재/과거 경계·실행 조건을 정리했다.

## Task 2: 기록 보관과 현재 요약.

- [x] 종료 문서 17개를 6개 history로 보관하고 원문 동일성·경로·앵커를 확인했다.
- [x] current-state·체크리스트·CI 안내·history 목차와 기존 구조 검사 기대값을 갱신했다.
- [x] 모든 내부 링크·공개 정보·전체 103개 회귀·독립 리뷰를 검증하고 이번 리뷰 증거를 기록했다.

## Task 3: 배포와 정리.

- [ ] 한글 커밋·main 통합 후 회귀·일반 push·원격 SHA·두 OS CI를 확인한다.
- [ ] 최종 기록과 소유 임시 worktree·브랜치·파일 정리를 마친다.
