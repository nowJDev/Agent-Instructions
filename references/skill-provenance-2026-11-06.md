<!-- 설치 스킬의 공개 원본·변환 여부와 조사 경계를 기록한다. -->
# 스킬 공개 원본 조사 기록.

> 이 문서의 설치·카탈로그 수치와 버전은 2026-11-06 조사 당시 스냅샷이다. [같은 날 후속 갱신 기록](codex-skill-update-2026-11-06.md)과 구분하고, 현재 설명·출처·추가 설치 안내는 [스킬 목차](../Skill/README.md)와 [전체 카탈로그](../Skill/CATALOG.md)를 확인한다. 아래 과거 사실과 미확인 경계는 그대로 보존한다.

조사일은 2026-11-06이다. 이름·설명·참고 링크만으로 출처를 판정하지 않고 공개 저장소의 실제 파일과 설치된 `SKILL.md` 전체 본문을 대조했다. 공개 원본이 있다는 사실, 특정 버전과의 본문 일치, 실제 호출 성공은 서로 다른 결과다. 이 기록은 당시 한 환경의 조사 결과이며 다른 PC의 설치 완료나 향후 최신 상태를 뜻하지 않는다.

## 조사 범위와 집계.

처음 조사한 Codex 전역 스킬은 106개였다. 사용자 요청으로 개인 스킬 3개를 제거한 후 전역 설치본은 103개다. 별도 사용자 설치 1개·내장 5개·현재 세션에 노출된 플러그인 24개까지 공개 기록 대상은 133개 설치본이다. 같은 이름이 다른 경로에 있으면 설치본별로 구분한다.

| 범위 | 본문 일치 | 본문 차이·변환 | 공개 실행 원본 미확인 | 공식 배포·공개 원본 미확인 | 합계 |
|---|---:|---:|---:|---:|---:|
| Codex 전역. | 91 | 9 | 3 | 0 | 103 |
| 별도 설치·내장·플러그인. | 12 | 0 | 0 | 18 | 30 |
| 합계. | 103 | 9 | 3 | 18 | 133 |

현재 세션에 노출되지 않은 `openai-templates` 캐시 20개는 위 합계에 넣지 않았다. 캐시에 파일이 있다는 사실만으로 활성 설치라고 판단하지 않는다. 저장소의 [설명 카탈로그](../Skill/CATALOG.md)는 별도 기준의 99개 항목이므로 이 PC의 전역 설치 103개와 합산하거나 같다고 보지 않는다.

## 판정 기준.

- **본문 일치.** 표에 연결한 특정 공개 커밋의 전체 본문과 일치한다. UTF-8 BOM·CRLF/LF·문서 양끝 공백을 정규화했으며 최신 main과의 일치를 뜻하지 않는다.
- **본문 차이·변환.** 원본 계보는 확인했으나 버전 차이·패키지 링크 변경·개인 참조 추가·command 요약 변환 등이 있다. 본문 차이를 임의 로컬 수정으로 단정하지 않는다.
- **공개 실행 원본 미확인.** 로컬 원본이나 공개 설명 문서는 있어도 배포 가능한 실행 원본을 확인하지 못했다. 공개 저장소가 존재하지 않는다는 단정이 아니다.
- **공식 배포·공개 원본 미확인.** 배포 매니페스트의 OpenAI 제작자와 설치 실물은 확인했다. 저장소 문자열이나 제작자 표기만으로 공개 접근 가능한 실행 원본이라고 판정하지 않는다.

## 현재 설치 버전의 읽는 법.

버전 재확인일은 2026-11-06이다. 원본 링크의 Git 커밋만으로 설치 버전을 대신하지 않고 설치 기록, 설치 플러그인의 manifest, SKILL.md frontmatter의 version·metadata.version을 확인했다.

