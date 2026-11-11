<!-- Unity MCP 문서 검증 결과와 실제 설치 검증의 경계를 기록한다. -->
# Unity MCP 설치 검증 기록.

## 범위와 기준선.

기준선은 `1900d96`이다. `MCP/README.md`, `MCP/coplay-funplay-unity-mcp.md`, `PORTABILITY.md`, `Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md`, 자체 제작·스킬 목차, 기존 패키지 집합 검사와 이번 설계·계획·현재 상태·체크리스트가 대상이다. 전역 개인 설정과 Unity 프로젝트 파일은 공개 커밋 대상이 아니다.

## 확인한 출처.

CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp 공식 README에서 프로젝트별 UPM 설치와 클라이언트 설정을 확인했다. FunplayAI/funplay-unity-mcp 공식 `package.json`은 `0.7.5`, Unity 최소 `2022.3`이며 공식 다중 프로젝트 안내에서 프로젝트별 URL·fallback 포트·루트 URL의 쓰기 제한을 확인했다. 상세 출처 링크는 [설치 안내](../../MCP/coplay-funplay-unity-mcp.md)에 있다.

## 검증 상태.

변경 전 Windows Python 3.12 전체 84개 unittest가 통과했다. 새 스킬을 기존 패키지 집합 검사에 추가했을 때 누락에 의한 실패 1개·오류 1개를 확인했고, 스킬 작성 후 해당 검사 8개가 통과했다. 사용자 명명 요청을 반영한 최종 상태에서 Windows Python 3.12 전체 84개가 25.764초에 통과했고 내부 링크 검사가 포함됐다. `git diff --check`와 workflow completion 검사도 통과했다. 스킬 제작자의 `quick_validate.py`는 Python 3.11의 UTF-8 모드에서 `Skill is valid!`로 통과했다. Python 3.12에는 검사기의 `yaml` 모듈이 없었고 Python 3.11의 기본 CP949 읽기가 실패해, 설치된 의존성과 `-X utf8`을 사용했다.

전체 변경의 버전·transport·프로젝트 식별·공개 정보·스킬 트리거 경계를 자체 리뷰했고 독립 리뷰에서도 차단 결함을 발견하지 못했다. 선택 보강으로 제작자 `Configure`의 기본 키와 수동 등록 키가 중복될 수 있는 조건을 확인해, 명령·인자 또는 URL 비교로 같은 서버를 재사용하고 요청한 항목만 정리하는 절차를 스킬·설치 안내에 추가했다. 저장소 커밋·로컬 통합은 설치 담당이 최종 변경 파일을 검토한 뒤 수행하며 원격 push는 범위 밖이다.

설치 담당은 `uv 0.13.7`과 `mcpforunityserver 10.3.0`의 설치, Codex 전역 `coplaydev-unity-mcp`의 버전 고정 stdio 등록을 확인했다. 기존 백업에서 새 항목만 제외한 파싱 설정이 같은지 assert로 대조했다. MCP `initialize`·`ping`·`tools/list`가 성공했고 48개 도구와 `manage_scene`을 확인했다. handshake의 `serverInfo.version = 3.4.11`은 FastMCP 프레임워크 버전이며 Python 패키지 버전과 구분한다.

등록 이름을 제작자 식별자로 변경한 뒤 SDK의 MCP `initialize`·`ping`·`tools/list` 48개와 기존 설정 동일성 assert를 다시 통과했다. 전역 스킬과 문서 6개의 원본 해시를 비교했고, 이전 스킬·문서는 백업 후 이번 작업에서 만든 항목만 제거해 중복을 남기지 않았다. 새 Codex app-server 프로세스의 `initialize`와 `skills/list(forceReload=true)`가 성공했으며 `coplay-funplay-unity-mcp-setup`의 enabled·user scope·실제 `.agents/skills` 경로와 두 저장소 식별자가 들어간 본문을 확인했다. 실제 모델 호출과 Codex 세션의 MCP 도구 발견은 이 검사에 포함하지 않았다.

프로토콜 검증에만 시작 시 Unity 연결을 건너뛰는 `UNITY_MCP_SKIP_STARTUP_CONNECT=1`과 telemetry 비활성 환경을 사용했다. 실제 Unity 연결·프로젝트 조작은 수행하지 않았다. 사용자가 프로젝트 설치를 명시적으로 연기했으므로 FunplayAI/funplay-unity-mcp의 프로젝트별 주소 등록·Unity 패키지 설치·Editor 조회와 Play Mode는 이번 범위에서 보류다. 새 Codex 세션의 도구 발견도 추후 확인 대상이다.
