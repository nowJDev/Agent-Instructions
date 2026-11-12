<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-11-11-readme-bilingual 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-11-11-readme-bilingual-design.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/3c4dd83a3bf91b687532b4bf346af2374ad6a416/docs/superpowers/specs/2026-11-11-readme-bilingual-design.md).

<!-- 승인된 README 시각 개편과 한·영 안내의 범위 및 완료 기준을 기록한다. -->
<a id="spec--readme-개편과-영어-안내-설계"></a>
### README 개편과 영어 안내 설계.

<a id="spec--승인과-목적"></a>
#### 승인과 목적.

사용자는 2026-11-11에 제시한 상세 설계대로 실행하고 커밋·푸시하도록 승인했다. 한국어 기본과 English 전환을 직접 선택했다. 처음 방문한 사람과 AI가 목적, 시작 프롬프트와 상세 문서 위치를 쉽게 찾도록 한다.

<a id="spec--접근법과-선택"></a>
#### 접근법과 선택.

문서 중심은 유지비가 작지만 시각적 인상이 약하고, 캐릭터 중심은 이미지 관리가 늘어난다. 승인된 작업 흐름 중심 안은 정적 대표 이미지 하나와 짧은 본문을 사용한다. [claude-seo](https://github.com/AgriciDaniel/claude-seo)의 시각적 계층과 [Paseo](https://github.com/getpaseo/paseo)의 언어 전환을 참고하되 그림·문구를 복제하지 않는다.

<a id="spec--파일과-책임"></a>
#### 파일과 책임.

- `README.md`는 한국어 기본 진입점, `README.en.md`는 같은 의미의 영어 안내다.
- 대표 이미지는 `assets/readme/hero-light.svg`, `hero-dark.svg`의 1200×300 정적 SVG다. 외부 폰트·이미지·스크립트를 사용하지 않는다.
- 기존 GUIDE에 상세 작업 흐름·파일 역할·용어 설명이 이미 있으므로 대조 후 없는 설명만 보완한다.
- 실제 스킬·MCP·설치 절차·AGENTS의 한국어 응답 정책과 전역 복제본은 변경하지 않는다.

<a id="spec--구성과-사용자-흐름"></a>
#### 구성과 사용자 흐름.

제목·짧은 설명·언어 링크·CI/MIT 배지·대표 이미지 다음에 시작 프롬프트를 배치한다. 이후 제공 내용, 짧은 작업 흐름, 환경별 적용, 문서 지도, 접이식 FAQ, 라이선스 순서다. 지침 적용 프롬프트는 펼친 상태로, Windows 세팅 요청은 별도 접이식 안내로 제공한다. 조회·진단은 승인된 조사 범위에서 답하며 구현 절차를 강제하지 않는다.

색상은 밝은 배경 `#F6F8FA`, 윤곽 `#243247`, 안내 `#2563EB`, 검증 `#0F766E`, 확인 `#B45309`, 어두운 배경 `#0D1117`을 기준으로 한다. 중요한 설명은 Markdown 본문에도 남기고 모바일에서 작은 그림 글자에 의존하지 않는다.

<a id="spec--언어와-호환성"></a>
#### 언어와 호환성.

두 README는 서로 연결하고 영어 링크에는 하위 한국어 문서임을 표시한다. 시작 프롬프트, 필수 읽기 순서, 적용과 설치의 구분, 한계·라이선스의 의미를 맞춘다. 영어 문서 추가가 에이전트의 한국어 응답 정책을 바꾸지 않는다고 안내한다. 내용 변경 시 같은 커밋에서 두 문서를 검토한다.

기존 README의 H2/H3 fragment 9개를 모두 유지한다. 유지하는 제목은 자동 앵커를 사용하며, 변경·삭제한 제목만 명시 앵커로 대응한다. Windows 세팅 fragment는 접이식 영역 밖의 바로 앞에 둔다. 그림 실패 시 alt와 본문으로 시작할 수 있어야 한다.

<a id="spec--검증과-완료-기준"></a>
#### 검증과 완료 기준.

새 문서·이미지가 없는 기준선에서 실패하는 README 계약 검사를 먼저 확인한다. 기존 문서 링크 검사와 전체 회귀를 실행하고, HTML 언어 링크·밝은/어두운 이미지·fallback 누락을 검출한다. SVG는 XML과 자체 완결성을 검사한다. 실제 GitHub의 데스크톱·모바일·밝은/어두운 화면, 언어 전환과 접이식 안내를 확인한다. 전체 변경을 독립 리뷰한 뒤 main에 병합·푸시하고 원격 SHA·CI를 확인한다.

SVG 이미지와 영어 README는 MIT로 직접 작성한다. 공개 자료만 사용하고 설정·인증·개인 경로는 커밋하지 않는다. 실패하면 작업 브랜치에서 수정·재검증하며 기존 main은 검증 전 변경하지 않는다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-11-11-readme-bilingual.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/3c4dd83a3bf91b687532b4bf346af2374ad6a416/docs/superpowers/plans/2026-11-11-readme-bilingual.md).