- **설치 버전.** Superpowers는 별도 설치 기록의 7.0.2이며, Codex 플러그인은 설치 manifest의 번들 버전이다. 개별 스킬이 독립 릴리스를 가진다는 뜻은 아니다.
- **원본 번들 버전.** Codex 전역 이식본은 자체 버전 필드와 연결된 Claude 원본 플러그인의 설치 버전을 나눠 적는다. 원본 번들 버전이 이식본의 확정 버전이나 무수정 상태를 보장하지 않는다.
- **자체 선언.** frontmatter의 version과 metadata.version은 파일에 적힌 값을 그대로 표시한다. 특히 transformers-js의 metadata 4.x를 독립 스킬 릴리스나 실제 설치 라이브러리 버전으로 단정하지 않는다.
- **미표기·미확인.** 개별 버전 선언이 없으면 미표기, 번들 기록이 unknown이거나 manifest에 버전이 없으면 버전 미확인이다. 공개 비교 커밋을 임의로 설치 버전명으로 바꾸지 않는다.
- **본문 식별자.** 각 설치 SKILL.md의 정규화 본문 SHA-256 앞 16자다. UTF-8 BOM·CRLF/LF·양끝 공백을 정규화하며 Git 커밋 SHA나 버전명이 아니다. 보조파일 전체의 식별자도 아니다.

## 제작자 저장소와 설치 계보.

