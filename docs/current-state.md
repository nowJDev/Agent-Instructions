<!-- 저장소의 최신 CI 작업 상태와 검증 경계를 요약한다. -->
# 현재 상태.

2026-10-15 기준선 `981744c`에서 자동 회귀 테스트 CI 1단계를 구현했다. [운영 안내](ci.md), [승인 설계](superpowers/specs/2026-10-15-regression-ci.md), [구현 계획](superpowers/plans/2026-10-15-regression-ci.md), [검증 기록](reviews/2026-10-15-regression-ci.md)을 따른다.

패치 작성 환경의 Linux Python 3.12에서는 전체 64개 중 60개 통과·Windows 전용 4개 skip을 확인했다. 사용자 Windows Python 3.12.10에서는 적용 전·후와 runner 회귀 수정 후 각각 64개가 모두 통과했다. 실제 GitHub 첫 실행의 Windows fixture 경로 오류를 재현하고 한 줄 수정한 뒤 [재실행](https://github.com/nowJDev/Agent-Instructions/actions/runs/38678117512)에서 Ubuntu 60개 통과·4개 의도적 skip, Windows 64개 전부 통과를 확인했다.

내부 문서 링크 자동 검사·외부 링크 정기 점검은 이번 단계에 포함하지 않았다. 과거 기능·설치 안내의 상세 이력은 CHANGELOG와 기존 리뷰 문서를 보존한다.

패치 작성 환경의 GitHub 403 제한은 사용자 환경에서 재현되지 않았다. 원격 main에서 분기한 `codex/ci-regression-tests`에 두 커밋을 git am으로 적용하고 push하여 [PR #1](https://github.com/nowJDev/Agent-Instructions/pull/1)을 생성했다. 원본 작업 폴더와 로컬 main의 미전송 커밋 `b77f3ed`는 보존했다. main 병합과 필수 병합 규칙 변경은 수행하지 않는다.
