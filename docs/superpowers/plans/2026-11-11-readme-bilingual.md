# README 개편과 영어 안내 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 한국어 README를 정리하고 영어 전환과 정적 대표 이미지를 제공한 뒤 검증·커밋·푸시한다.

**Architecture:** 기존 README와 GUIDE의 역할을 유지한다. 두 README가 자체 완결 SVG를 공유하고 기존 링크 검사에 README 전용 HTML 자원 검사를 더한다.

**Tech Stack:** GitHub Markdown, HTML picture/details, SVG, Python 3.12 unittest.

**Spec:** [승인 설계](../specs/2026-11-11-readme-bilingual-design.md).

## Global Constraints

- `README.md` 한국어 기본, `README.en.md` 영어 안내를 제공한다.
- 적용 프롬프트와 Windows 세팅 범위를 분리하고 기존 fragment 9개를 보존한다.
- SVG는 1200×300, 정적·자체 완결이며 중요 의미를 본문에도 제공한다.
- 설정·스킬·MCP·응답 언어 정책·전역 복제본은 변경하지 않는다. 의존성을 추가하지 않는다.

## Review Focus

- 영어 문서에서 한국어 상세 문서와 응답 정책을 오해하지 않는지 확인한다.
- 기존 fragment와 접힌 세팅 안내의 도착 위치를 확인한다.
- 이미지 실패·모바일·테마에서 시작 프롬프트와 언어 전환을 사용할 수 있는지 확인한다.
- HTML 이미지·언어 링크 누락을 실제 반례로 검출하는지 확인한다.
- GUIDE와 번역에 기존 의미·라이선스·설치 경계가 보존되는지 확인한다.

### Task 1: README 계약, 콘텐츠와 대표 이미지.

**Files:** `tests/test_readme.py`, `README.md`, `README.en.md`, `assets/readme/hero-light.svg`, `assets/readme/hero-dark.svg`. 기존 GUIDE는 내용 대조 후 필요한 부분만 보완한다.

**Interfaces:** 기존 `anchor_ids`, `link_errors`, `prose_only`를 소비한다. 두 README는 언어 전환, 9개 기존 앵커, 같은 로컬 이미지 경로와 유효한 상세 문서 링크를 제공한다.

- [x] README 언어 전환·기존 앵커·HTML 자원·SVG 검사와 누락 반례를 작성했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_readme.py -v`에서 새 README·이미지 부재로 RED를 확인했다.
- [x] 승인된 구조로 두 README와 SVG를 작성하고 GUIDE와 의미를 대조했다.
- [x] 대상4개와 전체84개 회귀가 통과했다.

### Task 2: 검증, 기록과 배포.

**Files:** `docs/reviews/2026-11-11-readme-bilingual.md`, `docs/current-state.md`, `docs/design-progress-checklist.md`, 본 계획. CI 운영 안내는 검사 범위 변경만 반영한다.

**Interfaces:** Task 1의 README와 검사 결과를 받아 실제 GitHub 화면·배포 결과를 검증한다.

- [x] 전체 변경의 독립 리뷰와 로컬 SVG·테마 확인을 마쳤다. 작은 화면은 푸시 후 실제 GitHub에서 확인한다.
- [x] 결과와 한계를 기록하고 `git diff --check` 및 전체84개 회귀·skip0을 확인했다.
- [ ] 한글 메시지로 커밋하고 main에 일반 병합·푸시한다.
- [ ] 원격 SHA·실제 GitHub 한·영 화면·두 OS CI를 확인하고 소유한 임시 worktree를 정리한다.

## 실행 원장.

- 기준선은 `090a4c0`이며 사용자는 설계 실행·커밋·푸시를 승인했다.
- Task 1의 문서·이미지가 Task 2의 화면 검증 입력이며 인터페이스 충돌은 없다.
- Task 1: complete. 새 문서·이미지 부재 RED와 기존 앵커 오타 재현 후 GREEN, Windows Python 3.12 전체84개 통과·skip0을 확인했다.
- GUIDE의 기존 상세 작업 흐름·파일 역할·용어 설명으로 축약 내용을 설명할 수 있어 GUIDE는 보존했다.
