# diagnosing-superpowers

> Superpowers 세션의 반복 작업·계획 이탈·비용·실패를 대화 기록의 파일·줄 근거로 보고하는 스킬.

## 📌 용도

현재 또는 지정한 과거 세션에서 무엇을 기대했고 실제 무엇이 일어났는지 확인한다. 세션 증거를 보고하며, 스킬 결함 확정이나 수정 제안은 유지보수자의 판단으로 남긴다.

## 🎯 트리거 조건

사용자가 세션이 오래 걸린 이유, 반복 작업, 스킬 미작동, 결과 품질이나 버그 보고 자료를 조사해 달라고 할 때 사용한다.

## 💻 사용 예시 / 호출 방법

1. 세션·구간·기대한 결과·관찰한 문제를 확인한 뒤 `references/session-discovery.md`로 기록을 찾는다.
2. `templates/case.md`에 출처를 정리하고 스킬 타임라인·계획 준수·반복 작업·문제·품질·요청 충돌·비용과 시간의 일곱 관점을 조사한다.
3. 모든 발견에 `path:line`을 붙이고 `templates/report.md`의 순서로 보고한다. 근거 없는 수치는 쓰지 않는다.
4. 조건이 맞으면 기존 GitHub 이슈를 찾는다. 게시할 정확한 내용을 보여 주고 승인받은 뒤에만 이슈를 생성한다.

## 🛠️ 제공 내용 / 핵심 절차

- 세션 원본은 수정·이동·삭제하지 않는다. 작업 자료는 `~/.superpowers/diagnosing-superpowers/<session-id>/`에 보관한다.
- 세션을 읽을 때 `references/context-safety.md`를 따른다. 번들 내보내기는 별도 요청이 있을 때만 하며 민감정보 제거·감사를 거친다.
- 압축 전 파일 목록과 제거 로그를 보여 주고 승인받는다. 공유 전에는 사용자가 파일을 직접 검토해야 한다.

## 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 diagnosing-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-버전과-설치-채널)에 따라 확인한다.
