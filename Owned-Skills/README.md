# 자체 제작 Agent Skills 원본.

이 디렉터리는 이 저장소에서 직접 작성한 Agent Skill 24개를 보관한다. 기존 design-driven-delivery와 범용 보강 23개다. 동명의 내장 기능·공식 플러그인과는 별도의 지침이며 해당 기능·도구·권한이 자동으로 생기지 않는다.

## 포함 항목.

| 용도 | 자체 제작 패키지 |
|---|---|
| 변경 작업 조율. | [design-driven-delivery](design-driven-delivery/SKILL.md), [feature-dev](feature-dev/SKILL.md). |
| 검토·실행·검증. | [code-review](code-review/SKILL.md), [review](review/SKILL.md), [review-pr](review-pr/SKILL.md), [security-review](security-review/SKILL.md), [simplify](simplify/SKILL.md), [run](run/SKILL.md), [verify](verify/SKILL.md). |
| 조사·Claude 개발. | [deep-research](deep-research/SKILL.md), [claude-news](claude-news/SKILL.md), [claude-api](claude-api/SKILL.md), [new-sdk-app](new-sdk-app/SKILL.md). |
| 지침·설정·세션. | [init](init/SKILL.md), [update-config](update-config/SKILL.md), [keybindings-help](keybindings-help/SKILL.md), [fewer-permission-prompts](fewer-permission-prompts/SKILL.md), [handover](handover/SKILL.md), [delete-session](delete-session/SKILL.md). |
| 유한 반복. | [loop](loop/SKILL.md), [ralph-loop](ralph-loop/SKILL.md), [cancel-ralph](cancel-ralph/SKILL.md), [help](help/SKILL.md). |
| 프로젝트 계획. | [figma-generate-project-plan](figma-generate-project-plan/SKILL.md). |

## 타사 Skill과의 경계.

- 직접 작성한 본문과 필요한 자체 리소스만 담는다. 저장소 [MIT License](../LICENSE)가 적용된다.
- 타사 플러그인·내장 명령의 원문을 복제하지 않는다. 공개 출처와 채택 경계는 [보강 기록](../references/skill-strengthening.md), 설치 출처는 [Skill 인덱스](../Skill/README.md)를 따른다.
- 패키지 리소스는 그 디렉터리 안에서 완결한다. 다른 스킬을 이름으로 재사용할 때는 실제 설치를 확인하고 미설치 시 핵심 절차를 직접 수행하거나 지원 부재를 보고한다.
- Figma 편집처럼 필수 가이드·인증·도구가 필요한 작업은 전제를 충족해야 한다. 미충족이면 외부 편집 없이 초안만 준비한다.
- 개인 기본 경로·비공개 참조·로컬 설정은 사용자 환경에만 보관한다. 업데이트 전 기존 본문과 개인 예외를 비교해 보존한다.

## 설치와 업데이트.

요청한 클라이언트의 사용자 스킬 경로에 원하는 패키지 디렉터리 전체를 복사한다. Codex는 기본적으로 ~/.agents/skills, Claude Code는 ~/.claude/skills를 사용한다. 사용자 지정 경로와 관리 정책이 있으면 그것을 먼저 확인한다. 프로젝트 전용 설치와 사용자 전역 설치를 구분한다.

기존 같은 이름이 있으면 본문·참조와 설치 출처를 확인하고 별도의 비공개 백업을 만든다. 같은 디렉터리에 필요한 파일만 병합하며 개인 참조·알 수 없는 파일·타사 원본을 통째로 삭제하지 않는다. 기존 로컬 본문에 개인 규칙이 있다면 업데이트 후 별도 로컬 참조로 연결한다. 백업 전후 해시를 확인하고 실패 시 이번 변경만 복구한다.

예를 들어 저장소 루트에서 새 패키지 하나를 Codex에 설치할 때 다음과 같이 복사한다. 기존 패키지 업데이트에는 위 백업·비교 절차를 먼저 적용한다.

~~~powershell
$skillName = 'verify'
$skillTarget = Join-Path $env:USERPROFILE ".agents/skills/$skillName"
if (Test-Path -LiteralPath $skillTarget) {
    throw '기존 패키지는 백업하고 개인 변경을 비교한 뒤 업데이트하세요.'
}
Copy-Item -LiteralPath (Join-Path './Owned-Skills' $skillName) -Destination $skillTarget -Recurse -ErrorAction Stop
~~~

대상 부모 skills 디렉터리는 미리 준비하고, 실제 경로가 지정 사용자 경로 안에 있는지 확인한다. 다른 위치로 연결된 junction·symlink를 무심코 덮어쓰지 않는다. Claude Code의 기존 내장 명령을 보존하려면 새 패키지는 portable- 접두어를 붙인 디렉터리에 설치하고 SKILL.md의 name도 같은 이름으로 바꾼다. 본문의 다른 자체 제작 스킬명도 설치 이름에 맞춰 연결한다. 예를 들어 portable-help는 Ralph 도움말이고 기존 /help는 그대로 쓴다. 이미 사용자 소유로 설치한 claude-news처럼 의도적으로 교체할 이름만 기존 위치를 업데이트한다. 플러그인은 자체 namespace를 유지한다.

설치 후 UTF-8 본문과 참조 링크를 확인한다. 이름 변환이 없는 파일은 원본 해시와 대조하고 Claude 이름 변환 본문은 변환한 예상본의 해시·허용 diff와 대조한다. 개인 예외를 추가한 본문도 해당 차이를 별도 기록한다. 나머지 리소스는 원본 해시 일치를 확인한다. 새 세션에서 이름이 발견되고 필요한 본문을 읽는지도 확인한다. 파일 복사 성공과 실제 발견·호출 성공은 서로 다른 결과다. 동명 내장 명령·플러그인이 있으면 클라이언트의 이름 충돌·호출 우선순위를 확인하고 어떤 구현을 사용했는지 구분한다. [Codex 스킬 경로](https://learn.chatgpt.com/docs/build-skills)와 [Claude 이름 충돌 규칙](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name)을 실제 앱 버전에 맞춰 확인한다. 이 설치는 MCP·hooks·권한·플러그인 활성화 설정을 변경하지 않는다.

## 검증.

저장소 루트에서 다음을 실행한다.

~~~text
python -X utf8 -B -m unittest discover -s tests -v
~~~

패키지 이름·frontmatter·자기완결 링크·공개 정보 경계를 검사한다. agents/openai.yaml이 포함된 기존 패키지는 해당 메타데이터와 참조 리소스도 보존한다. 정적 검사 통과가 외부 서비스·실제 앱 실행·새 세션 로딩의 성공을 뜻하지 않는다. 각 작업에서는 해당 스킬의 실제 검증 절차를 수행한다.
