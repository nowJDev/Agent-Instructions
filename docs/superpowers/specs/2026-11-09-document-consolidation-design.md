<!-- 파일 수를 줄이는 문서 통합의 범위·이전 규칙·검증 기준을 정의한다. -->
# 문서 통합 상세 설계.

작성일은 2026-11-09다. 상태는 2026-11-09 사용자 승인 후 구현·검증·글로벌 적용을 마쳤다. 사용자가 설계 실행과 PC 글로벌 적용·저장소 반영·커밋·푸시까지 승인했다. 실제 검증·배포 결과는 이번 리뷰에 기록한다.

## 1. 목적과 승인 범위.

사용자는 무의미하게 많은 파일을 줄이고 찾기 쉬운 문서 구조를 원한다. 앞선 대화의 분류별 카탈로그 통합과 과거 작업별 기록 통합을 추천안으로 구체화한다. 세부 경로·호환성 정책·파일 수는 이번 설계자의 제안이며 이 문서 승인 전에는 구현하지 않는다.

목표는 다음과 같다.

- 카탈로그의 121개 설명 항목을 보존하면서 파일을 23개 분류 문서로 줄인다.
- 과거 설계·계획·리뷰 37개를 작업별 14개 보관 기록으로 묶는다.
- 현재 안내, 설치 원본, 과거 증거의 역할을 구분하고 중복 설명을 줄인다.
- 목차에서 원하는 항목으로 직접 이동하고 테스트가 실제 문서 예제를 계속 검사하게 한다.
- 전체 추적 파일 수를 기준선 270개에서 예상 154개로 줄인다.

비목표는 다음과 같다.

- 설치 가능한 스킬 패키지 25개나 MCP 서버 기능을 삭제하거나 합치는 일.
- 실제 전역 지침·스킬 설치본·MCP 설정·로그인·바탕화면을 변경하는 일.
- 파일 수만 줄이려고 테스트·출처·해시·평가 자료를 제거하는 일.
- 외부 도구 전체의 최신 버전 갱신, 정기 링크 모니터링, 문서 생성 시스템 도입.
- 이번 변경으로 범용 design-driven-delivery 스킬의 문서 계약·검증기를 개편하는 일.

## 2. 기준선과 확인한 의존성.

기준 커밋은 `a559c66d71aee886e717ff91bffce6270accdb17`이다. 설계 시작 시 main의 작업 트리는 깨끗했다. 추적 파일은 270개이며 Markdown은 249개다. 앞선 감사에서 Windows Python 3.11.9 전체 회귀 72개 통과를 확인했다. 이는 이번 통합 구현의 검증 결과가 아니다.

| 영역 | 기준 파일 수 | 통합 후 파일 수 | 처리. |
|---|---:|---:|---|
| Skill 설명 본문. | 121 | 23 | 기존 그룹 폴더의 README로 병합. |
| Skill 상위 안내·목차. | 2 | 2 | 출처 안내와 항목별 링크를 유지. |
| 과거 작업 설계·계획·리뷰. | 37 | 14 | docs/history의 작업별 기록으로 병합. |
| 과거 작업 목차. | 0 | 1 | docs/history/README.md 추가. |
| 이번 작업 설계·계획·리뷰. | 0 | 3 | 진행 중에는 기존 승인 구조 사용. |
| 문서 계약 회귀 테스트. | 0 | 1 | tests/test_documentation.py 추가. |
| 그 밖의 파일. | 110 | 110 | 개수 유지, 필요한 참조·중복 본문만 갱신. |
| 합계. | 270 | 154 | 순감소 116개, 약 43퍼센트. |

154개는 이번 설계·계획·리뷰와 새 테스트까지 포함한 구현 완료 시 예상치다. 설계 초안만 있던 승인 전 작업 트리의 물리적 파일 수는 271개였다. 기준선이 바뀌면 구현 계획에서 목록과 개수를 다시 대조한다. 개수에 맞추려고 다른 파일을 삭제하지 않는다.

필수 의존성은 다음과 같다.