| 계열 | 공개 원본 | 현재 설치 버전·확인 범위 | 구분 |
|---|---|---|---|
| Superpowers. | [obra/superpowers](https://github.com/obra/superpowers/tree/v7.0.2/skills) | `7.0.2` · 설치 기록·고정 커밋·80개 파일 해시 확인. | 15개 본문이 v7.0.2와 일치한다. 설치 기록이 추적한 보조파일 포함 80개 파일 해시도 모두 일치했다. |
| Hugging Face. | [huggingface/skills](https://github.com/huggingface/skills) | 원본 플러그인 `1.0.8`. hf-cli 생성기 `huggingface_hub 1.18.0`. 이식본 자체 버전과 구분한다. | 18개. hf-cli는 CLI 버전에서 생성된 본문이다. |
| Firecrawl. | [firecrawl/firecrawl-claude-plugin](https://github.com/firecrawl/firecrawl-claude-plugin) | 원본 플러그인 `1.0.9`. 이식·명령 변환본은 별도 버전 미표기. | 10개 스킬과 과거 skill-gen command의 변환본이다. 현재 브랜치의 경로가 바뀌거나 제거된 항목은 아래 고정 커밋을 따른다. |
| Chrome DevTools. | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp/tree/main/skills) | 원본 플러그인 `1.2.0`. 이식본 자체 버전은 미표기. | 설치된 6개 실제 스킬 원본을 확인했다. MCP 실행 래퍼만 있는 것으로 분류하지 않는다. |
| Figma. | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | 원본 플러그인 `2.2.50`. 이식본 자체 버전은 미표기. | 8개 외부 원본. figma-generate-project-plan 설치본은 아래 자체 제작 원본이다. |
| Qodo. | [qodo-ai/qodo-skills](https://github.com/qodo-ai/qodo-skills) | 원본 플러그인 `0.6.1`. 이식본 자체 버전은 미표기. | 설치된 2개 원본 계보를 확인했다. |
| Anthropic 플러그인. | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | claude-code-setup·claude-md-management `1.0.0`. plugin-dev·frontend-design·playground·skill-creator 번들은 버전 미확인. 스킬 자체 선언은 아래 개별 표에 기록한다. | 12개 SKILL.md와 2개 command 변환본이다. |
| Unity. | [Unity-Technologies/skills](https://github.com/Unity-Technologies/skills) | 스킬 버전 미표기. 일치 원본 커밋 `e91a6c4f9acf`를 별도로 확인했다. | unity-cli의 일치하는 과거 커밋을 확인했다. |
| 자체 제작. | [Owned-Skills](../Owned-Skills/README.md) | 패키지별 버전 미표기. 비교 원본 커밋 `ca45d94f0929`와 설치 본문 식별자로 구분한다. | 이 저장소의 직접 작성 원본 25개다. 외부 참고 자료를 이 설치본의 원본으로 오인하지 않는다. |
| Codex 내장. | [openai/codex](https://github.com/openai/codex/tree/main/codex-rs/skills/src/assets/samples) | 스킬별 버전 미표기. 비교 원본 커밋 `55897425e839`와 설치 본문 식별자로 구분한다. | 내장 5개 실제 원본과 일치한다. |
| OpenAI curated. | [openai/skills](https://github.com/openai/skills) | migrate-to-codex 버전 미표기. 비교 원본 커밋 `49f948faa925`를 별도로 확인했다. | migrate-to-codex 설치본과 일치한다. |
| Ponytail. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/v5.3.3/skills) | 설치 플러그인 `5.3.3` · manifest와 공개 v5.3.3 본문 확인. | 플러그인의 6개 본문이 v5.3.3과 일치한다. |

출처 확인은 타사 파일 재배포 허가를 뜻하지 않는다. 실제 설치·재배포 시 해당 고정 원본의 라이선스와 제작자 조건을 별도로 확인한다. 이 저장소에는 타사 실행 원문·개인 설정·설치 경로·복구 백업을 포함하지 않는다.

## 전역 스킬 103개별 근거.

| 설치 이름 | 계열 | 설치 스킬 버전·원본 번들 | 본문 SHA-256 앞 16자 | 판정 | 실제 공개 원본 |
|---|---|---|---|---|---|
| `a11y-debugging` | Chrome DevTools | 미표기 · 원본 번들 `1.2.0` | `e226a19346d46ec3` | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/a11y-debugging/SKILL.md) |
| `agent-development` | Anthropic 플러그인 | `0.1.0` (자체 선언) · 원본 번들 미확인 | `975cfc640270450b` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/agent-development/SKILL.md) |
| `brainstorming` | Superpowers | `7.0.2` (설치 기록) | `110366dea1e3b09c` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) |
| `cancel-ralph` | 자체 제작 | 미표기 | `a269519cee9a596b` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/cancel-ralph/SKILL.md) |
| `chrome-devtools` | Chrome DevTools | 미표기 · 원본 번들 `1.2.0` | `ee96a0808f78d6db` | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/chrome-devtools/SKILL.md) |
| `chrome-devtools-cli` | Chrome DevTools | 미표기 · 원본 번들 `1.2.0` | `53614b0e35580297` | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/chrome-devtools-cli/SKILL.md) |
| `claude-api` | 자체 제작 | 미표기 | `ae3873462656201a` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/claude-api/SKILL.md) |
| `claude-automation-recommender` | Anthropic 플러그인 | 미표기 · 원본 번들 `1.0.0` | `7e36ad2b5f15b950` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/146d4788ff321cd6e4703f9ba9c07113be7abb5c/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md) |
| `claude-md-improver` | Anthropic 플러그인 | 미표기 · 원본 번들 `1.0.0` | `092974387c61fe7a` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/claude-md-management/skills/claude-md-improver/SKILL.md) |
| `claude-news` | 자체 제작 | 미표기 | `2d6d5d7948f7eea4` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/claude-news/SKILL.md) |
| `code-review` | 자체 제작 | 미표기 | `2225497dee1fe08d` | 본문 차이·변환 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/code-review/SKILL.md) |
| `command-development` | Anthropic 플러그인 | `0.2.0` (자체 선언) · 원본 번들 미확인 | `24632f1e6a5f8a13` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/command-development/SKILL.md) |
| `create-plugin` | Anthropic 플러그인 | 미표기 · 원본 번들 미확인 | `bfdf8c7548609c6f` | 본문 차이·변환 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/commands/create-plugin.md) |
| `daily-work-report` | 자체 제작 | 미표기 | `a5a41820edb6b0e6` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/daily-work-report/SKILL.md) |
| `debug-optimize-lcp` | Chrome DevTools | 미표기 · 원본 번들 `1.2.0` | `2a1025f0f9b84bfc` | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/debug-optimize-lcp/SKILL.md) |
| `deep-research` | 자체 제작 | 미표기 | `6e624e50ca058639` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/deep-research/SKILL.md) |
| `delete-session` | 자체 제작 | 미표기 | `d5dc5eaf446ae6bf` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/delete-session/SKILL.md) |
| `design-driven-delivery` | 자체 제작 | 미표기 | `31b194cab1ba21ca` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/design-driven-delivery/SKILL.md) |
| `diagnosing-superpowers` | Superpowers | `7.0.2` (설치 기록) | `0cd431d0ccd58724` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md) |
| `dispatching-parallel-agents` | Superpowers | `7.0.2` (설치 기록) | `eed8724a63a6c70a` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) |
| `executing-plans` | Superpowers | `7.0.2` (설치 기록) | `9a5c6d1ca75b4d04` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) |
| `feature-dev` | 자체 제작 | 미표기 | `f3e117f57b459ce3` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/feature-dev/SKILL.md) |
| `fewer-permission-prompts` | 자체 제작 | 미표기 | `76947c13d1fef5b3` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/fewer-permission-prompts/SKILL.md) |
| `figma-code-connect` | Figma | 미표기 · 원본 번들 `2.2.50` | `01d3ee9af6e4a914` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-code-connect/SKILL.md) |
| `figma-create-new-file` | Figma | 미표기 · 원본 번들 `2.2.50` | `d7980ccedfb5fe11` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-create-new-file/SKILL.md) |
| `figma-generate-design` | Figma | 미표기 · 원본 번들 `2.2.50` | `a5bb591e3a4d529c` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-generate-design/SKILL.md) |
| `figma-generate-diagram` | Figma | 미표기 · 원본 번들 `2.2.50` | `4f1034a818020c1f` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-generate-diagram/SKILL.md) |
| `figma-generate-library` | Figma | 미표기 · 원본 번들 `2.2.50` | `cb122b12c823bcfa` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-generate-library/SKILL.md) |
| `figma-generate-project-plan` | 자체 제작 | 미표기 | `b838e032a84b30ad` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/figma-generate-project-plan/SKILL.md) |
| `figma-use` | Figma | 미표기 · 원본 번들 `2.2.50` | `3acbc27e8e90aa91` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-use/SKILL.md) |
| `figma-use-figjam` | Figma | 미표기 · 원본 번들 `2.2.50` | `e5f0bef83ec36338` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-use-figjam/SKILL.md) |
| `figma-use-slides` | Figma | 미표기 · 원본 번들 `2.2.50` | `fca46f90efd4a452` | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-use-slides/SKILL.md) |
| `finishing-a-development-branch` | Superpowers | `7.0.2` (설치 기록) | `5e9c5f4b069243d8` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) |
| `firecrawl-agent` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `f9e0c42f40d94670` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-agent/SKILL.md) |
| `firecrawl-cli` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `4b36e59e34be6388` | 본문 차이·변환 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-cli/SKILL.md) |
| `firecrawl-crawl` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `3facc0eaed332fd2` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-crawl/SKILL.md) |
| `firecrawl-download` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `947d3436fca7559b` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-download/SKILL.md) |
| `firecrawl-interact` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `9bf62757d260019f` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-interact/SKILL.md) |
| `firecrawl-map` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `4b4778ab45659ab9` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-map/SKILL.md) |
| `firecrawl-monitor` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `75e4a063b0420152` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-monitor/SKILL.md) |
| `firecrawl-parse` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `ea22462791f06755` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-parse/SKILL.md) |
| `firecrawl-scrape` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `4db9c0171544f671` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-scrape/SKILL.md) |
| `firecrawl-search` | Firecrawl | 미표기 · 원본 번들 `1.0.9` | `f2963cb719d461e7` | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-search/SKILL.md) |
| `frontend-design` | Anthropic 플러그인 | 미표기 · 원본 번들 미확인 | `57cf1134b36c816a` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/d029127f7d29bdb8fd8902ac34dd7d5c8ba92b6e/plugins/frontend-design/skills/frontend-design/SKILL.md) |
| `handover` | 자체 제작 | 미표기 | `85c2470a60084b4b` | 본문 차이·변환 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/handover/SKILL.md) |
| `help` | 자체 제작 | 미표기 | `f400633b286f6682` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/help/SKILL.md) |
| `hf-cli` | Hugging Face | 미표기 · 생성기 `1.18.0` · 원본 번들 `1.0.8` | `7c818fe5f8adecb8` | 본문 차이·변환 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/hf-cli/SKILL.md) |
| `hook-development` | Anthropic 플러그인 | `0.1.0` (자체 선언) · 원본 번들 미확인 | `0d3372949fa2ba96` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/hook-development/SKILL.md) |
| `huggingface-best` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `eeaa8ab7f4b97196` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-best/SKILL.md) |
| `huggingface-community-evals` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `3c622c4b50ea9b56` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-community-evals/SKILL.md) |
| `huggingface-datasets` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `615f5c83e98147f6` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-datasets/SKILL.md) |
| `huggingface-gradio` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `037e16340be15eaa` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-gradio/SKILL.md) |
| `huggingface-llm-trainer` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `fd62fecb15011a6f` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-llm-trainer/SKILL.md) |
| `huggingface-local-models` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `14279c5c460b4adb` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-local-models/SKILL.md) |
| `huggingface-lora-space-builder` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `208fbefe87f3ce1a` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-lora-space-builder/SKILL.md) |
| `huggingface-paper-publisher` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `a22e00c2e57c22e3` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-paper-publisher/SKILL.md) |
| `huggingface-papers` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `985c2d5c7261aba2` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-papers/SKILL.md) |
| `huggingface-spaces` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `be89aa2e12d0bf92` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-spaces/SKILL.md) |
| `huggingface-tool-builder` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `62eff86a37ea47cd` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-tool-builder/SKILL.md) |
| `huggingface-trackio` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `e4018531811aecbb` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-trackio/SKILL.md) |
| `huggingface-vision-trainer` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `b49acd79b48be406` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-vision-trainer/SKILL.md) |
| `huggingface-zerogpu` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `c4c3e551bf20e215` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-zerogpu/SKILL.md) |
| `init` | 자체 제작 | 미표기 | `0e46677f993fafd4` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/init/SKILL.md) |
| `keybindings-help` | 자체 제작 | 미표기 | `a8d63d5f43204fb4` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/keybindings-help/SKILL.md) |
| `loop` | 자체 제작 | 미표기 | `4020dfb94bf8f5eb` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/loop/SKILL.md) |
| `mcp-integration` | Anthropic 플러그인 | `0.1.0` (자체 선언) · 원본 번들 미확인 | `8555b4a813d76748` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/2438937b32bebeee7727fd1ba989eec464750838/plugins/plugin-dev/skills/mcp-integration/SKILL.md) |
| `memory-leak-debugging` | Chrome DevTools | 미표기 · 원본 번들 `1.2.0` | `f9f8efb29e383e6e` | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/memory-leak-debugging/SKILL.md) |
| `new-sdk-app` | 자체 제작 | 미표기 | `e7577063e95d72ca` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/new-sdk-app/SKILL.md) |
| `playground` | Anthropic 플러그인 | 미표기 · 원본 번들 미확인 | `e5d89cbbdd77be9b` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/playground/skills/playground/SKILL.md) |
| `plugin-settings` | Anthropic 플러그인 | `0.1.0` (자체 선언) · 원본 번들 미확인 | `0ebfa63d6704901c` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/plugin-settings/SKILL.md) |
| `plugin-structure` | Anthropic 플러그인 | `0.1.0` (자체 선언) · 원본 번들 미확인 | `4333b3e6fd1824d6` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/plugin-structure/SKILL.md) |
| `qodo-get-rules` | Qodo | 미표기 · 원본 번들 `0.6.1` | `271f4582e8313cec` | 본문 차이·변환 | [고정 원본](https://github.com/qodo-ai/qodo-skills/blob/8aec13d6ac60feb9d9f84f36aa1753234de17dc8/skills/qodo-get-rules/SKILL.md) |
| `qodo-pr-resolver` | Qodo | 미표기 · 원본 번들 `0.6.1` | `b7119f08acbb2fd0` | 본문 차이·변환 | [고정 원본](https://github.com/qodo-ai/qodo-skills/blob/8aec13d6ac60feb9d9f84f36aa1753234de17dc8/skills/qodo-pr-resolver/SKILL.md) |
| `ralph-loop` | 자체 제작 | 미표기 | `c07777b00aad2da9` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/ralph-loop/SKILL.md) |
| `receiving-code-review` | Superpowers | `7.0.2` (설치 기록) | `4fb08b86f10c892e` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) |
| `requesting-code-review` | Superpowers | `7.0.2` (설치 기록) | `1a235acf066f4ee3` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) |
| `review` | 자체 제작 | 미표기 | `b20efe013cac32a0` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/review/SKILL.md) |
| `review-pr` | 자체 제작 | 미표기 | `ac51472a4513d68b` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/review-pr/SKILL.md) |
| `revise-claude-md` | Anthropic 플러그인 | 미표기 · 원본 번들 `1.0.0` | `e1e65759ec6002d5` | 본문 차이·변환 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/claude-md-management/commands/revise-claude-md.md) |
| `run` | 자체 제작 | 미표기 | `635a66bf4dd5cbef` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/run/SKILL.md) |
| `schedule` | 로컬·카탈로그 변환 | 미표기 | `f54df3cdca4eb898` | 공개 실행 원본 미확인 | 미확인. |
| `security-review` | 자체 제작 | 미표기 | `1e3bb2280ae5e7c4` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/security-review/SKILL.md) |
| `simplify` | 자체 제작 | 미표기 | `115b7fa5fa5983c1` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/simplify/SKILL.md) |
| `skill-creator` | Anthropic 플러그인 | 미표기 · 원본 번들 미확인 | `c08c99c48c173627` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/skill-creator/skills/skill-creator/SKILL.md) |
| `skill-development` | Anthropic 플러그인 | `0.1.0` (자체 선언) · 원본 번들 미확인 | `48917e494d7aebcf` | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/skill-development/SKILL.md) |
| `skill-gen` | Firecrawl 명령 변환 | 미표기 · 원본 번들 `1.0.9` | `22cc06d032f5f916` | 본문 차이·변환 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/commands/skill-gen.md) |
| `source-command-delete-session` | 로컬·카탈로그 변환 | 미표기 | `c4d0ba15bb67f7d0` | 공개 실행 원본 미확인 | 미확인. |
| `source-command-handover` | 로컬·카탈로그 변환 | 미표기 | `a5db2db5469d4f9e` | 공개 실행 원본 미확인 | 미확인. |
| `subagent-driven-development` | Superpowers | `7.0.2` (설치 기록) | `df2bcd230bde6cf5` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) |
| `systematic-debugging` | Superpowers | `7.0.2` (설치 기록) | `a9a79740379b1d42` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) |
| `test-driven-development` | Superpowers | `7.0.2` (설치 기록) | `89b7bbc7a3ef3a50` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md) |
| `train-sentence-transformers` | Hugging Face | 미표기 · 원본 번들 `1.0.8` | `4c50e50a0bd57d51` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/train-sentence-transformers/SKILL.md) |
| `transformers-js` | Hugging Face | `4.x` (metadata 선언) · 원본 번들 `1.0.8` | `8c3b1a1bd8bbf502` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/transformers-js/SKILL.md) |
| `trl-training` | Hugging Face | `1.0.0` (metadata 선언) · 원본 번들 `1.0.8` | `a3c59dd737e8f2b1` | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/trl-training/SKILL.md) |
| `troubleshooting` | Chrome DevTools | 미표기 · 원본 번들 `1.2.0` | `2b28e7c4a3da3c73` | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/troubleshooting/SKILL.md) |
| `unity-cli` | Unity | 미표기 | `247b021fee6b875f` | 본문 일치 | [고정 원본](https://github.com/Unity-Technologies/skills/blob/e91a6c4f9acf252e542c1228db1fc36b5a22a8d0/skills/unity-cli/SKILL.md) |
| `update-config` | 자체 제작 | 미표기 | `0e435cd4c2a13b90` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/update-config/SKILL.md) |
| `using-git-worktrees` | Superpowers | `7.0.2` (설치 기록) | `d27655775d8f9b40` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) |
| `using-superpowers` | Superpowers | `7.0.2` (설치 기록) | `2404d2e763fad2ac` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) |
| `verification-before-completion` | Superpowers | `7.0.2` (설치 기록) | `07e72bb5e99c67b5` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) |
| `verify` | 자체 제작 | 미표기 | `bb62353f849691d5` | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/verify/SKILL.md) |
| `writing-plans` | Superpowers | `7.0.2` (설치 기록) | `12110e45d07ecc42` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md) |
| `writing-skills` | Superpowers | `7.0.2` (설치 기록) | `67222569684b34ee` | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) |

