<!-- 최신 문서 구조와 검증·배포 상태 및 남은 확인만 요약한다. -->
# 현재 상태.

2026-11-09 [승인 설계](superpowers/specs/2026-11-09-document-consolidation-design.md)에 따라 문서 통합을 진행한다. [실행 계획](superpowers/plans/2026-11-09-document-consolidation.md)과 [검증·배포 기록](reviews/2026-11-09-document-consolidation.md)에서 실제 완료 범위를 확인한다.

## 현재 구성.

- 카탈로그 설명 121개는 23개 그룹 README에 있다. [전체 항목 목차](../Skill/CATALOG.md)에서 해당 절로 바로 이동한다.
- 과거 설계·계획·리뷰 37개는 [14개 작업 기록과 목차](history/README.md)로 보관하며 승인·실패·미검증 원문을 유지한다.
- 설치 가능한 자체 제작 스킬 25개·62파일, MCP 설명 17파일, 출처 JSON과 평가 자료를 보존한다.
- 이번 작업 문서와 문서 회귀를 포함한 최종 추적 파일 목표는154개다. 개인 추가 문서는 공개 저장소의 개수에 합산하지 않는다.

## 확인한 범위와 남은 작업.

- Windows Python3.12 전체80개와 문서·HF 안전 회귀가 통과했고 원문·보호 해시·내부 링크·수동 표시·독립 리뷰의 수정 검증을 마쳤다.
- 글로벌 보존 배포·새 세션 로드·main 통합·GitHub push·원격 CI는 실행 계획의 실제 증거로 갱신한다.
- 이전 [Superpowers 작업](history/2026-11-05-superpowers-update.md#review)의 Claude 로그인 후 실제 모델 호출은 당시 미검증이었다. 문서 보관이나 이번 문서 통합으로 통과 처리하지 않는다.
- 과거 설치본의 전역102개·출처132개·새 CLI 발견122개는 [2026-11-06 기록](history/2026-11-06-codex-skills-update.md#review)의 서로 다른 집계다. 현재 설치 수를 다시 측정한 값으로 사용하지 않는다.

일일 업무보고의 실제 새 세션·회귀·합성 비교 결과와 배치 시뮬레이션 제한은 [추가 검증 기록](history/2026-10-15-portable-skill-workflows.md#daily-work-report-verification)에 보존했다.