- `tests/test_upload_examples.py`는 Hugging Face의 datasets와 lora-space-builder 문서 파일을 직접 읽어 Python 블록을 실행한다.
- `tests/test_setup_profiles.py`와 `tests/test_review_regressions.py`는 설치 안내의 PowerShell·Bash·Python 예제를 직접 읽는다.
- 워크플로 검증기는 `docs/current-state.md`, `docs/design-progress-checklist.md`와 종류별 설계·계획·리뷰 문서를 요구한다. 현재 작업 문서를 명시적으로 선택할 수 있다.
- `Owned-Skills/`는 독립 설치 패키지다. `Skill/`의 설명 문서와 같은 이름이 있어도 서로 다른 배포 대상이다.

## 3. 검토한 접근법.

| 방식 | 장점. | 한계. | 결정. |
|---|---|---|---|
| 항목별 파일 유지. | 필요한 파일만 읽기 쉽다. | 파일 수가 줄지 않고 목차·출처 수정 지점이 많다. | 채택하지 않는다. |
| 분류별 README 통합. | 약 100개 감소, 기존 그룹 디렉터리 링크 유지, 항목별 이동 가능. | 긴 그룹 문서에서 해당 항목 범위를 찾아 읽어야 한다. | 추천안이다. |
| 카탈로그 전체 단일 파일. | 감소 폭이 가장 크다. | 서로 다른 출처·클라이언트가 한 긴 문서에 섞인다. | 채택하지 않는다. |

카탈로그가 길어져도 항목을 다시 개별 파일로 분리하지 않는다. 목차·검색·항목 경계를 이용한다. 앞으로 분리해야 할 독립 배포 단위가 생기면 별도 근거와 승인으로 결정한다.

## 4. 목표 디렉터리와 진입 흐름.

```text
README.md                          시작 문장과 핵심 안내.
GUIDE.md                           사람용 개념 설명과 FAQ.
GETTING_STARTED.md                 적용·설치 절차의 기준 문서.
AGENTS.md / codex-global-AGENTS.md  핵심 행동 규칙과 전역용 변형.
PORTABILITY.md                     클라이언트별 번역·이식 기준.
rules/                             기존 4개 상세 규칙.
Skill/
  README.md                        분류·출처·설치·이전 안내.
  CATALOG.md                       121개 항목의 한 줄 링크 목차.
  <그룹>/README.md                 분류별 설명 본문.
  _disabled/<플러그인>/README.md    비활성 카탈로그 5개.
MCP/                               기존 서버별 설명 유지.
Owned-Skills/                      설치 가능한 패키지 유지.
references/                        설치 예제와 출처·버전 자료 유지.
docs/
  current-state.md                 최신 상태와 남은 확인.
  design-progress-checklist.md     현재 작업의 진행 상태.
  ci.md                            기존 CI 운영 안내.
  history/
    README.md                      보관 작업 목록과 이전 안내.
    <날짜-작업>.md                 작업별 설계·계획·검증 증거.
  superpowers/specs/               진행 중인 설계.
  superpowers/plans/               진행 중인 계획.
  reviews/                        진행 중인 리뷰.
tests/
  기존 5개 테스트 파일.
  test_documentation.py            문서 구조·링크·항목 경계 검사.
```

사람은 README에서 시작하고 CATALOG의 항목을 클릭해 그룹 README의 해당 절로 이동한다. AI는 AGENTS에서 필요한 문서로 이동하고 항목별 목적·절차·실패 처리·출처를 확인한다. 스킬 설치는 계속 Owned-Skills 또는 타사 원본에서 수행한다.

## 5. Skill 통합 명세.

각 행의 기존 폴더 안 개별 Markdown 본문을 그 폴더의 README.md 하나로 합친다.

