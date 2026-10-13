# 전체 리뷰 발견 사항 수정 검증.

기준선은 `b9b443c`이며 사용자가 전체 리뷰의 11건에 대해 수정 실행을 승인했다. 저장소 원본만 수정했고 실제 전역 설정·서비스 데이터·원격 저장소는 변경하지 않았다.

## 발견 사항별 결과.

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

## 추가 리뷰와 실패 복구.

독립 리뷰에서 템플릿을 읽기 전에 목적 파일을 생성하면 읽기 실패 후 빈 파일이 남아 재실행을 잘못 통과시키는 문제가 재현됐다. 템플릿을 먼저 열고, 본인이 만든 문서의 복사 실패에는 불완전 파일을 정리한다. 읽기 실패·복사 중단 회귀 2건의 RED를 확인한 뒤 GREEN과 재실행을 확인했다.

주 검토자는 전체 diff·연결 문서·새 소스와 테스트를 검토했다. 독립 검토자는 스크립트·훅·백업·설정 루트·HTML 구조를 재검토했다. 리뷰에서 발견된 위 실패 복구를 포함해 관련 회귀를 실행했다.

## 검증 증거.

- `python -X utf8 -B -m unittest discover -s tests -v`에서 17개 통과, 실패·스킵 0개다.
- 초기 회귀에서는 matcher 생략·다른 안전 훅 누락·경쟁 파일 덮어쓰기·기존 경로 훼손·현재 문서 선택 실패를 확인했다. Windows 자식 Python의 출력 인코딩 오류는 UTF-8 실행 옵션으로 교정한 후 같은 검증을 실행했다.
- 전체 Markdown의 UTF-8·BOM·코드 블록, 로컬 링크·앵커, Python 문법·MCP 예제 JSON을 검사했다. 전역 배치용 문서는 실제 배치 기준 `Agent-Instructions/` 경로로 해석했다.
- `git diff --check`를 통과했고 변경 파일을 UTF-8 BOM 없음·LF로 유지했다.
- Chrome에서 체크박스 6개가 각각 이름과 상태를 제공했다. 키보드·label 클릭 확인 후 콘솔 warning·error는 0개였다.

## 공식 근거와 한계.

설정·API 안내는 [Claude hooks](https://code.claude.com/docs/en/hooks), [Claude MCP](https://code.claude.com/docs/en/mcp), [VS Code MCP](https://code.visualstudio.com/docs/agent-customization/mcp-servers), [Notion 블록 수정](https://developers.notion.com/reference/update-a-block), [Notion 검색](https://developers.notion.com/reference/post-search)을 기준으로 확인했다.

실제 hooks 실행·Notion 변경·VS Code 서버 연결은 검증하지 않았다. 테스트는 임시 프로젝트·백업 fixture에서 실행했다. ADR·RFC 등 임의 문서 구조의 초기화는 수동으로 유지하며, 완료 검사에서 현재 문서를 지정하지 않은 종류는 전체 기본 경로 검사로 동작한다. 저장소 원본이므로 이미 설치된 전역 복제본에는 별도 동기화가 필요하다.
