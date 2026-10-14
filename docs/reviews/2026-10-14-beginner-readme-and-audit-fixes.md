<!-- 네 가지 리뷰 발견 수정과 입문자 문서 개편의 검증 근거를 기록한다. -->
# 리뷰 수정과 입문자 문서 개편 검증.

## 범위와 승인.

기준선은 `3c4c082`다. 사용자는 읽기 전용 전체 리뷰에서 확인한 네 가지 결함의 수정과 README 전체의 쉬운 설명을 요청했다. 이후 사람용 HTML 상세 안내를 Markdown으로 바꾸고 README에서 연결하도록 추가 요청했다. [설계](../superpowers/specs/2026-10-14-beginner-readme-and-audit-fixes.md)와 [실행 계획](../superpowers/plans/2026-10-14-beginner-readme-and-audit-fixes.md)에 범위를 기록했다. 저장소 원본만 변경하고 논리 단위로 커밋했으며 푸시는 보류한다.

## 수정과 직접 검증.

| 리뷰 발견 | 수정 | 증거 |
|---|---|---|
| 기존 공개 HF 저장소에서 private 생성 옵션이 무시됐다. | dataset·Space 예제는 실제 비공개 여부를 조회한 뒤 파일·secret을 전송한다. 공개·불명확한 결과·조회 오류는 중단한다. | 실제 문서 Python 예제를 가짜 SDK로 실행했다. guard 제거 변이는 assertion 8건으로 검출했다. |
| 프로젝트 이름을 붙여도 전역 세션 폴더 전체를 전송했다. | 승인된 프로젝트·세션만 선정하고 민감정보를 제거한 별도 폴더를 사용한다. 원격 경로가 필터가 아님을 명시한다. | 임시 승인 세션과 다른 프로젝트 세션을 분리해 업로드 원본을 확인했다. 전역 폴더로 되돌린 변이는 assertion 1건으로 검출했다. |
| 목록·인용 안의 미완료 체크 항목을 놓쳤다. | 코드 예시를 제외한 명시적 컨테이너 안의 세 상태를 검사한다. fence의 목록·인용 순서를 함께 추적한다. | 18개 누락 사례 RED 후 GREEN. 독립 리뷰의 중첩 fence 오탐 3개도 RED 후 회귀를 추가했다. |
| 로컬 지침 파일명이 잘못됐다. | 검색·설명에 CLAUDE.local.md를 사용하고 전역 지침의 별도 조회를 명시한다. | 실제 Git Bash find를 임시 정상·잘못된 파일 6개에 실행해 정상 4개만 선택했다. |

실제 업로드나 정보 유출을 발생시키지 않았다. 비공개 조회는 업로드 전 확인이며, 외부 관리자가 조회 후 공개 여부를 변경하는 동시 상황을 잠그는 기능은 아니다. 준비 폴더의 파일 승인과 민감정보 제거는 문서의 필수 준비 단계다.

## 문서 개편.

README는 목적·복사할 요청 문장·작업 흐름·파일 역할·쉬운 용어·문서 찾기로 재작성했다. 그림 두 개와 시작 문장 두 종류를 유지했다. 사람이 읽는 자세한 설명은 GUIDE, AI가 따르는 규칙은 AGENTS와 rules로 연결한다. 설치를 수행하는 AI는 GETTING_STARTED와 공통 바로가기 절차를 반드시 읽도록 안내한다.

기존 index.html의 개요·설계 철학·구성·설치·사용·도구·규칙 관리·유지보수·공개 점검·한계·FAQ·라이선스를 GUIDE.md로 변환했다. 오래된 60줄 단정과 프로젝트 지식·실패 로그 안내는 현행 규칙에 맞췄다. Markdown 체크리스트가 정적이며 자동 검사·저장·설정 적용을 하지 않음을 명시했다. 변환 후 HTML은 개별 삭제하고 과거 계획·리뷰의 역사적 언급은 유지했다.

README 제목 변경의 직접 참조 4문서도 갱신했다. 사용자 지정 대상, 설정 홈, 기존 사용자 지침·설정 보존, CLI·아이콘·지침 로드·인증의 미완료 조건과 확장 별도 요청 계약을 유지했다.

## 자동·독립 검증.

- 기준선 전체 테스트 57개 통과 후 새 회귀 7개를 추가했다.
- `python -X utf8 -B -m unittest discover -s tests -v`는 전체 64개 통과, 실패·스킵 0개다. 부모의 통합 실행은 23.631초다.
- Markdown 대상 회귀 22개와 업로드 예제 회귀 4개는 각각 통과했다. 테스트는 임시 파일·프로젝트·설정과 인증 없는 가짜 API를 사용했다.
- 독립 검토자는 parser의 1~4단계 목록·인용과 열린·닫힌 fence를 추가 720개 조건으로 검사했다. 업로드 guard·폴더의 변이 검증도 수행했다. 보고된 중첩 코드 예시 오탐은 해결하고 재검토했다.
- README·GUIDE·연관 지침을 전체 읽고 원래 HTML의 본문과 비교했다. 독립 문서 리뷰에서 중요 결함이 없었고 설치 상세를 GUIDE로 옮긴 마지막 변경도 재검토했다.
- 전체 문서의 UTF-8·BOM 없음·LF, Python 파일·예제 문법, JSON 예제, Markdown fence·로컬 링크·앵커 및 git diff --check를 검사했다.

공식 계약은 [HF create_repo](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.HfApi.create_repo), [HF repo_info](https://huggingface.co/docs/huggingface_hub/package_reference/hf_api#huggingface_hub.HfApi.repo_info), [Claude memory](https://code.claude.com/docs/en/memory), [CommonMark 컨테이너](https://spec.commonmark.org/0.31.2/#container-blocks)를 대조했다.

## 커밋과 확인 범위.

완료 검사는 `276be49`, 카탈로그는 `921e52c`, README·GUIDE 전환은 `346ffbd`에 커밋했다. 종료 기록은 별도 커밋한다. 최종 로컬 통합과 Git 상태는 사용자에게 별도로 보고한다. 이 작업에서는 원격 푸시를 실행하지 않는다.

실제 사용자 설치·전역 복제본 동기화·로그인·외부 업로드·Space 실행·브라우저 또는 Markdown 뷰어의 그림 렌더링은 수행하지 않았다. 그림은 기존 Mermaid 구조와 명시적 flowchart 문법을 소스에서 확인했다. 완료 검증기는 완전한 CommonMark 파서가 아니며 HTML·들여쓴 코드·lazy continuation은 기존 문서 계약의 수동 확인 범위다. 저장소 원본 변경이 전역 설치본을 자동 갱신하지 않는다.
