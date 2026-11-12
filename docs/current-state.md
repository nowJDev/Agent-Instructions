<!-- 최신 문서 구조와 검증·배포 결과 및 남은 검증 경계만 요약한다. -->
# 현재 상태.

## 2026-11-12 Anthropic 스킬 설치.

[승인 설계](superpowers/specs/2026-11-12-anthropic-skills-design.md)에 따라 공식 19개 스킬을 전역에 설치하고 기존 2개를 백업·이전했다. 설치기·고정 명세·공급자 접두어와 141개 설명 카탈로그를 추가했다. [계획](superpowers/plans/2026-11-12-anthropic-skills.md)과 [전수조사·검증 기록](reviews/2026-11-12-anthropic-skills.md)에 조사 범위·기존 역할 중첩·호출 제한 10개와 독립 리뷰 결함 4개의 수정 증거를 기록한다. Python 3.12 전체 103개 회귀, 보호 971파일 동일성, 재설치 무변경과 새 사용자 프로세스의 홈·저장소 스킬 147개 발견을 확인했다. 동명·원문·정규화 본문 중복은 모두 0개다. 사용자가 승인한 새 패키지·상태 파일의 Windows ACL 상속을 복원한 뒤 현재 에이전트의 19개 본문 직접 읽기와 검사 CLI도 통과했다. 구현 커밋 `44e85c8`을 로컬 main에 통합하고 병합 후 103개 회귀를 재검증한 뒤 소유 임시 worktree·브랜치를 정리했다. 다른 클라이언트·플러그인·자체 제작 스킬·개인 자료와 이번 설치와 무관한 기존 역할 중첩은 보존했다. 실제 모델 기능 실행과 원격 push는 수행하지 않았다.

## 2026-11-11 Unity MCP 추가.

사용자 요청에 따라 CoplayDev/unity-mcp와 FunplayAI/funplay-unity-mcp의 설치·전역 등록 안내를 [Unity MCP 문서](../MCP/coplay-funplay-unity-mcp.md)에 추가하고 MCP 목차·이식 표에서 연결했다. 프로젝트 설치는 나중으로 미룬다는 후속 지시에 따라 [coplay-funplay-unity-mcp-setup](../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md)을 자체 제작 원본에 추가했다. 자체 제작 원본은 26개다. CoplayDev/unity-mcp 전역 서버 `10.3.0`과 Codex stdio 등록, SDK의 MCP 응답·도구 48개를 확인했으며 기존 설정을 보존했다. 전역 스킬·문서의 원본 해시와 중복 정리를 확인했고 새 Codex 프로세스에서 새 스킬의 enabled·사용자 범위·실제 경로를 발견했다. Windows Python 3.12 전체 84개 회귀·내부 링크·diff 검사와 스킬 유효성 검사를 통과했다. FunplayAI/funplay-unity-mcp 주소 등록·두 Unity 패키지 설치·실제 Editor 연결은 연기했으며 실제 모델 호출·Codex 세션의 MCP 도구 발견은 미검증이다. [설계](superpowers/specs/2026-11-11-coplay-funplay-unity-mcp-design.md), [계획](superpowers/plans/2026-11-11-coplay-funplay-unity-mcp.md), [검증 기록](reviews/2026-11-11-coplay-funplay-unity-mcp.md)에 범위와 증거를 남긴다. 구현 커밋 `be04619`를 로컬 main에 통합하고 병합 후 전체 84개 회귀를 다시 통과했다. 이번 임시 worktree·브랜치는 정리했으며 원격 push는 수행하지 않았다.

## 2026-11-11 README 개편.

사용자가 승인한 [설계](superpowers/specs/2026-11-11-readme-bilingual-design.md)와 [계획](superpowers/plans/2026-11-11-readme-bilingual.md)에 따라 한국어 README를 정리하고 영어 전환·대표 이미지2개를 추가했다. 기존 fragment9개와 운영 규칙·GUIDE를 보존했다. Windows Python3.12 전체84개가 통과했고 독립 리뷰에서 확정 결함을 발견하지 못했다. 구현 커밋 `5278e2a`를 main에 병합·push하고 원격 SHA 일치, 실제 GitHub의 한·영 전환·데스크톱·모바일·테마 및 두 OS CI 성공을 확인했다. 임시 브랜치·worktree·탭·캡처도 정리했다. 상세 증거는 [검증 기록](reviews/2026-11-11-readme-bilingual.md)에 있다. 전역 복제본 동기화는 이번 요청 범위에 포함하지 않는다.

## 이전 문서 통합 작업의 기록.

2026-11-09 [승인 설계](superpowers/specs/2026-11-09-document-consolidation-design.md)에 따라 문서 통합과 글로벌 적용을 완료했다. [실행 계획](superpowers/plans/2026-11-09-document-consolidation.md)과 [검증·배포 기록](reviews/2026-11-09-document-consolidation.md)에 증거를 남겼다.

## 문서 통합 당시 구성.

- 전체 추적 파일은270개에서154개로116개 줄었다.
- 카탈로그121개 설명은23개 그룹 README에 있다. [전체 항목 목차](../Skill/CATALOG.md)에서 해당 절로 이동한다.
- 과거 설계·계획·리뷰37개는 [14개 작업 기록과 목차](history/README.md)로 보관한다. 승인·실패·미검증 원문을 유지한다.
- 설치 가능한 자체 제작25개 패키지·62파일, MCP17파일, 출처 JSON과 평가 자료는 보존했다.

## 검증과 적용.

- Windows Python3.12 전체80개가 통과했다. 독립 리뷰의3개 발견은 실패 반례를 확인한 뒤 수정했다.
- 구현 커밋 b040f65를 main에 통합·push하고 [GitHub CI](https://github.com/nowJDev/Agent-Instructions/actions/runs/42541330739)의 Ubuntu·Windows 성공을 확인했다. Ubuntu는80개 중 Windows 전용4개를 의도적으로 건너뛰고 Windows는80개 전부 통과했다.
- 기존 글로벌 복사본은 관리 문서154개와 개인 문서2개를 합쳐156개다. 개인 목차·개인 지침과 설정·인증·실행 스킬743파일을 보존했다. 새 읽기 전용 CLI 세션에서 글로벌 지침과 통합 문서의 실제 로드를 확인했다.
- 임시 브랜치·worktree 등록과 내용 파일을 정리했다. 비어 있는 임시 폴더 하나는 운영체제 프로세스 잠금으로 남아 있으며 사용자 앱을 강제로 종료하지 않았다. 복구 백업은 비공개 글로벌 백업 위치에 보존했다.

## 과거 검증의 경계.

[이전 Superpowers 작업](history/2026-11-05-superpowers-update.md#review)의 Claude 실제 모델 호출은 당시 미검증이었다. 이번 문서 통합으로 통과 처리하지 않는다. 전역102개·출처132개·새 CLI 발견122개는 [2026-11-06 기록](history/2026-11-06-codex-skills-update.md#review)의 서로 다른 집계다.

일일 업무보고의 새 세션·회귀·합성 비교와 배치 시뮬레이션 제한은 [추가 검증 기록](history/2026-10-15-portable-skill-workflows.md#daily-work-report-verification)에 보존했다.
