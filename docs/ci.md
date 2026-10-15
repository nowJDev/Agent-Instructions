<!-- 이 저장소의 자동 테스트 실행 조건과 실패 확인 방법을 안내한다. -->
# 자동 회귀 테스트 안내.

이 저장소의 CI는 문서·설치 예제·작업 스크립트를 바꿨을 때 기존에 검증하던 동작이 유지되는지 확인한다. GitHub Actions의 **CI** 워크플로가 기존 Python unittest를 자동 실행한다.

## 언제 실행되나요.

| 상황 | 동작 |
|---|---|
| PR 생성·커밋 추가·다시 열기. | PR의 변경을 검사한다. |
| main 브랜치에 push. | 반영된 변경을 검사한다. |
| Actions에서 Run workflow 선택. | 선택한 브랜치를 수동 검사한다. |
| 같은 PR·브랜치에 새 실행 발생. | 오래된 실행을 취소하고 최신 실행을 남긴다. |

파일 경로 필터는 없다. Markdown 안의 설치 예제도 검사 대상이므로 문서만 바꿔도 실행한다. Draft PR도 검사한다. 저장소의 Actions 사용 설정이나 외부 기여 PR 승인 정책에 따라 실행 승인이 필요할 수 있다.

## 무엇을 검사하나요.

| 환경 | 검사 범위 |
|---|---|
| Ubuntu, Python 3.12. | 전체 테스트를 탐색하고 Bash 예제·설정 병합·백업·문서 경계 등을 검사한다. Windows 전용 테스트 4개는 의도적으로 건너뛴다. |
| Windows, Python 3.12. | 같은 전체 테스트와 PowerShell·CMD·바로가기 검사를 실행한다. 현재 테스트 구성에서는 skip 없이 실행되는 것이 기대 결과다. |

현재 테스트는 4개 파일, 64개 테스트다. `Ran 64 tests`는 건너뛴 테스트도 포함하므로 실제 결과의 실패·오류·skip을 함께 읽는다. 테스트가 늘면 실제 탐색 결과를 기준으로 확인한다.

추가 pip 패키지는 필요하지 않다. 테스트는 임시 디렉터리, 가짜 외부 SDK와 로컬 HTTP 서버를 사용한다. 실제 서비스로 업로드하거나 CLI를 설치·로그인하지 않는다.

CI는 Bash와 `mktemp`, `date`, `cp`, `curl`, `chmod`, `mv`, `rm`을 먼저 확인한다. Windows는 Git for Windows의 Bash를 선택해 WSL Bash 혼동을 방지하고 Windows PowerShell, CMD, `WScript.Shell`도 확인한다. 필수 도구가 없으면 사전 검사에서 실패한다. 테스트 단계에서 추가 skip이 발견되면 도구 부족이나 테스트 조건 변경을 확인한다.

## 내 컴퓨터에서 실행하려면.

저장소 루트에서 Python 3.12로 실행한다.

```bash
python -X utf8 -B -m unittest discover -s tests -v
```

Windows는 Git for Windows의 Bash가 Python 실행 환경의 PATH에서 선택되도록 준비한다. Windows 전용 검사는 `powershell.exe`, CMD, Windows Script Host COM을 사용하므로 PowerShell 7의 `pwsh`만으로 대체되지 않는다. Linux에서는 Windows 전용 테스트의 skip이 정상이다. 로컬 도구 부족으로 생긴 skip을 전체 검증 성공으로 해석하지 않는다.

## 실패했을 때 어디를 보나요.

1. PR의 Checks 또는 [Actions의 CI 목록](https://github.com/nowJDev/Agent-Instructions/actions/workflows/ci.yml)을 연다.
2. 실패한 `Regression (ubuntu-latest)` 또는 `Regression (windows-latest)` 작업을 연다.
3. 사전 검사 실패라면 도구 경로·실행 환경을 확인한다. 테스트 실패라면 `Run regression tests`의 실패한 테스트 이름과 traceback을 읽는다.
4. 원인을 수정하고 위 로컬 명령으로 관련 검사를 실행한 뒤 커밋을 올린다. 일시적인 runner 장애는 해당 실행의 Re-run failed jobs로 재시도한다.

한 OS가 실패해도 다른 OS 결과를 확인할 수 있다. 작업당 제한은 10분이며 제한 초과와 취소는 성공이 아니다. 테스트 종료 코드를 무시하지 않으므로 실패나 오류가 있으면 해당 작업도 실패한다.

## 적용 범위와 관리.

워크플로는 `.github/workflows/ci.yml`에 있다. 저장소 읽기 권한만 사용하고 checkout 인증 정보를 남기지 않는다. 공식 Actions는 확인한 커밋 SHA로 고정하며, 갱신할 때 upstream 릴리스·변경 내용과 두 OS 실행 결과를 확인한다. 별도 secrets나 배포 권한은 필요하지 않다.

README의 배지는 main의 결과를 표시한다. PR 단계의 상태는 PR Checks에서 확인하며, main에 워크플로가 처음 반영되기 전에는 배지 결과가 없을 수 있다.

이 CI는 기존 테스트가 확인하는 계약을 검사한다. 지침 의미의 정확성, 실제 사용자 설치·인증, 내부·외부 링크 전체 검사는 범위에 포함하지 않는다. 필수 병합 검사는 별도 저장소 규칙이며 이번 단계에서는 변경하지 않는다. 내부 문서 검사와 외부 링크 정기 점검은 후속 단계다.
