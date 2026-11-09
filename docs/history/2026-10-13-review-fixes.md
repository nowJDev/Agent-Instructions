<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-13-review-fixes 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-13-review-fixes.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-13-review-fixes.md).

<a id="plan--전체-리뷰-발견-사항-수정-계획"></a>
### 전체 리뷰 발견 사항 수정 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 사용자 요청으로 아래 11건의 수정 실행을 승인받았다.

<a id="plan--목표와-설계"></a>
#### 목표와 설계.

기준선은 `b9b443c`다. 전체 리뷰의 11건을 해결한다. Python 표준 라이브러리와 HTML 기본 체크박스를 사용하며 의존성을 추가하지 않는다. 실제 전역 설정·Notion 데이터·원격 저장소는 변경하지 않는다.

Notion 수정은 대상 블록 업데이트를 기본으로 한다. 훅은 matcher가 아닌 전체 설정 내용으로 중복을 제거한다. 백업은 정확한 새 디렉터리 하나에 선택된 원본만 복사한다. MCP·hooks 안내는 공식 클라이언트 스키마에 맞춘다.

작업 문서 경로는 초기화와 검사에서 같은 선택 함수를 사용한다. 기존 `docs/specs`·`docs/plans`가 있으면 유지하고, 없으면 기본 구조를 사용한다. 다른 승인 구조는 수동으로 유지한다. 완료 검증은 `--spec`, `--plan`, `--review`로 현재 문서를 지정할 수 있으며 경로는 프로젝트 내부의 Markdown 파일이어야 한다. 미지정 종류는 기존 전체 검사 동작을 유지한다. 파일 생성에는 배타적 생성 모드를 사용해 다른 작업자가 만든 파일을 보존한다.

<a id="plan--task-1-스크립트와-예제-회귀"></a>
#### Task 1. 스크립트와 예제 회귀.

Files: `tests/test_review_regressions.py`, `Owned-Skills/design-driven-delivery/scripts/{bootstrap_workflow,validate_workflow,workflow_paths}.py`, `references/claude-code-cli-setup.md`.

- [x] 재현 테스트를 작성하고 `python -X utf8 -B -m unittest discover -s tests -v`에서 기존 구조 훼손·경쟁 생성·과거 문서 검사·훅 병합 실패를 확인한다.
- [x] 공유 경로 선택, `open("xb")`, 작업별 문서 선택, 내용 기준 훅 병합을 구현하고 같은 명령의 통과를 확인한다.
- [x] Bash 백업 예제를 임시 디렉터리에서 반복 실행해 과거 백업 유입과 오류 은폐가 없는지 확인한다.
- [x] 최종 리뷰에서 발견한 템플릿 읽기·복사 중단의 불완전 파일 잔존을 실패 테스트로 재현하고 정리·재시작 동작을 검증한다.

<a id="plan--task-2-api설정-안내-및-키보드-접근성"></a>
#### Task 2. API·설정 안내 및 키보드 접근성.

Files: `rules/02_tool-boundaries.md`, `MCP/notion.md`, `Skill/plugin-dev/hook-development.md`, `PORTABILITY.md`, `GETTING_STARTED.md`, `index.html`, `Owned-Skills/design-driven-delivery/{SKILL.md,references/document-contracts.md}`, `Skill/_personal/design-driven-delivery.md`.

- [x] Notion 전체 삭제 기본값·데이터 소스 검색, 사용자 hooks 루트, Claude MCP 범위·프로젝트 설정 지원, VS Code `servers` 스키마를 공식 문서 근거와 함께 수정한다.
- [x] HTML 체크리스트에 기본 checkbox와 label을 쓰고 별도 클릭 토글 코드를 제거한다. Chrome에서 Tab·Space와 label 클릭을 확인한다.
- [x] 전체 문서 링크·UTF-8·코드 블록·차이 검사와 전체 회귀를 실행한다.

<a id="plan--task-3-리뷰와-전달"></a>
#### Task 3. 리뷰와 전달.

- [x] 기준선 대비 전체 변경을 리뷰하고 검증 결과를 `docs/reviews/2026-10-13-review-fixes.md`에 기록한다.
- [x] 계획의 검증 상태와 한글 커밋 메시지·로컬 main 통합 절차를 준비한다. 검증된 변경은 커밋 후 로컬 main으로 fast-forward 통합하고 원격에는 push하지 않는다.

<a id="plan--자동-검증-명령"></a>
#### 자동 검증 명령.

```powershell
python -X utf8 -B -m unittest discover -s tests -v
git diff --check
```

실패 경로는 누락·외부 경로·미완료 문서·기존 경로 충돌·경쟁 생성이며, 백업 실패 시 설치를 진행하지 않는다. 브라우저 검증이나 테스트가 실패하면 완료 표시와 커밋 전에 원인을 수정한다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-13-review-fixes.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-13-review-fixes.md).

<a id="review--전체-리뷰-발견-사항-수정-검증"></a>
### 전체 리뷰 발견 사항 수정 검증.

기준선은 `b9b443c`이며 사용자가 전체 리뷰의 11건에 대해 수정 실행을 승인했다. 저장소 원본만 수정했고 실제 전역 설정·서비스 데이터·원격 저장소는 변경하지 않았다.

<a id="review--발견-사항별-결과"></a>
#### 발견 사항별 결과.