| 기존 그룹 폴더. | 본문 항목 수. | 새 파일. |
|---|---:|---|
| Skill/_builtin/ | 13 | Skill/_builtin/README.md |
| Skill/_personal/ | 5 | Skill/_personal/README.md |
| Skill/superpowers/ | 15 | Skill/superpowers/README.md |
| Skill/huggingface-skills/ | 18 | Skill/huggingface-skills/README.md |
| Skill/firecrawl/ | 11 | Skill/firecrawl/README.md |
| Skill/figma/ | 9 | Skill/figma/README.md |
| Skill/plugin-dev/ | 8 | Skill/plugin-dev/README.md |
| Skill/chrome-devtools-mcp/ | 6 | Skill/chrome-devtools-mcp/README.md |
| Skill/ralph-loop/ | 3 | Skill/ralph-loop/README.md |
| Skill/claude-md-management/ | 2 | Skill/claude-md-management/README.md |
| Skill/qodo-skills/ | 2 | Skill/qodo-skills/README.md |
| Skill/agent-sdk-dev/ | 1 | Skill/agent-sdk-dev/README.md |
| Skill/pr-review-toolkit/ | 1 | Skill/pr-review-toolkit/README.md |
| Skill/feature-dev/ | 1 | Skill/feature-dev/README.md |
| Skill/claude-code-setup/ | 1 | Skill/claude-code-setup/README.md |
| Skill/skill-creator/ | 1 | Skill/skill-creator/README.md |
| Skill/frontend-design/ | 1 | Skill/frontend-design/README.md |
| Skill/playground/ | 1 | Skill/playground/README.md |
| Skill/_disabled/vercel/ | 13 | Skill/_disabled/vercel/README.md |
| Skill/_disabled/hookify/ | 5 | Skill/_disabled/hookify/README.md |
| Skill/_disabled/neon/ | 2 | Skill/_disabled/neon/README.md |
| Skill/_disabled/railway/ | 1 | Skill/_disabled/railway/README.md |
| Skill/_disabled/semgrep/ | 1 | Skill/_disabled/semgrep/README.md |

각 그룹 앞부분에 분류, 작성 시점, 설명 카탈로그라는 점과 항목별 링크 목차를 둔다.

- 문서 제목은 H1, 각 항목은 `## claude-news`와 같은 H2, 항목 내부의 용도·절차 등은 H3 이하로 구성한다.
- 항목 ID는 원래 파일명에서 확장자를 뺀 값을 사용하고 대소문자·하이픈·밑줄을 유지한다.
- help처럼 이름이 같은 항목은 그룹 상대경로로 구분한다. 121개 식별자는 그룹 상대경로와 항목 ID의 조합으로 검증한다.
- 코드 블록 안의 제목처럼 보이는 문자열은 수정하지 않는다. 테스트가 사용하는 코드, 입력·출력 제한, 실패 시 절차를 보존한다.
- 항목별 출처 URL, 확인 버전, 적용 클라이언트와 원문 미확인 고지를 보존한다. 실제로 같은 설명만 공통화한다.
- Vercel 내부 개발용 8개 항목도 삭제하지 않고 같은 README의 내부 개발용 작은 목차로 분류한다.
- CATALOG의 121개 항목을 모두 `<그룹>/README.md#<항목-ID>`로 연결하고 그룹 문서에도 상위 목차로 가는 링크를 둔다.
- 기존 99개와 OFF 22개 집계는 당시 카탈로그 항목 수로 설명한다. 명령·메타 문서까지 실제 호출 가능한 스킬 수로 표현하지 않는다.

## 6. 과거 37개 문서의 14개 기록 통합.

각 새 파일은 `docs/history/`에 둔다. 표의 설계·계획·리뷰는 가져오는 이전 문서 수다. 파일명을 기계적으로 잘라 분류하지 않고 대상·기준선·참조 관계로 같은 작업인지 확인한다.

