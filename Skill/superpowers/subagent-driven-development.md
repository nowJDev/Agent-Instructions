# subagent-driven-development

> 태스크마다 새 구현자와 스펙·품질을 함께 보는 리뷰어를 배치하고 최종 전체 브랜치 리뷰를 수행하는 스킬.

## 📌 용도

같은 세션에서 계획을 조율하되 구현·태스크 리뷰는 격리된 컨텍스트로 위임한다. 계획별 원장과 파일 형태의 brief·보고서·리뷰 패키지를 남겨 반복 작업과 컨텍스트 손실을 줄인다.

## 🎯 트리거 조건

승인 계획의 태스크가 대체로 독립적이고 태스크별 독립 리뷰가 필요할 때 사용한다. 인라인 실행을 선택했거나 위임 도구가 없으면 `executing-plans`를 사용한다.

## 💻 사용 예시 / 호출 방법

1. 격리 환경·스펙·계획을 확인하고 `scripts/sdd-workspace`가 정한 `.superpowers/sdd/<plan-basename>/progress.md`에서 재개한다.
2. `scripts/task-brief`로 정확한 요구사항을 추출하고 `implementer-prompt.md`와 함께 구현자에게 파일 경로로 전달한다.
3. 기록한 BASE부터 HEAD까지 `scripts/review-package`로 묶고 `task-reviewer-prompt.md`로 스펙 준수와 태스크 품질의 두 판정을 받는다.
4. 문제가 있으면 `references/fix-loop.md`를 매번 읽고 최대 다섯 차례의 수정·범위 제한 재리뷰를 수행한다. 판단과 보류 항목을 원장에 남긴다.
5. 전체 태스크 뒤 `references/final-review.md`에 따라 전체 브랜치를 검토하고 판단·보류 사항을 보고한 뒤 종료 스킬로 넘긴다.

## 🛠️ 제공 내용 / 핵심 절차

- 구현자를 병렬로 여러 명 실행하지 않는다. 구현자는 추가 서브에이전트를 만들지 않고 리뷰는 조율자가 맡긴다.
- 구 템플릿 두 개 대신 `task-reviewer-prompt.md`를 사용하며 재리뷰는 `re-review-prompt.md`를 따른다.
- 계획별 작업 자료는 Git 무시 대상이다. 정리 전 복구·보고 정보를 보존하고 다른 계획 자료는 남겨 둔다.

## 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 subagent-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-버전과-설치-채널)에 따라 확인한다.
