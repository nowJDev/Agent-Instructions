<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-15-regression-ci 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-10-15-regression-ci.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/specs/2026-10-15-regression-ci.md).

<!-- 승인된 자동 회귀 테스트 1단계의 범위와 완료 기준을 기록한다. -->
<a id="spec--자동-회귀-테스트-ci-설계"></a>
### 자동 회귀 테스트 CI 설계.

<a id="spec--승인과-기준선"></a>
#### 승인과 기준선.

2026-10-15 사용자가 설계안 실행을 승인했다. 기준선은 `981744c08151d43fbaf3e4065a775ae3edfec792`다. 기존 테스트 파일 4개에 테스트 64개가 있으며 GitHub Actions 워크플로는 없다. 새 작업 브랜치와 별도 클론에서 기존 사용자 작업을 보존한다.

<a id="spec--목표와-경계"></a>
#### 목표와 경계.

PR 생성·갱신, main push와 수동 실행에서 Python 3.12로 기존 전체 unittest를 Ubuntu·Windows에서 실행한다. 동일 PR·브랜치의 이전 실행은 취소하고 OS별 결과는 독립적으로 확인한다. README는 상태 배지와 운영 안내 링크만 보강한다.

이번 범위는 1단계다. 내부·외부 링크 검사, 추가 Python 버전, 필수 병합 검사, 전역 설정 변경과 자동 커밋은 포함하지 않는다. 지침 내용의 의미나 사용자 실제 설치 성공까지 자동으로 보장하지 않는다.

<a id="spec--실행과-실패-경로"></a>
#### 실행과 실패 경로.

checkout → Python 준비 → Windows Git Bash 선택 → 필수 도구 사전 검사 → 전체 테스트 순서다. Bash의 백업·다운로드 도구와 Windows의 PowerShell·CMD·COM을 확인한다. 도구 부재는 테스트 skip으로 숨기지 않고 실패한다. Ubuntu의 Windows 전용 테스트 4개 skip은 의도된 결과다. 실패는 원래 종료 코드와 traceback으로 확인하며 재시도는 수정 후 새 커밋 또는 Actions 수동 재실행으로 수행한다.

기준선 Linux 실행에서 심볼릭 링크를 os.rmdir로 정리하는 오류 2건을 재현했다. fixture의 Windows junction은 기존 os.rmdir, POSIX 심볼릭 링크는 unlink로 제거한다. 경계 거부 assertion과 실제 제품 코드는 변경하지 않는다.

<a id="spec--권한과-수명"></a>
#### 권한과 수명.

GitHub 호스트 임시 runner를 사용한다. 저장소 권한은 contents: read, checkout 인증 정보 보존은 끈다. 공식 Actions를 조회한 커밋 SHA로 고정한다. secrets, 외부 업로드, 배포와 사용자 계정 설치가 필요하지 않다. job 시간은 10분으로 제한한다. 테스트 fixture는 임시 디렉터리와 가짜 SDK·로컬 HTTP만 사용한다.

<a id="spec--검증과-완료-기준"></a>
#### 검증과 완료 기준.

- 두 정리 오류를 기존 테스트로 재현한 뒤 최소 수정으로 통과시킨다.
- 전체 64개 테스트의 통과·실패·skip을 기록한다.
- 임시 실패 테스트가 같은 unittest 명령을 비정상 종료시키는지 확인하고 임시 파일을 제거한다.
- YAML·GitHub Actions 정적 검사, UTF-8·LF·문서 링크·diff 검사를 수행한다.
- PR에서 두 OS의 실제 실행을 확인한다. 원격 권한이나 실행 제약이 있으면 미검증으로 기록한다.
- 전체 diff를 독립 검토하고 관련 문서를 한글 커밋으로 저장한다. main 병합과 보호 규칙 변경은 별도다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-15-regression-ci.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-15-regression-ci.md).