| 새 파일명. | 설계·계획·리뷰. | 가져올 문서의 식별. |
|---|---|---|
| 2026-10-12-readme-mermaid.md | 0·1·0 | 기존 plans의 readme-mermaid. |
| 2026-10-13-client-cli-setup.md | 1·1·1 | client-cli-setup-design, client-cli-setup, client-cli-setup-review. |
| 2026-10-13-codex-windows-setup.md | 1·1·1 | codex-windows-setup-design, codex-windows-setup, codex-windows-setup-review. |
| 2026-10-13-review-fixes.md | 0·1·1 | 같은 이름의 plans와 reviews. |
| 2026-10-13-review-followup.md | 0·1·1 | 같은 이름의 plans와 reviews. |
| 2026-10-13-starred-repo-adoption.md | 1·1·1 | starred-repo-adoption-design, starred-repo-adoption, starred-repo-adoption-review. |
| 2026-10-14-beginner-readme-and-audit-fixes.md | 1·1·1 | 같은 이름의 specs, plans, reviews. |
| 2026-10-14-chrome-devtools-mcp.md | 1·1·1 | 같은 이름의 specs, plans, reviews. |
| 2026-10-14-repository-review.md | 0·1·1 | repository-review라는 같은 이름의 plans와 reviews. |
| 2026-10-15-portable-skill-workflows.md | 1·1·1 | 같은 이름의 specs, plans, reviews. |
| 2026-10-15-regression-ci.md | 1·1·1 | 같은 이름의 specs, plans, reviews. |
| 2026-11-05-superpowers-update.md | 1·1·1 | 같은 이름의 specs, plans, reviews. |
| 2026-11-06-codex-skills-update.md | 1·1·1 | 같은 이름의 specs, plans, reviews. |
| 2026-11-06-skill-provenance.md | 1·1·1 | 같은 이름의 specs, plans, reviews. |

작업별 문서는 다음 순서로 구성한다.

1. 상태·작업 날짜·기준 커밋·후속 또는 대체 작업 링크.
2. 결과·남은 확인을 짧게 요약한 현재 관점의 안내.
3. 이전 설계 원문.
4. 이전 계획 원문.
5. 이전 리뷰·검증 원문.
6. 원본 경로와 고정 커밋을 포함한 출처 목록.

원문이 없었던 종류는 새 승인이나 리뷰를 만들어 채우지 않는다. 승인 문구·체크 상태·실패 증거·미검증·과거 테스트 수는 당시 상태 그대로 보존한다. 경로·앵커의 기계적 변경과 제목 수준 조정만 허용하고 원문을 새로운 요약으로 대체하지 않는다.

보관이 모든 기능의 실사용 검증 완료를 뜻하지 않는다. Claude 로그인 대기 등 남은 확인은 current-state에서도 해당 보관 문서로 연결해 유지한다. 날짜가 같은 설치 전후 집계 133개와 132개도 시점 차이를 보존한다.

docs/history/README.md에는 14개 작업의 날짜·상태·요약·새 주소와 37개 이전 문서의 새 절 매핑을 둔다. 이전 상세 기록을 CHANGELOG에 복제하지 않는다.

## 7. 진입 문서·중복 내용의 책임.

| 문서. | 남길 책임. | 다른 문서로 연결할 내용. |
|---|---|---|
| README.md | 목적, 두 시작 문장, 핵심 원칙, 문서 찾기. | 구체적인 설치·이식·도구 목록. |
| GUIDE.md | 사람용 개념, 예시, FAQ. | 실행 명령과 설치 완료 조건의 상세. |
| GETTING_STARTED.md | 설치 대상 선택, 적용·설치 순서, 확인·실패 기준. | 바로가기 구현 코드는 기존 references로 연결. |
| PORTABILITY.md | 환경별 차이·대체 방법·이식 원칙. | 공통 최소 설치 정책은 GETTING_STARTED로 연결. |
| AGENTS.md | 독립적으로 알아야 하는 의도·읽기·검증·보안·중단 규칙. | 긴 설치 정책·전체 개수·과거 상태. |
| codex-global-AGENTS.md | Codex 전역 경로와 도구 차이가 반영된 핵심 규칙. | 상세 정책은 복제본 경로로 연결. |
| docs/current-state.md | 최신 구조, 현재 검증 범위, 남은 확인, 작업 링크. | 과거 PR·패치·테스트 상세 이력. |
| docs/design-progress-checklist.md | 현재 작업의 실제 진행·검증 상태. | 이전 작업의 완료 목록. |

