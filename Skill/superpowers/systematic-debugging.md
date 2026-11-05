# systematic-debugging

> 수정안을 내기 전에 재현·증거·패턴 비교로 근본 원인을 찾는 네 단계 디버깅 스킬.

## 📌 용도

증상만 바꾸는 추측성 수정을 줄이고 원인이 확인된 한 곳을 고친다. 근본 원인 조사, 패턴 분석, 가설 검증, 구현의 순서를 지킨다.

## 🎯 트리거 조건

버그·테스트 실패·빌드 실패·성능·통합 문제와 예상 밖 동작이 발생했을 때 수정 제안 전에 사용한다.

## 💻 사용 예시 / 호출 방법

1. 에러와 스택을 끝까지 읽고 재현·최근 변경·컴포넌트 경계의 입출력과 설정 전달을 조사한다.
2. 작동하는 예제와 참조 구현을 비교해 차이·의존성·가정을 나열한다.
3. 단일 가설을 한 번에 하나의 최소 변경으로 검증한다.
4. 재현하는 실패 테스트를 먼저 만들고 원인을 수정한 뒤 대상·전체 검증으로 확인한다. 세 번 이상 실패하면 아키텍처와 접근을 다시 논의한다.

## 🛠️ 제공 내용 / 핵심 절차

- `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`와 `find-polluter.sh`가 보조 자료다.
- `test-driven-development`로 재현 테스트를 만들고 `verification-before-completion`으로 완료 주장을 확인한다.

## 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 systematic-debugging](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-버전과-설치-채널)에 따라 확인한다.