| 번호 | 발견 사항 | 수정과 확인 |
|---|---|---|
| 1 | Notion 전체 삭제가 기본값이었다. | 대상 업데이트를 우선하고 관련 없는 내용·ID를 보존하도록 rules·MCP·HTML을 맞췄다. 전체 재생성에는 승인·백업·복구가 필요하다. |
| 2 | 같은 matcher의 안전 훅 누락·matcher 생략 오류가 있었다. | 전체 설정이 동일할 때만 제외한다. 다른 명령 보존과 반복 병합을 회귀로 확인했다. |
| 3 | 사용자 hooks 설정 루트가 틀렸다. | 사용자 settings의 최상위 `hooks` 아래에 이벤트를 두도록 수정했다. |
| 4 | 초기화가 기존 문서 구조를 가렸다. | 초기화·검증의 경로 선택을 공유하고 기존 `docs/specs`·`docs/plans` 유지와 전후 완료 검사를 확인했다. |
| 5 | 존재 확인과 복사 사이에 생성된 파일을 덮어썼다. | 배타적 `xb` 생성과 경쟁 생성 회귀로 기존 내용을 보존했다. |
| 6 | 취소·과거 문서가 현재 완료 검사를 막았다. | `--spec`·`--plan`·`--review`로 현재 작업 문서를 지정한다. 반복 지정, 미완료·누락·외부 경로·다른 확장자 실패를 확인했다. 미지정 종류는 기존 전체 검사를 유지한다. |
| 7 | wildcard 백업이 이전 백업까지 복사했다. | 고유 백업 경로 하나와 명시된 원본만 사용한다. 3회 실행에서 매번 원본 3파일만 복사했고 중첩 백업은 없었다. 복사 실패 시 설치 전에 중단했다. |
| 8 | VS Code MCP 루트가 틀렸다. | `.vscode/mcp.json`의 `servers`와 공유용 `.mcp.json`의 `mcpServers`를 구분했다. |
| 9 | Claude `.mcp.json`을 미지원으로 안내했다. | CLI 우선·프로젝트 및 플러그인 설정 지원·user/project/local 범위를 명시했다. |
| 10 | Notion 검색에서 API 버전을 혼용했다. | 데이터 소스 검색 필터와 결과 ID를 사용하고 이전 database 필터·ID와 섞지 않도록 했다. |
| 11 | HTML 체크리스트에 키보드 접근성이 없었다. | 기본 checkbox·label 6개로 변경하고 별도 클릭 상태 코드를 제거했다. Chrome에서 이름·상태, Tab 이동·Space 토글·label 클릭과 화면을 확인했다. |

<a id="review--추가-리뷰와-실패-복구"></a>
#### 추가 리뷰와 실패 복구.

독립 리뷰에서 템플릿을 읽기 전에 목적 파일을 생성하면 읽기 실패 후 빈 파일이 남아 재실행을 잘못 통과시키는 문제가 재현됐다. 템플릿을 먼저 열고, 본인이 만든 문서의 복사 실패에는 불완전 파일을 정리한다. 읽기 실패·복사 중단 회귀 2건의 RED를 확인한 뒤 GREEN과 재실행을 확인했다.

주 검토자는 전체 diff·연결 문서·새 소스와 테스트를 검토했다. 독립 검토자는 스크립트·훅·백업·설정 루트·HTML 구조를 재검토했다. 리뷰에서 발견된 위 실패 복구를 포함해 관련 회귀를 실행했다.

<a id="review--검증-증거"></a>
#### 검증 증거.

- `python -X utf8 -B -m unittest discover -s tests -v`에서 17개 통과, 실패·스킵 0개다.
- 초기 회귀에서는 matcher 생략·다른 안전 훅 누락·경쟁 파일 덮어쓰기·기존 경로 훼손·현재 문서 선택 실패를 확인했다. Windows 자식 Python의 출력 인코딩 오류는 UTF-8 실행 옵션으로 교정한 후 같은 검증을 실행했다.
- 전체 Markdown의 UTF-8·BOM·코드 블록, 로컬 링크·앵커, Python 문법·MCP 예제 JSON을 검사했다. 전역 배치용 문서는 실제 배치 기준 `Agent-Instructions/` 경로로 해석했다.
- `git diff --check`를 통과했고 변경 파일을 UTF-8 BOM 없음·LF로 유지했다.
- Chrome에서 체크박스 6개가 각각 이름과 상태를 제공했다. 키보드·label 클릭 확인 후 콘솔 warning·error는 0개였다.

<a id="review--공식-근거와-한계"></a>
#### 공식 근거와 한계.

설정·API 안내는 [Claude hooks](https://code.claude.com/docs/en/hooks), [Claude MCP](https://code.claude.com/docs/en/mcp), [VS Code MCP](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [Notion 블록 수정](https://developers.notion.com/reference/update-a-block), [Notion 검색](https://developers.notion.com/reference/post-search)을 기준으로 확인했다.

실제 hooks 실행·Notion 변경·VS Code 서버 연결은 검증하지 않았다. 테스트는 임시 프로젝트·백업 fixture에서 실행했다. ADR·RFC 등 임의 문서 구조의 초기화는 수동으로 유지하며, 완료 검사에서 현재 문서를 지정하지 않은 종류는 전체 기본 경로 검사로 동작한다. 저장소 원본이므로 이미 설치된 전역 복제본에는 별도 동기화가 필요하다.
