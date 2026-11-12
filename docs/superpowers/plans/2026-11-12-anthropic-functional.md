# Anthropic 스킬 실제 작업 검증 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 사용자가 추가 요청한 19개 스킬의 실제 샘플 작업과 GitHub push를 수행하고 실행 범위·호환성 한계를 구분한다.

**Architecture:** 설치된 스킬을 각각 전체 읽고 합성 입력으로 실제 산출물·프로토콜·문서 작업을 수행한다. 실행 산출물·격리 종속성·원문 로그는 공개 저장소 밖에 두고 공개 저장소에는 비밀 값 없는 검증 결과만 기록한다.

**Tech Stack:** 설치된 Python·Node·Office·브라우저와 작업 폴더 안에만 설치하는 검증용 종속성, Git/GitHub Actions.

**Spec:** [전역 설치 설계](../specs/2026-11-12-anthropic-skills-design.md)의 후속 검증 범위를 사용자 최신 요청으로 확장한다. 이번 요청은 실제 샘플 작업과 GitHub push를 명시적으로 승인한다.

## Global Constraints

- 전역 스킬 원문·개인 설정·다른 프로젝트·기존 사용자 파일을 바꾸지 않는다.
- API 키·인증 값·비공개 자료·검증용 원문 산출물은 커밋하지 않는다.
- 유료 Claude 모델 호출·외부 메시지·콘텐츠 게시를 임의 실행하지 않는다. 로컬 SDK 검증과 실제 원격 모델 호출을 구분한다.
- 실패한 원본 helper, 대체 도구 실행과 환경 미검증을 성공 수에 섞지 않는다.
- 기존 main의 미푸시 커밋을 보존하고 일반 push만 수행한다.

## Review Focus

- 파일 배치·import·구문 검사만으로 실제 작업 성공이라고 하지 않는다.
- 원본 스크립트 변경 없이 가능한지, 격리 복사본을 보정했는지 구분한다.
- 샘플의 고정 사실·추정·수식·도구 결과를 실제 기대값으로 검사한다.
- 브라우저·Office·서버는 이번 검증에서 시작한 인스턴스만 정리한다.
- 공개 보고의 성공·조건부·실패·미검증과 실제 로그가 일치해야 한다.

## Task 1: 19개 실제 샘플 작업.

- [x] 문서 4개와 브랜드·테마 2개를 실제 파일 생성·재열기·표시 또는 계산으로 검사하고 미완료 단계를 기록했다.
- [x] 시각·웹 6개를 이미지·GIF·브라우저·원본 번들 도구 실행으로 검사했다.
- [x] API·MCP·스킬 제작 3개를 실제 SDK/stdio/평가 샘플로 검사했다.
- [x] Academy·공동 문서·내부 보고·후속 질문 4개를 실제 추천·초안·독자 검사·조건 분기로 검사했다.

## Task 2: 증거와 배포.

- [x] `docs/reviews/2026-11-12-anthropic-functional.md`에 19개별 입력·작업·판정·한계를 기록하고 현재 상태·체크리스트를 갱신했다.
- [x] 실제 결과를 독립 검토하고 문서 링크·전체 회귀·공개 정보 경계를 확인했다.
- [ ] 한글 커밋과 로컬 통합 후 GitHub main에 일반 push하고 원격 SHA·CI 결과를 확인한다.
- [ ] 소유 worktree·브랜치·서버를 정리하고 증거·복구 자료는 보존한다.
