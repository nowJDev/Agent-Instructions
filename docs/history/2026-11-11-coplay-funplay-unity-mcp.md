<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-11-11-coplay-funplay-unity-mcp 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

당시 미푸시 표기는 후속 [Anthropic 실제 작업 검증과 배포](2026-11-12-anthropic-functional.md#review)에서 해소됐다. 아래 원문은 각 작업 당시의 범위를 유지한다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-11-11-coplay-funplay-unity-mcp-design.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/3c4dd83a3bf91b687532b4bf346af2374ad6a416/docs/superpowers/specs/2026-11-11-coplay-funplay-unity-mcp-design.md).

<!-- Unity MCP 두 종류의 설치 요청과 공개 문서의 범위를 기록한다. -->
<a id="spec--unity-mcp-설치와-카탈로그-설계"></a>
### Unity MCP 설치와 카탈로그 설계.

사용자는 CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp를 PC 전역과 이 저장소에 추가하도록 요청했다. PC에서는 현재 사용 중인 Codex의 사용자 전역 MCP 설정을 보존하며 추가한다. 이 공개 저장소는 Unity 프로젝트가 아니므로 MCP 카탈로그와 재현 가능한 설치 안내를 추가한다.

후속 답변에서 사용자는 프로젝트 설치를 나중으로 미루고 해당 절차를 스킬 지침에 기록하도록 확정했다. 이번 범위는 CoplayDev/unity-mcp 전역 서버·등록 준비, FunplayAI/funplay-unity-mcp 설치·주소 등록 안내, 자체 제작 `coplay-funplay-unity-mcp-setup` 스킬의 저장소 추가와 전역 설치다. Unity 프로젝트 파일·패키지와 FunplayAI/funplay-unity-mcp 주소는 변경하지 않는다.

Unity 공식 도구와 혼동하지 않도록 표시 이름은 제작자·저장소 전체 식별자를 사용한다. 스킬 이름은 `coplay-funplay-unity-mcp-setup`, MCP 등록 이름은 `coplaydev-unity-mcp`, FunplayAI/funplay-unity-mcp의 프로젝트별 등록 예제는 `funplayai-unity-mcp-project`로 구분한다. 실제 Unity 메뉴 이름은 원문을 유지한다.

<a id="spec--방식과-경계"></a>
#### 방식과 경계.

공식 패키지·클라이언트 기능을 사용한다. 두 저장소를 지침 저장소에 통째로 복사하는 방식은 실행 목적에 맞지 않고 타사 코드·개인 설정을 불필요하게 섞으므로 채택하지 않는다. 임의의 공통 HTTP 주소를 등록하는 방식은 FunplayAI/funplay-unity-mcp의 프로젝트 식별 경계를 잃으므로 채택하지 않는다.

`MCP/README.md`와 `PORTABILITY.md`에서 두 도구를 찾아갈 수 있게 하고 `MCP/coplay-funplay-unity-mcp.md` 한곳에서 설치·전역 등록·오류·제거를 설명한다. Unity 패키지는 사용할 프로젝트마다 설치한다. FunplayAI/funplay-unity-mcp는 Unity 창에서 확인한 프로젝트별 URL을 사용하며 대상 프로젝트가 확정되기 전에는 주소를 만들어 등록하지 않는다. 기존 MCP·개인 파일·다른 Unity 프로젝트는 보존한다.

<a id="spec--검증과-완료-기준"></a>
#### 검증과 완료 기준.

문서 변경은 기존 전체 unittest, 내부 링크와 `git diff --check`로 검사한다. 새 스킬은 기존 패키지 집합 검사에 추가해 누락 실패와 작성 후 성공을 확인한다. 별도 실행 스크립트는 만들지 않는다. 전역 등록과 서버 시작은 실제 설정·프로토콜 응답으로 별도 검증하고, Unity 프로젝트 연결·씬 조회·Play Mode는 이번 범위에서 연기한다. 원격 push는 별도 승인 범위다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-11-11-coplay-funplay-unity-mcp.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/3c4dd83a3bf91b687532b4bf346af2374ad6a416/docs/superpowers/plans/2026-11-11-coplay-funplay-unity-mcp.md).

