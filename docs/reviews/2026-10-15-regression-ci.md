<!-- CI 1단계의 변경 범위와 실제 검증 결과를 기록한다. -->
# 자동 회귀 테스트 CI 검증.

## 기준과 범위.

기준선은 `981744c08151d43fbaf3e4065a775ae3edfec792`다. 사용자 승인 설계의 1단계인 Windows·Linux 전체 회귀 CI, 운영 안내와 README 연결을 구현했다. 내부·외부 링크 검사와 병합 규칙은 후속 범위다. [설계](../superpowers/specs/2026-10-15-regression-ci.md)와 [계획](../superpowers/plans/2026-10-15-regression-ci.md)에 범위와 순서를 기록했다.

## 기준선 발견과 수정.

Linux Python 3.12.14에서 전체 64개 실행 중 오류 2개, Windows 전용 skip 4개를 확인했다. 두 오류는 외부 디렉터리 접근 거부 assertion 이후 cleanup에서 발생했다. POSIX 디렉터리 symlink에 os.rmdir를 호출한 것이 원인이다. Windows junction의 os.rmdir는 유지하고 POSIX는 unlink로 분기했다. 테스트를 삭제하거나 skip하지 않았고 제품 스크립트는 변경하지 않았다.

## 패치 작성 환경의 로컬 검증.

- `python -X utf8 -B -m unittest discover -s tests -v`: 64개 실행, 60개 통과, 실패·오류 0개, Windows 전용 4개 skip, 5.260초다.
- CI YAML의 Bash 사전 검사 run 내용을 추출해 실제 Bash로 실행했다. Python과 Bash·필수 도구 조회를 통과했다.
- 별도 임시 디렉터리의 실패 unittest 1개를 동일 옵션으로 실행해 exit 1을 확인했다. 임시 테스트는 저장소에 추가하지 않았고 종료 후 제거했다. 실제 Actions에서의 실패 주입과는 구별한다.
- actionlint v1.7.12로 workflow를 검사했다. shellcheck와 pyflakes는 로컬에 없어 해당 선택 검사는 비활성화했으며 Actions YAML·표현식 검사에서 오류가 없었다.
- 변경 파일의 UTF-8·BOM 없음·LF와 Markdown fence·내부 파일 링크를 확인했다. git diff --check를 통과했다.
- 공식 actions/checkout v4와 actions/setup-python v5의 현재 tag commit을 조회해 SHA로 고정했다.

## 독립 리뷰.

독립 검토자가 네 테스트 파일 전체의 OS별 의존성, 전체 diff와 새 workflow·운영 안내·설계·계획을 검토했다. 표준 라이브러리만 필요하고 Git Bash·Windows PowerShell·CMD·COM을 사전 확인하는 구성을 확인했다. 현재 범위에서 차단·중요 발견은 없었다. 부모도 diff와 실제 검증 결과를 확인했다.

## 원격 실행 상태.

패치 작성 환경에서는 HTTPS 인증 정보 부재와 GitHub 앱의 `403 Resource not accessible by integration`으로 전달이 차단됐다. 사용자 Windows 환경에서는 원격 main 기준의 별도 worktree·브랜치에 두 커밋을 git am으로 적용하고 push하여 [PR #1](https://github.com/nowJDev/Agent-Instructions/pull/1)을 생성했다. 원본 main의 미전송 커밋 `b77f3ed`는 PR에서 제외하고 보존했다. 별도 필수 병합 검사 설정이나 main 병합은 수행하지 않는다.

## 사용자 Windows 검증과 runner 회귀 수정.

Windows Python 3.12.10 전체 unittest는 적용 전 64개·22.279초, 적용 후 64개·21.081초로 모두 통과했고 실패·오류·skip은 없었다. Bash·COM·CMD 사전 검사와 변경 파일 10개의 UTF-8·BOM 없음·LF·상대 문서 링크를 확인했다. 전체 패치와 네 테스트 파일의 독립 리뷰에서 차단·중요 발견은 없었다.

[첫 Actions 실행](https://github.com/nowJDev/Agent-Instructions/actions/runs/38677825016)에서 Ubuntu는 성공했으나 Windows는 `test_bootstrap_does_not_overwrite_concurrent_creation`이 실패했다. 제품 스크립트는 경로를 resolve하지만 fixture의 비교 대상은 원래 임시 경로여서 정규화 전후 표기가 다르면 경쟁 생성 mock이 실행되지 않았다. 로컬에서 `..`를 포함한 동일 디렉터리 경로로 같은 assertion 실패를 재현했다. 비교 대상에 resolve를 적용하는 한 줄 수정 후 재현 조건을 통과했다. 사용자 문서 보존 assertion과 제품 스크립트는 유지했으며 독립 재검토에서도 수정이 타당함을 확인했다. 수정 후 로컬 전체 64개도 22.126초에 실패·오류·skip 없이 통과했다.

## 실제 GitHub 재실행 결과.

2026-10-15 수정 커밋 `0558c94`의 [실행 38678117512](https://github.com/nowJDev/Agent-Instructions/actions/runs/38678117512)이 성공했다. 두 OS의 필수 도구 사전 검사와 테스트 단계 모두 성공했다.

| 환경 | 전체 탐색 | 통과 | 실패·오류 | skip | 테스트 시간 |
|---|---|---|---|---|---|
| Ubuntu, Python 3.12.15. | 64개. | 60개. | 0개. | Windows 전용 4개. | 6.627초. |
| Windows, Python 3.12.10. | 64개. | 64개. | 0개. | 0개. | 19.082초. |

runner에는 고정된 checkout v4·setup-python v5의 Node.js 20 지원 종료에 따른 Node.js 24 강제 실행 경고가 남는다. 이번 두 OS 실행은 성공했으며 Actions 주요 버전 갱신은 별도 범위다. ubuntu-latest의 Ubuntu 26 전환 예정 안내도 있으므로 향후 runner 이미지 변경 시 같은 회귀 결과를 확인한다.
