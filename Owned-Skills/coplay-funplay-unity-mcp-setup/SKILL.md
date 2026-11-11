---
name: coplay-funplay-unity-mcp-setup
description: "CoplayDev/unity-mcp 또는 FunplayAI/funplay-unity-mcp의 설치·초기 연결·재연결을 요청할 때 사용한다. 일반 Unity 코드 작업만으로 패키지를 새로 설치하지 않는다."
---

# CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp 설치·연결.

## 설치 범위.

- 클라이언트 전역 MCP 등록과 Unity 프로젝트별 UPM 패키지 설치를 구분한다. 두 MCP가 설치되어 있어도 각 Unity 프로젝트에 필요한 브리지가 자동 설치되지는 않는다.
- 대상 프로젝트에 `Assets`, `Packages`, `ProjectSettings`가 있는지 확인하고 적용 지침·`Packages/manifest.json`과 기존 MCP 설정을 읽는다. 기존 의존성·서버·사용자 변경을 보존한다.
- 사용자가 요청한 MCP만 준비한다. 일반 Unity 개발 요청을 두 MCP의 자동 설치 권한으로 해석하지 않는다. 연결 진단만 요청한 경우 누락 패키지는 보고한다.
- 프로젝트가 미정이거나 사용자가 프로젝트 설치를 나중으로 미루면 프로젝트 파일을 바꾸거나 가짜 URL을 등록하지 않는다. 승인된 전역 실행 도구·안내·스킬 준비는 계속하고 프로젝트 패키지·주소 등록·연결 검증을 대기로 명시한다.

## CoplayDev/unity-mcp.

공식 [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp)의 안정 버전과 실행 방식을 확인한다. 확인 기준 버전은 `10.3.0`이며 서버와 Unity 패키지는 같은 버전을 사용한다. 업데이트 요청이 없으면 설치 중 임의로 다른 버전으로 올리지 않는다.

- Python 3.10 이상과 `uv`를 확인한다. 사용자 전역 서버는 `uv tool install mcpforunityserver==10.3.0`으로 준비할 수 있다. 다른 버전이 있으면 사용처를 먼저 확인하고 덮어쓰지 않는다.
- 프로젝트 설치가 승인되면 기존 의존성을 보존하며 `com.coplaydev.unity-mcp`에 `https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#v10.3.0`을 사용한다. 이미 다른 버전이 있으면 서버와 호환성을 확인한 뒤 요청 범위에서 맞춘다.
- stdio로 등록할 때는 서버의 `--transport stdio`를 명시한다. HTTP로 연결할 때는 Unity 창에서 실제 시작한 서버 주소를 사용한다. 선택한 transport와 클라이언트 설정을 맞춘다.

## FunplayAI/funplay-unity-mcp.

공식 [FunplayAI/funplay-unity-mcp](https://github.com/FunplayAI/funplay-unity-mcp)의 확인 기준 버전은 `0.7.5`, Unity 최소 버전은 `2022.3`이다. 서버는 Unity Editor 안에서 실행되며 별도 Python 서버를 만들지 않는다.

- 프로젝트 설치가 승인되면 `com.gamebooom.unity.mcp`가 있는지 확인하고 누락된 경우 `https://github.com/FunplayAI/funplay-unity-mcp.git`으로 추가한다. 변경된 manifest 전체를 재생성하지 않는다.
- `Funplay → MCP Server`에서 실제 프로젝트의 서버를 시작하고 `Configure`를 우선한다. 내장 프로젝트 스킬 추가는 요청 범위에서만 선택한다.
- 수동 등록은 해당 Unity 창에 표시된 프로젝트별 전체 URL을 그대로 사용한다. 임의 고정 포트나 다른 프로젝트 주소·이전 루트 주소로 대체하지 않는다.
- 포트 충돌로 fallback 상태면 `Use Per-Project Port` 또는 `Pin Current Port`로 해결한 뒤 재설정한다. 프로젝트 이동·이름 변경 시 주소를 다시 확인한다. [공식 다중 프로젝트 안내](https://github.com/FunplayAI/funplay-unity-mcp/blob/main/Documentation~/multi-project-setup.md)를 따른다.

## 확인과 보고.

`Configure`는 CoplayDev/unity-mcp에서 `unityMCP`, FunplayAI/funplay-unity-mcp에서 `funplay-<folder>`라는 기본 키를 만들 수 있으므로 실행 전후 기존 명령·인자 또는 프로젝트별 URL을 비교해 같은 서버는 재사용하고, 자동 항목이 중복 생성됐다면 요청한 서버만 식별해 제작자 이름을 담은 키 하나로 정리하며 다른 Unity 서버는 보존한다.

1. 클라이언트의 MCP 목록·상세 설정을 확인해 중복과 기존 서버 보존을 검사한다. Codex는 `codex mcp list`, `codex mcp get <name> --json`을 사용한다. PowerShell의 래퍼 실행 정책 문제는 설치된 `.cmd` 진입점으로 해결하고 시스템 정책을 바꾸지 않는다.
2. 새 세션의 연결과 `tools/list`를 확인한다. Unity 프로젝트·활성 씬을 읽는 도구로 의도한 Editor임을 확인한 뒤 쓰기를 수행한다. 같은 대상을 두 MCP로 동시에 수정하지 않는다.
3. 전역 실행 도구 설치, 전역 등록, Unity 패키지 설치, 실제 Editor 연결·조회 결과를 구분해서 보고한다. 닫힌 Unity·미설치 프로젝트 브리지·미확정 FunplayAI/funplay-unity-mcp 주소를 전역 서버 설치 실패나 전체 완료로 표현하지 않는다.
4. 검증용으로 만든 프로세스만 종료하고 기존 Editor·다른 프로젝트 서버·개인 설정은 유지한다. 개인 설정·토큰·프로젝트별 주소를 공개 저장소에 커밋하지 않는다.
