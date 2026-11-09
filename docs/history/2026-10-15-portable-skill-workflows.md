<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-15-portable-skill-workflows 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="spec"></a>
## 이전 설계 원문.

원본 경로: `docs/superpowers/specs/2026-10-15-portable-skill-workflows.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/specs/2026-10-15-portable-skill-workflows.md).

<!-- 범용 스킬 원본과 전역 적용의 승인 범위를 기록한다. -->
<a id="spec--범용-스킬-원본과-전역-적용-설계"></a>
### 범용 스킬 원본과 전역 적용 설계.

<a id="spec--목표와-승인"></a>
#### 목표와 승인.
사용자는 앞서 보강한 23개 스킬을 저장소와 PC 전역에 적용하고 전체 커밋·푸시·필요한 병합과 안전한 정리를 요청했다. 이 요청 안에서 자체 작성 절차를 공개 원본으로 보관하고 Codex·Claude Code 사용자 스킬에 적용한다.

<a id="spec--기준선과-책임"></a>
#### 기준선과 책임.
기준선은 78252cd5fef3a24d800c17061f0d0a03cfc9402d다. 기존 Skill/는 99개 이름의 카탈로그이며 실행 패키지가 아니다. 기존 Owned-Skills/design-driven-delivery는 유지하고 보강 대상 23개만 자체 작성 범용 절차로 추가한다. 같은 이름의 Claude 내장 기능이나 타사 플러그인을 복제하지 않는다.

<a id="spec--접근-선택과-공개-경계"></a>
#### 접근 선택과 공개 경계.
PC 전역 패키지 전체를 복사하면 타사 원문과 개인 참조까지 공개된다. 설치 자동화와 원본 다운로드기를 새로 만드는 방식은 이번 적용에 불필요하다. 따라서 자체 작성한 SKILL.md만 공개하고 타사 문서는 공개 출처 링크로 연결한다. 다른 스킬은 이름으로 재사용하되 없을 때도 핵심 절차를 수행하거나 지원 부재를 보고하도록 한다. Figma 쓰기는 필요한 도구·필수 가이드가 없으면 초안으로 한정한다.

<a id="spec--적용-흐름과-실패"></a>
#### 적용 흐름과 실패.
패키지와 문서 검증 후 사용자 전역 대상 파일을 비공개 위치에 백업하고 변경된 원본 파일만 복사한다. 기존 타사 참조·개인 스킬·설정은 보존한다. 개인 기본 출력 위치와 비공개 리뷰 참조는 전역에만 별도로 연결한다. 기존 파일이 조사 후 바뀌었거나 경로가 외부를 가리키면 덮어쓰지 않는다. 복사 실패는 이번에 바꾼 파일만 복구한다.

Codex는 기존 이름을 유지한다. Claude Code의 새 22개는 portable- 접두어로 디렉터리·name·본문 스킬명 참조를 맞춰 내장 명령을 보존한다. 기존 사용자 스킬 claude-news만 기존 이름으로 업데이트한다. 이식 이름과 파일 해시는 비공개 적용 기록에 남긴다.

전역 지침의 문서 복사본도 저장소 추적 파일과 대조해 갱신한다. MCP·권한·hooks·모델 설정은 변경 대상이 아니다. 새 세션의 실제 발견·호출은 파일 배치 검증과 구분한다.

<a id="spec--검증과-완료-조건"></a>
#### 검증과 완료 조건.
- 23개 패키지의 이름·frontmatter·자기완결 링크·공개 정보 경계를 검사한다.
- 기존 전체 회귀와 새 패키지 검사를 실행하고 전체 diff를 검토한다.
- Codex·Claude 전역 파일 해시와 개인 예외, 보호 설정 보존을 확인한다.
- 검증한 변경을 한글 커밋으로 통합·일반 push하고 원격 SHA를 대조한다.
- 병합된 작업 브랜치와 복구에 불필요한 중간 산출물만 정리한다. 원본·개인 자료·복구 백업을 보존한다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-15-portable-skill-workflows.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-15-portable-skill-workflows.md).

<!-- 범용 스킬 반영의 파일·검증·통합 순서를 기록한다. -->
<a id="plan--범용-스킬-원본-반영-계획"></a>
### 범용 스킬 원본 반영 계획.

> **For agentic workers:** 승인된 범위에서 독립 패키지를 분담하고 결과를 직접 검토한다.

**Goal:** 보강한 23개 절차를 공개 가능한 원본과 PC 전역에 함께 반영한다.

**Architecture:** 자체 작성 SKILL.md는 Owned-Skills, 공개 출처는 문서 링크, 개인 참조와 타사 원문은 사용자 환경에서 관리한다.

**Tech Stack:** Markdown, Python 표준 unittest, Git, Windows 사용자 스킬 경로.

<a id="plan--task-1-기준선과-패키지"></a>
#### Task 1. 기준선과 패키지.
- [x] 기준선·원격·사용자 변경과 23개 설치 본문, 공개 정책을 확인한다.
- [x] 기존 23개 자체 패키지가 없는 상태를 RED 기준으로 확인한다.
- [x] Owned-Skills 아래 23개 SKILL.md를 자기완결 범용 절차로 작성한다.
- [x] tests/test_owned_skill_packages.py로 이름·frontmatter·링크·공개 경계를 검사한다.

<a id="plan--task-2-설치와-안내"></a>
#### Task 2. 설치와 안내.
- [x] Owned-Skills/README.md, PORTABILITY.md, Skill/README.md, README.md, CHANGELOG.md를 연결한다.
- [x] 사용자 전역 적용 전 대상과 설정 해시를 비공개 백업하고 Codex·Claude에 적용한다.
- [x] 복사한 전역 문서와 개인 예외·기존 리소스·보호 설정을 대조한다.

<a id="plan--task-3-검증과-통합"></a>
#### Task 3. 검증과 통합.
- [x] py -3.12 -X utf8 -B -m unittest discover -s tests -v 전체 회귀를 통과한다.
- [x] 전체 변경 리뷰·문서 검증·공개 정보 검사를 완료한다.
- [x] 한글 커밋·main 통합·일반 push와 원격 SHA 대조를 완료한다.
- [x] 병합된 작업 브랜치와 참조 없는 중간 산출물을 정리하고 복구 백업을 보존한다.

통합 증거는 구현 커밋 8d660a77d4f8e36adad37cfea95befaaa76cc839의 main fast-forward 통합·일반 push·원격 SHA 일치와 병합된 작업 브랜치 삭제다. 통합 main 전체 71개가 통과했다. 생성한 추가 worktree는 없으며 원래 작업 경로와 복구 백업은 유지했다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-15-portable-skill-workflows.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-15-portable-skill-workflows.md).

<!-- 범용 스킬 원본 반영의 검증 범위와 한계를 기록한다. -->
<a id="review--범용-스킬-원본-반영-검토"></a>
### 범용 스킬 원본 반영 검토.

<a id="review--범위와-결과"></a>
#### 범위와 결과.
기준선은 78252cd5fef3a24d800c17061f0d0a03cfc9402d다. 자체 작성 23개 스킬과 공개 출처·설치·이식 안내, 패키지 계약 검사를 추가했다. 기존 전달 스킬과 카탈로그 이름 수는 유지한다. 타사 원문·개인 설정·비공개 참조는 공개 변경에 포함하지 않는다.

<a id="review--검증"></a>
#### 검증.
- Windows Python 3.12.10 전체 회귀 명령 py -3.12 -X utf8 -B -m unittest discover -s tests -v에서 71개 전부 통과했다. 실패·오류·skip은 0개이며 실행 시간은 19.737초다.
- 새 패키지 계약 검사 7개가 23개 이름·제한된 frontmatter 형식·내부 링크·공개 HTTPS·비공개 경계와 검사 함수의 반례를 확인했다. 전체 YAML 표준 파서는 아니며 설치 전 별도 YAML parser로 실제 46개 양쪽 본문을 확인했다.
- Codex는 기존 이름으로, Claude는 새 22개에 portable- 접두어를 적용하고 기존 claude-news만 같은 이름으로 보강했다. 65개 배치 파일과 실제 로컬 링크를 대조했고 기존 비대상 파일·보호 설정 해시가 유지됐다. 개인 기본 위치와 선택 점검은 전역에서만 연결했다.
- 별도의 의도적 결함 CLI fixture를 새 run·verify·code-review 절차로 확인했다. 명령 4개를 실행해 종료코드 0인 계산 오류와 단위검사 1통과·1실패를 올바르게 구분했다. fixture 변경·남은 자체 프로세스·외부 전송은 없었다. 이는 스킬의 판정 검증이며 결함이 있는 fixture가 통과했다는 뜻이 아니다.
- 변경 파일의 UTF-8·BOM 부재·개인 식별 문자열·실제 비밀 후보·문서 링크와 git diff --check를 확인했다. 원문 덤프나 실제 개인 값을 공개 기록에 넣지 않았다.

<a id="review--독립-검토와-수정"></a>
#### 독립 검토와 수정.
담당자가 작성하지 않은 패키지·참조와 테스트·설치 문서를 교차 검토했다. 공개 테스트에 들어간 개인 식별 문자열은 범용 패턴으로 교체했다. 잘못된 YAML scalar가 통과하던 검사는 엄격한 단일행 문자열 형식과 실패 반례로 보완했다. Claude 이름 변환 후 원본 해시 일치를 요구하던 설명은 변환한 예상본·허용 diff와 대조하도록 수정했다.

Figma의 필수 도구·스킬 부재 시 초안 제한, 현재 호출 소유 ID만 처리하는 경계, 부분실패 재확인이 유지됐다. 세션 삭제의 선택·소유권·경로·백업 조건과 Ralph 유한 횟수·호스트 차이를 확인했다. 검토 범위에서 남은 차단 결함을 발견하지 못했다.

<a id="review--실제로-확인하지-않은-범위"></a>
#### 실제로 확인하지 않은 범위.
새 앱 세션에서의 발견·호출, 실제 Figma 쓰기·SDK 인증·모델 응답·예약·native 취소는 수행하지 않았다. 이들 외부 기능을 설치·배치 또는 정적 검사만으로 성공했다고 보고하지 않는다. 외부 문서의 모든 링크 도달성을 정기 점검하는 기능도 이번 범위에 없다.

<a id="review--통합"></a>
#### 통합.
구현 커밋 8d660a77d4f8e36adad37cfea95befaaa76cc839를 main에 fast-forward 통합했다. 통합 main에서 전체 71개를 다시 실행해 20.036초에 전부 통과했고, 일반 push 후 원격 main SHA와 일치함을 확인했다. 병합된 작업 브랜치만 삭제했고 추가 worktree는 생성하지 않았다. 전역 문서 복사본 243개의 일치와 개인 추가 문서 1개 보존을 확인했다. 일회성 적용 스크립트·커밋 메시지 파일은 최종 검증 후 정리하며 복구 백업과 개인 파일은 보존한다.

구현 main의 [실제 GitHub CI](https://github.com/nowJDev/Agent-Instructions/actions/runs/38704158560)도 두 OS에서 성공했다. Ubuntu는 전체 71개 중 67개 통과·Windows 전용 4개 의도적 skip, Windows는 71개 전부 통과했다.

<a id="daily-work-report-verification"></a>
## 2026-11-03 daily-work-report 추가 검증.

추가 기록 출처는 기준 커밋 a559c66의 docs/current-state.md다. 아래는 스킬 추가 후 당시의 검증·제한 원문이다.

2026-11-03에 [daily-work-report](../../Owned-Skills/daily-work-report/SKILL.md)를 추가했다. 로컬 지정 자료를 읽고 다음 메시지의 업무명·형식으로 작성하며 검사기와 합성 fixture를 포함한다. 실제 사용자 계정의 app-server skills/list에서 사용자 홈 밖을 포함한 세 작업 경로의 전역 발견·활성을 확인했다. Codex CLI의 읽기 전용 새 세션과 resume으로 STEP 1 대기·STEP 2의 12줄 보고서 및 원본 SHA 불변을 확인했다. 저장소 전체 회귀 72개와 패키지 회귀 16개가 통과했다. 별도 합성 비교는 스킬 사용 15/15, 미사용 13/15 assertion을 통과했으며 일부 후속·새 대화·오류 조건은 배치 시뮬레이션이다. 초기 샌드박스 계정의 로그인·탐색 결과는 실제 사용자 계정 검증 결과와 구분한다. 구현 당시 보류했던 커밋·푸시는 사용자의 후속 승인으로 진행한다.
