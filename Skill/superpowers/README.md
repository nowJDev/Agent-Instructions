<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# superpowers 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. ON/OFF·캐시 표시는 작성 당시 Claude Code 환경의 기록이며 현재 클라이언트의 설치·노출·인증 상태와 구분한다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [brainstorming](#brainstorming).
- [diagnosing-superpowers](#diagnosing-superpowers).
- [dispatching-parallel-agents](#dispatching-parallel-agents).
- [executing-plans](#executing-plans).
- [finishing-a-development-branch](#finishing-a-development-branch).
- [receiving-code-review](#receiving-code-review).
- [requesting-code-review](#requesting-code-review).
- [subagent-driven-development](#subagent-driven-development).
- [systematic-debugging](#systematic-debugging).
- [test-driven-development](#test-driven-development).
- [using-git-worktrees](#using-git-worktrees).
- [using-superpowers](#using-superpowers).
- [verification-before-completion](#verification-before-completion).
- [writing-plans](#writing-plans).
- [writing-skills](#writing-skills).

## brainstorming

> 새 작업의 목적·범위와 접근법을 확인하고, 규모에 맞는 승인 설계로 정리하는 대화형 스킬.

<a id="brainstorming---용도"></a>
### 📌 용도

소프트웨어와 비소프트웨어 창작 작업에서 사용자가 원하는 결과와 이유를 파악한다. 이미 결정된 내용을 다시 묻지 않고 기존 프로젝트를 먼저 조사하며, 작은 변경은 짧은 설계로, 프로젝트는 전체 설계로 정리한다.

<a id="brainstorming---트리거-조건"></a>
### 🎯 트리거 조건

새 기능·컴포넌트·동작 변경이나 새로운 계획을 시작할 때 사용한다. 요청만으로 필요한 정보가 모두 명확한 작은 작업은 바로 처리할 수 있다.

<a id="brainstorming---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 기존 자료·연결된 코드·이전 결정을 확인한 뒤 결과를 바꾸는 질문을 한 번에 하나씩 한다.
2. 실제 가능한 접근법과 장단점을 설명하고 선택을 정리한다. 선택권을 위임받았다면 판단과 이유를 명시한다.
3. 짧은 설계 또는 전체 설계를 작성한다. 소프트웨어 기본 경로는 `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`이며 사용자 지정 구조를 우선한다.
4. 프로젝트 규모라면 `builder-check-prompt.md`로 구현자 관점의 검토를 거친다. 설계 승인 후 `writing-plans`로 넘긴다.

<a id="brainstorming---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- Visual Companion은 시각 자료가 필요한 시점에 단독 메시지로 제안하고, 수락하면 `visual-companion.md`를 읽는다.
- 사용자가 질문 생략을 명시하거나 일회성 실험을 승인한 경우의 예외가 있다. 실험 결과를 실제 제품으로 유지하려면 다시 설계를 확인한다.
- 사용자 지침과 `design-driven-delivery`의 승인·범위 규칙을 함께 적용한다.

<a id="brainstorming---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 brainstorming](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## diagnosing-superpowers

> Superpowers 세션의 반복 작업·계획 이탈·비용·실패를 대화 기록의 파일·줄 근거로 보고하는 스킬.

<a id="diagnosing-superpowers---용도"></a>
### 📌 용도

현재 또는 지정한 과거 세션에서 무엇을 기대했고 실제 무엇이 일어났는지 확인한다. 세션 증거를 보고하며, 스킬 결함 확정이나 수정 제안은 유지보수자의 판단으로 남긴다.

<a id="diagnosing-superpowers---트리거-조건"></a>
### 🎯 트리거 조건

사용자가 세션이 오래 걸린 이유, 반복 작업, 스킬 미작동, 결과 품질이나 버그 보고 자료를 조사해 달라고 할 때 사용한다.

<a id="diagnosing-superpowers---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 세션·구간·기대한 결과·관찰한 문제를 확인한 뒤 `references/session-discovery.md`로 기록을 찾는다.
2. `templates/case.md`에 출처를 정리하고 스킬 타임라인·계획 준수·반복 작업·문제·품질·요청 충돌·비용과 시간의 일곱 관점을 조사한다.
3. 모든 발견에 `path:line`을 붙이고 `templates/report.md`의 순서로 보고한다. 근거 없는 수치는 쓰지 않는다.
4. 조건이 맞으면 기존 GitHub 이슈를 찾는다. 게시할 정확한 내용을 보여 주고 승인받은 뒤에만 이슈를 생성한다.

<a id="diagnosing-superpowers---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 세션 원본은 수정·이동·삭제하지 않는다. 작업 자료는 `~/.superpowers/diagnosing-superpowers/<session-id>/`에 보관한다.
- 세션을 읽을 때 `references/context-safety.md`를 따른다. 번들 내보내기는 별도 요청이 있을 때만 하며 민감정보 제거·감사를 거친다.
- 압축 전 파일 목록과 제거 로그를 보여 주고 승인받는다. 공유 전에는 사용자가 파일을 직접 검토해야 한다.

<a id="diagnosing-superpowers---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 diagnosing-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## dispatching-parallel-agents

> 공유 상태와 순차 의존성이 없는 독립 작업을 각각의 에이전트에게 병렬 위임하는 스킬.

<a id="dispatching-parallel-agents---용도"></a>
### 📌 용도

서로 다른 문제 영역의 조사와 수정을 분리해 수행한다. 각 에이전트에게 필요한 자료·목표·제약만 제공하고 결과를 통합할 때 충돌과 전체 동작을 검증한다.

<a id="dispatching-parallel-agents---트리거-조건"></a>
### 🎯 트리거 조건

독립적인 작업이 둘 이상이며 같은 파일·자원을 변경하지 않고 진행할 수 있을 때 사용한다. 서로 관련된 실패나 전체 상태를 알아야 하는 탐색에는 먼저 공통 원인을 조사한다.

<a id="dispatching-parallel-agents---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 문제를 근본 원인이나 서브시스템별로 나누고 독립성을 확인한다.
2. 각 태스크에 정확한 범위·목표·변경 제약·반환할 요약을 명시한다.
3. 플랫폼의 실제 병렬 도구로 위임하고 세션 전체 기록 대신 필요한 컨텍스트만 전달한다.
4. 결과를 검토하고 파일 충돌을 확인한 뒤 전체 테스트와 필요한 확인을 수행한다.

<a id="dispatching-parallel-agents---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 단순히 타임아웃을 늘려 실패를 가리지 않고 원인을 확인한다.
- 공유 상태가 있거나 에이전트가 서로의 작업을 덮어쓸 수 있으면 순차 실행한다.

<a id="dispatching-parallel-agents---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 dispatching-parallel-agents](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## executing-plans

> 현재 세션에서 계획을 직접 구현하고 진행 원장과 태스크별 검증·최종 브랜치 리뷰를 유지하는 스킬.

<a id="executing-plans---용도"></a>
### 📌 용도

사용자가 인라인 실행을 선택했거나 서브에이전트 도구가 없을 때 계획을 직접 수행한다. 태스크마다 구현자·리뷰어를 새로 띄우지 않고 진행 원장으로 재개 지점을 남기며 마지막에 전체 변경을 검토한다.

<a id="executing-plans---트리거-조건"></a>
### 🎯 트리거 조건

승인된 구현 계획을 같은 세션에서 직접 실행할 때 사용한다. 태스크마다 독립 리뷰를 원하면 `subagent-driven-development`를 선택한다.

<a id="executing-plans---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. `using-git-worktrees`로 격리를 확인하고 계획·스펙·공통 제약을 읽는다. `test-driven-development`를 로드한다.
2. `subagent-driven-development/scripts/sdd-workspace`로 계획별 `.superpowers/sdd/<plan-basename>/`을 만들고 `progress.md`를 확인한다.
3. `scripts/task-start`가 만든 brief를 읽고 단계별 기대 출력과 실제 결과를 대조한다. `scripts/task-done`은 테스트가 통과했을 때만 완료를 기록한다.
4. 전체 브랜치 리뷰를 새 리뷰어에게 맡긴다. 도구가 없으면 별도 셀프리뷰를 수행하고 한계를 명시한다.
5. 중요 발견은 한 차례 수정 과정에서 RED→GREEN과 전체 테스트로 검증한다. 판단·보류 항목을 보고한 뒤 `finishing-a-development-branch`로 넘긴다.

<a id="executing-plans---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 계획 충돌과 판단은 근거·잘못됐을 때의 비용을 포함한 `Ruling:`으로 원장에 기록한다. 파괴적 작업·보안·외부 영향 등은 사용자 권한을 따른다.
- Bash 스크립트는 설치된 실제 경로에서 실행하며 다른 계획의 작업 자료를 읽거나 정리하지 않는다.
- 새 세션이나 압축 후에는 기억 대신 원장과 Git 이력으로 이어간다.

<a id="executing-plans---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 executing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## finishing-a-development-branch

> 전체 테스트를 확인한 뒤 병합·PR·유지 중 승인된 통합을 수행하고 소유한 작업 공간을 정리하는 스킬.

<a id="finishing-a-development-branch---용도"></a>
### 📌 용도

구현을 끝낼 때 전체 테스트와 Git 환경을 확인하고 사용자가 정한 방식으로 반영한다. 병합 결과 검증과 임시 작업 공간의 안전한 정리를 연결한다.

<a id="finishing-a-development-branch---트리거-조건"></a>
### 🎯 트리거 조건

구현이 끝나고 프로젝트 전체 테스트가 통과한 뒤 사용한다. 테스트가 실패하면 먼저 실패를 보고하고 해결한다.

<a id="finishing-a-development-branch---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 전체 테스트를 실행하고 일반 저장소·연결 worktree·detached HEAD를 구분한다.
2. 실제로 분기한 기준 브랜치를 확인한다. 일반 브랜치는 로컬 병합·푸시 후 PR·유지의 세 가지, detached HEAD는 새 브랜치 푸시 후 PR·유지의 두 가지를 제시한다.
3. 사용자가 이미 승인한 통합 범위를 따르고, 병합 결과에서도 테스트를 확인한다.
4. 병합 또는 명시적으로 요청·확인된 폐기 때에만 자신이 만든 `.worktrees/`·`worktrees/`를 바깥 디렉터리에서 정리한다. PR과 유지에서는 보존한다.

<a id="finishing-a-development-branch---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 폐기는 기본 메뉴에서 제안하지 않는다. 사용자가 명시적으로 요청하면 대상·커밋·경로를 보여 주고 `discard` 확인을 받는다.
- worktree 제거가 미커밋·미추적 파일 때문에 거부되면 강제 제거하지 않고 보존·이동·삭제의 구체적 선택을 확인한다.
- 호스트가 관리하는 작업 공간은 남겨 두고 플랫폼의 종료 도구를 따른다.

<a id="finishing-a-development-branch---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 finishing-a-development-branch](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## receiving-code-review

> 리뷰 피드백을 코드·요구사항·검증 근거와 대조한 뒤 항목별로 반영하거나 기술적으로 반박하는 스킬.

<a id="receiving-code-review---용도"></a>
### 📌 용도

피드백을 맹목적으로 적용하지 않고 현재 코드베이스에 맞는지 확인한다. 실제 사용 여부와 기존 동작·호환성·설계 결정을 검토해 필요한 변경만 수행한다.

<a id="receiving-code-review---트리거-조건"></a>
### 🎯 트리거 조건

코드 리뷰 피드백을 받고 제안 구현에 착수하기 전에 사용한다. 불명확하거나 의심스러운 제안일수록 먼저 확인한다.

<a id="receiving-code-review---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 피드백 전체를 읽고 요구사항을 재진술하거나 질문한다.
2. 실제 호출자·기존 구현 이유·플랫폼 요구와 대조한다.
3. 불명확한 항목을 먼저 해소한 뒤 차단 문제·단순 수정·복잡 수정 순으로 처리한다.
4. 한 항목씩 검증하고 전체 회귀를 확인한다. 잘못된 제안에는 코드·테스트 근거로 답한다.

<a id="receiving-code-review---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 형식적인 칭찬·동의보다 확인한 사실과 변경 내용을 말한다.
- 사용자의 이전 결정과 충돌하면 먼저 논의한다. GitHub 인라인 피드백은 해당 스레드에 답하되 실제 게시 권한을 확인한다.

<a id="receiving-code-review---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 receiving-code-review](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## requesting-code-review

> 정확한 변경 범위와 요구사항을 전달해 작업 산출물의 독립 코드 리뷰를 요청하는 스킬.

<a id="requesting-code-review---용도"></a>
### 📌 용도

문제가 누적되기 전에 리뷰어가 요구사항과 실제 변경을 대조하도록 한다. 세션 전체 이력 대신 필요한 요약·스펙 또는 계획·시작과 종료 커밋을 제공한다.

<a id="requesting-code-review---트리거-조건"></a>
### 🎯 트리거 조건

서브에이전트 방식의 태스크 완료, 주요 기능 완료와 병합 전에 사용한다. 복잡한 수정 후나 진행이 막힌 상황에서도 활용할 수 있다.

<a id="requesting-code-review---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 리뷰 대상의 시작·종료 SHA와 실제 요구사항을 확보한다.
2. `code-reviewer.md` 템플릿에 변경 요약·요구사항·커밋 범위를 채워 리뷰어에게 전달한다.
3. Critical은 즉시, Important는 다음 진행 전에 해결하고 Minor는 기록한다.
4. 기술적으로 틀린 발견은 근거로 검증해 반박한다. 최종 통합은 승인된 범위를 따른다.

<a id="requesting-code-review---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 여러 커밋으로 이뤄진 태스크는 기록한 시작 SHA를 사용해 변경 범위가 누락되지 않게 한다.
- `subagent-driven-development`의 태스크 리뷰와 전체 브랜치 리뷰에는 해당 스킬의 패키지·재리뷰 절차를 함께 따른다.

<a id="requesting-code-review---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 requesting-code-review](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## subagent-driven-development

> 태스크마다 새 구현자와 스펙·품질을 함께 보는 리뷰어를 배치하고 최종 전체 브랜치 리뷰를 수행하는 스킬.

<a id="subagent-driven-development---용도"></a>
### 📌 용도

같은 세션에서 계획을 조율하되 구현·태스크 리뷰는 격리된 컨텍스트로 위임한다. 계획별 원장과 파일 형태의 brief·보고서·리뷰 패키지를 남겨 반복 작업과 컨텍스트 손실을 줄인다.

<a id="subagent-driven-development---트리거-조건"></a>
### 🎯 트리거 조건

승인 계획의 태스크가 대체로 독립적이고 태스크별 독립 리뷰가 필요할 때 사용한다. 인라인 실행을 선택했거나 위임 도구가 없으면 `executing-plans`를 사용한다.

<a id="subagent-driven-development---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 격리 환경·스펙·계획을 확인하고 `scripts/sdd-workspace`가 정한 `.superpowers/sdd/<plan-basename>/progress.md`에서 재개한다.
2. `scripts/task-brief`로 정확한 요구사항을 추출하고 `implementer-prompt.md`와 함께 구현자에게 파일 경로로 전달한다.
3. 기록한 BASE부터 HEAD까지 `scripts/review-package`로 묶고 `task-reviewer-prompt.md`로 스펙 준수와 태스크 품질의 두 판정을 받는다.
4. 문제가 있으면 `references/fix-loop.md`를 매번 읽고 최대 다섯 차례의 수정·범위 제한 재리뷰를 수행한다. 판단과 보류 항목을 원장에 남긴다.
5. 전체 태스크 뒤 `references/final-review.md`에 따라 전체 브랜치를 검토하고 판단·보류 사항을 보고한 뒤 종료 스킬로 넘긴다.

<a id="subagent-driven-development---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 구현자를 병렬로 여러 명 실행하지 않는다. 구현자는 추가 서브에이전트를 만들지 않고 리뷰는 조율자가 맡긴다.
- 구 템플릿 두 개 대신 `task-reviewer-prompt.md`를 사용하며 재리뷰는 `re-review-prompt.md`를 따른다.
- 계획별 작업 자료는 Git 무시 대상이다. 정리 전 복구·보고 정보를 보존하고 다른 계획 자료는 남겨 둔다.

<a id="subagent-driven-development---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 subagent-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## systematic-debugging

> 수정안을 내기 전에 재현·증거·패턴 비교로 근본 원인을 찾는 네 단계 디버깅 스킬.

<a id="systematic-debugging---용도"></a>
### 📌 용도

증상만 바꾸는 추측성 수정을 줄이고 원인이 확인된 한 곳을 고친다. 근본 원인 조사, 패턴 분석, 가설 검증, 구현의 순서를 지킨다.

<a id="systematic-debugging---트리거-조건"></a>
### 🎯 트리거 조건

버그·테스트 실패·빌드 실패·성능·통합 문제와 예상 밖 동작이 발생했을 때 수정 제안 전에 사용한다.

<a id="systematic-debugging---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 에러와 스택을 끝까지 읽고 재현·최근 변경·컴포넌트 경계의 입출력과 설정 전달을 조사한다.
2. 작동하는 예제와 참조 구현을 비교해 차이·의존성·가정을 나열한다.
3. 단일 가설을 한 번에 하나의 최소 변경으로 검증한다.
4. 재현하는 실패 테스트를 먼저 만들고 원인을 수정한 뒤 대상·전체 검증으로 확인한다. 세 번 이상 실패하면 아키텍처와 접근을 다시 논의한다.

<a id="systematic-debugging---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- `root-cause-tracing.md`, `defense-in-depth.md`, `condition-based-waiting.md`와 `find-polluter.sh`가 보조 자료다.
- `test-driven-development`로 재현 테스트를 만들고 `verification-before-completion`으로 완료 주장을 확인한다.

<a id="systematic-debugging---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 systematic-debugging](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## test-driven-development

> 실패 테스트를 먼저 확인하고 최소 구현과 전체 회귀를 거쳐 동작을 보장하는 TDD 스킬.

<a id="test-driven-development---용도"></a>
### 📌 용도

테스트가 원하는 실패를 실제로 잡는지 먼저 확인한 뒤 코드를 작성한다. RED→GREEN→REFACTOR를 반복하며 이미 통과하는 테스트만으로 수정 효과를 판단하지 않는다.

<a id="test-driven-development---트리거-조건"></a>
### 🎯 트리거 조건

새 기능·버그 수정·리팩터링·동작 변경의 구현 전에 사용한다. 일회성 실험·생성 코드·설정 등의 예외는 사용자 지침과 명시한 범위를 따른다.

<a id="test-driven-development---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 하나의 동작을 설명하는 최소 테스트를 작성한다.
2. 기능 부재로 예상한 방식으로 실패하는지 직접 실행해 확인한다.
3. 통과시키는 최소 코드를 작성하고 대상 테스트를 다시 실행한다.
4. 프로젝트 전체 테스트를 실행한다. 기존 실패도 이름과 근거를 보고하며 성공한 상태에서만 구조를 정리한다.

<a id="test-driven-development---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 테스트 작성·변경 전 `writing-good-tests.md`를 읽고 어떤 프로덕션 변경이 테스트를 실패시키는지 설명한다.
- mock의 호출 자체보다 실제 동작을 단언하고 테스트 전용 코드는 테스트 유틸리티에 둔다.
- 기존 `testing-anti-patterns.md` 대신 `writing-good-tests.md`가 테스트 품질 참조다.

<a id="test-driven-development---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 test-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## using-git-worktrees

> 기존 격리를 확인하고 네이티브 도구를 우선해 작업 공간을 준비하는 스킬.

<a id="using-git-worktrees---용도"></a>
### 📌 용도

원래 작업의 변경을 보존하며 기능 작업을 격리한다. 이미 연결 worktree라면 재사용하고, 네이티브 생성 도구가 없을 때만 Git 명령으로 준비한다.

<a id="using-git-worktrees---트리거-조건"></a>
### 🎯 트리거 조건

격리가 필요한 기능 작업이나 구현 계획 실행 전에 사용한다. 사용자가 지정한 선호와 기존 승인을 존중하고 불필요한 중첩 worktree를 만들지 않는다.

<a id="using-git-worktrees---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. Git 디렉터리·공통 디렉터리·브랜치를 확인하고 서브모듈을 구분한다.
2. 사용자 선호를 확인하고 플랫폼의 네이티브 도구를 우선한다.
3. Git 대안에서는 명시한 경로, 기존 `.worktrees/` 또는 `worktrees/`, 기본 `.worktrees/` 순으로 선택한다. 프로젝트 내부 경로는 ignore 여부를 확인한다.
4. 프로젝트에 맞는 의존성 준비와 전체 테스트로 기준선을 확인한다. 실패를 감춘 채 진행하지 않는다.

<a id="using-git-worktrees---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 기존 글로벌 `~/.config/superpowers/worktrees/` 경로는 기본 탐색·생성 규칙에서 빠졌다.
- 권한 오류의 경우 실제 제한을 보고하고 승인된 대안을 따른다. 호스트가 관리하는 격리 상태를 우회하지 않는다.

<a id="using-git-worktrees---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 using-git-worktrees](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## using-superpowers

> 응답과 탐색 전에 관련 스킬을 확인하고 현재 플랫폼의 도구로 적용하게 하는 진입 스킬.

<a id="using-superpowers---용도"></a>
### 📌 용도

요청에 맞는 스킬을 먼저 읽고 절차를 적용하도록 한다. 프로세스 스킬로 접근을 정한 뒤 구현·분야별 스킬을 사용하며, 사용자 지침이 스킬보다 우선한다.

<a id="using-superpowers---트리거-조건"></a>
### 🎯 트리거 조건

대화 시작과 작업 수행 전에 관련 스킬을 확인할 때 사용한다. 구체적인 태스크를 받은 서브에이전트는 이 진입 절차를 건너뛴다.

<a id="using-superpowers---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 관련·요청된 스킬을 응답·질문·파일 탐색 전에 로드한다.
2. Using 안내와 함께 적용 목적을 말하고 체크리스트가 있으면 작업 항목으로 관리한다.
3. 현재 플랫폼에 맞는 `references/` 안내를 확인하고 실제 도구 목록에 맞춰 실행한다.

<a id="using-superpowers---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- Codex는 `references/codex-tools.md`, Claude Code는 `references/claude-code-tools.md`를 참조한다.
- 원본의 플랫폼 예시와 실제 도구 계약이 다르면 현재 도구를 따른다. 모델·권한·설정 변경은 별도 승인 범위이며 스킬 로드만으로 변경하지 않는다.
- 사용자·프로젝트 지침과 이미 승인된 선택을 보존한다.

<a id="using-superpowers---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 using-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## verification-before-completion

> 완료·수정·통과를 주장하기 전에 실제 검증 명령과 전체 결과를 확인하는 스킬.

<a id="verification-before-completion---용도"></a>
### 📌 용도

변경이 그럴듯해 보이는지와 실제 동작하는지를 구분한다. 완료 주장마다 이를 증명하는 최신 명령·출력·종료 코드가 있어야 한다.

<a id="verification-before-completion---트리거-조건"></a>
### 🎯 트리거 조건

완료·성공을 보고하거나 커밋·PR·다음 단계로 넘어가기 전에 사용한다.

<a id="verification-before-completion---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 주장을 증명할 명령을 고른다.
2. 전체 명령을 실행하고 출력·종료 코드·실패 수를 읽는다.
3. 결과가 주장을 뒷받침하는지 확인한다.
4. 뒷받침되면 근거와 함께 보고하고, 아니면 실제 실패·미확인 상태를 말한다.

<a id="verification-before-completion---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 린터 통과는 빌드 성공이 아니며 대상 테스트 통과는 전체 요구사항 충족과 다르다.
- 에이전트의 성공 보고도 diff·테스트·요구사항으로 독립 확인한다. 회귀 테스트는 수정 전 실패와 수정 후 통과를 확인한다.

<a id="verification-before-completion---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 verification-before-completion](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## writing-plans

> 승인 스펙을 정확한 인터페이스·테스트·검증 결과가 있는 실행 가능한 태스크로 나누는 스킬.

<a id="writing-plans---용도"></a>
### 📌 용도

구현자가 모르는 설계 결정을 남기되 테스트와 시그니처만으로 정해지는 함수 본문까지 중복 작성하지 않는다. 각 태스크는 독립적으로 검증·리뷰할 수 있는 결과를 가진다.

<a id="writing-plans---트리거-조건"></a>
### 🎯 트리거 조건

다단계 작업의 스펙·요구사항이 있고 코드를 작성하기 전에 사용한다. 독립 프로젝트가 섞이면 계획을 분리한다.

<a id="writing-plans---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 변경할 파일과 책임·태스크 경계를 정한다. 기본 저장 경로는 `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md`이며 기존 구조를 우선한다.
2. Goal·Architecture·Tech Stack·Spec과 Global Constraints·Review Focus를 적는다.
3. 태스크마다 Files와 Consumes·Produces 인터페이스, 테스트 이름·단언, 구현 시그니처·정확한 값, 검증 명령·기대 출력을 작성한다.
4. 스펙 커버리지·모호함·타입 일관성·누락 실패 조건·분량을 스스로 검토한다.
5. 계획을 사용자에게 보여 주고 검토받는다. 이미 정한 실행 방식을 유지하고, 미정이면 태스크별 서브에이전트 방식과 인라인 방식의 비용·리뷰 차이를 설명한다.

<a id="writing-plans---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- 설정·초기 구조·문서는 해당 결과를 만드는 태스크에 포함한다. 의미 없는 작업 분리는 피한다.
- 코드 단계는 정확한 시그니처와 결정값을 쓰고 본문은 필요한 알고리즘·고정 문구에 한해 포함한다. 테스트 단계는 실제 단언 코드를 제공한다.
- 공통 제약과 Review Focus는 구현·최종 리뷰에 그대로 전달한다.

<a id="writing-plans---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 writing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.

## writing-skills

> 재사용 스킬의 설명·형태·실제 준수를 기준선과 비교해 검증하는 스킬 작성 절차.

<a id="writing-skills---용도"></a>
### 📌 용도

스킬 없이 발생하는 실패를 먼저 관찰하고 그 문제를 해결하는 최소 지침을 작성한다. 스킬 본문과 탐색용 설명을 분리하며 효과를 실제 시나리오로 확인한다.

<a id="writing-skills---트리거-조건"></a>
### 🎯 트리거 조건

새 스킬을 만들거나 기존 스킬을 편집·배포 검증할 때 사용한다. 일회성 기록이나 프로젝트 한정 규칙은 해당 문서에 둔다.

<a id="writing-skills---사용-예시--호출-방법"></a>
### 💻 사용 예시 / 호출 방법

1. 스킬 없는 기준선에서 실패·합리화·누락을 확인한다.
2. 규율 위반·출력 형태·필수 요소 누락·조건별 행동 중 실패 종류에 맞는 지침 형식을 선택한다.
3. 최소 스킬을 작성하고 같은 시나리오에서 효과를 확인한 뒤 허점을 보완한다.
4. 행동 형태를 조정하는 문구는 무지침 대조군과 변형별 다섯 번 이상의 작은 실험으로 먼저 비교한다. 규율 스킬의 압박 시나리오를 대체하지는 않는다.

<a id="writing-skills---제공-내용--핵심-절차"></a>
### 🛠️ 제공 내용 / 핵심 절차

- frontmatter·설명·이름·분량은 `references/discovery.md`, 도식은 `references/flowcharts.md`를 따른다.
- 규율 지침은 `references/bulletproofing.md`, 전체 검증은 `references/testing-skills-with-subagents.md`, 공식 참고는 `references/anthropic-best-practices.md`에 있다.
- 패키지의 스크립트는 실행 비트에만 의존하지 않고 `bash`·`node` 등 해당 인터프리터로 호출한다.

<a id="writing-skills---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 원본 기준은 [Superpowers v7.0.2의 writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md)이며 MIT License를 따른다.
- 이 문서는 요약 카탈로그다. 실제 설치·활성화·새 세션 로드 여부는 [버전·설치 채널 안내](../README.md#superpowers-%EB%B2%84%EC%A0%84%EA%B3%BC-%EC%84%A4%EC%B9%98-%EC%B1%84%EB%84%90)에 따라 확인한다.
