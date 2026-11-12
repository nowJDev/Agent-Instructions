# MCP 서버 인덱스

작성 시 확인한 클라이언트별 MCP(Model Context Protocol) 서버 목록이다. 기존 Claude Code 환경의 기록과 Codex의 Chrome DevTools·Unity MCP 안내를 함께 정리한다. ON/OFF·캐시 버전·도구 접두사는 해당 환경의 스냅샷이며 현재 클라이언트의 설치·연결·인증을 뜻하지 않는다. 실제 활성 상태·도구 수·입력 스키마는 현재 런타임 목록에서 확인한다.

## 출처별 분류

| MCP 서버 | 제공 경로 | 연결 방식 | 도구 수 | 문서 |
|---|---|---|---|---|
| **notion** | 글로벌 (`~/.claude.json` mcpServers) | stdio (`@notionhq/notion-mcp-server`) | 22 | [notion.md](notion.md) |
| **context7** | 플러그인 `context7` | stdio (npx) | 2 | [context7.md](context7.md) |
| **figma** | 플러그인 `figma` | http (원격 OAuth) | 런타임 목록 확인 | [figma.md](figma.md) |
| **huggingface-skills** | 플러그인 `huggingface-skills` | http (원격 OAuth) | 런타임 목록 확인 | [huggingface-skills.md](huggingface-skills.md) |
| **chrome-devtools** | Codex 글로벌 (`~/.codex/config.toml`) | stdio (`chrome-devtools-mcp`, 별도 Chrome 자동 실행) | 버전·옵션별 런타임 확인 | [chrome-devtools.md](chrome-devtools.md) |
| **CoplayDev/unity-mcp** | Codex 글로벌 `coplaydev-unity-mcp` + Unity 프로젝트별 패키지 | stdio (Python MCP 서버와 Unity 브리지) | 버전·옵션별 런타임 확인 | [coplay-funplay-unity-mcp.md](coplay-funplay-unity-mcp.md#coplaydevunity-mcp) |
| **FunplayAI/funplay-unity-mcp** | Codex 글로벌 `funplayai-unity-mcp-project` + Unity 프로젝트별 패키지 | http (Unity 내장 서버, 프로젝트별 주소) | 프로필별 런타임 확인 | [coplay-funplay-unity-mcp.md](coplay-funplay-unity-mcp.md#funplayaifunplay-unity-mcp) |
| **playwright** | 플러그인 `playwright` | stdio (npx) | 버전·capability별 런타임 확인 | [playwright.md](playwright.md) |
| **claude.ai PlayMCP** | claude.ai 계정 연동 (카카오 공식) | 원격 | 5개 하위 서버 | [claude-ai-PlayMCP/](claude-ai-PlayMCP/README.md) |

## 웹 작업 선택 기준.

- 웹 UI 테스트·브라우저 디버깅은 사용자 지정 도구를 우선하고, 지정이 없으면 사용 가능한 [Chrome DevTools MCP](chrome-devtools.md)를 우선한다.
- 웹 검색·자료 수집은 `firecrawl-*`를 사용한다. 기존 로그인·탭을 사용해야 하면 Chrome 플러그인을 선택한다.
- 연결 실패 시 설치·도구 노출·실행 오류를 확인하고 미검증 범위를 보고한다. 문서에 있다는 이유로 다른 클라이언트에도 설치됐다고 가정하지 않는다.

## claude.ai PlayMCP 하위 서버

| 하위 서버 | 주제 | 도구 수 | 문서 |
|---|---|---|---|
| NaverSearch | 네이버 검색 + 데이터랩 | 22 | [NaverSearch.md](claude-ai-PlayMCP/NaverSearch.md) |
| KakaotalkChat | 카카오톡 메모챗 | 1 | [KakaotalkChat.md](claude-ai-PlayMCP/KakaotalkChat.md) |
| SaraminMcp | 사람인 채용정보 | 8 | [SaraminMcp.md](claude-ai-PlayMCP/SaraminMcp.md) |
| UsStockInfo | 미국 주식 정보 | 9 | [UsStockInfo.md](claude-ai-PlayMCP/UsStockInfo.md) |
| opendart | 금융감독원 전자공시(DART) | 14 | [opendart.md](claude-ai-PlayMCP/opendart.md) |

## ⛔ 비활성(OFF) 플러그인 MCP (`_disabled/`)

작성 당시 Claude Code에서 플러그인이 OFF였던 항목이다. 활성화 뒤에도 필요한 실행 도구·인증·서버 연결과 실제 도구 노출을 확인한다. 다른 클라이언트의 상태는 이 기록으로 판단하지 않는다.

| MCP 서버 | 제공 플러그인 | 연결 방식 | 문서 |
|---|---|---|---|
| **vercel** | vercel (OFF) | http 원격 (`mcp.vercel.com`, OAuth, 조회·변경 도구 포함) | [_disabled/vercel.md](_disabled/vercel.md) |
| **railway** | railway (OFF) | stdio (`railway mcp`) + 원격 옵션 | [_disabled/railway.md](_disabled/railway.md) |
| **neon** | neon (OFF) | http 원격 (`mcp.neon.tech/mcp`) | [_disabled/neon.md](_disabled/neon.md) |
| **semgrep** | semgrep (OFF) | stdio (`semgrep mcp`) | [_disabled/semgrep.md](_disabled/semgrep.md) |

> 원격 MCP(vercel·neon)는 도구가 OAuth 후 런타임에 동적 노출되어 `.mcp.json`에 정적 도구 목록이 없습니다. 문서는 연결 정보 위주로 기술했습니다.

## ⚠️ 주의사항

- **인증 정보 관리**: Notion·Figma·Hugging Face 등 외부 서비스 토큰과 OAuth 인증 정보는 각 사용자 환경에서 주입한다. 실제 토큰·인증 헤더·개인 설정 파일은 저장소에 포함하지 않는다.
