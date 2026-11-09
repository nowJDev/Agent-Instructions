<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# ralph-loop 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. 활성 표시는 작성 당시 환경의 기록이다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [cancel-ralph](#cancel-ralph).
- [help](#help).
- [ralph-loop](#ralph-loop).

## cancel-ralph

> 활성화된 Ralph 루프의 상태 파일을 제거해 루프를 취소하는 명령어.

<a id="cancel-ralph---용도"></a>
### 📌 용도

`/cancel-ralph`은 진행 중인 Ralph 루프를 **중단**한다. Ralph 루프는 `.claude/ralph-loop.local.md` 상태 파일이 존재하는 한 Stop 훅이 세션 종료를 계속 가로채므로, 이 명령은 그 **상태 파일을 삭제**해 루프를 끝낸다. 삭제 직전에 현재 반복 번호를 읽어 "몇 번째 반복에서 취소되었는지"를 보고한다.

Ralph 루프는 기본적으로 수동으로 멈출 수 없도록(무한 실행) 설계되어 있어서, 이 명령이 사실상 유일한 정상 중단 수단이다.

<a id="cancel-ralph---트리거-조건"></a>
### 🎯 트리거 조건

- **언제 호출되는가**
  - 사용자가 `/cancel-ralph`을 입력할 때
  - 활성 Ralph 루프를 더 이상 돌리고 싶지 않을 때
  - 무한 루프(완료 프로미스/최대 반복 미설정)에 빠진 루프를 멈출 때
  - 작업이 충분히 진행되어 루프를 수동 종료하고 싶을 때

- **언제 쓰지 않는가**
  - 활성 Ralph 루프가 없을 때 (실행하면 "No active Ralph loop found." 안내만 나옴)
  - 루프를 멈추지 않고 일시 정지만 원할 때 (해당 기능 없음 — 취소 후 다시 `/ralph-loop` 시작해야 함)

<a id="cancel-ralph---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어

```
/cancel-ralph
```

인자 없음. 실행 결과 두 가지:
- 상태 파일 없음 → `"No active Ralph loop found."`
- 상태 파일 있음 → 제거 후 `"Cancelled Ralph loop (was at iteration N)"` (N은 상태 파일의 `iteration:` 값)

<a id="cancel-ralph---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터

**허용 도구(allowed-tools):**
- `Bash(test -f .claude/ralph-loop.local.md:*)` — 상태 파일 존재 확인
- `Bash(rm .claude/ralph-loop.local.md)` — 상태 파일 제거
- `Read(.claude/ralph-loop.local.md)` — 반복 번호 읽기

`hide-from-slash-command-tool: true`로 설정됨.

**절차:**
1. `test -f .claude/ralph-loop.local.md && echo "EXISTS" || echo "NOT_FOUND"`로 상태 파일 존재 확인
2. `NOT_FOUND`이면 → "No active Ralph loop found." 출력
3. `EXISTS`이면 →
   - `.claude/ralph-loop.local.md`를 Read해 프론트매터의 `iteration:` 값(N) 획득
   - `rm .claude/ralph-loop.local.md`로 파일 삭제
   - "Cancelled Ralph loop (was at iteration N)" 보고

**연관 명령:** `/ralph-loop`(루프 시작), `/help`(ralph-loop 플러그인 설명).

<a id="cancel-ralph---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 플러그인: ralph-loop@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/ralph-loop/1.0.0/commands/cancel-ralph.md`

## help

> Ralph Loop 플러그인의 개념·명령어·핵심 메커니즘을 사용자에게 설명하는 도움말 명령어.

<a id="help---용도"></a>
### 📌 용도

`/help`(ralph-loop 플러그인 제공)은 Ralph Loop가 무엇이고 어떻게 동작하는지, 어떤 명령어가 있는지를 **사용자에게 설명**하는 문서형 명령어다. 별도 작업을 수행하지 않고, 다음 내용을 안내한다.

- **Ralph Loop란**: Geoffrey Huntley가 정립한 Ralph Wiggum 기법 — 같은 프롬프트를 반복 주입하는 연속 AI 루프 방법론. "self-referential"은 출력을 입력으로 먹는 게 아니라 **파일·git 히스토리에 남은 이전 작업을 다음 반복이 보는 것**.
- **각 반복 흐름**: 동일 프롬프트 수신 → 작업·파일 수정 → 종료 시도 → Stop 훅이 가로채 같은 프롬프트 재주입 → 이전 작업을 보며 점진 개선.
- **사용 가능한 명령어**: `/ralph-loop`, `/cancel-ralph`.
- **핵심 개념**: 완료 프로미스(`<promise>` 태그), 자기참조 메커니즘.
- **언제 쓰고 안 쓰는지**, 그리고 더 알아볼 링크.

<a id="help---트리거-조건"></a>
### 🎯 트리거 조건

- **언제 호출되는가**
  - 사용자가 `/help`(ralph-loop 컨텍스트)를 입력할 때
  - Ralph Loop 사용법·개념을 처음 익히거나 명령어 레퍼런스가 필요할 때
  - `/ralph-loop` 옵션과 완료 프로미스 동작을 확인하고 싶을 때

- **언제 쓰지 않는가**
  - 실제로 루프를 시작/취소하려는 경우 (각각 `/ralph-loop`, `/cancel-ralph` 사용)
  - Claude Code 전반의 도움말이 필요한 경우 (이 명령은 ralph-loop 플러그인 전용 설명)

<a id="help---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어

```
/help
```

인자 없음. 실행하면 Ralph Loop 설명, 명령어 목록, 완료 프로미스/자기참조 개념, 사용 적합/부적합 사례, 예시를 출력한다.

설명에 포함되는 예시:
```
# 시작
/ralph-loop "Refactor the cache layer" --max-iterations 20
/ralph-loop "Add tests" --completion-promise "TESTS COMPLETE"

# 취소
/cancel-ralph

# 완료 신호 (Claude가 출력해야 하는 태그)
<promise>TASK COMPLETE</promise>

# 인터랙티브 버그 픽스 예시
/ralph-loop "Fix the token refresh logic in auth.ts. Output <promise>FIXED</promise> when all tests pass." --completion-promise "FIXED" --max-iterations 10
```

<a id="help---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터

별도 도구·인자 없음 (`description`만 가진 순수 설명형 명령). 명령은 다음을 설명하도록 지시한다.

**`/ralph-loop <PROMPT> [OPTIONS]`** — 현재 세션에서 루프 시작.
- `--max-iterations <n>`: 자동 중단 전 최대 반복.
- `--completion-promise <text>`: 완료를 알리는 문구.
- 동작: 상태 파일 생성 → 작업 → 종료 시 Stop 훅이 가로챔 → 같은 프롬프트 재주입 → 프로미스 감지 또는 최대 반복까지 반복.

**`/cancel-ralph`** — 활성 루프 취소(상태 파일 제거, 반복 횟수와 함께 보고).

**완료 프로미스(Completion Promises):** 완료를 알리려면 Claude가 `<promise>TASK COMPLETE</promise>` 태그를 출력해야 하며, Stop 훅이 이 태그를 찾는다. 태그(또는 `--max-iterations`)가 없으면 무한 실행.

**자기참조 메커니즘:** 같은 프롬프트 반복 + 작업이 파일에 영속 + 각 반복이 이전 시도를 봄 + 목표를 향해 점진 누적.

**사용 적합/부적합:**
- 적합: 성공 기준이 명확한 작업, 반복·정제가 필요한 작업, 자기 교정형 개발, 그린필드 프로젝트.
- 부적합: 인간 판단·설계 결정 필요, 일회성 작업, 성공 기준 불명확, 프로덕션 디버깅.

**더 알아보기:** 원 기법 `https://ghuntley.com/ralph/`, Ralph Orchestrator `https://github.com/mikeyobrien/ralph-orchestrator`.

<a id="help---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 플러그인: ralph-loop@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/ralph-loop/1.0.0/commands/help.md`

## ralph-loop

> 같은 프롬프트를 Stop 훅으로 반복 주입해 현재 세션 안에서 자기참조 반복 개발 루프(Ralph Wiggum 기법)를 시작하는 명령어.

<a id="ralph-loop---용도"></a>
### 📌 용도

`/ralph-loop`은 Geoffrey Huntley가 정립한 **Ralph Wiggum 기법**을 Claude Code 세션 내부에서 구현한다. 외부 `while true` 배시 루프 없이, **Stop 훅이 세션 종료를 가로채** 같은 프롬프트를 다시 주입하는 방식으로 동작한다.

```bash
# 개념 (외부 루프 형태):
while :; do
  cat PROMPT.md | claude-code --continue
done
```

각 반복(iteration)에서:
1. Claude가 **동일한 프롬프트**를 받음
2. 작업하며 파일을 수정
3. 종료 시도
4. Stop 훅이 종료를 차단하고 같은 프롬프트를 다시 주입
5. Claude가 **파일과 git 히스토리에 남은 자신의 이전 작업**을 봄
6. 완료(또는 최대 반복)까지 점진적으로 개선

"자기참조"란 Claude가 자기 출력을 입력으로 먹는 게 아니라, **이전 작업이 파일에 영속되어 다음 반복이 그것을 보는 것**을 의미한다. "deterministically bad in an undeterministic world" — 실패가 예측 가능하므로 프롬프트 튜닝으로 체계적 개선이 가능하다는 철학.

<a id="ralph-loop---트리거-조건"></a>
### 🎯 트리거 조건

- **언제 호출되는가**
  - 사용자가 `/ralph-loop "<프롬프트>" [옵션]`을 입력할 때
  - 성공 기준이 명확하고 **자동 검증(테스트, 린터)** 가능한 작업
  - 반복·정제가 필요한 작업 (예: 테스트를 통과시키기, TDD)
  - 그린필드 프로젝트, 자리를 비워도 되는 작업

- **언제 쓰지 않는가**
  - 인간의 판단·설계 결정이 필요한 작업
  - 일회성(one-shot) 작업
  - 성공 기준이 불명확한 작업
  - 프로덕션 디버깅 (타겟 디버깅을 쓸 것)

  ⚠️ 이 루프는 기본적으로 **수동으로 멈출 수 없고 무한 실행**된다. 반드시 `--max-iterations`나 `--completion-promise`로 종료 조건을 걸 것.

<a id="ralph-loop---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어

기본 형태 (`argument-hint: PROMPT [--max-iterations N] [--completion-promise TEXT]`):
```
/ralph-loop "<프롬프트>" --max-iterations <n> --completion-promise "<텍스트>"
```

예시:
```
/ralph-loop "Refactor the cache layer" --max-iterations 20
/ralph-loop "Add tests" --completion-promise "TESTS COMPLETE"
/ralph-loop Build a todo API --completion-promise 'DONE' --max-iterations 20
/ralph-loop --max-iterations 10 Fix the auth bug
/ralph-loop Refactor cache layer        # 종료 조건 없음 → 무한 실행
```

완전한 예시 (완료 프로미스 + 안전 한계 동시 사용 권장):
```
/ralph-loop "Build a REST API for todos. Requirements: CRUD, input validation, tests. Output <promise>COMPLETE</promise> when done." --completion-promise "COMPLETE" --max-iterations 50
```

**완료 신호(Completion Promise):** 루프를 끝내려면 Claude가 정확히 다음 태그를 출력해야 한다.
```
<promise>TASK COMPLETE</promise>
```
Stop 훅이 이 태그 안의 텍스트를 `--completion-promise` 값과 **정확한 문자열로 비교**한다. 글로빙(`*`, `?`) 아님. 따라서 "SUCCESS" vs "BLOCKED" 같은 다중 종료 조건엔 쓸 수 없고, `--max-iterations`가 주 안전장치다.

**상태 모니터링:**
```bash
grep '^iteration:' .claude/ralph-loop.local.md   # 현재 반복 횟수
head -10 .claude/ralph-loop.local.md             # 전체 상태
```

<a id="ralph-loop---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터

**허용 도구(allowed-tools):** `Bash(${CLAUDE_PLUGIN_ROOT}/scripts/setup-ralph-loop.sh:*)` — 명령은 셋업 스크립트만 실행한다. `hide-from-slash-command-tool: true`로 설정됨.

**옵션:**
- `--max-iterations <n>` — N회 후 자동 중단 (기본: 0 = 무제한). 양의 정수 또는 0만 허용 (소수·음수·텍스트 거부).
- `--completion-promise <text>` — 완료를 알리는 문구 (다중 단어는 따옴표 필수).
- `-h`, `--help` — 도움말.

**동작 메커니즘:**
1. `scripts/setup-ralph-loop.sh`가 인자를 파싱해 **상태 파일** `.claude/ralph-loop.local.md` 생성. 이 파일은 YAML 프론트매터(`active`, `iteration`, `session_id`, `max_iterations`, `completion_promise`, `started_at`) + 본문(프롬프트)로 구성.
2. 사용자가 작업하다 종료를 시도하면 `hooks/stop-hook.sh`(Stop 훅)가 가로챔.
3. 훅은 상태 파일을 읽어:
   - **세션 격리**: `session_id`가 현재 세션과 다르면 차단하지 않음 (프로젝트 단위 파일이 다른 세션 종료를 막지 않도록).
   - 최대 반복 도달 시 → 상태 파일 삭제 후 종료 허용.
   - 트랜스크립트(JSONL)에서 마지막 assistant 텍스트 블록을 추출해 `<promise>` 태그를 찾고, 완료 프로미스와 정확히 일치하면 → 상태 파일 삭제 후 종료 허용.
   - 아니면 `iteration`을 +1 갱신하고 `{"decision":"block","reason":"<프롬프트>","systemMessage":"🔄 Ralph iteration N..."}` JSON을 출력해 **같은 프롬프트를 재주입**.
4. 상태 파일 손상(숫자 필드 비정상, 프롬프트 누락, 트랜스크립트 없음) 시 안전하게 루프 중단.

**핵심 규칙(CRITICAL):** 완료 프로미스가 설정되면, 그 문장이 **완전하고 명백히 참일 때만** 출력해야 한다. 막혔다고 느껴도, 루프를 탈출하려고 거짓 프로미스를 내면 안 된다. 루프는 진짜 완료까지 계속되도록 설계됨.

**Windows 주의:** Stop 훅은 배시 스크립트라 Git for Windows가 필요. `bash`가 WSL bash로 잘못 잡히면 훅이 실패할 수 있으므로, 캐시된 `hooks/hooks.json`에서 Git Bash 경로(`"C:/Program Files/Git/bin/bash.exe"`)를 명시하는 워크어라운드가 있다. (`Git/bin/bash.exe` 사용, `Git/usr/bin/bash.exe` 아님.)

<a id="ralph-loop---출처--설치-상태"></a>
### 📦 출처 / 설치 상태

- 플러그인: ralph-loop@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/ralph-loop/1.0.0/commands/ralph-loop.md`
