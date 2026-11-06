<!-- Codex 스킬 갱신 후의 출처·버전과 보류·검증 범위를 기록한다. -->
# Codex 스킬 업데이트 기록.

2026-11-06에 승인된 설계를 Codex에만 적용했다. [이전 출처 조사](skill-provenance-2026-11-06.md)는 당시 이력으로 보존한다. 아래 표와 [기계 판독 가능한 버전·파일 해시](codex-skill-versions-2026-11-06.json)는 갱신 후 상태다. 타사 실행 원문·개인 설정·백업은 저장소에 포함하지 않는다.

## 결과와 제작자 계보.

57개 후보 중 48개 패키지의 파일을 갱신하고 9개는 동일 원본을 유지했다. 264개 파일 쓰기와 7개 개별 삭제를 검증했다. Firecrawl 대표 이름은 `firecrawl-cli`에서 `firecrawl`로 전환했으며 `skill-gen`은 Codex에서 퇴역했다. 기존 패키지 49개·253개 파일을 전체 백업하고 변경 파일별 복구 자료도 보존했다.

| 제작자 원본 | 적용 버전·구분 | 범위 |
|---|---|---|
| [huggingface/skills](https://github.com/huggingface/skills/tree/c3ff942be3e07116b475253f0a8fc4f54682c1a8) | 원본 번들 1.0.35. hf-cli 생성기 huggingface_hub 2.2.0. | 기존 18개. 실제 CLI 설치 버전과 구분한다. |
| [figma/mcp-server-guide](https://github.com/figma/mcp-server-guide/tree/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5) | 원본 번들 2.2.157. | 기존 8개. 필요한 motion 참조만 내장했다. |
| [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp/tree/af2834411a564d366f9cab63efb046d9084f4dba) | 스킬 원본 안정 배포 1.12.0. | 기존 6개. 실제 MCP 실행 설정·버전은 변경하지 않았다. |
| [anthropics/claude-plugins-public](https://github.com/anthropics/claude-plugins-public/tree/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853) | plugin-dev 0.1.1, claude-code-setup·claude-md-management 1.0.0, frontend-design 1.1.1. 나머지 미표기. | 기존 14개 후보 중 9개 동일, command 한국어 변환 2개 보존. |
| [Unity-Technologies/skills](https://github.com/Unity-Technologies/skills/tree/ba28c24fc7e569fa0fd5b6bf16ab2bb0acef0594) | 스킬 버전 미표기. 고정 커밋으로 식별한다. | unity-cli 1개. CLI·Editor 설치 버전을 뜻하지 않는다. |
| [firecrawl/cli](https://github.com/firecrawl/cli/tree/da25d5cd06db21cb33b100661cea0d9b89d457a3) | 고정 snapshot da25d5cd06db. 소스 package.json 1.28.0. | 기존 기능 10개. 독립 스킬 버전이나 설치 CLI 버전으로 표기하지 않는다. |

자체 제작 25개와 Superpowers 7.0.2·15개, migrate-to-codex·내장 5개·Ponytail 5.3.3은 확인한 원본을 유지한다. 공개 실행 원본 미확인 로컬 변환 3개도 교체하지 않았다.

## 패치·보류·노출의 경계.

Hugging Face의 채팅 토큰 요청과 원본 세션 일괄 업로드 예시는 공식 로그인 및 승인·민감정보 제거·별도 준비 폴더·대상 비공개 검증 절차로 보정했다. Figma의 누락 보조 참조를 내장하고 잘못된 상대 링크를 수정했다. HF 문서 링크 23개를 공식 URL로 보정했다. Chrome 메모리 도구가 없으면 중단하며 설정을 자동 변경하지 않는다. Firecrawl 신규 index 3개는 대표 스킬의 reference.md 보조 자료로만 내장해 활성 스킬을 추가하지 않았다. Anthropic command 변환 2개는 한국어 요약을 보존하고 고정 원문 참조·Codex 도구 해석만 추가했다. 원본과 다른 패키지는 JSON의 adapted와 adaptation_count로 구분하며 전체 파일 해시를 제공한다.

Qodo 2개는 새 배포 2.1.8의 CLI/API 호환성을 확인하지 못해 원본 번들 0.6.1 기반 설치본을 유지한다. 새 CLI·MCP·인증은 설치하지 않았다. OpenAI 관리형 스킬은 제공 버전과 설치 실물을 확인하고 공식 버전 선택·업데이트 경로를 확보하지 못한 항목을 보류했다. 관리 캐시를 직접 수정하지 않았다. Browser·Chrome 관리 플러그인은 원본 리소스가 있으나 설치 캐시에 스킬 파일이 없어 임의 복구하지 않았다.

| 구분 | 수량 | 의미 |
|---|---:|---|
| Codex 전역. | 102 | 갱신 후 활성 SKILL.md 패키지. |
| 별도 사용자·내장. | 6 | migrate-to-codex 1개와 내장 5개. |
| 출처 관리 대상 플러그인. | 24 | 현재 앱에 노출된 자료·등록·설치 실물을 포함한 기존 조사 범위. |
| 출처 관리 설치본 합계. | 132 | 모든 항목이 새 CLI에서 노출된다는 뜻은 아니다. |
| 실제 사용자 새 CLI 발견. | 122 | 전역 102 + 별도·내장 6 + 플러그인 14. 홈·저장소 두 경로에서 오류 0개. |

pages 4개·plugin-management 1개·sites 2개·work-pets 3개는 등록상 installed/enabled이나 이번 새 CLI 조회에는 반환되지 않았다. 비활성이라고 단정하지 않는다. OpenAI templates 캐시 20개도 활성 수에 추가하지 않았다. Presentations·Spreadsheets의 실제 선언 대소문자는 호스트에 따라 표기 차이가 있다. 기존 설명 카탈로그 99개는 Claude 기준 이력이므로 Codex 설치 102개와 합산하지 않는다.

## 검증과 남은 범위.

271개 작업 결과·전체 준비 파일 해시와 비대상 563개 파일, 그중 Claude 52개 및 보호 설정 5개 해시 보존을 확인했다. Python 스크립트 42개 AST 검사가 통과했다. 안전 배치 도구의 충돌·경로 이탈·실제 Windows junction 거부·실패 복구 테스트 14개가 통과했다. 독립 리뷰에서 검토 범위 안의 차단 결함을 발견하지 못했다. 파일 바이트 복구는 프로세스 중단·동시 작성자 상황을 보장하지 않는다.

실제 외부 로그인·업로드·GPU·Unity Editor·새 모델 호출과 Bash 구문 검사는 수행하지 않았다. 새 조회의 발견·전체 파일 읽기는 외부 서비스 실동작 성공과 구분한다. 열린 Codex 대화는 이전 스킬 목록을 유지할 수 있으므로 새 세션에서 사용한다. 저장소 회귀와 최종 문서 검증은 [검증 기록](../docs/reviews/2026-11-06-codex-skills-update.md)을 따른다.

## 설치본별 버전과 고정 원본.

본문 SHA-256은 UTF-8 BOM·CRLF/LF·문서 양끝 공백을 정규화한 본문의 앞 16자이며 Git 커밋이나 전체 패키지 해시가 아니다. 개별 선언·원본 번들·실제 런타임 버전은 구분한다. 전체 패키지 파일 해시는 JSON을 따른다.

| 구분·설치 이름 | 설치 버전·원본 번들 | 본문 SHA-256 앞 16자 | 처리 | 고정 원본 |
|---|---|---|---|---|
| `global / a11y-debugging` | 스킬 독립 버전 미표기 · 원본 번들 1.12.0 | `5859d6c8e586d59e` | 갱신 | [원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/af2834411a564d366f9cab63efb046d9084f4dba/skills/a11y-debugging/SKILL.md) |
| `global / agent-development` | 0.1.0 (자체 선언) · 원본 번들 0.1.1 | `975cfc640270450b` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/skills/agent-development/SKILL.md) |
| `global / brainstorming` | `7.0.2` (설치 기록) | `110366dea1e3b09c` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) |
| `global / cancel-ralph` | 미표기 | `a269519cee9a596b` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/cancel-ralph/SKILL.md) |
| `global / chrome-devtools` | 스킬 독립 버전 미표기 · 원본 번들 1.12.0 | `a7f8dd47cccface6` | 갱신 | [원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/af2834411a564d366f9cab63efb046d9084f4dba/skills/chrome-devtools/SKILL.md) |
| `global / chrome-devtools-cli` | 스킬 독립 버전 미표기 · 원본 번들 1.12.0 | `54c11e2cb97b1343` | 갱신 | [원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/af2834411a564d366f9cab63efb046d9084f4dba/skills/chrome-devtools-cli/SKILL.md) |
| `global / claude-api` | 미표기 | `ae3873462656201a` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/claude-api/SKILL.md) |
| `global / claude-automation-recommender` | 스킬 독립 버전 미표기 · 원본 번들 1.0.0 | `c4940198f360a863` | 갱신 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/claude-code-setup/skills/claude-automation-recommender/SKILL.md) |
| `global / claude-md-improver` | 스킬 독립 버전 미표기 · 원본 번들 1.0.0 | `092974387c61fe7a` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/claude-md-management/skills/claude-md-improver/SKILL.md) |
| `global / claude-news` | 미표기 | `2d6d5d7948f7eea4` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/claude-news/SKILL.md) |
| `global / code-review` | 미표기 | `2225497dee1fe08d` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/code-review/SKILL.md) |
| `global / command-development` | 0.2.0 (자체 선언) · 원본 번들 0.1.1 | `24632f1e6a5f8a13` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/skills/command-development/SKILL.md) |
| `global / create-plugin` | 스킬 독립 버전 미표기 · 원본 번들 0.1.1 | `e4799894004b39df` | 갱신 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/commands/create-plugin.md) |
| `global / daily-work-report` | 미표기 | `a5a41820edb6b0e6` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/daily-work-report/SKILL.md) |
| `global / debug-optimize-lcp` | 스킬 독립 버전 미표기 · 원본 번들 1.12.0 | `ea6ab73b3ba725a3` | 갱신 | [원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/af2834411a564d366f9cab63efb046d9084f4dba/skills/debug-optimize-lcp/SKILL.md) |
| `global / deep-research` | 미표기 | `6e624e50ca058639` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/deep-research/SKILL.md) |
| `global / delete-session` | 미표기 | `d5dc5eaf446ae6bf` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/delete-session/SKILL.md) |
| `global / design-driven-delivery` | 미표기 | `31b194cab1ba21ca` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/design-driven-delivery/SKILL.md) |
| `global / diagnosing-superpowers` | `7.0.2` (설치 기록) | `0cd431d0ccd58724` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md) |
| `global / dispatching-parallel-agents` | `7.0.2` (설치 기록) | `eed8724a63a6c70a` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) |
| `global / executing-plans` | `7.0.2` (설치 기록) | `9a5c6d1ca75b4d04` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) |
| `global / feature-dev` | 미표기 | `f3e117f57b459ce3` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/feature-dev/SKILL.md) |
| `global / fewer-permission-prompts` | 미표기 | `76947c13d1fef5b3` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/fewer-permission-prompts/SKILL.md) |
| `global / figma-code-connect` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `5ab449c54441abbf` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-code-connect/SKILL.md) |
| `global / figma-create-new-file` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `8b2c9fe5661ef28b` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-create-new-file/SKILL.md) |
| `global / figma-generate-design` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `d2b852c3b8c66593` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-generate-design/SKILL.md) |
| `global / figma-generate-diagram` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `4f1034a818020c1f` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-generate-diagram/SKILL.md) |
| `global / figma-generate-library` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `51a31d7800af4f1d` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-generate-library/SKILL.md) |
| `global / figma-generate-project-plan` | 미표기 | `b838e032a84b30ad` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/figma-generate-project-plan/SKILL.md) |
| `global / figma-use` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `426046a535cc02f0` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-use/SKILL.md) |
| `global / figma-use-figjam` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `6c9f43a03664a613` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-use-figjam/SKILL.md) |
| `global / figma-use-slides` | 스킬 독립 버전 미표기 · 원본 번들 2.2.157 | `a7027ece70c19aa2` | 갱신 | [원본](https://github.com/figma/mcp-server-guide/blob/f2789420e7e8b4e2465dfeb1e12e1fc6a31397e5/skills/figma-use-slides/SKILL.md) |
| `global / finishing-a-development-branch` | `7.0.2` (설치 기록) | `5e9c5f4b069243d8` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) |
| `global / firecrawl-agent` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `5aa156c84e43484c` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-agent/SKILL.md) |
| `global / firecrawl` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `47a357533bee037f` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl/SKILL.md) |
| `global / firecrawl-crawl` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `6a81ec2446b27955` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-crawl/SKILL.md) |
| `global / firecrawl-download` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `ba2c7de0d72d9114` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-download/SKILL.md) |
| `global / firecrawl-interact` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `5f4cefd723a60405` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-interact/SKILL.md) |
| `global / firecrawl-map` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `7cf61c76c9532091` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-map/SKILL.md) |
| `global / firecrawl-monitor` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `22438432e8d67fe2` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-monitor/SKILL.md) |
| `global / firecrawl-parse` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `1a8ce8f1d8b2709e` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-parse/SKILL.md) |
| `global / firecrawl-scrape` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `a6a4203d24a3d6e2` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-scrape/SKILL.md) |
| `global / firecrawl-search` | 스킬 버전 미표기 · 고정 CLI 저장소 snapshot da25d5cd06db | `d33adfbfbfef411e` | 갱신 | [원본](https://github.com/firecrawl/cli/blob/da25d5cd06db21cb33b100661cea0d9b89d457a3/skills/firecrawl-search/SKILL.md) |
| `global / frontend-design` | 스킬 독립 버전 미표기 · 원본 번들 1.1.1 | `c3d0d3ea592ad4f0` | 갱신 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/frontend-design/skills/frontend-design/SKILL.md) |
| `global / handover` | 미표기 | `85c2470a60084b4b` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/handover/SKILL.md) |
| `global / help` | 미표기 | `f400633b286f6682` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/help/SKILL.md) |
| `global / hf-cli` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `34279ba64a7573ad` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/hf-cli/SKILL.md) |
| `global / hook-development` | 0.1.0 (자체 선언) · 원본 번들 0.1.1 | `0d3372949fa2ba96` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/skills/hook-development/SKILL.md) |
| `global / huggingface-best` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `1196acb1d67326ed` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-best/SKILL.md) |
| `global / huggingface-community-evals` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `3c622c4b50ea9b56` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-community-evals/SKILL.md) |
| `global / huggingface-datasets` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `f3e50f24c778390c` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-datasets/SKILL.md) |
| `global / huggingface-gradio` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `037e16340be15eaa` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-gradio/SKILL.md) |
| `global / huggingface-llm-trainer` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `fd62fecb15011a6f` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-llm-trainer/SKILL.md) |
| `global / huggingface-local-models` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `14279c5c460b4adb` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-local-models/SKILL.md) |
| `global / huggingface-lora-space-builder` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `477198dc0cb4b065` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-lora-space-builder/SKILL.md) |
| `global / huggingface-paper-publisher` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `a22e00c2e57c22e3` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-paper-publisher/SKILL.md) |
| `global / huggingface-papers` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `985c2d5c7261aba2` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-papers/SKILL.md) |
| `global / huggingface-spaces` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `bff5535aab436102` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-spaces/SKILL.md) |
| `global / huggingface-tool-builder` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `62eff86a37ea47cd` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-tool-builder/SKILL.md) |
| `global / huggingface-trackio` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `a0d2aebc2f390907` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-trackio/SKILL.md) |
| `global / huggingface-vision-trainer` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `b49acd79b48be406` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-vision-trainer/SKILL.md) |
| `global / huggingface-zerogpu` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `c4c3e551bf20e215` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/huggingface-zerogpu/SKILL.md) |
| `global / init` | 미표기 | `0e46677f993fafd4` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/init/SKILL.md) |
| `global / keybindings-help` | 미표기 | `a8d63d5f43204fb4` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/keybindings-help/SKILL.md) |
| `global / loop` | 미표기 | `4020dfb94bf8f5eb` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/loop/SKILL.md) |
| `global / mcp-integration` | 0.1.0 (자체 선언) · 원본 번들 0.1.1 | `388667714063fbda` | 갱신 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/skills/mcp-integration/SKILL.md) |
| `global / memory-leak-debugging` | 스킬 독립 버전 미표기 · 원본 번들 1.12.0 | `bafec5c3e993644d` | 갱신 | [원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/af2834411a564d366f9cab63efb046d9084f4dba/skills/memory-leak-debugging/SKILL.md) |
| `global / new-sdk-app` | 미표기 | `e7577063e95d72ca` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/new-sdk-app/SKILL.md) |
| `global / playground` | 스킬 독립 버전 미표기 · 원본 번들 미표기 | `e5d89cbbdd77be9b` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/playground/skills/playground/SKILL.md) |
| `global / plugin-settings` | 0.1.0 (자체 선언) · 원본 번들 0.1.1 | `0ebfa63d6704901c` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/skills/plugin-settings/SKILL.md) |
| `global / plugin-structure` | 0.1.0 (자체 선언) · 원본 번들 0.1.1 | `4333b3e6fd1824d6` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/skills/plugin-structure/SKILL.md) |
| `global / qodo-get-rules` | 미표기 · 원본 번들 `0.6.1` | `271f4582e8313cec` | 호환성 보류 | [원본](https://github.com/qodo-ai/qodo-skills/blob/8aec13d6ac60feb9d9f84f36aa1753234de17dc8/skills/qodo-get-rules/SKILL.md) |
| `global / qodo-pr-resolver` | 미표기 · 원본 번들 `0.6.1` | `b7119f08acbb2fd0` | 호환성 보류 | [원본](https://github.com/qodo-ai/qodo-skills/blob/8aec13d6ac60feb9d9f84f36aa1753234de17dc8/skills/qodo-pr-resolver/SKILL.md) |
| `global / ralph-loop` | 미표기 | `c07777b00aad2da9` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/ralph-loop/SKILL.md) |
| `global / receiving-code-review` | `7.0.2` (설치 기록) | `4fb08b86f10c892e` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) |
| `global / requesting-code-review` | `7.0.2` (설치 기록) | `1a235acf066f4ee3` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) |
| `global / review` | 미표기 | `b20efe013cac32a0` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/review/SKILL.md) |
| `global / review-pr` | 미표기 | `ac51472a4513d68b` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/review-pr/SKILL.md) |
| `global / revise-claude-md` | 스킬 독립 버전 미표기 · 원본 번들 1.0.0 | `2aa485a05c1c06db` | 갱신 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/claude-md-management/commands/revise-claude-md.md) |
| `global / run` | 미표기 | `635a66bf4dd5cbef` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/run/SKILL.md) |
| `global / schedule` | 미표기 | `f54df3cdca4eb898` | 유지 | 공개 실행 원본 미확인. |
| `global / security-review` | 미표기 | `1e3bb2280ae5e7c4` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/security-review/SKILL.md) |
| `global / simplify` | 미표기 | `115b7fa5fa5983c1` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/simplify/SKILL.md) |
| `global / skill-creator` | 스킬 독립 버전 미표기 · 원본 번들 미표기 | `c08c99c48c173627` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/skill-creator/skills/skill-creator/SKILL.md) |
| `global / skill-development` | 0.1.0 (자체 선언) · 원본 번들 0.1.1 | `48917e494d7aebcf` | 동일 원본 유지 | [원본](https://github.com/anthropics/claude-plugins-public/blob/a1ecfbc7f138a0ef455088f7f28cda2d22a0f853/plugins/plugin-dev/skills/skill-development/SKILL.md) |
| `global / source-command-delete-session` | 미표기 | `c4d0ba15bb67f7d0` | 유지 | 공개 실행 원본 미확인. |
| `global / source-command-handover` | 미표기 | `a5db2db5469d4f9e` | 유지 | 공개 실행 원본 미확인. |
| `global / subagent-driven-development` | `7.0.2` (설치 기록) | `df2bcd230bde6cf5` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) |
| `global / systematic-debugging` | `7.0.2` (설치 기록) | `a9a79740379b1d42` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) |
| `global / test-driven-development` | `7.0.2` (설치 기록) | `89b7bbc7a3ef3a50` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md) |
| `global / train-sentence-transformers` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `a37590f8cc36c185` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/train-sentence-transformers/SKILL.md) |
| `global / transformers-js` | 4.x (metadata 선언) · 원본 번들 1.0.35 | `8c3b1a1bd8bbf502` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/transformers-js/SKILL.md) |
| `global / trl-training` | 스킬 독립 버전 미표기 · 원본 번들 1.0.35 | `5223755ff3a12cb7` | 갱신 | [원본](https://github.com/huggingface/skills/blob/c3ff942be3e07116b475253f0a8fc4f54682c1a8/skills/trl-training/SKILL.md) |
| `global / troubleshooting` | 스킬 독립 버전 미표기 · 원본 번들 1.12.0 | `7680492483939bf1` | 갱신 | [원본](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/af2834411a564d366f9cab63efb046d9084f4dba/skills/troubleshooting/SKILL.md) |
| `global / unity-cli` | 스킬 독립 버전 미표기 · 원본 번들 미표기 | `143c3d95072cd9d8` | 갱신 | [원본](https://github.com/Unity-Technologies/skills/blob/ba28c24fc7e569fa0fd5b6bf16ab2bb0acef0594/skills/unity-cli/SKILL.md) |
| `global / update-config` | 미표기 | `0e435cd4c2a13b90` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/update-config/SKILL.md) |
| `global / using-git-worktrees` | `7.0.2` (설치 기록) | `d27655775d8f9b40` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) |
| `global / using-superpowers` | `7.0.2` (설치 기록) | `2404d2e763fad2ac` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) |
| `global / verification-before-completion` | `7.0.2` (설치 기록) | `07e72bb5e99c67b5` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) |
| `global / verify` | 미표기 | `bb62353f849691d5` | 유지 | [원본](https://github.com/nowJDev/Agent-Instructions/blob/ca45d94f09291096ee66cead06c5a540b2164a51/Owned-Skills/verify/SKILL.md) |
| `global / writing-plans` | `7.0.2` (설치 기록) | `12110e45d07ecc42` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md) |
| `global / writing-skills` | `7.0.2` (설치 기록) | `67222569684b34ee` | 유지 | [원본](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) |
| `codex-local / migrate-to-codex` | 미표기 | `a60f3e9adac1dc0c` | 유지 | [원본](https://github.com/openai/skills/blob/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/migrate-to-codex/SKILL.md) |
| `system / imagegen` | 미표기 | `976a0163c2cff076` | 유지 | [원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/imagegen/SKILL.md) |
| `system / openai-docs` | 미표기 | `dd4e1e262e07cf0d` | 유지 | [원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/openai-docs/SKILL.md) |
| `system / skill-creator` | 미표기 | `a2fa8da9ce13d832` | 유지 | [원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md) |
| `system / skill-installer` | 미표기 | `98494ab86339217c` | 유지 | [원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/skill-installer/SKILL.md) |
| `system / review-agent` | 미표기 | `14a3e54e79741c77` | 유지 | [원본](https://github.com/openai/codex/blob/55897425e839d943a744c658701445ff732568a0/codex-rs/skills/src/assets/samples/review-agent/SKILL.md) |
| `loaded-plugin / computer-use:computer-use` | `26.1029.61003` (설치 번들) | `3afee01398880c51` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / visualize:visualize` | `1.0.74` (설치 번들) | `0d3142bd912bb6a3` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / pages:maintain-space` | `0.1.26` (설치 번들) | `d184ed1a9bf8e4f2` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / pages:manage-schedules` | `0.1.26` (설치 번들) | `4111ec989acb456e` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / pages:organize-space` | `0.1.26` (설치 번들) | `8b758e4aea230db7` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / pages:write-page` | `0.1.26` (설치 번들) | `aaee911385f5ead8` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / plugin-management:plugin-management` | `0.1.0` (설치 번들) | `651302048609e1e0` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / sites:sites` | `1.1.3` (설치 번들) | `a184aeb3f2014e40` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / sites:sites-remix` | `1.1.3` (설치 번들) | `1db46845872fac95` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / work-pets:create-pet` | `0.1.6` (설치 번들) | `b2196bf4715ad2e8` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / work-pets:pets` | `0.1.6` (설치 번들) | `6eff15058cbaa1b2` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / work-pets:update-pet` | `0.1.6` (설치 번들) | `9a85794de784ba49` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / documents:documents` | `26.1104.11149` (설치 번들) | `93d8393595f50e87` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / pdf:pdf` | `26.1104.11149` (설치 번들) | `b075edf46e34dad7` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / presentations:presentations` | `26.1104.11149` (설치 번들) | `52f435233ce9d832` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / spreadsheets:excel-live-control` | `26.1104.11149` (설치 번들) | `bac2c56dece96b71` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / spreadsheets:spreadsheets` | `26.1104.11149` (설치 번들) | `6a88a48af0bfdbfc` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / template-creator:template-creator` | `26.1104.11149` (설치 번들) | `ca7a9303d7079c59` | 관리형 제공 버전 유지 | 공개 실행 원본 미확인. |
| `loaded-plugin / ponytail:ponytail` | `5.3.3` (설치 번들) | `54ba3851a4ea7100` | 유지 | [원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail/SKILL.md) |
| `loaded-plugin / ponytail:ponytail-audit` | `5.3.3` (설치 번들) | `10eaedd92a34194d` | 유지 | [원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-audit/SKILL.md) |
| `loaded-plugin / ponytail:ponytail-debt` | `5.3.3` (설치 번들) | `688de7b5be11e7a8` | 유지 | [원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-debt/SKILL.md) |
| `loaded-plugin / ponytail:ponytail-gain` | `5.3.3` (설치 번들) | `5f5cfdfba6750244` | 유지 | [원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-gain/SKILL.md) |
| `loaded-plugin / ponytail:ponytail-help` | `5.3.3` (설치 번들) | `f68337ee993f626e` | 유지 | [원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-help/SKILL.md) |
| `loaded-plugin / ponytail:ponytail-review` | `5.3.3` (설치 번들) | `125036d590f6de8f` | 유지 | [원본](https://github.com/DietrichGebert/ponytail/blob/v5.3.3/skills/ponytail-review/SKILL.md) |
