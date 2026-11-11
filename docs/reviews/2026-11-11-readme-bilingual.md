<!-- README 개편의 자동 검사·독립 리뷰와 실제 배포 확인 결과를 기록한다. -->
# README 개편과 영어 안내 검증.

## 범위와 승인.

기준선은 `090a4c0`이다. 사용자는 [설계](../superpowers/specs/2026-11-11-readme-bilingual-design.md)에 따른 실행과 커밋·푸시를 승인했다. [계획](../superpowers/plans/2026-11-11-readme-bilingual.md)에 따라 한국어 README, 영어 README, 대표 이미지와 검사·운영 문서를 변경한다. 설정·스킬·MCP·AGENTS·GUIDE와 전역 복제본은 보존한다.

## 자동 검증.

- Windows Python 3.12에서 README 계약4개를 먼저 실행해 영어 문서·이미지 부재로 RED를 확인했다.
- 누락된 dark 이미지·다중 srcset·fallback·영어 링크4개가 검출되며 fenced/inline 예시는 제외된다.
- 기존 앵커 오타1개를 실제 실패로 확인하고 수정해 기존 fragment9개를 보존했다.
- `python -X utf8 -B -m unittest discover -s tests -v`는84개 통과, 실패·오류·skip0이며25.008초가 걸렸다. 패키지 내부 daily-work-report 회귀16개는 별도로 호출된다.
- SVG2개는 XML·1200×300 viewBox·정적 자체 완결성과 title/desc를 검사했다.

## 독립 리뷰와 화면 확인.

별도 리뷰어가 기준선부터 전체 변경과 신규 파일을 읽고 확정 결함을 발견하지 못했다. 한·영 의미, 적용과 설치의 구분, 한국어 문서·응답 정책 안내, 기존 fragment, HTML 누락 반례와 변경 경계를 확인했다. 리뷰어가 직접 실행한 README4개·문서8개 검사와 `git diff --check`도 통과했다.

Chrome에서 로컬 light/dark SVG를 각각 렌더·캡처해 문서·연결선·체크 표시와 글자 잘림이 없는지 확인했다. 실제 GitHub에서도 밝은·어두운 테마에 맞는 이미지가 로드되며, 1440px 데스크톱과390px 모바일에서 제목·소개·언어 전환·시작 안내를 확인했다.

## 배포 확인.

- 구현 커밋 `5278e2a979fc680bbfde9ea3765d87768b0d5029`를 main에 fast-forward 병합·일반 push했다. 로컬 HEAD와 `git ls-remote origin refs/heads/main`이 일치했다.
- [구현 커밋 CI](https://github.com/nowJDev/Agent-Instructions/actions/runs/42934511908)의 `Regression (ubuntu-latest)`와 `Regression (windows-latest)`가 모두 success다.
- 실제 GitHub의 English 링크와 한국어 링크를 차례로 클릭해 두 README의 시작 프롬프트가 표시되는지 확인했다. 각 언어의 Windows 세팅 summary도 클릭해 해당 프롬프트가 펼쳐지는지 확인했다.
- 기존 fragment9개가 GitHub DOM에도 존재한다. 1440px 데스크톱의 문서 폭은838px이며390px 모바일의 문서 폭은324px, 전체 페이지 폭은390px로 가로 넘침이 없다. 코드블록은 GitHub 기본 내부 가로 스크롤을 사용한다.
- 대표 이미지를 임시로 숨겨도 적용 프롬프트와 언어 전환을 사용할 수 있음을 확인했다. 밝은 데스크톱과 어두운 모바일 캡처를 직접 읽었다.
- 생성한 브라우저 탭3개·캡처3개·작업 브랜치·worktree를 정리했다. 기존 사용자 탭과 파일은 보존했다. 배포 확인 기록의 후속 커밋 SHA와 CI는 최종 보고에서 확인한다.

## 검증 경계.

영어 제공 범위는 README다. 상세 운영 문서·한국어 응답 정책·사용자 전역 복제본은 이번 작업에서 변경하지 않는다. HTML 검사는 이 README의 단순 href/src/srcset 사용법을 대상으로 하며 전체 HTML·CommonMark·SVG 보안 표준 검증기가 아니다. 실제 CLI 설치나 서비스 인증도 재실행하지 않았다.
