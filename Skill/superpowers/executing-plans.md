# executing-plans

> 현재 세션에서 계획을 직접 구현하고 진행 원장과 태스크별 검증·최종 브랜치 리뷰를 유지하는 스킬.

## 📌 용도

사용자가 인라인 실행을 선택했거나 서브에이전트 도구가 없을 때 계획을 직접 수행한다. 태스크마다 구현자·리뷰어를 새로 띄우지 않고 진행 원장으로 재개 지점을 남기며 마지막에 전체 변경을 검토한다.

## 🎯 트리거 조건

승인된 구현 계획을 같은 세션에서 직접 실행할 때 사용한다. 태스크마다 독립 리뷰를 원하면 `subagent-driven-development`를 선택한다.

## 💻 사용 예시 / 호출 방법

1. `using-git-worktrees`로 격리를 확인하고 계획·스펙·공통 제약을 읽는다. `test-driven-development`를 로드한다.
2. `subagent-driven-development/scripts/sdd-workspace`로 계획별 `.superpowers/sdd/<plan-basename>/`을 만들고 `progress.md`를 확인한다.
3. `scripts/task-start`가 만든 brief를 읽고 단계별 기대 출력과 실제 결과를 대조한다. `scripts/task-done`은 테스트가 통과했을 때만 완료를 기록한다.
4. 전체 브랜치 리뷰를 새 리뷰어에게 맡긴다. 도구가 없으면 별도 셀프리뷰를 수행하고 한계를 명시한다.
5. 중요 발견은 한 차례 수정 과정에서 RED→GREEN과 전체 테스트로 검증한다. 판단·보류 항목을 보고한 뒤 `finishing-a-development-branch`로 넘긴다.

## 🛠️ 제공 내용 / 핵심 절차

- 계획 충돌과 판단은 근거·잘못됐을 때의 비용을 포함한 `Ruling:`으로 원장에 기록한다. 파괴적 작업·보안·외부 영향 등은 사용자 권한을 따른다.
- Bash 스크립트는 설치된 실제 경로에서 실행하며 다른 계획의 작업 자료를 읽거나 정리하지 않는다.
- 새 세션이나 압축 후에는 기억 대신 원장과 Git 이력으로 이어간다.

## 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 executing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-버전과-설치-채널)에 따라 확인한다.