핵심 안전 규칙은 자동으로 링크 문서가 읽히지 않는 환경을 위해 두 AGENTS 본문에 계속 둔다. 설명 중복과 필수 규칙의 의도된 반복을 구분한다.

이번 구현에서는 통합 대상에 직접 관련된 아래 정합성도 함께 맞춘다.

- claude-news의 선택 기준은 Owned-Skills 원본의 10일 이내 전부 표시와 일치시킨다. 설치 원본의 동작을 바꾸지 않는다.
- pr-review-toolkit 포함·제외 설명을 실제 카탈로그 수록 기준에 맞춘다.
- Codex 시작 대기 키와 Firecrawl 최소 주기는 해당 버전의 공식 근거를 확인한 뒤 하나로 설명한다. 확인할 수 없으면 수치 예제를 제거하고 확인 가능한 공식 안내로 연결하며 검증하지 않은 값을 확정하지 않는다.
- Claude 확장 설치의 구형 바로가기 생성 블록은 공통 절차 링크로 대체한다. 지침·스킬·키바인딩은 기존 사용자 파일 확인·백업·보존 병합 원칙을 적용한다. 교체가 필요한 경우의 범위·복구를 명시한다.
- rules/01의 특정 작업 폴더 상태와 rules/03의 dotfiles·sync.py는 사용자별 환경의 선택 절차임을 밝힌다. 실제 원본·동기화 체계를 확인하지 않고 해당 명령을 강제하지 않는다.

검증되는 설치 코드의 실행 계약을 바꿀 필요가 생기면 문서 정리 범위에서 임의로 확장하지 않고 별도 결함 수정 범위로 분리한다.

## 8. 링크·호환성 이전 규칙.

기존 파일을 지우기 전에 이전 경로·제목과 새 경로·앵커의 대응을 확정한다. 내부 Markdown 링크, 참조형 링크, 목차, 현재 안내의 인라인 코드 경로, 테스트 문자열을 구분해 갱신한다.

- 예를 들어 `Skill/_personal/claude-news.md`는 `Skill/_personal/README.md#claude-news`로 옮긴다.
- 그룹 README의 부모 폴더는 원래와 같으므로 변경 없는 상대 링크는 유지한다. 다른 삭제 대상 파일을 가리키는 링크는 항목의 새 주소로 바꾼다.
- 이전 링크에 하위 제목 fragment가 있으면 새 문서의 해당 절에 항목명을 접두사로 붙인 명시적 앵커를 둔다. 중복 ID, 누락 fragment, 이름 충돌이 있으면 삭제를 중단한다.
- 이전 기록의 설계·계획·리뷰에는 각각 `#spec`, `#plan`, `#review` 명시적 앵커를 둔다. 원문의 하위 제목 링크는 종류별 접두사로 구분한다.
- 코드 예제 문자열, 변경 이력의 이전 경로 인용, 이전 매핑표는 과거 기록으로 유지할 수 있다. 실제 내부 링크 누락에는 예외를 적용하지 않는다.
- codex-global-AGENTS.md의 `Agent-Instructions/` 상대 링크는 설치 위치 기준으로 해석한다. 이 파일의 알려진 접두사만 가상 배치로 검사하고 파일 전체를 검사에서 제외하지 않는다.
- 새로운 리다이렉트 파일이나 심볼릭 링크는 만들지 않는다. 기존 codex-windows-shortcut.md는 기존 주소 호환용의 작은 안내로 유지한다.

