# vercel (MCP)

> Vercel 공식 원격 MCP 서버 — OAuth 인증으로 문서·프로젝트·배포 조회와 배포 등 변경 도구를 제공한다.

## 📌 용도
**사용자용 원격 MCP 서버**다. vercel 플러그인이 제공하는 공식 Vercel MCP 서버(`https://mcp.vercel.com`)에 연결해 Vercel 플랫폼을 조회·조작한다. [공식 배포 도구 목록](https://vercel.com/docs/agent-resources/vercel-mcp/tools/deployments)에는 `create_deployment` 등 쓰기 도구도 포함된다. 초기 릴리스의 읽기 전용 설명으로 현재 원격 서버의 권한을 판단하지 않는다.

플러그인의 commands(/deploy, /status, /env 등)가 "MCP-first, CLI-fallback" 규약을 따르므로, 현재 노출된 도구가 지원하는 작업은 MCP를 우선하고 필요한 CLI 작업으로 폴백한다.

## 🎯 사용 맥락
- **언제 쓰이는가**: 프로젝트·배포 조회, 공식 문서 검색, 로그 검사와 현재 도구가 지원하는 배포 등 변경 작업.
- **작업 경계**: 인증 후 도구 목록·인자·계정 권한을 확인한다. 배포·구매·외부 전송은 요청·승인된 범위에서만 수행하며 [외부 작업 경계](../../rules/02_tool-boundaries.md#7-외부로-나가는-작업의-경계)를 따른다. 지원되지 않는 작업만 CLI로 폴백한다.

## 🛠️ 제공 도구 목록
이 MCP는 **원격 HTTP 서버**(`type: http`)이며, `.mcp.json`에 정적 도구 목록이 정의되어 있지 않다. 실제 도구는 **OAuth 인증 후 런타임에 원격 서버가 노출**한다. 첫 연결 시 에이전트는 Vercel 인증(authorize) 프롬프트를 받는다.

| 항목 | 값 |
|------|-----|
| 서버 타입 | `http` (원격) |
| URL | `https://mcp.vercel.com` |
| 인증 | OAuth (첫 연결 시 Vercel 인증 프롬프트) |
| 권한 | 조회·변경 도구 포함. 실제 계정 권한과 런타임 도구별 계약 확인 |
| 노출 도구 | 런타임에 동적 노출 — `.mcp.json`에 목록 없음 |

대표 도구는 `list_projects`·`list_deployments`·`get_runtime_logs`·`create_deployment`이다. 카탈로그나 플러그인 명령에 적힌 이름만으로 호출하지 않고 현재 MCP `tools/list`에서 노출 여부와 스키마를 확인한다.

## 💻 사용 예시
```text
# 첫 연결: 에이전트가 Vercel OAuth authorize 프롬프트를 표시 → 사용자 승인

# 이후 자연어 요청으로 읽기 도구 사용 (런타임 노출 도구명에 의존):
"이 프로젝트의 최근 배포 목록을 보여줘"        → 배포 조회 도구
"프로덕션 런타임 에러 로그를 가져와"            → get_runtime_logs (level=error)
"Vercel의 cron jobs 설정 문서를 검색해"        → 문서 검색 도구
```

## 📦 출처 / 설치 상태
- 제공: vercel 플러그인
- 활성화: ⛔ **OFF** (enabledPlugins = false)
- 연결 방식: 원격 HTTP MCP (`type: http`, `https://mcp.vercel.com`), OAuth 인증, 조회·변경 도구 포함
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/vercel/0.43.0/.mcp.json`
