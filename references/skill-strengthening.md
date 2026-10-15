<!-- 범용 스킬 보강에 참고한 공개 출처와 채택 경계를 기록한다. -->
# 범용 스킬 보강 출처와 경계.

2026-10-15에 카탈로그 설명 수준이던 23개 절차를 입력·실행 환경·수행 단계·실패·관찰 증거를 갖춘 자체 작성 스킬로 보강했다. 공개 원본은 [Owned-Skills](../Owned-Skills/README.md), 카탈로그는 [Skill](../Skill/README.md)에서 구분한다. 카탈로그의 99개 이름을 23개 추가 이름으로 세지 않는다.

## 참고한 공개 출처.

| 출처 | 확인 기준 | 채택과 제외. |
|---|---|---|
| [context-forge](https://github.com/glowElephant/context-forge/tree/4228ee7246a5306f3a1a7d73c9bea8e57c55ce6c). | 공개 소스 인덱스·분류·출처 정보. | 관련 원본을 찾는 지도에 사용했다. 출처 목록을 설치 완료로 간주하거나 새 저장소 생성·푸시 워크플로를 가져오지 않았다. |
| [Addy Osmani agent-skills](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d). | 리뷰·단순화·보안 점검. | 실제 영향·호출자·실패 경로·동작 보존을 판단하는 관점을 참고했다. 타사 본문과 언어별 변환 예제는 복제하지 않았다. |
| [Everything Claude Code](https://github.com/affaan-m/everything-claude-code/tree/b92f181b3b748d1abbc2afd94af6aa7d8c8fca29). | 조사·검증 절차. | 원문 대조·출처·불확실성·검증 증거를 참고했다. 고정 도구·커버리지·자동 게시·설정 등록은 가져오지 않았다. |
| [Anthropic skills](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44). | API·언어별 문서와 웹 동작 검증. | 제공자·설치 버전·공식 문서·실제 관찰을 구분한다. 원본 패키지는 각자 해당 라이선스를 확인해 설치한다. |
| [Claude 공식 플러그인](https://github.com/anthropics/claude-plugins-official). | 기능 개발·Agent SDK·Ralph·리뷰 명령. | 작업 목적과 검토 관점을 참고한다. 고정 Claude 도구명·명령·Stop hook을 다른 호스트에 있다고 가정하지 않는다. |
| [Claude Code 공식 문서](https://code.claude.com/docs/en/skills), [Codex 스킬 안내](https://developers.openai.com/codex/skills). | 사용자 스킬·클라이언트 차이. | 실제 설치 경로·이름 충돌·지원 버전·인증·가용 도구를 확인한다. 링크 문서의 현재 계약을 재확인한다. |

## 공개 범위와 이식.

이 표는 출처 포인터이며 타사 구현·라이선스의 재배포 허가를 대체하지 않는다. 자체 작성 본문에만 이 저장소 License를 적용한다. 내부 자료·개인 설정·사용자별 검토 지식과 원문 보관본은 공개 패키지에 포함하지 않는다.

패키지는 문서 절차다. Claude 내장 명령·Stop hook·세션 저장소·예약 API를 Codex에 복사한 기능 구현이 아니다. 반복은 호스트 지원을 확인하고 한계·취소·증거를 갖춰 수행한다. 영구 예약·MCP 설치·권한 확대는 별도 범위다.

## 검증의 해석.

패키지 계약 검사는 이름·메타데이터·실제 링크·공개 정보 경계를 확인한다. 원본과 설치본 해시 대조는 파일 배치를 확인한다. 문서의 사례 충족 여부, CLI fixture 관찰과 실제 외부 서비스 실행은 각각 별도 증거이며 하나로 묶어 모든 스킬의 실사용 성공이라고 보고하지 않는다.
