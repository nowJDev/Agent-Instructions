# 자체 제작 Agent Skills 원본.

이 디렉터리는 이 저장소에서 직접 설계·작성해 재배포할 수 있는 Agent Skill 실물을 보관한다.

## 포함 항목.

- [`design-driven-delivery`](design-driven-delivery/SKILL.md) — 상태 변경 요청을 설계·계획·구현·검증·리뷰·통합 순서로 통제하는 최상위 전달 프로세스다.

## 타사 Skill과의 경계.

- `Owned-Skills/`에는 직접 작성한 Skill만 둔다.
- 타사 플러그인 Skill은 실물을 복사하지 않고 `Skill/` 카탈로그에서 공개 원본과 설치 방법만 안내한다.
- 각 Skill의 스크립트·참조·템플릿은 해당 Skill 디렉터리 안에서 완결되게 유지한다.

## 설치.

Agent Skills 호환 클라이언트의 사용자 Skill 디렉터리에 원하는 패키지 디렉터리를 그대로 복사한다.

Codex의 기본 사용자 경로 예시는 다음과 같다.

```powershell
$skillTarget = "$env:USERPROFILE\.agents\skills\design-driven-delivery"
New-Item -ItemType Directory -Force -Path $skillTarget | Out-Null
Copy-Item -Path ".\Owned-Skills\design-driven-delivery\*" `
  -Destination $skillTarget -Recurse -Force
```

설치 후에는 새 세션을 시작해 Skill 목록과 암시적 호출 정책이 반영됐는지 확인한다.

## 검증.

각 패키지의 `SKILL.md`, `agents/openai.yaml`, 참조 링크와 스크립트를 확인한다. `design-driven-delivery`는 자체 검증 스크립트만으로 프로젝트 완료를 선언하지 않으며 프로젝트 고유 테스트·빌드·수동 검증을 함께 요구한다.
