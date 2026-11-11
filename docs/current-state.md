<!-- 최신 문서 구조와 검증·배포 결과 및 남은 검증 경계만 요약한다. -->
# 현재 상태.

## 2026-11-11 README 개편.

사용자가 승인한 [설계](superpowers/specs/2026-11-11-readme-bilingual-design.md)와 [계획](superpowers/plans/2026-11-11-readme-bilingual.md)에 따라 한국어 README를 정리하고 영어 전환·대표 이미지2개를 추가했다. 기존 fragment9개와 운영 규칙·GUIDE를 보존했다. Windows Python3.12 전체84개가 통과했고 독립 리뷰에서 확정 결함을 발견하지 못했다. 실제 GitHub 화면·원격 SHA·CI는 배포 후 [검증 기록](reviews/2026-11-11-readme-bilingual.md)에 갱신한다. 전역 복제본 동기화는 이번 요청 범위에 포함하지 않는다.

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