GitHub main에서 삭제된 개별 파일 URL은 그대로 열리지 않게 된다. 이번 설계에서 제안하는 명시적 호환성 변경이다. 모든 이전 URL을 유지하려면 121개 이상의 연결용 파일을 남겨야 하므로 파일 감소 목적을 만족하지 못한다. Skill/README와 history/README에 새 위치를 찾는 방법과 [고정된 이전 버전](https://github.com/nowJDev/Agent-Instructions/tree/a559c66d71aee886e717ff91bffce6270accdb17) 링크를 둔다. 외부 사이트의 링크가 자동으로 전환된다고 설명하지 않는다.

이전 로컬 복사본은 자동 갱신되지 않는다. 사용자의 후속 승인으로 이번 작업에 기존 글로벌 복사본과 활성 전역 지침의 적용을 포함한다. 소유 파일과 개인 추가 파일을 구분하고 백업·보존 병합하여 오래된 파일이 남는 단순 덮어쓰기를 피한다.

## 9. 유지할 파일과 재증가 방지.

- Owned-Skills의 62개 파일과 25개 패키지를 유지한다. 독립 설치와 자기완결 리소스의 경계를 바꾸지 않는다.
- MCP 17개와 rules 4개 파일을 유지한다. 인증과 서버별로 독립된 설명을 무리하게 하나로 합치지 않는다.
- references의 8개 파일을 유지한다. 같은 날짜의 출처 기록·업데이트 기록·JSON은 설치 전후 시점과 사람용·기계용 역할을 목차에서 구분한다.
- daily-work-report의 평가 자료는 삭제하지 않는다. 수동 평가 방법 정비를 파일 감소의 조건으로 삼지 않는다.
- 기존 그룹에 새 카탈로그 항목을 추가할 때는 README에 절을 추가한다. 개별 파일을 늘리지 않는다.
- 진행 중 작업의 설계·계획·리뷰는 분리하고 작업 종료 시 history 한 기록으로 묶는다. 구현 완료와 외부 검증 대기는 서로 다른 상태로 남긴다.
- 이번 설계·계획·리뷰 3개는 구현 직후 그대로 둔다. 다음 작업에서 보관할 때 3개를 1개로 줄일 수 있지만 이번 154개 계산에는 반영하지 않는다.
- 이전 매핑, 검증용 고정값, 복구 설명만을 위한 별도 JSON·설정·설명 파일은 만들지 않는다. 필요한 목록은 기존 목차·기록과 테스트 파일 하나에 둔다.

## 10. 테스트와 완료 조건.

새 `tests/test_documentation.py`는 표준 라이브러리 unittest를 사용한다. 기존 `test_owned_skill_packages.py`의 Markdown 링크 추출 함수를 재사용하고 외부 의존성을 추가하지 않는다. 검사기의 한계를 명시하며 의미의 정확성을 단순 문자열 일치로 보장한다고 주장하지 않는다.

필수 자동 검증은 다음과 같다.

1. 23개 그룹에 121개 항목이 한 번씩 있으며 CATALOG 링크 대상이 모두 존재한다. 누락·중복·추가 항목을 반례로 검사한다.
2. 전체 Markdown의 내부 링크와 참조형 링크의 파일·디렉터리·제목·명시적 앵커를 확인한다. 코드 예제를 링크로 오인하지 않고 존재하지 않는 fragment를 놓치지 않는 반례를 둔다.
3. Hugging Face 테스트는 datasets와 lora-space-builder의 해당 항목 절에서만 Python 코드를 추출하도록 갱신한다. 전체 README에서 업로드 블록 하나를 고르는 방식으로 바꾸지 않는다. 공개·불명확·조회 실패 시 전송하지 않는 기존 4개 동작 테스트를 유지한다.
4. 일회성 이전 검증에서 기준 커밋의 121개 항목·37개 원문·코드 예제·출처 URL을 새 배치와 비교한다. 구조 변경과 명시한 정합성 수정 외에 내용이 빠지면 실패다. 비교에 필요한 임시 목록은 저장소 밖 임시 공간에 두고 상시 생성 시스템을 만들지 않는다.
5. Owned-Skills와 변경 대상이 아닌 바이너리·JSON의 해시를 기준선과 비교해 의도하지 않은 변경이 없음을 확인한다.
6. `python -X utf8 -B -m unittest discover -s tests -v`, `git diff --check`, UTF-8/BOM·코드 펜스·금지 정보 검사를 실행한다. 테스트가 추가되므로 72개 고정 수치를 성공 조건으로 삼지 않는다.
7. 워크플로 완료 검사에는 이번 spec·plan·review를 명시적으로 지정한다. 과거 보관 기록을 현재 완료 증거 대신 전달하지 않는다. 기존 검증기를 수정하거나 빈 디렉터리 보존용 .gitkeep을 추가하지 않는다.
8. 추적 파일 수, 카탈로그 식별자 수, 기록 원문 수, 변경·유지 대상을 최종 차이와 대조한다.

기존 CI는 tests를 자동 탐색하므로 workflow 변경은 원칙적으로 필요하지 않다. 구현 후 가능한 Windows Python 3.12와 CI의 Ubuntu·Windows 결과를 구분해 보고한다. 실행하지 못한 환경을 통과로 취급하지 않는다.

수동으로 README에서 CATALOG와 임의의 3개 그룹, OFF에서 Vercel 내부 개발 항목, GUIDE에서 설치 안내, 기록에서 설계·계획·리뷰, 고정된 이전 버전으로 가는 경로를 확인한다. GitHub 또는 사용 가능한 Markdown 뷰어에서 목차·앵커·코드 블록 표시를 확인한다. 외부 원문 전체의 도달성 조사나 실제 서비스 로그인은 완료 조건에 포함하지 않는다.

합격 조건은 내용 누락·중복·내부 링크 누락 없음, 기존 안전 테스트 유지, 과거 미검증 상태 보존, 보호 파일 불변, 파일 수 감소 근거 일치다. 154개에서 벗어나는 추가 파일이 필요하면 목적과 증감을 설명하고 설계를 갱신한다.

## 11. 실행 순서와 중단·복구.

설계 승인 후 writing-plans로 정확한 경로·테스트·커밋 단위로 구체화한다. 여기서는 실행 순서의 계약만 정의하며 구현 계획이 승인된 것으로 취급하지 않는다.

1. 기준 커밋과 사용자 변경을 재확인하고 기존 격리 상태·네이티브 기능을 우선해 작업 위치를 준비한다. 기준선이 바뀌면 목록과 개수를 다시 계산한다.
2. 문서 계약 검사와 대상 테스트 변경을 먼저 준비하고 누락·링크 손상·항목 경계의 실패를 확인한다.
3. 카탈로그 23개 문서와 새 목차를 만들고 이전 121개 항목을 일대일로 대조한 뒤 원래 파일을 개별 삭제한다.
4. 기록 14개 문서와 목차를 만들고 37개 원문의 이관을 대조한 뒤 원래 파일을 개별 삭제한다.
5. 현재 링크, 진입 문서 중복, 발견된 관련 정합성 문제, 현재 상태와 체크리스트를 갱신한다.
6. 대상 테스트·전체 회귀·구조 검사·수동 탐색·전체 차이 리뷰를 마치고 검증한 논리 단위로 커밋한다.
7. main 통합과 push는 구현 시점에 사용자에게 승인된 범위에서 수행한다. 이번 설계 요청만으로 원격을 변경하지 않는다.

원문 누락, 의도하지 않은 차이, 미확인 의존성, 링크 충돌이 발생하면 삭제를 중단한다. 성공으로 취급하지 않고 설계 또는 원인 조사로 돌아간다. 이전은 그룹별·작업별로 진행하며 이미 만든 출력과 원문의 대응을 확인해 재개한다.

복구는 이번 변경 경로를 특정한 뒤 수행한다. 작업 중에는 기준 커밋에서 대상 파일만 복원하고 커밋 후에는 해당 논리 커밋을 일반 revert로 되돌린다. 사용자 변경을 포함한 일괄 reset, force push, 재귀적 일괄 삭제는 사용하지 않는다. 원시 자료나 개인 설정을 Git에 추가하지 않는다.

## 12. 승인 대상.

승인 대상은 23개 분류 문서·14개 보관 기록으로 통합, 원래 파일 삭제, 내부 링크 갱신, 이전 main 개별 URL의 호환성 변경, 필요한 테스트 갱신, 관련 문서 정합성 수정, 실행 원본 유지, 예상 154개 파일이라는 하나의 설계다.

설계와 후속 실행 지시에 따라 구현 계획을 작성하고 실행한다. 글로벌 개인 내용과 인증 자료는 공개 저장소에 포함하지 않는다.