<!-- 자동 회귀 테스트 CI의 구현 순서와 검증 증거를 기록한다. -->
<a id="plan--자동-회귀-테스트-ci-실행-계획"></a>
### 자동 회귀 테스트 CI 실행 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 사용자의 설계안 실행 승인에 따라 진행한다.

Goal: 기존 회귀 테스트를 Ubuntu·Windows의 PR·main push·수동 CI로 실행한다.
Architecture: 표준 unittest와 GitHub 호스트 runner를 사용하며 제품 스크립트와 테스트 계약을 보존한다.
Tech Stack: Python 3.12, GitHub Actions YAML, Bash, PowerShell, Markdown.

<a id="plan--task-1-기준선과-최소-호환-수정"></a>
#### Task 1. 기준선과 최소 호환 수정.

Files: `tests/test_review_regressions.py`.

- [x] 전체 64개를 실행하여 POSIX link 정리 오류 2개와 Windows 전용 skip 4개를 확인했다.
- [x] link_directory의 정리를 플랫폼별로 분리하고 기존 경계 테스트 2개로 GREEN을 확인한다.

```python
self.addCleanup(os.rmdir, link) if os.name == 'nt' else self.addCleanup(link.unlink)
```

실제 구현은 각 OS 분기 안에 정리 등록을 배치한다. 실패 테스트를 제거하거나 skip하지 않는다.

<a id="plan--task-2-ci와-운영-안내"></a>
#### Task 2. CI와 운영 안내.

Files: `.github/workflows/ci.yml`, `docs/ci.md`, `README.md`, `CHANGELOG.md`.

- [x] PR·main push·수동 트리거, Python 3.12, Ubuntu·Windows, 읽기 권한, SHA 고정, 중복 취소와 timeout을 구현한다.
- [x] Git Bash와 Windows 도구·COM 사전 검사를 추가하고 원래 테스트 종료 코드를 보존한다.
- [x] 운영 안내와 README 상태 배지·링크, 변경 이력을 작성한다.

```bash
python -X utf8 -B -m unittest discover -s tests -v
```

기대 GREEN은 Ubuntu 60개 통과·4개 의도적 skip, Windows 64개 통과·skip 0개다. 테스트 목록 변경 시 실제 수를 기준으로 보고한다.

<a id="plan--task-3-검증리뷰전달"></a>
#### Task 3. 검증·리뷰·전달.

Files: 이 계획, `docs/reviews/2026-10-15-regression-ci.md`, `docs/current-state.md`, `docs/design-progress-checklist.md`.

- [x] 전체 회귀와 임시 실패 테스트를 통한 exit 1 검출을 확인한다.
- [x] actionlint·인코딩·문서 링크·git diff --check와 독립 리뷰를 확인한다.
- [x] 한글 커밋으로 저장하고 적용용 패치를 준비한다.
- [x] 사용자 환경의 별도 worktree에서 두 커밋을 git am으로 적용하고 push하여 PR #1을 생성했다. 기존 main의 미전송 커밋은 보존했다.
- [x] 첫 Actions 실행의 Windows 경쟁 생성 fixture 오류를 경로 정규화 한 줄 수정으로 보완했다. 로컬 별칭 경로 RED·GREEN과 전체 64개 회귀, 독립 재검토 및 GitHub 두 OS 재실행 성공을 확인했다.

```bash
git diff --check
git add .github/workflows/ci.yml README.md CHANGELOG.md tests/test_review_regressions.py docs
git commit -m "Windows와 Linux 자동 회귀 테스트 CI 추가"
```

<a id="plan--task-4-후속-승인된-통합과-정리"></a>
#### Task 4. 후속 승인된 통합과 정리.

Files: 현재 상태·진행 체크리스트·이 계획과 CI 및 Chrome DevTools 검증 기록.

- [x] 전체 push·병합·정리 추가 승인을 확인하고 PR #1을 커밋 이력을 보존해 병합했다.
- [x] 기존 로컬 커밋 `b77f3ed`의 공개 범위와 통합 diff를 검토하고 일반 merge했다. 통합 main의 전체 64개 회귀를 통과했다.
- [x] 실제 경로·미커밋 파일·로컬과 원격 병합을 확인하고 이번 임시 worktree와 로컬·원격 작업 브랜치를 정리했다. 개인 파일·원본 패치·Git 이력은 보존했다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-15-regression-ci.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-15-regression-ci.md).

