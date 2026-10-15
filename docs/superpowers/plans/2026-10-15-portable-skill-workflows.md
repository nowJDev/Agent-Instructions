<!-- 범용 스킬 반영의 파일·검증·통합 순서를 기록한다. -->
# 범용 스킬 원본 반영 계획.

> **For agentic workers:** 승인된 범위에서 독립 패키지를 분담하고 결과를 직접 검토한다.

**Goal:** 보강한 23개 절차를 공개 가능한 원본과 PC 전역에 함께 반영한다.

**Architecture:** 자체 작성 SKILL.md는 Owned-Skills, 공개 출처는 문서 링크, 개인 참조와 타사 원문은 사용자 환경에서 관리한다.

**Tech Stack:** Markdown, Python 표준 unittest, Git, Windows 사용자 스킬 경로.

## Task 1. 기준선과 패키지.
- [x] 기준선·원격·사용자 변경과 23개 설치 본문, 공개 정책을 확인한다.
- [x] 기존 23개 자체 패키지가 없는 상태를 RED 기준으로 확인한다.
- [x] Owned-Skills 아래 23개 SKILL.md를 자기완결 범용 절차로 작성한다.
- [x] tests/test_owned_skill_packages.py로 이름·frontmatter·링크·공개 경계를 검사한다.

## Task 2. 설치와 안내.
- [x] Owned-Skills/README.md, PORTABILITY.md, Skill/README.md, README.md, CHANGELOG.md를 연결한다.
- [x] 사용자 전역 적용 전 대상과 설정 해시를 비공개 백업하고 Codex·Claude에 적용한다.
- [x] 복사한 전역 문서와 개인 예외·기존 리소스·보호 설정을 대조한다.

## Task 3. 검증과 통합.
- [x] py -3.12 -X utf8 -B -m unittest discover -s tests -v 전체 회귀를 통과한다.
- [x] 전체 변경 리뷰·문서 검증·공개 정보 검사를 완료한다.
- [ ] 한글 커밋·main 통합·일반 push와 원격 SHA 대조를 완료한다.
- [ ] 병합된 작업 브랜치와 참조 없는 중간 산출물을 정리하고 복구 백업을 보존한다.
