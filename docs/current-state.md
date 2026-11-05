<!-- 저장소의 최신 스킬·CI 작업 상태와 검증 경계를 요약한다. -->
# 현재 상태.

2026-11-05에 [Superpowers 업데이트 설계](superpowers/specs/2026-11-05-superpowers-update.md)에 따라 글로벌 설치와 카탈로그를 v7.0.2 기준으로 갱신했다. Claude는 제작자 마켓플레이스 한 출처만 활성화했고 Codex는 기존 패키지 구조로 15개 스킬·80개 파일을 고정 원본과 일치시켰다. 카탈로그·배포 채널·설치 안내를 함께 갱신하며 사용자 제작 스킬과 전역 행동 지침은 보존한다. [실행 계획](superpowers/plans/2026-11-05-superpowers-update.md)과 [검증 기록](reviews/2026-11-05-superpowers-update.md)에 결과와 남은 확인을 구분한다.

새 Codex 앱 서버에서 두 작업 경로의 15개 스킬 활성·중복 부재를 확인했고 읽기 전용 새 Codex 세션에서 신규 진단 스킬을 실제로 읽었다. Claude도 새 세션 초기화에서 15개 스킬을 발견했으나 모델 호출은 `Not logged in · Please run /login`으로 막혔다. 사용자 로그인 후 Claude 실제 스킬 호출을 추가 확인해야 하며 이 부분은 통과로 보고하지 않는다. 설치 파일과 보조 스크립트의 로컬 검증은 계정 인증과 구분한다.

2026-11-03에 [daily-work-report](../Owned-Skills/daily-work-report/SKILL.md)를 추가했다. 로컬 지정 자료를 읽고 다음 메시지의 업무명·형식으로 작성하며 검사기와 합성 fixture를 포함한다. 실제 사용자 계정의 app-server skills/list에서 사용자 홈 밖을 포함한 세 작업 경로의 전역 발견·활성을 확인했다. Codex CLI의 읽기 전용 새 세션과 resume으로 STEP 1 대기·STEP 2의 12줄 보고서 및 원본 SHA 불변을 확인했다. 저장소 전체 회귀 72개와 패키지 회귀 16개가 통과했다. 별도 합성 비교는 스킬 사용 15/15, 미사용 13/15 assertion을 통과했으며 일부 후속·새 대화·오류 조건은 배치 시뮬레이션이다. 초기 샌드박스 계정의 로그인·탐색 결과는 실제 사용자 계정 검증 결과와 구분한다. 구현 당시 보류했던 커밋·푸시는 사용자의 후속 승인으로 진행한다.

2026-10-15에 [범용 보강 설계](superpowers/specs/2026-10-15-portable-skill-workflows.md)에 따라 자체 제작 23개 스킬을 추가했다. 기존 전달 스킬과 daily-work-report를 포함해 Owned-Skills 원본은 현재 25개다. 당시 카탈로그 99개 이름과 중복되는 범용 스킬은 합산하지 않는다. [설치 안내](../Owned-Skills/README.md), [구현 계획](superpowers/plans/2026-10-15-portable-skill-workflows.md), [검증 기록](reviews/2026-10-15-portable-skill-workflows.md)을 따른다.

사용자 Windows 전체 회귀 71개와 패키지 계약 검사 7개가 통과했다. Codex·Claude 사용자 전역 파일 배치·개인 예외·비대상 파일·보호 설정 보존을 확인했다. Claude의 새 항목은 portable- 이름을 사용해 기존 내장 명령을 보존한다. 실제 새 세션 호출과 외부 기능 실행은 미검증이다. 아래 CI 도입 이력의 64개는 당시 테스트 수다.

구현 커밋 8d660a7을 main에 fast-forward 통합·일반 push하고 원격 SHA 일치를 확인했다. 통합 main의 전체 71개가 다시 통과했다. 병합된 임시 브랜치는 정리했고 추가 worktree 없이 원래 작업 경로와 복구 백업을 유지했다. 전역 문서 복사본 243개와 개인 추가 문서 1개 보존을 대조했다.

## 이전 CI 도입과 통합 기록.

2026-10-15 기준선 `981744c`에서 자동 회귀 테스트 CI 1단계를 구현했다. [운영 안내](ci.md), [승인 설계](superpowers/specs/2026-10-15-regression-ci.md), [구현 계획](superpowers/plans/2026-10-15-regression-ci.md), [검증 기록](reviews/2026-10-15-regression-ci.md)을 따른다.

패치 작성 환경의 Linux Python 3.12에서는 전체 64개 중 60개 통과·Windows 전용 4개 skip을 확인했다. 사용자 Windows Python 3.12.10에서는 적용 전·후와 runner 회귀 수정 후 각각 64개가 모두 통과했다. 실제 GitHub 첫 실행의 Windows fixture 경로 오류를 재현하고 한 줄 수정한 뒤 [재실행](https://github.com/nowJDev/Agent-Instructions/actions/runs/38678117512)에서 Ubuntu 60개 통과·4개 의도적 skip, Windows 64개 전부 통과를 확인했다.

내부 문서 링크 자동 검사·외부 링크 정기 점검은 이번 단계에 포함하지 않았다. 과거 기능·설치 안내의 상세 이력은 CHANGELOG와 기존 리뷰 문서를 보존한다.

패치 작성 환경의 GitHub 403 제한은 사용자 환경에서 재현되지 않았다. 원격 main에서 분기한 `codex/ci-regression-tests`에 두 커밋을 git am으로 적용하고 push하여 [PR #1](https://github.com/nowJDev/Agent-Instructions/pull/1)을 생성했다. 이후 사용자의 전체 push·병합·정리 승인에 따라 PR을 `eaeb985`로 병합하고 기존 Chrome DevTools 지침 커밋 `b77f3ed`도 이력을 보존해 main에 통합했다. 통합 main의 로컬 전체 64개가 통과했으며 임시 CI worktree와 병합된 로컬·원격 작업 브랜치를 정리했다. 개인 파일과 원본 패치는 보존했고 필수 병합 규칙은 변경하지 않았다.
