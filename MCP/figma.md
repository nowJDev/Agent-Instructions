# figma

> Figma 공식 원격 MCP 서버. OAuth 인증을 거쳐 Figma 디자인/디자인 시스템과 코드 생성을 연동한다.

## 📌 용도
Figma의 공식 HTTP MCP 서버(`https://mcp.figma.com/mcp`)에 연결해 디자인 조회·수정·Code Connect 등의 도구를 사용한다. OAuth는 클라이언트의 인증 절차로 진행하며 인증 화면이나 래퍼에서 보이는 항목을 서버의 전체 도구 목록으로 해석하지 않는다. 설치한 `figma` 스킬은 작업 절차를 안내하지만 MCP 서버 연결의 필수 조건은 아니다.

## 🎯 트리거 조건 / 사용 맥락
- Figma에 디자인/다이어그램/슬라이드/FigJam을 생성하거나 불러올 때
- Figma 디자인을 코드로 변환(Code Connect)하거나 디자인 시스템/라이브러리를 다룰 때
- 위 작업 전, Figma 계정 연동이 필요할 때.

## 🛠️ 제공 도구 목록

| 대표 도구명 | 기능 | 주요 파라미터 |
|--------|------|----------------|
| get_design_context | 디자인을 코드로 구현하는 데 필요한 컨텍스트 조회 | 파일·노드 식별자는 런타임 스키마 확인 |
| get_metadata | 디자인 구조·노드 메타데이터 조회 | 파일·노드 식별자는 런타임 스키마 확인 |
| get_screenshot | 디자인·FigJam·Slides 화면 확인 | 파일·노드 식별자는 런타임 스키마 확인 |

전체 기능은 [공식 도구 목록](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)을 참고한다. 실제 사용 가능한 도구와 인자는 인증 후 클라이언트의 도구 목록 또는 MCP `tools/list`에서 확인한다. 지원 클라이언트·계정 권한에 따라 사용 범위가 다르며 스킬이 없어도 노출된 도구를 직접 사용할 수 있다.

관련 스킬: `figma-generate-design`, `figma-create-new-file`, `figma-generate-diagram`, `figma-generate-library`, `figma-code-connect`, `figma-use`, `figma-use-figjam`, `figma-use-slides`.

## 💻 사용 예시

**예시 1 — 최초 연동**
1. 지원 클라이언트에서 Figma MCP 연결을 확인한다.
2. 클라이언트의 OAuth 안내로 사용자가 Figma 로그인·권한 승인을 진행한다. Claude Code는 `/mcp`에서 Figma의 인증을 선택한다. [공식 연결 안내](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)를 따른다.
3. 연결 완료 후 실제 도구 목록과 스키마를 확인한다.

**예시 2 — 디자인 생성**
- 인증 완료 상태에서 현재 노출된 디자인 생성 도구를 사용한다. `figma:figma-generate-design` 스킬이 설치돼 있으면 해당 작업 절차를 따른다.

## 📦 출처 / 설치 상태
- 제공: **플러그인** `figma@claude-plugins-official` (버전 2.2.12)
- 활성화: ON (`settings.json` → `enabledPlugins["figma@claude-plugins-official"]: true`)
- 연결 방식: **http** — `https://mcp.figma.com/mcp` (원격 서버, OAuth 인증 필요)
- 설정/캐시 경로:
  - `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/.mcp.json`
  - `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/figma-power/mcp.json`
- 세션 내 도구 식별자 접두사: `mcp__plugin_figma_figma__`
