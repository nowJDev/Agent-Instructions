<!-- 현재 문서 구성과 사용 안내·실제 검증 경계를 요약한다. -->
# 현재 상태.

## 현재 구성과 길찾기.

2026-11-12 기준이다. README는 시작 안내, GUIDE는 사용법, AGENTS와 rules는 행동 규칙이다. [스킬 카탈로그](../Skill/CATALOG.md)는 기존 144개 설명에 직접·시스템 보완 16개·현재 플러그인 패키지와 전문 가이드 108개·[자체 제작 원본](../Owned-Skills/README.md) 26개를 연결해 총 294개 주소를 등록한다. 상세 설명은 28그룹과 자체 제작 패키지에서 관리한다. 설명 수는 설치·인증·현재 노출 수와 다르다. [MCP 안내](../MCP/README.md)도 도구별 조건과 작성 당시 상태를 구분한다.

[분야별 전체 스킬 안내](../Skill/BY-TASK.md)는 294개 등록 주소 모두를 최소 한 분야에 연결한다. 기존 12개 분야에 데이터 분석·지식 관리·금융·음악을 보완한 16개 분야다. 엑셀의 32개 관련 항목은 파일 편집·live Excel·데이터 분석·추출·금융 모델을 구분한다. 한·영 README·스킬 인덱스·전체 카탈로그에서 진입하며 이후 설치 변경은 [날짜별 조사](../references/skill-inventory-2026-11-12.json)를 다시 대조해야 한다.

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
- 과거 글로벌 문서 복제·개인 자료 보존과 고정 출처 조사는 [보관 목차](history/README.md)에 있다. 이전 문서 전체 정리는 지정 저장소만을 대상으로 했다. 이번 전역 문서 복제는 아래 별도 기록으로 구분하며 설치 스킬·인증·권한은 보존한다.

## 이전 문서 정리.

[설계](superpowers/specs/2026-11-12-docs-refresh-design.md)·[계획](superpowers/plans/2026-11-12-docs-refresh.md)·[검증 기록](reviews/2026-11-12-docs-refresh.md)에 전수조사·보관·링크·보호·배포 결과를 기록한다. 이전 설치 작업의 최종 기록은 `3c4dd83`이다. 이번 정리 커밋 `1b380db`를 main에 통합·push하고 전체 103개 회귀·독립 리뷰·원격 SHA 일치와 [Ubuntu·Windows CI 성공](https://github.com/nowJDev/Agent-Instructions/actions/runs/43142480610)을 확인했다. 소유 임시 worktree·브랜치는 정리했으며 전역 복제본·설치 환경은 이번 변경 대상에 포함하지 않았다.

## 이전 대표 안내와 전역 복제.

[설계](superpowers/specs/2026-11-12-task-navigation-design.md)·[계획](superpowers/plans/2026-11-12-task-navigation.md)·[검증 기록](reviews/2026-11-12-task-navigation.md)을 기준으로 한다. 사용자는 저장소를 기준으로 전역 문서를 동일하게 독립 복제하도록 승인했다. 기존 전역 문서·개인 자료·진입점은 비공개 백업에 보존하며, 설치 스킬·인증·권한은 변경하지 않는다.

저장소와 main 통합 결과의 전체 106개 회귀·독립 리뷰를 통과했다. 전역 177개 파일의 동일성과 148개 Markdown 링크를 확인하고, 원본 저장소·임시 worktree 접근을 차단한 전역 전체 106개 회귀도 통과했다. 구현 커밋 `d7bffa3`을 main에 통합·push하고 원격 SHA 일치와 [Ubuntu·Windows CI 성공](https://github.com/nowJDev/Agent-Instructions/actions/runs/43170669712)을 확인했다. 소유 임시 worktree·브랜치는 정리했으며 최종 증거 문서도 전역 동일성 검사에 포함한다.

## 전체 스킬 누락 보완.

[설계](superpowers/specs/2026-11-12-skill-coverage-design.md)·[계획](superpowers/plans/2026-11-12-skill-coverage.md)·[검증 기록](reviews/2026-11-12-skill-coverage.md)을 기준으로 한다. 기존 대표 목록과 제한된 카탈로그에서 빠졌던 시스템·플러그인과 전체 분야 배치를 보완한다. 조사한 유효 패키지는 직접·시스템 136개와 선택된 플러그인 108개, 합계 244개이며 조사 세션 노출은 181개다. 루트 SKILL이 없는 후보 2개는 제외 사유를 기록한다. 미노출 63개 중 금융 라우터 전문 가이드 44개·Data 부속 5개는 직접 호출 가능성으로 바꾸지 않는다.

전체 108개 회귀와 독립 리뷰를 통과했고 발견된 라우터 metadata 분류는 RED→GREEN으로 수정했다. 전역 백업 후 183개 파일·SHA 동일성과 153개 Markdown 링크를 확인하고 원본 저장소·작업 공간 접근 차단 전체 108개 회귀도 통과했다. 구현 커밋 `c4edf3c`을 main에 통합·push하고 원격 SHA 일치와 [Ubuntu·Windows CI 성공](https://github.com/nowJDev/Agent-Instructions/actions/runs/43175064452)을 확인했다. 소유 임시 worktree·브랜치는 정리했으며 최종 증거 문서도 전역 동일성 검사에 포함한다. 실행 스킬·권한·인증과 기존 history는 보존한다.
