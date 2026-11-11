<!-- 최신 작업과 이전 문서 통합의 구현·검증·배포 결과를 추적한다. -->
# 설계 진행 체크리스트.

## 2026-11-11 Unity MCP 추가.

[설계](superpowers/specs/2026-11-11-coplay-funplay-unity-mcp-design.md), [계획](superpowers/plans/2026-11-11-coplay-funplay-unity-mcp.md), [검증 기록](reviews/2026-11-11-coplay-funplay-unity-mcp.md)에 실제 진행 상태를 기록한다.

- [x] 두 Unity MCP의 전역 설치와 저장소 추가 요청·기존 설정 보존 범위를 확인했다.
- [x] MCP 목차·이식 표·통합 설치 안내를 작성했다.
- [x] 프로젝트 설치 연기와 스킬 지침 요청을 반영해 자기완결 `coplay-funplay-unity-mcp-setup`을 추가했다.
- [x] CoplayDev/unity-mcp 전역 서버 10.3.0·Codex 등록·MCP 도구 48개와 기존 설정 보존을 확인했다.
- [x] 문서 전체 84개 회귀·내부 링크·자체 리뷰·스킬 유효성 검사를 마쳤다.
- [x] 제작자 식별자 적용 후 전역 설정 동일성·SDK 도구 48개를 재검증하고 스킬·문서 해시와 중복 정리를 확인했다.
- [x] 새 Codex 프로세스에서 새 스킬 이름·enabled·사용자 범위·실제 경로·본문을 확인했다.
- [x] 독립 리뷰의 자동 Configure 키 중복 조건을 반영해 요청한 서버만 재사용·정리하도록 보강했다.

FunplayAI/funplay-unity-mcp 주소 등록·프로젝트별 패키지·실제 Unity 연결은 사용자가 나중으로 미뤘다. 실제 모델 호출·Codex 세션의 MCP 도구 발견은 미검증이며 SDK 프로토콜 검사·새 프로세스 스킬 발견과 구분한다. 저장소 커밋·로컬 통합은 최종 확인 대상이고 원격 push는 범위 밖이다.

## 2026-11-11 README 개편.

[승인 설계](superpowers/specs/2026-11-11-readme-bilingual-design.md), [실행 계획](superpowers/plans/2026-11-11-readme-bilingual.md), [검증 기록](reviews/2026-11-11-readme-bilingual.md)에 현재 작업의 범위와 증거를 기록한다.

- [x] 한국어 기본·영어 전환·시각 개편과 커밋·푸시 승인을 확인했다.
- [x] 한·영 README·light/dark SVG를 작성하고 기존 fragment9개·설정·GUIDE를 보존했다.
- [x] 새 검사 RED→GREEN과 전체84개 회귀·독립 리뷰·로컬 SVG 확인을 마쳤다.
- [x] 구현 커밋5278e2a의 main 병합·푸시와 원격 SHA 일치를 확인했다.
- [x] 실제 GitHub의 한·영 전환·모바일·테마·접이식 안내와 두 OS CI 성공을 확인했다.
- [x] 검증·배포 기록을 갱신하고 소유한 임시 worktree·브랜치·탭·캡처를 정리했다.

## 이전 문서 통합 작업의 결과.

대상은 [문서 통합과 글로벌 적용](superpowers/specs/2026-11-09-document-consolidation-design.md)이다. [실행 계획](superpowers/plans/2026-11-09-document-consolidation.md)과 [검증 기록](reviews/2026-11-09-document-consolidation.md)에 실제 증거를 남겼다. 이전 작업은 [보관 목차](history/README.md)에서 확인한다.

- [x] 사용자 설계 실행·글로벌 적용·저장소 커밋·push 승인을 확인했다.
- [x] 카탈로그121개와 과거37개 원문을 보존 통합하고 원래 코드 예제를 대조했다.
- [x] 구조 검사 RED→GREEN, HF 안전 회귀와 리뷰 반례3개를 검증했다.
- [x] 전체80개 회귀·내부 링크·인코딩·보호 해시·수동 표시·독립 리뷰 수정 검증을 마쳤다.
- [x] 로컬 main 통합과 글로벌 문서·개인 규칙 보존 배포를 검증했다.
- [x] 실제 새 세션의 글로벌 지침과 새 카탈로그 로드를 확인했다.
- [x] 구현 커밋의 GitHub push·원격 SHA와 두 OS CI 성공을 확인했다.
- [x] 병합된 임시 브랜치·worktree 등록·내용 파일을 정리하고 복구 백업을 보존했다.

비어 있는 임시 폴더 하나는 운영체제 프로세스 잠금으로 남았다. 데이터·브랜치·Git 등록은 남아 있지 않으며 사용자 앱을 강제 종료하지 않았다. 최종 기록 커밋의 원격 SHA·CI는 실제 GitHub 결과와 최종 보고로 확인한다.
