# writing-skills

> 재사용 스킬의 설명·형태·실제 준수를 기준선과 비교해 검증하는 스킬 작성 절차.

## 📌 용도

스킬 없이 발생하는 실패를 먼저 관찰하고 그 문제를 해결하는 최소 지침을 작성한다. 스킬 본문과 탐색용 설명을 분리하며 효과를 실제 시나리오로 확인한다.

## 🎯 트리거 조건

새 스킬을 만들거나 기존 스킬을 편집·배포 검증할 때 사용한다. 일회성 기록이나 프로젝트 한정 규칙은 해당 문서에 둔다.

## 💻 사용 예시 / 호출 방법

1. 스킬 없는 기준선에서 실패·합리화·누락을 확인한다.
2. 규율 위반·출력 형태·필수 요소 누락·조건별 행동 중 실패 종류에 맞는 지침 형식을 선택한다.
3. 최소 스킬을 작성하고 같은 시나리오에서 효과를 확인한 뒤 허점을 보완한다.
4. 행동 형태를 조정하는 문구는 무지침 대조군과 변형별 다섯 번 이상의 작은 실험으로 먼저 비교한다. 규율 스킬의 압박 시나리오를 대체하지는 않는다.

## 🛠️ 제공 내용 / 핵심 절차

- frontmatter·설명·이름·분량은 `references/discovery.md`, 도식은 `references/flowcharts.md`를 따른다.
- 규율 지침은 `references/bulletproofing.md`, 전체 검증은 `references/testing-skills-with-subagents.md`, 공식 참고는 `references/anthropic-best-practices.md`에 있다.
- 패키지의 스크립트는 실행 비트에만 의존하지 않고 `bash`·`node` 등 해당 인터프리터로 호출한다.

## 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-버전과-설치-채널)에 따라 확인한다.
