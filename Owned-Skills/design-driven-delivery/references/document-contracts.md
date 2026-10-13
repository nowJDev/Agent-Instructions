# 문서 계약.

## 기본 경로.

기존 승인 구조가 없을 때 다음을 사용한다.

```text
docs/
├─ superpowers/
│  ├─ specs/
│  └─ plans/
├─ reviews/
├─ handovers/
├─ design-progress-checklist.md
└─ current-state.md
```

기존 프로젝트가 `docs/specs`, ADR, RFC, issue tracker 또는 다른 승인 구조를 사용하면 새 구조를 중복 생성하지 않고 기존 구조를 따른다.

## 설계 문서.

설계 문서는 무엇을 왜 만들고 어떤 경계를 지킬지 기록한다.

- 목표·비목표.
- 기준선·문제.
- 사용자 흐름.
- 아키텍처·책임.
- 데이터·이벤트 흐름.
- 실패·수명·정리.
- 검증·보안·배포.
- 완료 기준.

기본 템플릿은 `assets/templates/spec-template.md`다.

## 구현 계획.

계획은 설계를 파일·테스트·검증·커밋 단위로 변환한다.

- Task별 파일 경로.
- 실패 테스트와 RED.
- 최소 구현과 GREEN.
- 대상·전체 회귀.
- 수동 검증.
- 문서·커밋.

기본 템플릿은 `assets/templates/plan-template.md`다.

## 진행 체크리스트.

상태 표기는 다음을 사용한다.

- `[x]`: 구현과 필수 자동·수동 검증 완료.
- `[-]`: 일부 구현 또는 수동 검증 대기.
- `[ ]`: 미착수.
- `[?]`: 사용자·고객·외부 환경 결정 필요.

검증하지 않은 항목을 `[x]`로 올리지 않는다. 기본 템플릿은 `assets/templates/progress-checklist-template.md`다.

## 리뷰 문서.

기준선부터 전체 대상 파일을 검토하고 정확성, 단순화, 효율성, 주석, 검증과 발견 사항을 기록한다. 기본 템플릿은 `assets/templates/review-template.md`다.

## 현재 상태와 인수인계.

`current-state.md`는 기준선, 버전, 주요 구성, 검증과 다음 작업을 요약한다. 세션을 넘길 때 `handover`에는 브랜치, HEAD, 완료·미완료, 로그, 보호 변경과 재개 명령을 기록한다.

기본 템플릿은 다음과 같다.

- `assets/templates/current-state-template.md`.
- `assets/templates/handover-template.md`.

## 정합성.

- 상세 규칙은 한곳에서 관리하고, 다른 문서에서는 해당 경로와 읽어야 하는 조건을 안내한다.
- 같은 논리 변경의 코드·테스트·설계·계획·체크리스트를 함께 커밋한다.
- 계획 체크박스와 테스트 증거가 맞는지 확인한다.
- 수동 게이트가 남으면 상태를 부분 완료로 유지한다.
- 삭제되거나 대체된 문서의 링크를 정리한다.
- 내부 판단, 시크릿과 불필요한 개인 경로를 문서에 넣지 않는다.
