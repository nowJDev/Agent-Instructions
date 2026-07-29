---
name: design-driven-delivery
description: 모든 사용자 메시지에서 요청을 읽기 전용·진단·상태 변경·모니터링으로 먼저 분류하고, 기능 개발·버그 수정·리팩터링·코드·설정·문서·데이터·배포 변경에는 프로젝트 조사, 요구사항 논의, 설계 승인, 구현 계획, 격리 작업, TDD, 자동·수동 검증, 전체 코드 리뷰, 문서화, 커밋과 승인된 통합 순서를 강제하는 최상위 프로젝트 전달 스킬. 어떤 응답·명확화 질문·파일 탐색·도구 호출보다 먼저 변경 범위를 판정할 때 사용한다.
---

# Design-Driven Delivery

## 요청을 먼저 분류하기.

어떤 응답, 명확화 질문, 파일 탐색과 도구 호출보다 먼저 사용자 요청을 다음 네 종류 중 하나로 분류한다.

| 종류 | 판단 기준 | 수행 방식 |
|---|---|---|
| 읽기 전용 | 설명, 조회, 코드 해석, 상태 보고 | 필요한 증거를 조사한 뒤 답하고 상태를 변경하지 않는다. |
| 진단 | 원인 분석, 리뷰, 감사, 장애 조사 | 원인과 증거를 보고하고 수정 요청이 없으면 구현하지 않는다. |
| 상태 변경 | 기능, 버그 수정, 리팩터링, 코드·설정·문서·데이터·배포·병합·푸시 | 전체 변경 워크플로를 적용한다. |
| 모니터링 | 대기, 진행 추적, 반복 확인 | 승인된 범위만 추적하며 새로운 변경 권한으로 확대하지 않는다. |

분류가 불명확하고 결과가 달라질 수 있으면 사용자에게 한 번에 한 가지를 질문한다. 읽기 전용 요청을 이유 없이 설계 프로젝트로 확대하지 않는다.

## 상태 변경 워크플로를 시작하기.

상태 변경 요청이면 다음 순서로 진행한다.

1. [references/change-workflow.md](references/change-workflow.md)를 전부 읽는다.
2. 프로젝트의 모든 적용 가능한 `AGENTS.md`와 기존 문서 구조를 확인한다.
3. 새 기능·동작 변경이면 `brainstorming`을 사용한다.
4. 승인 설계를 구현할 때 `writing-plans`를 사용한다.
5. Git 저장소의 구현이면 `using-git-worktrees`로 격리 상태를 확인한다.
6. 기능·버그 구현이면 `test-driven-development`를 사용한다.
7. 예상 밖 동작이나 테스트 실패가 발생하면 `systematic-debugging`으로 돌아간다.
8. 완료를 주장하기 전에 `verification-before-completion`을 사용한다.
9. 전체 변경에 `code-review`를 사용한다.
10. 브랜치를 통합할 때 `finishing-a-development-branch`를 사용한다.
11. 세션을 넘기면 `handover`를 사용한다.

기존 전문 Skill의 절차를 이 Skill 안에서 흉내 내거나 생략하지 않는다. 사용자가 명시한 요구사항과 프로젝트 지침을 최우선으로 적용한다.

## 증거 게이트를 유지하기.

다음 상태를 순서대로 통과한다.

```text
DISCOVERED.
→ DISCUSSING.
→ DESIGN_APPROVED.
→ PLAN_APPROVED.
→ IMPLEMENTING.
→ VERIFIED.
→ REVIEWED.
→ DOCUMENTED.
→ COMMITTED.
→ INTEGRATED.
```

현재 작업에 필요하지 않은 마지막 상태는 생략할 수 있지만 순서를 바꾸지 않는다. 예를 들어 사용자가 진단만 요청했다면 `DISCOVERED`에서 원인을 보고하고 종료한다. 구현 중 예상과 다른 결과가 나오면 진단 또는 설계 단계로 돌아간다.

세부 단계와 필수 증거는 [references/change-workflow.md](references/change-workflow.md)를 따른다.

## 기존 문서 구조를 보존하기.

문서를 만들기 전에 [references/document-contracts.md](references/document-contracts.md)를 읽는다.

- 기존 승인 문서 구조가 있으면 그것을 우선한다.
- 구조가 없을 때만 기본 `docs/superpowers/specs`, `docs/superpowers/plans`, `docs/reviews`, `docs/handovers`를 사용한다.
- 코드·테스트·설계·계획·체크리스트가 같은 사실을 말하게 한다.
- 자동 또는 수동 검증이 남아 있으면 완료 상태로 올리지 않는다.

문서 구조 초기화가 승인됐으면 다음 스크립트를 사용할 수 있다.

```text
python scripts/bootstrap_workflow.py --project <project-root>
```

기존 파일을 덮어쓰지 않는다. 생성 결과를 반드시 확인한다.

## 프로젝트에 맞는 검증을 선택하기.

검증 전에 다음을 읽는다.

- 공통 종료 게이트는 [references/verification-gates.md](references/verification-gates.md)를 따른다.
- 프로젝트 유형별 테스트와 수동 검증은 [references/project-adapters.md](references/project-adapters.md)를 따른다.

완료 단계의 문서 누락을 검사하려면 다음을 실행한다.

```text
python scripts/validate_workflow.py --project <project-root> --stage completion
```

스크립트 성공만으로 완료를 선언하지 않는다. 실제 테스트 결과, 로그, 수동 검증과 Git 상태를 함께 확인한다.

## 비협상 규칙.

- 설계 승인이 필요한 변경에서 승인 전에 구현하지 않는다.
- 사용자가 요청하지 않은 상태 변경을 진단이나 조회에 포함하지 않는다.
- 검증 없이 완료·커밋·병합·푸시하지 않는다.
- 실패 테스트를 삭제하거나 계약을 약화해 GREEN을 만들지 않는다.
- 사용자 변경과 보호 경로를 덮어쓰지 않는다.
- 새로운 프로젝트 고유 규칙을 이 범용 Skill에 하드코딩하지 않는다.
- 단순 작업이라는 이유로 필요한 안전·검증 게이트를 생략하지 않는다.