## 본문 차이와 동명 스킬의 경계.

| 항목 | 확인한 차이 |
|---|---|
| code-review, handover. | 이 저장소 자체 제작 원본에 개인 로컬 참조 링크가 추가됐다. 개인 참조 본문은 공개하지 않는다. |
| create-plugin, revise-claude-md. | Anthropic의 공개 command를 한국어 요약·스킬 형식으로 변환했다. 원본 SKILL.md 그대로가 아니다. |
| skill-gen. | 과거 Firecrawl command의 카탈로그 요약 변환본이다. 구식 --maxDepth 설명이 남아 있으며 이 조사에서 자동 갱신하지 않았다. |
| firecrawl-cli. | 설치 이름이 firecrawl-cli로 바뀌었으며 조회한 원본의 endpoint feedback 절이 설치본에는 없다. |
| hf-cli. | 설치본은 huggingface_hub 1.18.0 생성본, 조회본은 1.19.0이다. 로컬 Claude 캐시와 설치본은 일치한다. |
| qodo-get-rules. | README 상대 링크를 패키지 내부 references/configuration.md로 변경했다. |
| qodo-pr-resolver. | 조회한 공개 버전의 단일 지적 처리 규칙과 차이가 있다. 설치본은 로컬 Claude 캐시와 일치한다. |

