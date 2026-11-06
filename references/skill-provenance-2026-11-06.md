<!-- 설치 스킬의 공개 원본·변환 여부와 조사 경계를 기록한다. -->
# 스킬 공개 원본 조사 기록.

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

## 제작자 저장소와 설치 계보.

| 계열 | 공개 원본 | 구분 |
|---|---|---|
| Superpowers. | [obra/superpowers](https://github.com/obra/superpowers/tree/v7.0.2/skills) | 15개 본문이 v7.0.2와 일치한다. 설치 기록이 추적한 보조파일 포함 80개 파일 해시도 모두 일치했다. |
| Hugging Face. | [huggingface/skills](https://github.com/huggingface/skills) | 18개. hf-cli는 CLI 버전에서 생성된 본문이다. |
| Firecrawl. | [firecrawl/firecrawl-claude-plugin](https://github.com/firecrawl/firecrawl-claude-plugin) | 10개 스킬과 과거 skill-gen command의 변환본이다. 현재 브랜치의 경로가 바뀌거나 제거된 항목은 아래 고정 커밋을 따른다. |
| Chrome DevTools. | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp/tree/main/skills) | 설치된 6개 실제 스킬 원본을 확인했다. MCP 실행 래퍼만 있는 것으로 분류하지 않는다. |
| Figma. | [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide) | 8개 외부 원본. figma-generate-project-plan 설치본은 아래 자체 제작 원본이다. |
| Qodo. | [qodo-ai/qodo-skills](https://github.com/qodo-ai/qodo-skills) | 설치된 2개 원본 계보를 확인했다. |
| Anthropic 플러그인. | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | 12개 SKILL.md와 2개 command 변환본이다. |
| Unity. | [Unity-Technologies/skills](https://github.com/Unity-Technologies/skills) | unity-cli의 일치하는 과거 커밋을 확인했다. |
| 자체 제작. | [Owned-Skills](../Owned-Skills/README.md) | 이 저장소의 직접 작성 원본 25개다. 외부 참고 자료를 이 설치본의 원본으로 오인하지 않는다. |
| Codex 내장. | [openai/codex](https://github.com/openai/codex/tree/main/codex-rs/skills/src/assets/samples) | 내장 5개 실제 원본과 일치한다. |
| OpenAI curated. | [openai/skills](https://github.com/openai/skills) | migrate-to-codex 설치본과 일치한다. |
| Ponytail. | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail/tree/v5.3.3/skills) | 플러그인의 6개 본문이 v5.3.3과 일치한다. |

출처 확인은 타사 파일 재배포 허가를 뜻하지 않는다. 실제 설치·재배포 시 해당 고정 원본의 라이선스와 제작자 조건을 별도로 확인한다. 이 저장소에는 타사 실행 원문·개인 설정·설치 경로·복구 백업을 포함하지 않는다.

## 전역 스킬 103개별 근거.

| 설치 이름 | 계열 | 판정 | 실제 공개 원본 |
|---|---|---|---|
| `a11y-debugging` | Chrome DevTools | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/a11y-debugging/SKILL.md) |
| `agent-development` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/agent-development/SKILL.md) |
| `brainstorming` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) |
| `cancel-ralph` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/cancel-ralph/SKILL.md) |
| `chrome-devtools` | Chrome DevTools | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/chrome-devtools/SKILL.md) |
| `chrome-devtools-cli` | Chrome DevTools | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/chrome-devtools-cli/SKILL.md) |
| `claude-api` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/claude-api/SKILL.md) |
| `claude-automation-recommender` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/146d4788ff321cd6e4703f9ba9c07113be7abb5c/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md) |
| `claude-md-improver` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/claude-md-management/skills/claude-md-improver/SKILL.md) |
| `claude-news` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/claude-news/SKILL.md) |
| `code-review` | 자체 제작 | 본문 차이·변환 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/code-review/SKILL.md) |
| `command-development` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/command-development/SKILL.md) |
| `create-plugin` | Anthropic 플러그인 | 본문 차이·변환 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/commands/create-plugin.md) |
| `daily-work-report` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/daily-work-report/SKILL.md) |
| `debug-optimize-lcp` | Chrome DevTools | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/debug-optimize-lcp/SKILL.md) |
| `deep-research` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/deep-research/SKILL.md) |
| `delete-session` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/delete-session/SKILL.md) |
| `design-driven-delivery` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/design-driven-delivery/SKILL.md) |
| `diagnosing-superpowers` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md) |
| `dispatching-parallel-agents` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) |
| `executing-plans` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) |
| `feature-dev` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/feature-dev/SKILL.md) |
| `fewer-permission-prompts` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/fewer-permission-prompts/SKILL.md) |
| `figma-code-connect` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-code-connect/SKILL.md) |
| `figma-create-new-file` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-create-new-file/SKILL.md) |
| `figma-generate-design` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-generate-design/SKILL.md) |
| `figma-generate-diagram` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-generate-diagram/SKILL.md) |
| `figma-generate-library` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-generate-library/SKILL.md) |
| `figma-generate-project-plan` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/figma-generate-project-plan/SKILL.md) |
| `figma-use` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-use/SKILL.md) |
| `figma-use-figjam` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-use-figjam/SKILL.md) |
| `figma-use-slides` | Figma | 본문 일치 | [고정 원본](https://github.com/figma/mcp-server-guide/blob/2efd0e37d10c35c4a7cf6d2b7381c9dc1a569bd4/skills/figma-use-slides/SKILL.md) |
| `finishing-a-development-branch` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) |
| `firecrawl-agent` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-agent/SKILL.md) |
| `firecrawl-cli` | Firecrawl | 본문 차이·변환 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-cli/SKILL.md) |
| `firecrawl-crawl` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-crawl/SKILL.md) |
| `firecrawl-download` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-download/SKILL.md) |
| `firecrawl-interact` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-interact/SKILL.md) |
| `firecrawl-map` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-map/SKILL.md) |
| `firecrawl-monitor` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-monitor/SKILL.md) |
| `firecrawl-parse` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-parse/SKILL.md) |
| `firecrawl-scrape` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-scrape/SKILL.md) |
| `firecrawl-search` | Firecrawl | 본문 일치 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/skills/firecrawl-search/SKILL.md) |
| `frontend-design` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/d029127f7d29bdb8fd8902ac34dd7d5c8ba92b6e/plugins/frontend-design/skills/frontend-design/SKILL.md) |
| `handover` | 자체 제작 | 본문 차이·변환 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/handover/SKILL.md) |
| `help` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/help/SKILL.md) |
| `hf-cli` | Hugging Face | 본문 차이·변환 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/hf-cli/SKILL.md) |
| `hook-development` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/hook-development/SKILL.md) |
| `huggingface-best` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-best/SKILL.md) |
| `huggingface-community-evals` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-community-evals/SKILL.md) |
| `huggingface-datasets` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-datasets/SKILL.md) |
| `huggingface-gradio` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-gradio/SKILL.md) |
| `huggingface-llm-trainer` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-llm-trainer/SKILL.md) |
| `huggingface-local-models` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-local-models/SKILL.md) |
| `huggingface-lora-space-builder` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-lora-space-builder/SKILL.md) |
| `huggingface-paper-publisher` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-paper-publisher/SKILL.md) |
| `huggingface-papers` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-papers/SKILL.md) |
| `huggingface-spaces` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-spaces/SKILL.md) |
| `huggingface-tool-builder` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-tool-builder/SKILL.md) |
| `huggingface-trackio` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-trackio/SKILL.md) |
| `huggingface-vision-trainer` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-vision-trainer/SKILL.md) |
| `huggingface-zerogpu` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/huggingface-zerogpu/SKILL.md) |
| `init` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/init/SKILL.md) |
| `keybindings-help` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/keybindings-help/SKILL.md) |
| `loop` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/loop/SKILL.md) |
| `mcp-integration` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/2438937b32bebeee7727fd1ba989eec464750838/plugins/plugin-dev/skills/mcp-integration/SKILL.md) |
| `memory-leak-debugging` | Chrome DevTools | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/memory-leak-debugging/SKILL.md) |
| `new-sdk-app` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/new-sdk-app/SKILL.md) |
| `playground` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/playground/skills/playground/SKILL.md) |
| `plugin-settings` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/plugin-settings/SKILL.md) |
| `plugin-structure` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/plugin-structure/SKILL.md) |
| `qodo-get-rules` | Qodo | 본문 차이·변환 | [고정 원본](https://github.com/qodo-ai/qodo-skills/blob/8aec13d6ac60feb9d9f84f36aa1753234de17dc8/skills/qodo-get-rules/SKILL.md) |
| `qodo-pr-resolver` | Qodo | 본문 차이·변환 | [고정 원본](https://github.com/qodo-ai/qodo-skills/blob/8aec13d6ac60feb9d9f84f36aa1753234de17dc8/skills/qodo-pr-resolver/SKILL.md) |
| `ralph-loop` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/ralph-loop/SKILL.md) |
| `receiving-code-review` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) |
| `requesting-code-review` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) |
| `review` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/review/SKILL.md) |
| `review-pr` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/review-pr/SKILL.md) |
| `revise-claude-md` | Anthropic 플러그인 | 본문 차이·변환 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/claude-md-management/commands/revise-claude-md.md) |
| `run` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/run/SKILL.md) |
| `schedule` | 로컬·카탈로그 변환 | 공개 실행 원본 미확인 | 미확인. |
| `security-review` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/security-review/SKILL.md) |
| `simplify` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/simplify/SKILL.md) |
| `skill-creator` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/skill-creator/skills/skill-creator/SKILL.md) |
| `skill-development` | Anthropic 플러그인 | 본문 일치 | [고정 원본](https://github.com/anthropics/claude-plugins-official/blob/cb421c81df4274fd28fd1ead817bc6ffea723fed/plugins/plugin-dev/skills/skill-development/SKILL.md) |
| `skill-gen` | Firecrawl 명령 변환 | 본문 차이·변환 | [고정 원본](https://github.com/firecrawl/firecrawl-claude-plugin/blob/e30c89f7b065b29a7283d49a4dcc5e302900fda3/commands/skill-gen.md) |
| `source-command-delete-session` | 로컬·카탈로그 변환 | 공개 실행 원본 미확인 | 미확인. |
| `source-command-handover` | 로컬·카탈로그 변환 | 공개 실행 원본 미확인 | 미확인. |
| `subagent-driven-development` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) |
| `systematic-debugging` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) |
| `test-driven-development` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md) |
| `train-sentence-transformers` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/train-sentence-transformers/SKILL.md) |
| `transformers-js` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/transformers-js/SKILL.md) |
| `trl-training` | Hugging Face | 본문 일치 | [고정 원본](https://github.com/huggingface/skills/blob/c68f1b08d9eb3af22cdc1d3fb60e9cdb78522556/skills/trl-training/SKILL.md) |
| `troubleshooting` | Chrome DevTools | 본문 일치 | [고정 원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/ed02047ae90f25c4c15adb8fd7e224b963f43135/skills/troubleshooting/SKILL.md) |
| `unity-cli` | Unity | 본문 일치 | [고정 원본](https://github.com/Unity-Technologies/skills/blob/e91a6c4f9acf252e542c1228db1fc36b5a22a8d0/skills/unity-cli/SKILL.md) |
| `update-config` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/update-config/SKILL.md) |
| `using-git-worktrees` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) |
| `using-superpowers` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) |
| `verification-before-completion` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) |
| `verify` | 자체 제작 | 본문 일치 | [고정 원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/verify/SKILL.md) |
| `writing-plans` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md) |
| `writing-skills` | Superpowers | 본문 일치 | [고정 원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) |

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

