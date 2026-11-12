# 전체 스킬 분야별 안내 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 현재 조사 대상과 기존 등록 항목 모두를 분야에서 찾고 누락을 자동 검출한다.

**Architecture:** 기존 상세 설명과 CATALOG를 보완하고 BY-TASK를 전체 분류로 확장한다. 날짜별 공개 메타데이터 증거로 설치·노출·정책·제외를 대조한다.

**Tech Stack:** UTF-8 Markdown·JSON, Python unittest, Git·PowerShell.

**Spec:** [승인 설계](../specs/2026-11-12-skill-coverage-design.md).

## Global Constraints

- 기존 144개 설명 주소·자체 제작 원본 26개·과거 증거·설치본을 보존한다.
- 캐시 존재를 현재 노출로 바꾸지 않고 명시 호출·동명 구현을 구분한다.
- 공개 조사 자료에는 개인 절대경로·설정·인증·원본 실행 본문을 넣지 않는다.
- 분야별 전체 목록은 상세 설명 주소를 재사용하며 최소 한 분야에서 모든 등록 항목을 찾게 한다.
- 검증 후 전역 독립 복제·백업·개인 지침 보존과 원격 검증을 수행한다.

## Review Focus

- 현재 노출된 spreadsheets·live Excel·Data 등의 누락을 잡는가.
- 설치 조사 항목이 등록됐거나 구체적 제외 사유가 있는가.
- 모든 출처별 항목·자체 제작 원본이 분야에서 발견되는가.
- 동일 이름의 다른 구현과 비노출·명시 정책·과거 비활성이 보존되는가.
- 원본 작업 폴더 없이 전역 내용과 참조가 완결하는가.

## Task 1: 전수조사와 누락 회귀.

**Files:** `references/skill-inventory-2026-11-12.json`, `tests/test_documentation.py`, 필요한 출처별 `Skill/<group>/README.md`.

**Interfaces:** 로컬·시스템·현재 플러그인 메타데이터를 공개 조사 레코드와 등록 주소/제외 사유로 변환한다.

- [x] 직접·시스템 136개·플러그인 108개와 기존 카탈로그를 조사하고 중복·노출·명시 정책을 대조했다.
- [x] 전수 분류·시스템/플러그인·조사 등록·제외 검사를 추가하고 기존 누락의 RED를 확인했다.
- [x] 공개 조사 증거와 누락 상세 설명을 작성했다.

## Task 2: 전체 분류와 안내.

**Files:** `Skill/BY-TASK.md`, `Skill/CATALOG.md`, `Skill/README.md`, `README.md`, `README.en.md`, `CHANGELOG.md`, 현재 상태·체크리스트·이번 리뷰.

**Interfaces:** Task 1의 등록 주소 집합을 분야별 전체 목록과 빠른 선택 안내에 연결한다.

- [x] 기존 144개·자체 제작 26개·직접 보완 16개·플러그인 108개의 전체 294개 주소를 등록했다.
- [x] 전체 16개 분야 배치와 엑셀 32개 관련 항목의 유형별 안내·README를 갱신했다.
- [x] 문서 대상 13개·전체 108개 회귀·공개 정보·보존 검사·독립 전체 리뷰를 통과했다. 라우터 분류 발견은 RED→GREEN으로 수정했다.

## Task 3: 독립 복제와 마무리.

**Files:** 전역 문서 복제본, 개인 지침을 보존한 전역 진입점, 이번 작업 증거 문서.

**Interfaces:** 검증된 저장소 파일 집합과 전역 파일 집합·SHA를 대조한다.

- [x] 전역 백업 후 183개 파일의 물리 복제·동일성·153개 Markdown 링크와 원본 접근 차단 전체 108개 회귀를 확인했다.
- [x] 한글 구현 커밋 `c4edf3c`을 main에 통합·일반 push하고 원격 SHA 일치·Ubuntu와 Windows CI 성공을 확인했다.
- [x] 소유 임시 worktree·브랜치를 정리했다. 최종 증거 문서도 전역에 복제하고 파일 집합·SHA·링크를 다시 검사한다.

## 실행 판단.

사용자의 명시적 실행 요청에 따라 연속 수행한다. 이전 태스크에서 네이티브 worktree가 홈을 저장소로 인식하지 못한 점을 확인했으므로 이번에도 사용자 영역의 소유 Git worktree를 사용한다. 로컬·플러그인 메타데이터 조사는 독립 읽기 전용 에이전트에게 나누며 구현과 통합은 주 에이전트가 수행한다.
