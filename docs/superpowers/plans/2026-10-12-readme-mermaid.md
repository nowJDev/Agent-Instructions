<!-- README 소개와 작동 구조를 정리하는 구현 계획을 기록한다. -->
# README 정리 구현 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 단계는 체크박스로 관리한다.

## Goal.

사용자가 승인한 구성 관계·요청 처리 Mermaid 그림 두 개를 포함하고, context-forge처럼 소개부터 사용법까지 읽기 쉬운 README로 정리한다.

## Architecture.

README와 CHANGELOG를 수정한다. 기존 §0~9와 §5.5, 상세 카탈로그·보안·이식 안내는 유지한다. 긴 목록은 details로 접는다. 실제 지침과 도구 동작은 변경하지 않는다. 설계와 정리 범위는 사용자 대화에서 승인됐다.

## Tech Stack.

GitHub Markdown, Mermaid flowchart, HTML details. 실행 코드 변경이 없어 TDD 대신 문서 링크·문법·렌더링을 검증한다. 별도 프로젝트 의존성을 추가하지 않는다.

## Task 1. README와 변경 이력 정리.

Files: Modify README.md, CHANGELOG.md.

- [x] 소개·바로가기·Quick Start를 간결하게 정리한다.
- [x] Quick Start 다음에 구성 관계 다이어그램을 넣는다.
- [x] §2에 조회·진단·모니터링·상태 변경 분기와 승인·검증·리뷰·복귀 흐름을 넣는다.
- [x] 기존 섹션과 카탈로그를 보존하고 긴 목록을 details로 접는다.
- [x] CHANGELOG에 2026-10-12 변경을 기록한다.

## Task 2. 검증·리뷰.

Files: Verify README.md, CHANGELOG.md, this plan.

- [x] 상대 링크와 앵커, 코드 펜스, details 균형, 카탈로그 수치를 검사한다. 기대 결과는 누락 0개다.
- [x] Mermaid 두 블록을 파싱·렌더링하고 실제 배치와 텍스트 가독성을 확인한다.
- [x] 전체 diff를 승인 설계·기존 지침과 대조해 리뷰한다.
- [x] git diff --check를 실행한다. 기대 결과는 exit 0이다.

## 커밋·통합 절차.

검증을 마친 관련 세 문서만 한글 제목·bullet 본문으로 커밋하고 git status와 git show --stat을 확인한다. main에 반영한 뒤 origin/main으로 일반 push하고 git ls-remote 결과와 로컬 HEAD를 비교한다. 커밋·푸시 결과는 Git 이력과 원격 브랜치에서 확인한다.

## 범위 밖.

index.html, AGENTS.md, 설치 스킬, 전역 복제본은 변경하지 않는다. 사용자가 전체 커밋과 푸시를 추가 요청했다. 검증·리뷰 후 기본 브랜치 main에 반영하고 origin/main에 푸시한다.

## 검증 증거.

- 기존 번호 섹션 11개와 그룹별 전체 스킬 목록을 보존했다.
- 상대 링크·앵커 48개를 검사했으며 누락은 0개다.
- 활성 스킬 99개와 OFF 22개를 실제 추적 파일 수와 대조했다.
- Mermaid 10.9.3으로 두 블록의 파싱과 SVG 렌더링이 통과했다.
- Edge 브라우저에서 다이어그램과 README 상단을 확인했고 페이지 오류는 0개다.
- details 네 개의 균형과 스킬 목록 펼치기·접기를 확인했다.
- 별도 읽기 전용 리뷰에서 확실한 지침·링크·Markdown 결함을 발견하지 못했다.
- git diff --check가 exit 0으로 통과했다.
