<!-- CI 1단계의 변경 범위와 실제 검증 결과를 기록한다. -->
# 자동 회귀 테스트 CI 검증.

## 기준과 범위.

기준선은 `981744c08151d43fbaf3e4065a775ae3edfec792`다. 사용자 승인 설계의 1단계인 Windows·Linux 전체 회귀 CI, 운영 안내와 README 연결을 구현했다. 내부·외부 링크 검사와 병합 규칙은 후속 범위다. [설계](../superpowers/specs/2026-10-15-regression-ci.md)와 [계획](../superpowers/plans/2026-10-15-regression-ci.md)에 범위와 순서를 기록했다.

## 기준선 발견과 수정.

Linux Python 3.12.14에서 전체 64개 실행 중 오류 2개, Windows 전용 skip 4개를 확인했다. 두 오류는 외부 디렉터리 접근 거부 assertion 이후 cleanup에서 발생했다. POSIX 디렉터리 symlink에 os.rmdir를 호출한 것이 원인이다. Windows junction의 os.rmdir는 유지하고 POSIX는 unlink로 분기했다. 테스트를 삭제하거나 skip하지 않았고 제품 스크립트는 변경하지 않았다.

## 실제 로컬 검증.

- `python -X utf8 -B -m unittest discover -s tests -v`: 64개 실행, 60개 통과, 실패·오류 0개, Windows 전용 4개 skip, 5.260초다.
- CI YAML의 Bash 사전 검사 run 내용을 추출해 실제 Bash로 실행했다. Python과 Bash·필수 도구 조회를 통과했다.
- 별도 임시 디렉터리의 실패 unittest 1개를 동일 옵션으로 실행해 exit 1을 확인했다. 임시 테스트는 저장소에 추가하지 않았고 종료 후 제거했다. 실제 Actions에서의 실패 주입과는 구별한다.
- actionlint v1.7.12로 workflow를 검사했다. shellcheck와 pyflakes는 로컬에 없어 해당 선택 검사는 비활성화했으며 Actions YAML·표현식 검사에서 오류가 없었다.
- 변경 파일의 UTF-8·BOM 없음·LF와 Markdown fence·내부 파일 링크를 확인했다. git diff --check를 통과했다.
- 공식 actions/checkout v4와 actions/setup-python v5의 현재 tag commit을 조회해 SHA로 고정했다.

## 독립 리뷰.

독립 검토자가 네 테스트 파일 전체의 OS별 의존성, 전체 diff와 새 workflow·운영 안내·설계·계획을 검토했다. 표준 라이브러리만 필요하고 Git Bash·Windows PowerShell·CMD·COM을 사전 확인하는 구성을 확인했다. 현재 범위에서 차단·중요 발견은 없었다. 부모도 diff와 실제 검증 결과를 확인했다.

## 원격 실행 상태.

PR에서 실제 Ubuntu·Windows runner 실행을 확인하기 전까지 원격 검증은 대기 상태다. 로컬 Linux 결과만으로 Windows 통과를 주장하지 않는다. 별도 필수 병합 검사 설정이나 main 병합은 수행하지 않는다.

일반 git push는 사용 가능한 HTTPS 인증 정보가 없어 실패했다. 연결된 GitHub 앱의 git tree 생성도 `403 Resource not accessible by integration`으로 거부됐다. 원격 브랜치·PR·Actions 실행은 생성하지 못했고 main은 변경하지 않았다. 구현 커밋과 적용 가능한 git format-patch를 전달한다. 사용자 환경에서 패치를 적용·push한 뒤 실제 두 OS 결과를 확인해야 한다.