<a id="plan--readme-개편과-영어-안내-implementation-plan"></a>
### README 개편과 영어 안내 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 한국어 README를 정리하고 영어 전환과 정적 대표 이미지를 제공한 뒤 검증·커밋·푸시한다.

**Architecture:** 기존 README와 GUIDE의 역할을 유지한다. 두 README가 자체 완결 SVG를 공유하고 기존 링크 검사에 README 전용 HTML 자원 검사를 더한다.

**Tech Stack:** GitHub Markdown, HTML picture/details, SVG, Python 3.12 unittest.

**Spec:** [승인 설계](#spec).

<a id="plan--global-constraints"></a>
#### Global Constraints

- `README.md` 한국어 기본, `README.en.md` 영어 안내를 제공한다.
- 적용 프롬프트와 Windows 세팅 범위를 분리하고 기존 fragment 9개를 보존한다.
- SVG는 1200×300, 정적·자체 완결이며 중요 의미를 본문에도 제공한다.
- 설정·스킬·MCP·응답 언어 정책·전역 복제본은 변경하지 않는다. 의존성을 추가하지 않는다.

<a id="plan--review-focus"></a>
#### Review Focus

- 영어 문서에서 한국어 상세 문서와 응답 정책을 오해하지 않는지 확인한다.
- 기존 fragment와 접힌 세팅 안내의 도착 위치를 확인한다.
- 이미지 실패·모바일·테마에서 시작 프롬프트와 언어 전환을 사용할 수 있는지 확인한다.
- HTML 이미지·언어 링크 누락을 실제 반례로 검출하는지 확인한다.
- GUIDE와 번역에 기존 의미·라이선스·설치 경계가 보존되는지 확인한다.

<a id="plan--task-1-readme-계약-콘텐츠와-대표-이미지"></a>
##### Task 1: README 계약, 콘텐츠와 대표 이미지.

**Files:** `tests/test_readme.py`, `README.md`, `README.en.md`, `assets/readme/hero-light.svg`, `assets/readme/hero-dark.svg`. 기존 GUIDE는 내용 대조 후 필요한 부분만 보완한다.

**Interfaces:** 기존 `anchor_ids`, `link_errors`, `prose_only`를 소비한다. 두 README는 언어 전환, 9개 기존 앵커, 같은 로컬 이미지 경로와 유효한 상세 문서 링크를 제공한다.

- [x] README 언어 전환·기존 앵커·HTML 자원·SVG 검사와 누락 반례를 작성했다.
- [x] `python -X utf8 -B -m unittest discover -s tests -p test_readme.py -v`에서 새 README·이미지 부재로 RED를 확인했다.
- [x] 승인된 구조로 두 README와 SVG를 작성하고 GUIDE와 의미를 대조했다.
- [x] 대상4개와 전체84개 회귀가 통과했다.

<a id="plan--task-2-검증-기록과-배포"></a>
##### Task 2: 검증, 기록과 배포.

**Files:** `docs/reviews/2026-11-11-readme-bilingual.md`, `docs/current-state.md`, `docs/design-progress-checklist.md`, 본 계획. CI 운영 안내는 검사 범위 변경만 반영한다.

**Interfaces:** Task 1의 README와 검사 결과를 받아 실제 GitHub 화면·배포 결과를 검증한다.

- [x] 전체 변경의 독립 리뷰와 로컬 SVG·테마 및 실제 GitHub 작은 화면 확인을 마쳤다.
- [x] 결과와 한계를 기록하고 `git diff --check` 및 전체84개 회귀·skip0을 확인했다.
- [x] 한글 메시지로 커밋하고 main에 fast-forward 병합·일반 푸시했다.
- [x] 원격 SHA·실제 GitHub 한·영 화면·두 OS CI를 확인하고 소유한 임시 worktree를 정리했다.

<a id="plan--실행-원장"></a>
#### 실행 원장.

- 기준선은 `090a4c0`이며 사용자는 설계 실행·커밋·푸시를 승인했다.
- Task 1의 문서·이미지가 Task 2의 화면 검증 입력이며 인터페이스 충돌은 없다.
- Task 1: complete. 새 문서·이미지 부재 RED와 기존 앵커 오타 재현 후 GREEN, Windows Python 3.12 전체84개 통과·skip0을 확인했다.
- GUIDE의 기존 상세 작업 흐름·파일 역할·용어 설명으로 축약 내용을 설명할 수 있어 GUIDE는 보존했다.
- Task 2: complete. 구현5278e2a의 원격 SHA·실제 GitHub 전환·390px 모바일·light/dark 표시와 두 OS CI 성공을 확인했다. 임시 작업 공간을 정리했으며 후속 기록 커밋의 원격 확인은 최종 보고로 남긴다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-11-11-readme-bilingual.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/3c4dd83a3bf91b687532b4bf346af2374ad6a416/docs/reviews/2026-11-11-readme-bilingual.md).

