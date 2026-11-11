<!-- Unity MCP 두 종류의 설치 요청과 공개 문서의 범위를 기록한다. -->
# Unity MCP 설치와 카탈로그 설계.

사용자는 CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp를 PC 전역과 이 저장소에 추가하도록 요청했다. PC에서는 현재 사용 중인 Codex의 사용자 전역 MCP 설정을 보존하며 추가한다. 이 공개 저장소는 Unity 프로젝트가 아니므로 MCP 카탈로그와 재현 가능한 설치 안내를 추가한다.

후속 답변에서 사용자는 프로젝트 설치를 나중으로 미루고 해당 절차를 스킬 지침에 기록하도록 확정했다. 이번 범위는 CoplayDev/unity-mcp 전역 서버·등록 준비, FunplayAI/funplay-unity-mcp 설치·주소 등록 안내, 자체 제작 `coplay-funplay-unity-mcp-setup` 스킬의 저장소 추가와 전역 설치다. Unity 프로젝트 파일·패키지와 FunplayAI/funplay-unity-mcp 주소는 변경하지 않는다.

Unity 공식 도구와 혼동하지 않도록 표시 이름은 제작자·저장소 전체 식별자를 사용한다. 스킬 이름은 `coplay-funplay-unity-mcp-setup`, MCP 등록 이름은 `coplaydev-unity-mcp`, FunplayAI/funplay-unity-mcp의 프로젝트별 등록 예제는 `funplayai-unity-mcp-project`로 구분한다. 실제 Unity 메뉴 이름은 원문을 유지한다.

## 방식과 경계.

공식 패키지·클라이언트 기능을 사용한다. 두 저장소를 지침 저장소에 통째로 복사하는 방식은 실행 목적에 맞지 않고 타사 코드·개인 설정을 불필요하게 섞으므로 채택하지 않는다. 임의의 공통 HTTP 주소를 등록하는 방식은 FunplayAI/funplay-unity-mcp의 프로젝트 식별 경계를 잃으므로 채택하지 않는다.

`MCP/README.md`와 `PORTABILITY.md`에서 두 도구를 찾아갈 수 있게 하고 `MCP/coplay-funplay-unity-mcp.md` 한곳에서 설치·전역 등록·오류·제거를 설명한다. Unity 패키지는 사용할 프로젝트마다 설치한다. FunplayAI/funplay-unity-mcp는 Unity 창에서 확인한 프로젝트별 URL을 사용하며 대상 프로젝트가 확정되기 전에는 주소를 만들어 등록하지 않는다. 기존 MCP·개인 파일·다른 Unity 프로젝트는 보존한다.

## 검증과 완료 기준.

문서 변경은 기존 전체 unittest, 내부 링크와 `git diff --check`로 검사한다. 새 스킬은 기존 패키지 집합 검사에 추가해 누락 실패와 작성 후 성공을 확인한다. 별도 실행 스크립트는 만들지 않는다. 전역 등록과 서버 시작은 실제 설정·프로토콜 응답으로 별도 검증하고, Unity 프로젝트 연결·씬 조회·Play Mode는 이번 범위에서 연기한다. 원격 push는 별도 승인 범위다.
