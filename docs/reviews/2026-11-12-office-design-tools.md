<!-- 전역 설치·원본 보존·실제 샘플 검증과 공개 배포의 증거를 기록한다. -->
# Office·디자인 도구 세 가지의 설치와 검증.

## 요청과 설치.

사용자는 [PPT Master](https://github.com/hugohe3/ppt-master), [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI), [Huashu Design](https://github.com/alchaincyf/huashu-design)의 PC 전역 설치와 Agent-Instructions 반영·커밋·push를 요청했다. [설계](../superpowers/specs/2026-11-12-office-design-tools-design.md)와 [계획](../superpowers/plans/2026-11-12-office-design-tools.md)에 따라 기존 전역 실행본·공개 설명 분리 방식을 유지한다. 타사 원문·대형 자산·바이너리·종속성·샘플·원문 로그는 공개 커밋에 넣지 않는다.

| 항목. | 고정 원본과 설치. | 보존과 정책. |
|---|---|---|
| PPT Master. | 커밋 `e2820d326d049f1fcbe90523983def3d52280233`, metadata 6.9.0, `skills/ppt-master` 전체를 `~/.agents/skills/ppt-master`에 설치했다. | 원본 13,091파일·39,915,468바이트를 Git blob과 대조했다. MIT·SPONSORS·attribution guard를 보존했다. |
| OfficeCLI. | v1.0.160의 커밋 `c56512c8c7b76fe284f09940e4cd492470099d3e` 스킬 하나와 Windows x64 바이너리를 설치했다. | 릴리스 SHA256·크기 33,546,152바이트와 일치했다. Apache-2.0·NOTICE·제3자 고지를 실행본 옆에 보존했다. |
| Huashu Design. | 커밋 `e8d1148a80d5a281d4247cffe320add3df017928`, 버전 3.3.0, 루트 전체를 `~/.agents/skills/huashu-design`에 설치했다. | 원본 445파일·43,450,899바이트를 Git blob과 대조했다. MIT 및 스티커 22개의 PolyForm Shield 1.0.0 예외를 보존했다. |

세 이름은 기존 설치 조사에서 발견되지 않았다. 세 패키지의 본문을 변경하지 않고 별도 `agents/openai.yaml`에서 명시 호출 전용으로 설정했다. 스킬은 `$ppt-master`, `$officecli`, `$huashu-design`으로 호출한다. 실제 원본·실행 파일의 SHA256은 [고정 명세](../../references/office-design-tools.lock.json)에 기록했다. 새 범용 설치기는 만들지 않고 Codex의 표준 skill-installer를 사용했다.

OfficeCLI는 사용자 도구 폴더에 설치하고 해당 사용자 PATH 항목 하나만 추가했다. `OFFICECLI_SKIP_UPDATE=1`, `OFFICECLI_NO_AUTO_INSTALL=1` 두 전용 사용자 환경변수로 자동 갱신·다른 클라이언트 스킬 설치를 막았다. 공식 일괄 설치·`officecli install`·MCP 등록은 실행하지 않았다. 기계 전체 PATH·인증·기존 스킬·권한은 변경하지 않았다. 저장된 사용자 환경으로 구성한 프로세스에서 전역 `officecli`가 기대 경로와 버전 1.0.160을 찾는 것을 별도 확인했다.

## 실제 작업 검증.

### PPT Master.

전용 Python 3.12 venv에 공식 requirements를 설치하고 `pip check`·원본 attribution guard를 통과했다. 닫힌 합성 브리프와 SVG 3장으로 원본 canonical Quick 최종 검사·native export를 실행했다. blocking 0·exit 0·quality gate passed이며, root fill을 의미 있는 그룹으로 옮기라는 advisory 3개를 보존했다. 경고가 없었다고 하지 않는다.

생성 PPTX는 16:9·3장이며 기대 문장 9개, 장당 native leaf shape 4개, 슬라이드 이미지 0개를 재열어 확인했다. 필수 최종 품질 보고서가 없는 입력은 원본 exporter가 exit 1로 거부하고 PPTX를 만들지 않았다. 초기 검사기가 그룹 내부 텍스트를 놓친 오류는 검사기만 재귀 탐색으로 고쳤고 원본 스킬은 바꾸지 않았다. SVG 미리보기 3장을 렌더·확인했지만 MuPDF의 폰트 대체가 보여 실제 PowerPoint 렌더 증거와 구분한다.

### OfficeCLI.

원본 `SKILL.md`와 바이너리의 word·pptx·excel 규칙을 읽고 합성 DOCX·PPTX·XLSX를 생성·편집·조회했다. 세 파일의 OpenXML validate는 오류 0이며 독립 재열기로 저장 내용을 대조했다. XLSX의 42,000+45,000+48,000 합계 수식은 캐시 135,000이고 비율 수식도 별도 검산했다. 잘못된 sheet를 포함한 atomic batch는 실패·rollback을 반환해 변경 파일 동일성을 검사했다.

독립 assertion 30개와 HTML 3개·PNG 4개를 확인했다. PPTX PNG 2장은 별도 실행자의 시각 검사도 통과했다. 차트의 기본 범례 여백은 샘플만 보정하고 다시 검사했다. HTML 렌더 경로를 명시해 Office COM을 사용하지 않았다. DOCX 들여쓰기 권고는 블록 문단 스타일에서 예상되는 7개를 구분하며 PPTX·XLSX issues는 0개다. 149개 명령 기록에는 반복 QA와 의도된 실패가 포함돼 있으므로 테스트 수로 부풀리지 않는다. 비상주 검증 뒤 OfficeCLI 프로세스는 없었고 개인 설정 폴더도 생성되지 않았다.

### Huashu Design.

원문 Node lock으로 `npm ci`를 실행했고 전용 Python·브라우저 런타임을 준비했다. Python Playwright 1.59.0과 Node 1.59.1이 같은 Chromium 1217을 사용함을 확인했다. Python 1.59.1은 배포되지 않아 실제 배포 1.59.0을 선택했다. 원본 38개 회귀가 전부 통과했고 스킵은 0개다.

원본 fixture를 Python 변환기로 PPTX 1장으로 변환한 뒤 텍스트 상자 6개·이미지 2개와 예상 원문 전체를 재열어 대조했다. 없는 selector는 exit 1·파일 미생성, clean/broken HTML lint는 각각 exit 0/1이었다. 원본 verify.py로 1920×1080·390×844에서 JS·콘솔 오류가 없음을 확인하고 스크린샷을 검사했다. 고정 1920px fixture는 작은 viewport에서 잘리므로 반응형 성공으로 처리하지 않는다. 개인 기억은 검증 경로로 격리했고 브라우저 context를 닫았다.

## 보호와 발견.

사용자 홈·저장소의 새 Codex 프로세스에서 각각 enabled 스킬 151개와 신규 세 항목의 사용자 범위·전역 경로를 확인했다. enabled 동명 중복은 0개다. 자동화 계정의 별도 홈을 읽는 초기 검사는 사용자 전역 발견 증거로 사용하지 않고 실제 설치 대상 사용자 권한으로 다시 검사했다. 다른 계정의 스킬·중복은 수정하지 않았다.

기존 전역 파일 1,193개의 해시가 유지됐다. PPT Master·Huashu는 실행 후 원본 전체 파일을 다시 대조했고 OfficeCLI의 본문·바이너리 해시도 유지됐다. 새 패키지의 부모 ACL 상속은 활성 상태이며 이번 작업에서 ACL 변경은 없었다. Node 설치로 Huashu 패키지에 생긴 node_modules와 별도 정책 파일은 원본 파일 수와 구분한다.

전용 Python은 기본 Python과 다르며 PPT Master는 `.venv/Scripts/python.exe`, Huashu는 `Scripts/python.exe`를 사용한다. Huashu 실행 프로세스에는 전용 `PLAYWRIGHT_BROWSERS_PATH`가 필요하다. [운영 안내](../../Skill/office-design-tools/README.md)에 실제 사용 경로를 기록한다. 클라우드·TTS·영상·외부 API·일반 디자인 품질·실제 Office 렌더 동일성은 미검증이다. 이 작업은 이전 Anthropic helper 실패를 수정하거나 통과 처리한 작업도 아니다.

## 공개 검증과 배포.

카탈로그는 일반 설명 122개와 OFF 22개, 총 144개·26그룹으로 갱신했다. 구조 검사 fixture도 같은 수로 맞췄다. Windows Python 3.12 전체 회귀 103개와 문서 링크·diff 검사를 통과했다. 주 에이전트가 PPT Master 36개·Huashu 8개·OfficeCLI 10개의 산출물/로그 해시를 별도 대조하고 세 PPTX·DOCX 내용·XLSX 계산값을 재열었다. OfficeCLI 차트 PNG도 직접 확인했다. 기존 자체 제작 패키지·실행 스킬과 다른 프로젝트는 보존한다.

독립 리뷰는 공개 변경 10파일 전체·실제 설치 정책·고정 해시·라이선스·런타임·샘플을 대조했고 확정 결함이나 배포 차단 사항을 발견하지 못했다. 별도 리뷰어도 PPT Master 13,091개·Huashu 445개 원본과 기존 보호 1,193파일을 직접 재대조했고 문서 검사 8개·diff 검사를 통과했다. 공개 정보 검사에서 시크릿·개인 절대 경로는 0개였다.

구현 커밋 `91c57638c1d7f8bdc2034ef081753249d14c1576`을 main에 fast-forward 통합한 뒤 전체 103개 회귀를 다시 통과했다. 일반 push 후 원격 main의 SHA 일치와 [GitHub Actions](https://github.com/nowJDev/Agent-Instructions/actions/runs/43137534239)의 Ubuntu·Windows 성공을 확인했다. 소유 임시 worktree·브랜치를 정리했으며 이번 검증의 상주 서버·OfficeCLI 프로세스도 남지 않았다. 사용자 프로세스는 종료하지 않았다. 실행본·runtime·원문 증거와 재검증 샘플은 비공개 로컬에 보존했다. 최종 기록 커밋의 원격 SHA·CI는 실제 결과와 최종 보고에서 확인한다.
