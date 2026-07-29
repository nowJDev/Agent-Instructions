# design-driven-delivery.

> 상태 변경 요청을 분류하고 설계·계획·구현·검증·리뷰·문서화·통합 순서로 통제하는 자체 제작 최상위 프로젝트 전달 Skill이다.

## 📌 용도.

모든 사용자 요청을 읽기 전용, 진단, 상태 변경 또는 모니터링으로 먼저 분류한다. 기능 개발·버그 수정·리팩터링·코드·설정·문서·데이터·배포 변경에는 증거 기반 상태 머신을 적용하고, 기존 전문 Skill을 승인된 순서로 호출한다.

## 🎯 트리거 조건.

- **언제 호출되는가.**
  - 모든 사용자 메시지에서 변경 범위를 먼저 판정할 때.
  - 기능·버그·리팩터링·문서·설정·데이터·배포·커밋·병합·푸시 작업을 시작할 때.
- **언제 전체 워크플로를 실행하지 않는가.**
  - 단순 조회·설명·상태 보고.
  - 수정 요청이 없는 원인 진단·리뷰·감사.
  - 승인된 범위만 추적하는 모니터링.
- **Skill 유형.**
  - 최상위 라우터이자 증거 게이트다. 전문 Skill의 절차를 중복 구현하지 않는다.

## 💻 사용 예시.

- `$design-driven-delivery로 이 기능을 설계부터 검증과 통합까지 진행해 주세요.`
- “이 오류를 진단하고 수정까지 진행해줘.”
- “전체 변경을 검증하고 코드 리뷰 후 커밋·푸시해줘.”
- “현재 상태만 설명해줘.”라고 요청하면 읽기 전용 흐름으로 종료한다.

## 🛠️ 제공 절차와 도구.

- 상태 흐름은 `DISCOVERED → DISCUSSING → DESIGN_APPROVED → PLAN_APPROVED → IMPLEMENTING → VERIFIED → REVIEWED → DOCUMENTED → COMMITTED → INTEGRATED`다.
- 새 기능은 `brainstorming`, 승인 설계는 `writing-plans`, 구현은 Worktree·TDD·체계적 디버깅을 조율한다.
- 완료 전 `verification-before-completion`, 전체 변경에 `code-review`, 브랜치 통합에 `finishing-a-development-branch`를 호출한다.
- 기본 문서 구조를 비덮어쓰기 방식으로 초기화하는 `bootstrap_workflow.py`와 완료 증거를 검사하는 `validate_workflow.py`를 제공한다.
- 프로젝트별 검증은 Unity, Web, Backend, Python·CLI, Data, Mobile·Desktop, Infrastructure Adapter에서 선택한다.

## 📦 출처와 설치 상태.

- 분류: **자체 제작 개인 글로벌 Skill**.
- 공개 원본: [`Owned-Skills/design-driven-delivery`](../../Owned-Skills/design-driven-delivery/SKILL.md).
- Codex 사용자 설치 예시: `~/.agents/skills/design-driven-delivery`.
- UI 메타데이터는 `agents/openai.yaml`에 있으며 암시적 호출을 허용한다.
- 저장소의 MIT License가 직접 작성한 Skill 원본에 적용된다.
