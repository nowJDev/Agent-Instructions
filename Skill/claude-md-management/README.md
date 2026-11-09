<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# claude-md-management 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. 활성 표시는 작성 당시 환경의 기록이다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [claude-md-improver](#claude-md-improver).
- [revise-claude-md](#revise-claude-md).

## claude-md-improver

> 저장소의 CLAUDE.md 파일들을 감사·평가하고 타겟 개선을 수행하는 스킬

<a id="claude-md-improver---용도"></a>
### 📌 용도
코드베이스 전반의 CLAUDE.md 파일을 감사·평가·개선해 Claude Code가 최적의 프로젝트 컨텍스트를 갖도록 한다. 모든 CLAUDE.md를 스캔하고 템플릿 대비 품질을 평가하여 품질 리포트를 출력한 뒤, 사용자 승인을 받아 타겟 개선을 적용한다. **이 스킬은 CLAUDE.md 파일에 쓰기 작업을 수행한다.**

<a id="claude-md-improver---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: CLAUDE.md 파일을 점검·감사·업데이트·개선·수정 요청 시. "CLAUDE.md maintenance" 또는 "project memory optimization" 언급 시.
- **언제 쓰지 않는가**: 현재 세션 학습만 반영할 때는 revise-claude-md 명령 사용. 이 스킬은 저장소 전체 감사·품질 평가에 특화.

<a id="claude-md-improver---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- "우리 프로젝트 CLAUDE.md 파일들을 감사해줘"
- "CLAUDE.md를 최신 코드베이스 상태에 맞게 업데이트해줘"
- "project memory를 최적화하고 싶어"

<a id="claude-md-improver---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**5단계 워크플로**:

1. **Discovery**: `find . -type f \( -name "CLAUDE.md" -o -name "CLAUDE.local.md" \)`로 프로젝트 파일 탐색. 파일 유형: 프로젝트 지침(`./CLAUDE.md` 또는 `./.claude/CLAUDE.md`), 개인 로컬 지침(`CLAUDE.local.md`), 패키지별(monorepo), 서브디렉터리. 전역 기본(`~/.claude/CLAUDE.md`)은 프로젝트 밖에 있으므로 별도로 읽는다. [공식 파일명과 로딩 규칙](https://code.claude.com/docs/en/memory)을 따른다.

2. **Quality Assessment**: 각 파일을 품질 기준으로 평가 — 명령/워크플로 문서화(High), 아키텍처 명확성(High), 비자명 패턴(Medium), 간결성(Medium), 최신성(High), 실행 가능성(High). 점수: A(90~100) ~ F(0~29). 상세 루브릭은 `references/quality-criteria.md`.

3. **Quality Report 출력**(업데이트 전 항상 먼저): 요약(파일 수, 평균 점수, 업데이트 필요 수) + 파일별 평가(기준별 점수표, 이슈, 권장 추가).

4. **Targeted Updates**: 리포트 출력 후 사용자 확인. 진짜 유용한 정보만 타겟 추가(발견한 명령/워크플로, gotcha, 패키지 관계, 테스트 접근법, 설정 특이사항). 자명한 것·일반 베스트 프랙티스·일회성 수정·장황한 설명은 피할 것. diff로 변경 표시.

5. **Apply Updates**: 승인 후 Edit 도구로 적용, 기존 구조 보존.

**흔히 지적할 이슈**: stale 명령, 누락 의존성, 구식 아키텍처, 환경 설정 누락, 깨진 테스트 명령, 미문서화 gotcha.

**사용자 팁**: `#` 키 단축키(세션 중 학습 자동 반영), 간결 유지, 실행 가능한 명령, `CLAUDE.local.md`(개인 로컬 지침), `~/.claude/CLAUDE.md`(전역 기본).

**참조 파일**: `references/quality-criteria.md`, `references/templates.md`
**tools**: Read, Glob, Grep, Bash, Edit

<a id="claude-md-improver---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: claude-md-management@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/claude-md-management/1.0.0/skills/claude-md-improver/SKILL.md`

## revise-claude-md

> 현재 세션에서 얻은 학습 내용을 CLAUDE.md에 반영해 업데이트하는 슬래시 명령

<a id="revise-claude-md---용도"></a>
### 📌 용도
현재 세션에서 이 코드베이스로 작업하며 얻은 학습 내용을 검토하고, 향후 Claude 세션이 더 효과적으로 작업할 수 있도록 CLAUDE.md에 컨텍스트를 추가한다. 이번 세션에서 발견한 명령어, 코드 스타일 패턴, 테스트 접근법, 환경/설정 특이사항, 주의사항(gotcha)을 다음 세션을 위해 기록한다.

<a id="revise-claude-md---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: `/claude-md-management:revise-claude-md` 실행 시. 세션에서 배운 것을 CLAUDE.md에 반영하고 싶을 때.
- **언제 쓰지 않는가**: 저장소 전체의 CLAUDE.md 품질 감사·평가는 claude-md-improver 스킬 사용. 이 명령은 "현재 세션 학습 반영"에 특화.

<a id="revise-claude-md---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/claude-md-management:revise-claude-md
```
- allowed-tools: Read, Edit, Glob

<a id="revise-claude-md---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
**5단계 워크플로**:

1. **Reflect(반성)**: 무엇이 있었으면 Claude가 더 효과적으로 작업했을지 파악 — 사용/발견한 bash 명령, 따른 코드 스타일 패턴, 통한 테스트 접근법, 환경/설정 특이사항, 마주친 경고/gotcha.

2. **CLAUDE.md 파일 찾기**:
   ```bash
   find . -name "CLAUDE.md" -o -name "CLAUDE.local.md" 2>/dev/null | head -20
   ```
   추가 위치 결정: `CLAUDE.md`(팀 공유, git 체크인)와 `CLAUDE.local.md`(개인/로컬, gitignore). [공식 지침 파일 안내](https://code.claude.com/docs/en/memory#choose-where-to-put-claudemd-files)를 따른다.

3. **추가 내용 초안**: **간결하게** — 개념당 한 줄. CLAUDE.md는 프롬프트의 일부이므로 간결함이 중요. 형식 `<명령 또는 패턴>` - `<짧은 설명>`. 장황한 설명·자명한 정보·재발 가능성 낮은 일회성 수정은 피할 것.

4. **변경 제안 표시**: 각 추가에 대해 대상 파일, 이유(한 줄), diff 형식으로 제시.
   ````markdown
   ### Update: ./CLAUDE.md
   **Why:** [한 줄 이유]
   ```diff
   + [간결한 추가]
   ```
   ````

5. **승인 후 적용**: 사용자에게 적용 여부 질문, 승인한 파일만 편집.

<a id="revise-claude-md---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: claude-md-management@claude-plugins-official
- 활성화: ON
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/claude-md-management/1.0.0/commands/revise-claude-md.md`