<!-- CI 1단계의 변경 범위와 실제 검증 결과를 기록한다. -->
<a id="review--자동-회귀-테스트-ci-검증"></a>
### 자동 회귀 테스트 CI 검증.

<a id="review--기준과-범위"></a>
#### 기준과 범위.

기준선은 `981744c08151d43fbaf3e4065a775ae3edfec792`다. 사용자 승인 설계의 1단계인 Windows·Linux 전체 회귀 CI, 운영 안내와 README 연결을 구현했다. 내부·외부 링크 검사와 병합 규칙은 후속 범위다. [설계](#spec)와 [계획](#plan)에 범위와 순서를 기록했다.

<a id="review--기준선-발견과-수정"></a>
#### 기준선 발견과 수정.

Linux Python 3.12.14에서 전체 64개 실행 중 오류 2개, Windows 전용 skip 4개를 확인했다. 두 오류는 외부 디렉터리 접근 거부 assertion 이후 cleanup에서 발생했다. POSIX 디렉터리 symlink에 os.rmdir를 호출한 것이 원인이다. Windows junction의 os.rmdir는 유지하고 POSIX는 unlink로 분기했다. 테스트를 삭제하거나 skip하지 않았고 제품 스크립트는 변경하지 않았다.

<a id="review--패치-작성-환경의-로컬-검증"></a>
#### 패치 작성 환경의 로컬 검증.

- `python -X utf8 -B -m unittest discover -s tests -v`: 64개 실행, 60개 통과, 실패·오류 0개, Windows 전용 4개 skip, 5.260초다.
- CI YAML의 Bash 사전 검사 run 내용을 추출해 실제 Bash로 실행했다. Python과 Bash·필수 도구 조회를 통과했다.
- 별도 임시 디렉터리의 실패 unittest 1개를 동일 옵션으로 실행해 exit 1을 확인했다. 임시 테스트는 저장소에 추가하지 않았고 종료 후 제거했다. 실제 Actions에서의 실패 주입과는 구별한다.
- actionlint v1.7.12로 workflow를 검사했다. shellcheck와 pyflakes는 로컬에 없어 해당 선택 검사는 비활성화했으며 Actions YAML·표현식 검사에서 오류가 없었다.
- 변경 파일의 UTF-8·BOM 없음·LF와 Markdown fence·내부 파일 링크를 확인했다. git diff --check를 통과했다.
- 공식 actions/checkout v4와 actions/setup-python v5의 현재 tag commit을 조회해 SHA로 고정했다.

<a id="review--독립-리뷰"></a>
#### 독립 리뷰.

독립 검토자가 네 테스트 파일 전체의 OS별 의존성, 전체 diff와 새 workflow·운영 안내·설계·계획을 검토했다. 표준 라이브러리만 필요하고 Git Bash·Windows PowerShell·CMD·COM을 사전 확인하는 구성을 확인했다. 현재 범위에서 차단·중요 발견은 없었다. 부모도 diff와 실제 검증 결과를 확인했다.

<a id="review--원격-실행-상태"></a>
#### 원격 실행 상태.

패치 작성 환경에서는 HTTPS 인증 정보 부재와 GitHub 앱의 `403 Resource not accessible by integration`으로 전달이 차단됐다. 사용자 Windows 환경에서는 원격 main 기준의 별도 worktree·브랜치에 두 커밋을 git am으로 적용하고 push하여 [PR #1](https://github.com/nowJDev/Agent-Instructions/pull/1)을 생성했다. 원본 main의 미전송 커밋 `b77f3ed`는 PR에서 제외하고 보존했다. 최초 전달에는 main 병합을 포함하지 않았으며 이후 승인된 통합은 아래에 기록한다.

<a id="review--사용자-windows-검증과-runner-회귀-수정"></a>
#### 사용자 Windows 검증과 runner 회귀 수정.

Windows Python 3.12.10 전체 unittest는 적용 전 64개·22.279초, 적용 후 64개·21.081초로 모두 통과했고 실패·오류·skip은 없었다. Bash·COM·CMD 사전 검사와 변경 파일 10개의 UTF-8·BOM 없음·LF·상대 문서 링크를 확인했다. 전체 패치와 네 테스트 파일의 독립 리뷰에서 차단·중요 발견은 없었다.

[첫 Actions 실행](https://github.com/nowJDev/Agent-Instructions/actions/runs/38677825016)에서 Ubuntu는 성공했으나 Windows는 `test_bootstrap_does_not_overwrite_concurrent_creation`이 실패했다. 제품 스크립트는 경로를 resolve하지만 fixture의 비교 대상은 원래 임시 경로여서 정규화 전후 표기가 다르면 경쟁 생성 mock이 실행되지 않았다. 로컬에서 `..`를 포함한 동일 디렉터리 경로로 같은 assertion 실패를 재현했다. 비교 대상에 resolve를 적용하는 한 줄 수정 후 재현 조건을 통과했다. 사용자 문서 보존 assertion과 제품 스크립트는 유지했으며 독립 재검토에서도 수정이 타당함을 확인했다. 수정 후 로컬 전체 64개도 22.126초에 실패·오류·skip 없이 통과했다.

<a id="review--실제-github-재실행-결과"></a>
#### 실제 GitHub 재실행 결과.

2026-10-15 수정 커밋 `0558c94`의 [실행 38678117512](https://github.com/nowJDev/Agent-Instructions/actions/runs/38678117512)이 성공했다. 두 OS의 필수 도구 사전 검사와 테스트 단계 모두 성공했다.

| 환경 | 전체 탐색 | 통과 | 실패·오류 | skip | 테스트 시간 |
|---|---|---|---|---|---|
| Ubuntu, Python 3.12.15. | 64개. | 60개. | 0개. | Windows 전용 4개. | 6.627초. |
| Windows, Python 3.12.10. | 64개. | 64개. | 0개. | 0개. | 19.082초. |

runner에는 고정된 checkout v4·setup-python v5의 Node.js 20 지원 종료에 따른 Node.js 24 강제 실행 경고가 남는다. 이번 두 OS 실행은 성공했으며 Actions 주요 버전 갱신은 별도 범위다. ubuntu-latest의 Ubuntu 26 전환 예정 안내도 있으므로 향후 runner 이미지 변경 시 같은 회귀 결과를 확인한다.

<a id="review--후속-승인에-따른-main-통합과-정리"></a>
#### 후속 승인에 따른 main 통합과 정리.

사용자가 전체 커밋·push·병합·안전한 임시 파일 정리를 승인했다. 최종 PR 커밋 `64560ec`의 [두 OS 실행](https://github.com/nowJDev/Agent-Instructions/actions/runs/38678337763) 성공을 확인한 뒤 PR #1을 merge commit `eaeb985`로 병합했다. 기존 Chrome DevTools 지침 커밋 `b77f3ed`는 독립 검토에서 공개를 막을 시크릿·내부 자료나 중요한 결함이 없음을 확인하고 일반 merge `0804445`로 통합했다. CHANGELOG의 두 작업 항목과 모든 기존 커밋 이력을 보존했다.

통합 main의 Windows Python 3.12.10 전체 64개 테스트가 23.216초에 통과했고 실패·오류·skip은 없었다. 실제 경로와 reparse point 여부, 미커밋·untracked·ignored 파일 부재 및 로컬·원격 main에서의 병합 여부를 확인한 뒤 이번 임시 CI worktree와 로컬·원격 작업 브랜치를 삭제했다. 원본 다운로드 패치·개인 파일·복구용 Git 이력은 보존했다. 필수 병합 규칙과 Actions 주요 버전은 변경하지 않았다.
