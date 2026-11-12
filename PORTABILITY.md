# PORTABILITY.md — 다른 AI 에이전트에서 사용하기

> 이 저장소의 **스킬·MCP를 Claude 이외의 AI 에이전트**(OpenAI Codex/Agents SDK, Gemini, Cursor, Copilot 등)에서 쓰는 방법.
> 핵심 원칙: **MCP는 대상 클라이언트의 연결·인증·도구 지원을 확인해 이식**, **타사 Skill은 출처 포인터 + 각자 설치**, **자체 제작 Skill은 `Owned-Skills/` 원본에서 설치**한다.

---

## 0. 30초 요약

| 대상 | 다른 AI에서 | 방법 |
|---|---|---|
| **MCP** | ⚠️ 지원 조건 확인 | 서버의 연결 방식·인증과 클라이언트 지원을 확인한 뒤 등록·검증(아래 §2) |
| **Skill** | ⚠️ 조건부 | 타사는 공개 **원본에서 각자 설치**(§3-A), 자체 제작은 `Owned-Skills/`, 미지원 AI는 참조 활용(§3-B)·MCP 래핑(§3-C) |

> 전제: 이 저장소의 `Skill/`·`MCP/`는 **설명 문서(카탈로그)**다. 실행 실물이 아니다. 단, 직접 작성한 Agent Skill은 `Owned-Skills/`에 공개 원본을 함께 둔다.

