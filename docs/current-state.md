<!-- 현재 문서 구성과 사용 안내·실제 검증 경계를 요약한다. -->
# 현재 상태.

## 현재 구성과 길찾기.

2026-11-12 기준이다. README는 시작 안내, GUIDE는 사용법, AGENTS와 rules는 행동 규칙이다. [스킬 카탈로그](../Skill/CATALOG.md)는 설명 144개를 26그룹으로 정리하며 [자체 제작 원본](../Owned-Skills/README.md)은 26패키지다. 설명 수는 설치·인증·현재 클라이언트 노출 수와 다르다. [MCP 안내](../MCP/README.md)도 도구별 조건과 작성 당시 상태를 구분한다.

| 필요한 안내. | 기준 문서. |
|---|---|
| Anthropic 19개 이름·이전·명시 호출 10개. | [전역 설치 안내](../Skill/anthropic-skills/README.md), [고정 명세](../references/anthropic-skills.lock.json). |
| PPT Master·OfficeCLI·Huashu Design. | [설치·전용 런타임·명시 호출 안내](../Skill/office-design-tools/README.md), [고정 명세](../references/office-design-tools.lock.json). |
| Unity MCP와 프로젝트 연결. | [Coplay·Funplay 안내](../MCP/coplay-funplay-unity-mcp.md). |
| 다른 AI로 이식하거나 현재 도구 확인. | [PORTABILITY](../PORTABILITY.md), [사용 안내](../GUIDE.md). |
| 실행 기록·과거 주소·버전별 증거. | [작업 기록 목차](history/README.md). |

종료한 설계·계획·리뷰 54개는 작업별 기록 20개로 보관한다. 과거의 설치 수·미푸시·대기 문구는 당시 상태이며 현재 지시가 아니다. 최초 파일 배치·새 프로세스 발견·실제 기능 수행은 서로 다른 검증이다.

## 확인된 기능과 남은 경계.

- Anthropic 설치·중복 조사는 [설치 기록](history/2026-11-12-anthropic-skills.md#review)에 있다. 별도 [실제 작업 검증](history/2026-11-12-anthropic-functional.md#review)은 대표 통과 13개·조건부 5개·SWC 번들 실패 1개다. Windows Office helper의 AF_UNIX·렌더·재계산과 웹 helper의 자동 자식 서버 정리 문제를 통과 처리하지 않는다.
- Office/design 세 도구의 [별도 샘플](history/2026-11-12-office-design-tools.md#review)은 파일 생성·변환·수식 캐시·HTML 렌더와 실패 조건을 확인했다. 전용 Python과 Huashu 브라우저 경로가 필요하며 실제 Office 렌더 동일성·외부 API·전체 기능은 미검증이다. 다른 Anthropic helper의 실패를 수정한 증거는 아니다.
- Unity의 [설치 기록](history/2026-11-11-coplay-funplay-unity-mcp.md#review)은 SDK 연결·도구와 새 스킬 발견을 확인했다. 두 프로젝트 패키지·실제 Editor 연결과 Funplay 주소 등록은 연기됐다.
- 과거 글로벌 문서 복제·개인 자료 보존과 고정 출처 조사는 [보관 목차](history/README.md)에 있다. 이번 문서 정리는 지정 저장소를 대상으로 하며 전역 실행본·개인 설정·권한을 변경하지 않는다.

## 이번 문서 정리.

[설계](superpowers/specs/2026-11-12-docs-refresh-design.md)·[계획](superpowers/plans/2026-11-12-docs-refresh.md)·[검증 기록](reviews/2026-11-12-docs-refresh.md)에 전수조사·보관·링크·보호·배포 결과를 기록한다. 이전 설치 작업의 최종 기록은 `3c4dd83`이다. 이번 정리 커밋 `1b380db`를 main에 통합·push하고 전체 103개 회귀·독립 리뷰·원격 SHA 일치와 [Ubuntu·Windows CI 성공](https://github.com/nowJDev/Agent-Instructions/actions/runs/43142480610)을 확인했다. 소유 임시 worktree·브랜치는 정리했으며 전역 복제본·설치 환경은 이번 변경 대상에 포함하지 않았다.