<!-- README 개편의 자동 검사·독립 리뷰와 실제 배포 확인 결과를 기록한다. -->
<a id="review--readme-개편과-영어-안내-검증"></a>
### README 개편과 영어 안내 검증.

<a id="review--범위와-승인"></a>
#### 범위와 승인.

기준선은 `090a4c0`이다. 사용자는 [설계](#spec)에 따른 실행과 커밋·푸시를 승인했다. [계획](#plan)에 따라 한국어 README, 영어 README, 대표 이미지와 검사·운영 문서를 변경한다. 설정·스킬·MCP·AGENTS·GUIDE와 전역 복제본은 보존한다.

<a id="review--자동-검증"></a>
#### 자동 검증.

- Windows Python 3.12에서 README 계약4개를 먼저 실행해 영어 문서·이미지 부재로 RED를 확인했다.
- 누락된 dark 이미지·다중 srcset·fallback·영어 링크4개가 검출되며 fenced/inline 예시는 제외된다.
- 기존 앵커 오타1개를 실제 실패로 확인하고 수정해 기존 fragment9개를 보존했다.
- `python -X utf8 -B -m unittest discover -s tests -v`는84개 통과, 실패·오류·skip0이며25.008초가 걸렸다. 패키지 내부 daily-work-report 회귀16개는 별도로 호출된다.
- SVG2개는 XML·1200×300 viewBox·정적 자체 완결성과 title/desc를 검사했다.

<a id="review--독립-리뷰와-화면-확인"></a>
#### 독립 리뷰와 화면 확인.

별도 리뷰어가 기준선부터 전체 변경과 신규 파일을 읽고 확정 결함을 발견하지 못했다. 한·영 의미, 적용과 설치의 구분, 한국어 문서·응답 정책 안내, 기존 fragment, HTML 누락 반례와 변경 경계를 확인했다. 리뷰어가 직접 실행한 README4개·문서8개 검사와 `git diff --check`도 통과했다.

Chrome에서 로컬 light/dark SVG를 각각 렌더·캡처해 문서·연결선·체크 표시와 글자 잘림이 없는지 확인했다. 실제 GitHub에서도 밝은·어두운 테마에 맞는 이미지가 로드되며, 1440px 데스크톱과390px 모바일에서 제목·소개·언어 전환·시작 안내를 확인했다.

<a id="review--배포-확인"></a>
#### 배포 확인.

- 구현 커밋 `5278e2a979fc680bbfde9ea3765d87768b0d5029`를 main에 fast-forward 병합·일반 push했다. 로컬 HEAD와 `git ls-remote origin refs/heads/main`이 일치했다.
- [구현 커밋 CI](https://github.com/nowJDev/Agent-Instructions/actions/runs/42934511908)의 `Regression (ubuntu-latest)`와 `Regression (windows-latest)`가 모두 success다.
- 실제 GitHub의 English 링크와 한국어 링크를 차례로 클릭해 두 README의 시작 프롬프트가 표시되는지 확인했다. 각 언어의 Windows 세팅 summary도 클릭해 해당 프롬프트가 펼쳐지는지 확인했다.
- 기존 fragment9개가 GitHub DOM에도 존재한다. 1440px 데스크톱의 문서 폭은838px이며390px 모바일의 문서 폭은324px, 전체 페이지 폭은390px로 가로 넘침이 없다. 코드블록은 GitHub 기본 내부 가로 스크롤을 사용한다.
- 대표 이미지를 임시로 숨겨도 적용 프롬프트와 언어 전환을 사용할 수 있음을 확인했다. 밝은 데스크톱과 어두운 모바일 캡처를 직접 읽었다.
- 생성한 브라우저 탭3개·캡처3개·작업 브랜치·worktree를 정리했다. 기존 사용자 탭과 파일은 보존했다. 배포 확인 기록의 후속 커밋 SHA와 CI는 최종 보고에서 확인한다.

<a id="review--검증-경계"></a>
#### 검증 경계.

영어 제공 범위는 README다. 상세 운영 문서·한국어 응답 정책·사용자 전역 복제본은 이번 작업에서 변경하지 않는다. HTML 검사는 이 README의 단순 href/src/srcset 사용법을 대상으로 하며 전체 HTML·CommonMark·SVG 보안 표준 검증기가 아니다. 실제 CLI 설치나 서비스 인증도 재실행하지 않았다.