기본 CLI 준비와 전역 지침·바로가기 절차는 [시작 안내](GETTING_STARTED.md#41-windows-codex-환경-세팅)를 따른다. 아래 스킬·MCP 이식은 별도 확장 요청 범위다.

---

## 1. 무엇이 왜 이식되는가

- **MCP (Model Context Protocol)** — 오픈 표준이다. 클라이언트가 서버의 연결 방식·인증과 필요한 도구 계약을 지원해야 한다. 서버 등록, 인증 완료, 실제 도구 노출과 호출 성공은 각각 확인한다.
- **Agent Skills (SKILL.md)** — 역시 오픈 표준이나, **"skills-호환 에이전트"**여야 자동 작동한다. 타사 Skill은 원본에서 설치하고, 이 저장소가 직접 작성한 Skill은 `Owned-Skills/`에서 설치한다.

---

## 1.5 Claude 전용 용어 → 외부 AI 대체 (번역표)

저장소 지침(`AGENTS.md`·`rules/`·`Skill·MCP` 문서)에 등장하는 Claude Code 전용 용어와 외부 AI에서의 대체. ([README 환경별 안내](README.md#쓰는-ai가-다르면-어떻게-하나요)와 대응)

| Claude 전용 | 무엇인가 | 외부 AI 대체 |
|---|---|---|
| `rag_agent` (rag-search MCP) | 코드/프로젝트 RAG 검색 도구 | 자체 검색·임베딩, 또는 동등 RAG MCP |
| `Skill` 도구 / "Using [skill]" | SKILL.md를 트리거·로드 | §3 경로 A(설치)/B(참조)/C(MCP 래핑) |
| `Task` / `Explore` 서브에이전트 | 탐색·작업 위임 | 그 AI의 서브에이전트/위임 기능 |
| `PreToolUse 훅` 자동차단 | 위험 명령(rm -rf·시크릿) 사전 차단 | 호스트의 사전 승인·정책 기능 확인. 동등한 자동 차단이 없어도 규칙은 직접 준수 |
| `claude mcp add` | MCP 등록 CLI | 자기 `mcp.json`/SDK 설정 (§2.2) |
| `TeamCreate`/`TeamDelete` · `team-monitor` clone(`rules/02 §3`) | 멀티에이전트 팀 + 모니터 | 그 AI의 멀티에이전트 기능, team-monitor clone은 건너뜀 |
| `MEMORY.md` / `Compact` | 자동 메모리 / 컨텍스트 압축 | 동등 기능에 매핑, 없으면 제외 |
| `~/.claude/` 설치체계 · `dotfiles`/`sync.py` 프로토콜(`rules/03 §6`) | Claude Code 설정 디렉토리·동기화 | 해당 없음 — 설치/동기화 절차는 CC 전용, 제외 |

> 행동 규율(작업 3단계·DO/DON'T·검증 게이트·디버깅·GC)은 용어와 무관하게 **그대로 적용**된다([README 환경별 안내](README.md#쓰는-ai가-다르면-어떻게-하나요)). 막히는 건 위 도구·하네스 종속 항목뿐이며, 표대로 번역/제외한다.

---

## 2. MCP 이식

### 2.1 서버별 연결정보

| 서버 | 타입 | 등록값 | 타 AI 사용 |
|---|---|---|---|
| `context7` | stdio | `npx -y @upstash/context7-mcp` | ✅ |
| `chrome-devtools` | stdio | `npx -y chrome-devtools-mcp@1.10.1 --headless --no-usage-statistics --no-performance-crux` | ✅ (Chrome·Node.js 필요, [상세 안내](MCP/chrome-devtools.md)) |
| `CoplayDev/unity-mcp` | stdio | `coplaydev-unity-mcp` 이름의 Python MCP 서버 + 프로젝트별 Unity 브리지 | ✅ (Python·uv·Unity 필요, [설치 안내](MCP/coplay-funplay-unity-mcp.md#coplaydevunity-mcp)) |
| `FunplayAI/funplay-unity-mcp` | http | `funplayai-unity-mcp-project` 이름과 Unity 창에서 확인한 프로젝트별 전체 URL | ✅ (Unity 2022.3+·프로젝트별 패키지 필요, [설치 안내](MCP/coplay-funplay-unity-mcp.md#funplayaifunplay-unity-mcp)) |
| `playwright` | stdio | `npx @playwright/mcp@latest` | ✅ |
| `figma` | http | `https://mcp.figma.com/mcp` (OAuth) | ✅ (http MCP 지원 시) |
| `huggingface-skills` | http | `https://huggingface.co/mcp?login` (OAuth) | ✅ |
| `notion` | stdio | `npx @notionhq/notion-mcp-server` (+ 통합 토큰) | ✅ (자기 토큰 필요) |
| **claude.ai PlayMCP** | 계정 연동 | 기존 연결 자동 이전 없음 | 대상 클라이언트의 별도 제공·연결·인증과 실제 도구 확인 (§2.4) |

### 2.2 클라이언트별 등록법

MCP 프로토콜은 공통이지만 설정 파일의 최상위 키와 서버 필드는 클라이언트마다 다르다. 대상 클라이언트의 형식을 확인한다.

**Cursor `.cursor/mcp.json`**
```jsonc
{
  "mcpServers": {
    "context7":  { "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
    "playwright":{ "command": "npx", "args": ["@playwright/mcp@latest"] },
    "figma":     { "type": "http", "url": "https://mcp.figma.com/mcp" }
  }
}
```

**VS Code `.vscode/mcp.json`** — 최상위 키는 `servers`다.
```jsonc
{
  "servers": {
    "context7": { "type": "stdio", "command": "npx", "args": ["-y", "@upstash/context7-mcp"] },
    "figma": { "type": "http", "url": "https://mcp.figma.com/mcp" }
  }
}
```

VS Code가 지원하는 공유용 루트 `.mcp.json`은 `mcpServers` 형식이다. `.vscode/mcp.json`과 혼동하지 않는다. [공식 VS Code MCP 안내](https://code.visualstudio.com/docs/agent-customization/mcp-servers)를 따른다.

**OpenAI Agents SDK (Python)**
```python
from agents.mcp import MCPServerStdio, MCPServerStreamableHttp

context7 = MCPServerStdio(params={"command": "npx", "args": ["-y", "@upstash/context7-mcp"]})
figma    = MCPServerStreamableHttp(params={"url": "https://mcp.figma.com/mcp"})
# agent = Agent(..., mcp_servers=[context7, figma])
```

**Gemini CLI** — `~/.gemini/settings.json` 의 `mcpServers`에 서버 정보를 추가한다.

**Claude Code(참고)** — `claude mcp add <name> --scope user -- npx -y @upstash/context7-mcp`

### 2.3 인증·OAuth 주의
- `figma`·`huggingface-skills` = **원격 http + OAuth**. 등록 후 브라우저 로그인으로 인증. 다른 AI 클라이언트도 http MCP + OAuth를 지원해야 한다.
- `notion` = stdio지만 **통합 토큰** 필요. 받는 사람이 자기 Notion 토큰을 환경변수(`OPENAPI_MCP_HEADERS` 등)로 넣는다. **토큰을 저장소에 커밋하지 말 것.**

<a id="24-이식-불가--claudeai-playmcp"></a>
### 2.4 PlayMCP 연결과 클라이언트 지원.

`NaverSearch`·`KakaotalkChat`·`SaraminMcp`·`UsStockInfo`·`opendart`는 작성 당시 **claude.ai 계정에 연결된 도구의 기록**이다. 이 연결과 권한은 다른 클라이언트로 자동 이전되지 않는다.

대상 호스트가 PlayMCP나 같은 서비스를 별도 연결 도구로 제공하는지 먼저 확인하고, 현재 노출된 도구·지원 범위·계정 인증을 기준으로 사용한다. 제공되지 않거나 필요한 기능이 없으면 각 서비스의 **독립 MCP 서버나 공개 API**를 검토한다. 과거 연결 기록만으로 다른 AI의 지원 여부를 단정하지 않는다.

---

## 3. Skill 이식.

### 3.1 원칙
**타사 Skill 실물을 이 패키지에 복사·재배포하지 않는다.** 대신 공개 원본을 가리키고 받는 팀이 직접 설치한다. 이 저장소에서 직접 작성한 Skill은 `Owned-Skills/`에 원본을 보관하며 저장소 License에 따라 설치·재사용할 수 있다.

현재 자체 제작 원본은 26개다. 전체 이름과 Codex·Claude Code 사용자 전역 설치·업데이트 방법은 [Owned-Skills 안내](Owned-Skills/README.md)를 따른다. 기존 전역 패키지는 먼저 비공개 백업하고 개인 참조·알 수 없는 파일을 보존하며 요청한 파일만 병합한다.

주요 구성은 다음과 같다.

- [`design-driven-delivery`](Owned-Skills/design-driven-delivery/SKILL.md) — 상태 변경 작업의 설계·계획·구현·검증·리뷰·통합을 조율한다.
- [범용 보강 23개](Owned-Skills/README.md) — 코드 리뷰·실행·검증·조사·설정·인수인계·유한 반복·Claude 개발·FigJam 계획의 자체 작성 절차다. 같은 이름의 내장 명령·타사 플러그인과 구분하고 호스트 지원·필수 가이드·실제 도구를 확인한다.

### 3.2 경로 A — 출처에서 각자 설치 (주력)

카탈로그에 기록된 **일부 Claude Code 플러그인**의 배포 마켓플레이스다. ON 표시는 당시 환경의 기록이며, 제작자 원본과 현재 설치 경로는 각 분류의 안내에서 확인한다.
```
github.com/anthropics/claude-plugins-official   (= claude-plugins-official 마켓플레이스)
```

- **받는 AI가 Claude Code면**: 일반 번들은 `/plugin marketplace add anthropics/claude-plugins-official` 후 원하는 플러그인을 설치한다. Superpowers v7.0.2 기준의 제작자 채널 `superpowers@superpowers-marketplace`와 버전 확인은 [전용 안내](Skill/README.md#superpowers-버전과-설치-채널)를 따른다.
- **받는 AI가 Agent Skills를 지원하면**: 해당 원본에서 **스킬 루트 디렉터리 전체**를 그 AI의 skills 폴더에 배치한다. `SKILL.md`가 참조하는 `scripts/`·`references/`·`assets/`·예제와 상대경로 의존 리소스를 함께 보존한다. 별도 플러그인의 커맨드·훅 등 Claude 전용 구성은 제외하고, 스킬의 도구·환경 요구는 대상 클라이언트에 맞게 확인한다. [Agent Skills 패키지 구조](https://agentskills.io/specification#directory-structure)를 따른다.
- **스킬별 정확한 공개 원본·License**는 [`Skill/README.md`](Skill/README.md)의 **"📦 출처·설치 매핑"** 표 참조. 주의: 전부 마켓플레이스 번들이 아니다 — 일부는 **외부 repo가 원본**이다:
  - `superpowers` → `github.com/obra/superpowers` (MIT) · `huggingface-skills` → `github.com/huggingface/skills` (Apache-2.0) · `qodo-skills` → `github.com/qodo-ai/qodo-skills` (MIT) · `vercel`/`railway`/`neon`도 각사 repo
  - Figma는 `github.com/figma/mcp-server-guide`, Firecrawl의 갱신 원본은 `github.com/firecrawl/cli`, Chrome DevTools는 `github.com/ChromeDevTools/chrome-devtools-mcp`다. [11월 6일 출처 조사](references/skill-provenance-2026-11-06.md)와 [같은 날 갱신 기록](references/codex-skill-update-2026-11-06.md)은 각각 당시 근거로 보존하며, 사용할 원본·설치 조건은 분류별 최신 안내를 확인한다.
  - Anthropic 제작과 외부 번들은 `github.com/anthropics/claude-plugins-official`을 통해 배포될 수 있다. **plugin.json에 license 미기재 항목은 원본 라이선스와 제작사 조건을 별도로 확인한다.**

Codex에서 Superpowers를 패키지로 관리할 때는 확인한 원본의 15개 `skills/<name>`을 각각 `~/.agents/skills/<name>`에 배치하고 `scripts/`·`references/`·템플릿 등 상대경로 의존성을 보존한다. 플러그인 방식과 중복 설치하지 않으며, 기존 개인 파일·전역 지침·커스텀 스킬은 보존한다. 채널 버전과 파일 비교 후 새 세션에서 실제 발견·로드를 확인해야 설치 검증이 끝난다.

[Anthropic 공식 스킬](Skill/anthropic-skills/README.md)과 [Office·디자인 도구](Skill/office-design-tools/README.md)는 각 분류의 고정 원본·명시 호출 정책·기존 도구와의 역할 중첩을 확인한다. 패키지 복사와 Python·Node·CLI·브라우저 등 실행 종속성 준비를 구분하고, 새 세션에서 실제 발견된 이름과 호출 정책을 확인한다. Unity 연결은 [프로젝트별 설치·브리지 안내](MCP/coplay-funplay-unity-mcp.md)를 따른다.

### 3.3 경로 B — 참조 활용 (자동 트리거 없이)
받는 AI가 Agent Skills를 **미지원**하면, 카탈로그 문서(설명) 자체를 **컨텍스트에 넣어 지침으로** 쓴다. 자동 트리거·progressive disclosure는 없지만, "이 스킬이 무엇을 어떻게 하는지"를 AI가 읽고 가용 도구로 수행할 수 있다. 자체 작성 설명은 이 저장소 [License](LICENSE)에 따라 활용하며 타사 원문·리소스에는 해당 출처의 조건을 적용한다.

### 3.4 경로 C — MCP/도구로 래핑 (가장 이식성 높음)
스킬의 **기능**을 직접 MCP 서버나 함수 도구로 구현해 노출할 수도 있다. 대상 AI의 연결·인증·도구 지원을 확인하고 실제 호출로 검증한다. 자체 구현 여부만으로 타사 원문·코드·리소스의 라이선스 조건이 사라지지는 않으며, 복제·변환·재배포한 자료의 출처와 이용 조건을 별도로 확인한다.

### 3.5 라이선스 가드 (필수 확인)
- 이 저장소엔 **타사 Skill 실물을 넣지 않는다**(출처 링크만). 그래야 재배포 문제가 없다.
- 받는 팀은 원본(`anthropics/claude-plugins-official` 등)의 **LICENSE**를 확인하고 그 조건에 따라 설치·사용한다.
- 직접 작성한 Skill은 `Owned-Skills/`에만 두고 이 저장소의 License와 출처를 명시한다.

### 3.6 사전 점검 — 받는 AI가 Agent Skills를 지원하는가?
- **지원** → 경로 A(출처 설치)로 스킬 루트 패키지와 참조 리소스를 함께 배치한다.
- **지원 + 자체 제작 Skill** → `Owned-Skills/<name>` 패키지를 사용자 Skill 디렉터리에 복사.
- **미지원** → 경로 B(참조) 또는 경로 C(MCP 래핑).

---

## 4. 이식 체크리스트

- [ ] **MCP**: 필요한 서버를 대상 AI의 설정 형식에 맞춰 등록한다 (§2.2).
- [ ] **MCP 인증**: figma·hf는 OAuth 로그인, notion은 자기 토큰 주입(커밋 금지)
- [ ] **PlayMCP 지원 확인**: 기존 claude.ai 연결과 구분해 대상 호스트의 도구·연결·인증을 확인하고 필요하면 대체 MCP/API 검토 (§2.4).
- [ ] **Skill 출처 확인**: 쓰려는 스킬의 공개 원본(`anthropics/claude-plugins-official` 등) 확보
- [ ] **Skill 리소스 보존**: `SKILL.md`의 상대경로 참조·실행 스크립트·템플릿이 설치 위치에서도 존재하는지 확인한다.
- [ ] **자체 제작 Skill**: `Owned-Skills/`의 선택 패키지 전체를 배치하고, 포함된 경우 `agents/openai.yaml`과 리소스를 보존한다.
- [ ] **Agent Skills 지원 여부** 확인 → 경로 A / B / C 결정
- [ ] **LICENSE 확인**: 원본 라이선스 조건 준수, 실물 재배포 금지
- [ ] (선택) 자주 쓰는 스킬을 **경로 C(MCP 래핑)**로 만들어 크로스-AI 표준화

---

*이 문서는 이식 방법을 안내한다. 타사 Skill 실물은 담지 않고, 자체 제작 Skill만 `Owned-Skills/`에 보관한다. MCP 연결정보는 작성 당시 설정과 공개 안내의 예시이며 현재 호스트의 지원·연결·인증·도구 노출을 보장하지 않는다.*
