<!-- 저장소의 최신 CI 작업 상태와 검증 경계를 요약한다. -->
# 현재 상태.

2026-10-15 기준선 `981744c`에서 자동 회귀 테스트 CI 1단계를 구현했다. [운영 안내](ci.md), [승인 설계](superpowers/specs/2026-10-15-regression-ci.md), [구현 계획](superpowers/plans/2026-10-15-regression-ci.md), [검증 기록](reviews/2026-10-15-regression-ci.md)을 따른다.

로컬 Linux Python 3.12의 전체 64개 중 60개가 통과했고 Windows 전용 4개는 의도적 skip이다. Bash 사전 검사·실패 종료 코드·actionlint·문서 검사를 통과했다. 실제 GitHub Ubuntu·Windows 실행은 PR에서 확인할 단계다. main 병합과 필수 병합 규칙은 별도로 수행한다.

내부 문서 링크 자동 검사·외부 링크 정기 점검은 이번 단계에 포함하지 않았다. 과거 기능·설치 안내의 상세 이력은 CHANGELOG와 기존 리뷰 문서를 보존한다.
