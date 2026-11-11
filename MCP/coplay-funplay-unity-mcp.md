<!-- CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp Unity MCP의 프로젝트별 설치와 클라이언트 전역 등록 경계를 안내한다. -->
# CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp.

[CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp)와 [FunplayAI/funplay-unity-mcp](https://github.com/FunplayAI/funplay-unity-mcp)는 AI 클라이언트에서 Unity Editor를 제어하는 별도 도구다. 둘 다 MIT 라이선스이며 씬·에셋·스크립트 등 프로젝트를 변경할 수 있다.

클라이언트 전역 등록과 Unity 패키지 설치는 별개다. Codex의 사용자 전역 MCP 설정은 `~/.codex/config.toml`에 저장하지만 Unity 쪽 패키지는 사용할 각 Unity 프로젝트에 설치해야 한다. 이 지침 저장소에는 설치 안내만 보관하며 Unity 패키지나 개인 MCP 설정을 복사하지 않는다. 기존 `unity` 등 다른 서버 등록도 별도 도구로 취급하고 보존한다.

프로젝트 설치·연결을 실제로 요청할 때는 자체 제작 [coplay-funplay-unity-mcp-setup 스킬](../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md)을 사용한다. 프로젝트 설치를 나중으로 미룬 경우 전역 실행 도구와 안내만 준비하고 패키지·프로젝트별 주소·Editor 연결은 대기로 남긴다.

## CoplayDev/unity-mcp.

Unity 2021.3 LTS 이상, Python 3.10 이상과 `uv`가 필요하다. 공식 [Quickstart](https://github.com/CoplayDev/unity-mcp#quickstart)에 따라 Unity의 `Window → Package Manager → Add package from git URL`에서 다음 주소를 추가한다.

```text
https://github.com/CoplayDev/unity-mcp.git?path=/MCPForUnity#v10.3.0
```

확인 기준 안정 버전은 `10.3.0`이며 Python 서버와 Unity 패키지 버전을 맞춘다. `beta` 개발 브랜치를 안정 버전으로 오인하지 않는다.

전역 Python 서버를 설치하고 Codex에서 stdio로 실행하려면 다음과 같이 준비한다. `uvx`가 PATH에서 검색되는지 확인하고 설치 버전을 지정해 실행한다.

```powershell
uv tool install mcpforunityserver==10.3.0
codex mcp list
codex mcp add coplaydev-unity-mcp -- uvx --from mcpforunityserver==10.3.0 mcp-for-unity --transport stdio
codex mcp get coplaydev-unity-mcp --json
```

`Window → MCP for Unity`에서 연결 방식과 클라이언트를 설정한다. stdio는 Codex가 Python MCP 서버를 실행하고 서버가 Unity 브리지에 연결하는 방식이다. HTTP는 Unity 창에서 시작한 별도 로컬 Python 서버의 실제 주소로 연결한다. 선택한 방식의 공식 실행 인자와 현재 버전을 확인한 뒤 등록하고, stdio 설정에 HTTP URL을 혼용하지 않는다.

Windows에서 `uvx`가 클라이언트 환경의 PATH에 없으면 실제 설치 경로를 해당 PC의 전역 설정에 사용한다. 해당 서버의 `env.SystemRoot`에 현재 Windows의 `SystemRoot`를 전달하고 `startup_timeout_sec = 60`을 설정할 수 있다. 이 개인 경로·설정은 공개 저장소에 복사하지 않는다.

## FunplayAI/funplay-unity-mcp.

2026-11-11 공식 [package.json](https://github.com/FunplayAI/funplay-unity-mcp/blob/main/package.json)에서 버전 `0.7.5`, 패키지 이름 `com.gamebooom.unity.mcp`, Unity 최소 버전 `2022.3`을 확인했다. MCP 서버는 Unity Editor 안에서 실행되므로 별도의 Python 서버 설치는 필요하지 않다.

1. Unity Package Manager의 `Add package from git URL`로 `https://github.com/FunplayAI/funplay-unity-mcp.git`을 추가한다.
2. `Funplay → MCP Server`를 열고 서버를 활성화한다.
3. Unity 창에 표시된 프로젝트별 전체 주소를 확인하고 클라이언트 설정의 `Configure`를 우선 사용한다. 내장 프로젝트 스킬까지 필요할 때만 `Configure + Skills`를 선택한다.
4. Codex를 새로 시작해 등록·연결을 확인한다.

주소 형식은 `http://127.0.0.1:<port>/mcp/project/<project-id>/`다. 포트와 프로젝트 ID를 임의로 정하지 않고 해당 Unity 창에서 복사한다. 기본 포트는 프로젝트 경로에서 결정되며 프로젝트를 옮기거나 이름을 바꾸면 재설정한다. 포트 충돌로 fallback 상태면 `Use Per-Project Port` 또는 `Pin Current Port`로 해결한 뒤 다시 설정한다. [공식 다중 프로젝트 안내](https://github.com/FunplayAI/funplay-unity-mcp/blob/main/Documentation~/multi-project-setup.md)를 따른다.

수동으로 Codex 전역에 등록할 때는 다음과 같이 실제 주소를 입력한다. 아래 변수 값의 `<port>`와 `<project-id>`는 설명용이므로 그대로 실행하지 않는다.

```powershell
$funplayUrl = 'http://127.0.0.1:<port>/mcp/project/<project-id>/'
codex mcp list
codex mcp add funplayai-unity-mcp-project --url $funplayUrl
codex mcp get funplayai-unity-mcp-project --json
```

프로젝트마다 서버 이름과 주소를 구분한다. 기존 `/mcp` 루트 주소를 새 프로젝트 주소 대신 등록하지 않는다. 이전 루트 주소로 쓰기를 수행하려면 별도로 검증한 `expected_context`가 필요하다. 프로젝트별 URL은 잘못된 Editor 연결을 막는 장치이며 인증 수단은 아니다.

## 검증과 운영.

- `Configure`는 CoplayDev/unity-mcp에서 `unityMCP`, FunplayAI/funplay-unity-mcp에서 `funplay-<folder>` 기본 키를 만들 수 있으므로 실행 전후 기존 명령·인자 또는 프로젝트별 URL을 비교해 같은 서버는 재사용하고, 자동 항목이 중복 생성됐다면 요청한 서버만 식별해 제작자 이름을 담은 키 하나로 정리하며 다른 Unity 서버는 보존한다.
- 등록 후 `codex mcp list`와 `codex mcp get <name> --json`으로 기존 서버 보존과 추가 항목을 확인한다. PowerShell 실행 정책이 `.ps1` 래퍼만 차단하면 설치된 `codex.cmd`를 사용하며 시스템 실행 정책을 바꾸지 않는다.
- 새 Codex 세션에서 MCP 연결과 `tools/list`를 확인하고 프로젝트·활성 씬을 읽는 도구로 의도한 Editor인지 확인한다. Unity가 닫혀 있으면 연결 실패와 패키지 설치 실패를 구분한다.
- 두 서버를 동시에 등록할 수 있지만 쓰기 작업 전 대상 프로젝트를 확인하고, 같은 씬·에셋을 두 서버에서 동시에 수정하지 않는다.
- 실제 씬 변경·Play Mode·화면 캡처 검증은 대상 Unity 프로젝트에서 수행한다. 전역 설정 등록이나 이 문서의 추가만으로 이를 통과 처리하지 않는다.
- 비활성화·제거는 해당 Codex MCP 항목과 대상 프로젝트의 UPM 패키지를 각각 처리한다. 다른 프로젝트의 서버·패키지·개인 설정은 보존한다.

Codex 등록 형식은 [OpenAI 공식 MCP 안내](https://learn.chatgpt.com/docs/extend/mcp?surface=cli), 각 Unity 패키지의 설정·변경 이력은 위 제작자 문서를 따른다.