<!-- Unity MCP 설치 문서의 변경 파일과 검증 순서를 기록한다. -->
<a id="plan--unity-mcp-설치-구현-계획"></a>
### Unity MCP 설치 구현 계획.

> **For agentic workers:** 이 계획은 현재 세션에서 실행하며 문서 검증 뒤 전체 변경을 리뷰한다.

**Goal:** CoplayDev/unity-mcp 전역 서버를 준비하고 두 MCP의 프로젝트별 설치·연결 절차를 공개 카탈로그와 전역 스킬에 반영한다.

**Architecture:** 기존 MCP 목차·이식 표에 항목을 추가하고 `MCP/coplay-funplay-unity-mcp.md`에서 상세 절차를 관리한다. 개인 설정과 실행 패키지는 공개 저장소 밖에 둔다.

**Tech Stack:** Markdown, Codex MCP, Unity UPM, 기존 Python unittest.

**Spec:** [설계](#spec).

<a id="plan--제약과-리뷰-초점"></a>
#### 제약과 리뷰 초점.

개인 경로·설정·토큰은 공개 문서에 넣지 않는다. 기존 서버 등록·사용자 파일을 보존한다. CoplayDev/unity-mcp의 서버/Unity 패키지 버전 정합성, FunplayAI/funplay-unity-mcp의 프로젝트별 주소·포트 충돌, 닫힌 Unity의 연결 실패, 여러 Editor의 대상 구분, 미검증 항목의 완료 과장을 검토한다.

<a id="plan--작업"></a>
#### 작업.

- [x] 기준선 `1900d96`의 깨끗한 상태와 격리 worktree를 확인했다.
- [x] 변경 전 전체 84개 unittest가 통과했다.
- [x] `MCP/README.md`, `PORTABILITY.md`, `MCP/coplay-funplay-unity-mcp.md`에 설치·등록·검증 안내를 작성했다.
- [x] 사용자 확정에 따라 프로젝트 설치를 연기하고 `Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md`와 목차를 추가했다.
- [x] `tests/test_owned_skill_packages.py`의 패키지 집합을 추가해 스킬 누락 RED와 작성 후 8개 검사 GREEN을 확인했다.
- [x] 변경 후 전체 84개 unittest와 `git diff --check`를 통과했다.
- [x] 전체 문서 diff를 자체 검토하고 검증 기록·현재 상태·체크리스트를 갱신했다.

전역 설정 등록·Unity 패키지 설치와 실제 연결 결과는 설치 담당의 증거를 기록한다. 문서 검증 결과로 Unity 동작 검증을 대신하지 않는다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-11-11-coplay-funplay-unity-mcp.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/3c4dd83a3bf91b687532b4bf346af2374ad6a416/docs/reviews/2026-11-11-coplay-funplay-unity-mcp.md).

<!-- Unity MCP 문서 검증 결과와 실제 설치 검증의 경계를 기록한다. -->
<a id="review--unity-mcp-설치-검증-기록"></a>
### Unity MCP 설치 검증 기록.

<a id="review--범위와-기준선"></a>
#### 범위와 기준선.

기준선은 `1900d96`이다. `MCP/README.md`, `MCP/coplay-funplay-unity-mcp.md`, `PORTABILITY.md`, `Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md`, 자체 제작·스킬 목차, 기존 패키지 집합 검사와 이번 설계·계획·현재 상태·체크리스트가 대상이다. 전역 개인 설정과 Unity 프로젝트 파일은 공개 커밋 대상이 아니다.

<a id="review--확인한-출처"></a>
#### 확인한 출처.

CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp 공식 README에서 프로젝트별 UPM 설치와 클라이언트 설정을 확인했다. FunplayAI/funplay-unity-mcp 공식 `package.json`은 `0.7.5`, Unity 최소 `2022.3`이며 공식 다중 프로젝트 안내에서 프로젝트별 URL·fallback 포트·루트 URL의 쓰기 제한을 확인했다. 상세 출처 링크는 [설치 안내](../../MCP/coplay-funplay-unity-mcp.md)에 있다.