| 설치 구분·이름 | 판정 | 공개 원본 또는 확인 범위 |
|---|---|---|
| `별도 사용자 설치 / migrate-to-codex` | 본문 일치 | [고정 원본](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/migrate-to-codex/SKILL.md) |
| `Codex 내장 / imagegen` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/imagegen/SKILL.md) |
| `Codex 내장 / openai-docs` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/openai-docs/SKILL.md) |
| `Codex 내장 / skill-creator` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md) |
| `Codex 내장 / skill-installer` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/skill-installer/SKILL.md) |
| `Codex 내장 / review-agent` | 본문 일치 | [고정 원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/review-agent/SKILL.md) |
| `computer-use:computer-use` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `visualize:visualize` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:maintain-space` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:manage-schedules` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:organize-space` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pages:write-page` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `plugin-management:plugin-management` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `sites:sites` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `sites:sites-remix` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `work-pets:create-pet` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `work-pets:pets` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `work-pets:update-pet` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `documents:documents` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `pdf:pdf` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `presentations:presentations` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `spreadsheets:excel-live-control` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `spreadsheets:spreadsheets` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `template-creator:template-creator` | 공식 배포·공개 원본 미확인 | OpenAI 제작자·설치 실물 확인. 공개 실행 원본은 미확인. |
| `ponytail:ponytail` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail/SKILL.md) |
| `ponytail:ponytail-audit` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-audit/SKILL.md) |
| `ponytail:ponytail-debt` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-debt/SKILL.md) |
| `ponytail:ponytail-gain` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-gain/SKILL.md) |
| `ponytail:ponytail-help` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-help/SKILL.md) |
| `ponytail:ponytail-review` | 본문 일치 | [고정 원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-review/SKILL.md) |

## 요청에 따라 제거한 개인 스킬.

사용자가 digital-twin-jobs-watch, hexagonal-code-review, us-stock-holding-report를 Codex와 Claude 양쪽에서 삭제하도록 요청했다. 세 이름의 사용자 전역 설치 후보 9개 경로 중 실제 존재하던 5개 디렉터리·12개 파일을 제거했다. 다른 스킬 본문과 두 클라이언트 설정의 확인 대상 136개 파일 해시가 유지됐으며 복구 자료는 공개 저장소 밖에 보관했다. 과거 설치와 변경 이력은 현재 활성 목록과 구분한다.

## 검증과 한계.

각 스킬의 공개 파일 존재와 전체 본문을 대조했고 정확히 일치하는 과거 커밋을 찾은 항목은 그 커밋으로 연결했다. Superpowers 외의 scripts·references·assets 전체 내용은 전수 대조하지 않았다. 실제 스킬 호출·필수 MCP 인증·모든 호스트 동작·자동 업데이트·재배포 적합성은 이 출처 조사로 검증한 것이 아니다. 열린 세션에는 이전 스킬 목록이 남을 수 있으므로 새 세션의 발견 결과와 디스크 삭제 검증을 구분한다.