feature-dev, claude-api, deep-research, code-review, security-review, simplify 등 현재 전역 설치본은 이 저장소의 자체 작성 원본이다. 각 references/sources.md에 있는 Anthropic·ECC·Addy Osmani 링크는 참고와 채택 경계이며 이 설치본의 직접 원본과 구분한다.

남은 공개 실행 원본 미확인은 schedule, source-command-delete-session, source-command-handover 3개다. schedule은 실제 내장 원문이 아니라 공개 카탈로그 설명을 스킬로 변환한 것이며 옛 설명에 세션 Cron과 클라우드 routines 혼동이 있다. source-command 두 개는 로컬 Claude command 원문과 변환 래퍼 제외 본문이 일치하지만 공개 실행 원본은 확인하지 못했다.

## 별도 설치·내장·플러그인 30개.

아래 두 skill-creator는 서로 다른 구현이다. 전역 항목은 Anthropic 플러그인 원본이며 내장 항목은 openai/codex 원본이다. 이름만으로 합치지 않는다.

| 설치 구분·이름 | 설치 버전·빌드 | 본문 SHA-256 앞 16자 | 판정 | 공개 원본 또는 확인 범위 |
|---|---|---|---|---|
| `별도 사용자 설치 / migrate-to-codex` | 미표기 | `a60f3e9adac1dc0c` | 본문 일치 | [고정 원본](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/migrate-to-codex/SKILL.md) |
| `Codex 내장 / imagegen` | 미표기 | `976a0163c2cff076` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/imagegen/SKILL.md) |
| `Codex 내장 / openai-docs` | 미표기 | `dd4e1e262e07cf0d` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/openai-docs/SKILL.md) |
| `Codex 내장 / skill-creator` | 미표기 | `a2fa8da9ce13d832` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md) |
| `Codex 내장 / skill-installer` | 미표기 | `98494ab86339217c` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/skill-installer/SKILL.md) |
| `Codex 내장 / review-agent` | 미표기 | `14a3e54e79741c77` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/review-agent/SKILL.md) |
| `computer-use:computer-use` | `26.1029.61003` (설치 번들) | `3afee01398880c51` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `visualize:visualize` | `1.0.74` (설치 번들) | `0d3142bd912bb6a3` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:maintain-space` | `0.1.26` (설치 번들) | `d184ed1a9bf8e4f2` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:manage-schedules` | `0.1.26` (설치 번들) | `4111ec989acb456e` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:organize-space` | `0.1.26` (설치 번들) | `8b758e4aea230db7` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:write-page` | `0.1.26` (설치 번들) | `aaee911385f5ead8` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `plugin-management:plugin-management` | `0.1.0` (설치 번들) | `651302048609e1e0` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `sites:sites` | `1.1.3` (설치 번들) | `a184aeb3f2014e40` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `sites:sites-remix` | `1.1.3` (설치 번들) | `1db46845872fac95` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `work-pets:create-pet` | `0.1.6` (설치 번들) | `b2196bf4715ad2e8` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `work-pets:pets` | `0.1.6` (설치 번들) | `6eff15058cbaa1b2` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `work-pets:update-pet` | `0.1.6` (설치 번들) | `9a85794de784ba49` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `documents:documents` | `26.1104.11149` (설치 번들) | `93d8393595f50e87` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pdf:pdf` | `26.1104.11149` (설치 번들) | `b075edf46e34dad7` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `presentations:presentations` | `26.1104.11149` (설치 번들) | `52f435233ce9d832` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `spreadsheets:excel-live-control` | `26.1104.11149` (설치 번들) | `bac2c56dece96b71` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `spreadsheets:spreadsheets` | `26.1104.11149` (설치 번들) | `6a88a48af0bfdbfc` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `template-creator:template-creator` | `26.1104.11149` (설치 번들) | `ca7a9303d7079c59` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `ponytail:ponytail` | `5.3.3` (설치 번들) | `54ba3851a4ea7100` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail/SKILL.md) |
| `ponytail:ponytail-audit` | `5.3.3` (설치 번들) | `10eaedd92a34194d` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-audit/SKILL.md) |
| `ponytail:ponytail-debt` | `5.3.3` (설치 번들) | `688de7b5be11e7a8` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-debt/SKILL.md) |
| `ponytail:ponytail-gain` | `5.3.3` (설치 번들) | `5f5cfdfba6750244` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-gain/SKILL.md) |
| `ponytail:ponytail-help` | `5.3.3` (설치 번들) | `f68337ee993f626e` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-help/SKILL.md) |
| `ponytail:ponytail-review` | `5.3.3` (설치 번들) | `125036d590f6de8f` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-review/SKILL.md) |

## 요청에 따라 제거한 개인 스킬.

사용자가 digital-twin-jobs-watch, hexagonal-code-review, us-stock-holding-report를 Codex와 Claude 양쪽에서 삭제하도록 요청했다. 세 이름의 사용자 전역 설치 후보 9개 경로 중 실제 존재하던 5개 디렉터리·12개 파일을 제거했다. 다른 스킬 본문과 두 클라이언트 설정의 확인 대상 136개 파일 해시가 유지됐으며 복구 자료는 공개 저장소 밖에 보관했다. 과거 설치와 변경 이력은 현재 활성 목록과 구분한다.

## 검증과 한계.

각 스킬의 공개 파일 존재와 전체 본문을 대조했고 정확히 일치하는 과거 커밋을 찾은 항목은 그 커밋으로 연결했다. Superpowers 외의 scripts·references·assets 전체 내용은 전수 대조하지 않았다. 실제 스킬 호출·필수 MCP 인증·모든 호스트 동작·자동 업데이트·재배포 적합성은 이 출처 조사로 검증한 것이 아니다. 열린 세션에는 이전 스킬 목록이 남을 수 있으므로 새 세션의 발견 결과와 디스크 삭제 검증을 구분한다.