<a id="review--검증-상태"></a>
#### 검증 상태.

변경 전 Windows Python 3.12 전체 84개 unittest가 통과했다. 새 스킬을 기존 패키지 집합 검사에 추가했을 때 누락에 의한 실패 1개·오류 1개를 확인했고, 스킬 작성 후 해당 검사 8개가 통과했다. 사용자 명명 요청을 반영한 최종 상태에서 Windows Python 3.12 전체 84개가 25.764초에 통과했고 내부 링크 검사가 포함됐다. `git diff --check`와 workflow completion 검사도 통과했다. 스킬 제작자의 `quick_validate.py`는 Python 3.11의 UTF-8 모드에서 `Skill is valid!`로 통과했다. Python 3.12에는 검사기의 `yaml` 모듈이 없었고 Python 3.11의 기본 CP949 읽기가 실패해, 설치된 의존성과 `-X utf8`을 사용했다.

전체 변경의 버전·transport·프로젝트 식별·공개 정보·스킬 트리거 경계를 자체 리뷰했고 독립 리뷰에서도 차단 결함을 발견하지 못했다. 선택 보강으로 제작자 `Configure`의 기본 키와 수동 등록 키가 중복될 수 있는 조건을 확인해, 명령·인자 또는 URL 비교로 같은 서버를 재사용하고 요청한 항목만 정리하는 절차를 스킬·설치 안내에 추가했다.

설치 담당은 `uv 0.13.7`과 `mcpforunityserver 10.3.0`의 설치, Codex 전역 `coplaydev-unity-mcp`의 버전 고정 stdio 등록을 확인했다. 기존 백업에서 새 항목만 제외한 파싱 설정이 같은지 assert로 대조했다. MCP `initialize`·`ping`·`tools/list`가 성공했고 48개 도구와 `manage_scene`을 확인했다. handshake의 `serverInfo.version = 3.4.11`은 FastMCP 프레임워크 버전이며 Python 패키지 버전과 구분한다.

등록 이름을 제작자 식별자로 변경한 뒤 SDK의 MCP `initialize`·`ping`·`tools/list` 48개와 기존 설정 동일성 assert를 다시 통과했다. 전역 스킬과 문서 6개의 원본 해시를 비교했고, 이전 스킬·문서는 백업 후 이번 작업에서 만든 항목만 제거해 중복을 남기지 않았다. 새 Codex app-server 프로세스의 `initialize`와 `skills/list(forceReload=true)`가 성공했으며 `coplay-funplay-unity-mcp-setup`의 enabled·user scope·실제 `.agents/skills` 경로와 두 저장소 식별자가 들어간 본문을 확인했다. 실제 모델 호출과 Codex 세션의 MCP 도구 발견은 이 검사에 포함하지 않았다.

프로토콜 검증에만 시작 시 Unity 연결을 건너뛰는 `UNITY_MCP_SKIP_STARTUP_CONNECT=1`과 telemetry 비활성 환경을 사용했다. 실제 Unity 연결·프로젝트 조작은 수행하지 않았다. 사용자가 프로젝트 설치를 명시적으로 연기했으므로 FunplayAI/funplay-unity-mcp의 프로젝트별 주소 등록·Unity 패키지 설치·Editor 조회와 Play Mode는 이번 범위에서 보류다. 새 Codex 세션의 도구 발견도 추후 확인 대상이다.

<a id="review--로컬-통합-결과"></a>
#### 로컬 통합 결과.

최종 보강을 포함한 전체 84개 회귀가 27.281초에 통과했다. 구현 커밋 `be04619`를 로컬 main에 fast-forward 병합했고 병합 후 전체 84개 회귀도 26.555초에 통과했다. 실패·스킵은 각각 0개다. 깨끗한 상태와 병합 관계를 확인한 뒤 이번에 만든 worktree·임시 브랜치를 정리했다. 원격 main은 변경하지 않았다. 개인 설정 백업과 검증 로그는 공개 저장소 밖에 보존한다.
