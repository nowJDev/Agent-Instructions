<!-- Anthropic 설치 전수조사·실패 반례·실제 배포와 검증 경계를 기록한다. -->
# Anthropic 스킬 설치와 중복 전수조사.

[승인 설계](../superpowers/specs/2026-11-12-anthropic-skills-design.md), [실행 계획](../superpowers/plans/2026-11-12-anthropic-skills.md), [고정 설치 명세](../../references/anthropic-skills.lock.json), [사용 안내](../../Skill/anthropic-skills/README.md)를 기준으로 수행했다. 기준선은 `e6beb2b`다. 사용자는 설계를 승인하고 실행을 요청했으며 진행 중 중복 전수조사를 추가 확인했다.

## 중복 전수조사.

초기 확인은 신규 19개와 전역·내장의 동명 충돌 조사였으며 전체 조사 완료로 보고하지 않았다. 후속 요청 뒤 다음 영역을 실제 파일·등록 매니페스트와 대조했다.

| 설치 전 영역. | SKILL.md 파일 수. | 해석. |
|---|---:|---|
| 사용자 `.agents/skills`. | 110 | Codex 사용자 설치다. |
| 사용자 `.codex/skills`. | 6 | 내장 5개와 migrate-to-codex 1개다. |
| 사용자 `.claude/skills`. | 6 | 별도 Claude 클라이언트 설치다. |
| 대상 저장소 Owned-Skills. | 26 | 자체 제작 원본 보관이며 프로젝트 활성 설치가 아니다. |
| 전역 문서 복제본 Owned-Skills. | 26 | 문서·배포 원본 보관이다. |
| 플러그인 캐시. | 134 | 18개 공급자·버전 번들의 파일이며 활성 여부는 매니페스트로 구분했다. |
| 합계. | 308 | 활성 스킬 수와 합산하지 않는다. |

name, 원문 SHA256, frontmatter를 제외하고 LF·주변 공백을 정규화한 본문 SHA256으로 비교했다. 대상 저장소와 전역 문서 복제본, Desktop 상위에는 별도 `.agents/skills`·`.claude/skills`·`.codex/skills` 실행본이 없었다. `.cursor/skills`, `.gemini/skills`, `.config/opencode/skills`도 없었다.

- Codex 전역·내장 116개에서 동명은 `skill-creator` 한 그룹의 서로 다른 2개 구현이다. 원문·정규화 본문 동일 그룹은 0개다. Anthropic 항목의 이름 이전으로 해결한다.
- Claude의 Paseo 6개는 Codex 설치본과 본문이 같지만 다른 클라이언트 설치다. 임의 삭제하지 않는다.
- 플러그인 금융 계열의 `company-tearsheet`, `comps-valuation`, `dcf-model-builder`, `financials-normalizer`, `meeting-prep`, `memo-builder`, `model-audit-tieout`, `scenario-sensitivity-generator`, `three-statement-model-builder`, `user-context`는 동명 10그룹이지만 서로 다른 본문·플러그인 namespace다. 캐시 이름만으로 활성 충돌이나 동일 구현이라고 판단하지 않는다.
- Ponytail의 `.openclaw/skills`와 `skills`에는 동일 본문 6그룹이 있다. Codex 매니페스트는 `./skills/`만 등록하므로 다른 호스트용 배포 사본을 활성 중복으로 세지 않는다.
- vendor_imports 39개, 플러그인 staging 54개, `.codex/.tmp` 555개, backups 327개로 비활성 저장 영역의 SKILL.md 경로 975개를 추가 확인했다. 실행 목록에 합산하거나 복구 자료를 삭제하지 않았다.

실제 사용자 계정의 Codex CLI `0.167.2` 새 app-server에서 홈·대상 저장소·격리 worktree 3개 cwd의 `skills/list(forceReload=true)`를 조회했다. 모두 설치 전 130개 enabled, user 125개와 system 5개, 오류 0개다. 동명은 Anthropic 전역과 OpenAI 내장의 `skill-creator`만 있으며 원문 동일 중복은 0개다. 이 130개는 CLI가 실제 반환한 목록이며 현재 대화 호스트의 모든 연결형 플러그인을 포함한다고 주장하지 않는다. 호스트에 제공된 플러그인 설명과 로컬 캐시·등록을 별도로 대조했다.

제한된 샌드박스 계정으로 먼저 조회한 목록은 사용자 계정의 결과와 달랐다. 샌드박스 전용 digital-twin-jobs-watch 사본은 사용자 활성 중복으로 보고하지 않았으며 실제 사용자 컨텍스트에서 재조회했다. 원문 목록·전체 파일 해시는 공개 저장소 밖의 개인 검증 증거로만 보존한다.

## 역할 중첩과 정책.

신규 19개의 description을 전부 읽고 다음과 같이 비교했다. 이름 중복·동일 구현·역할 중첩은 구분한다.

| 신규 원본명. | 기존 기능과의 관계·처리. |
|---|---|
| academy-guide. | Claude 학습 과정 안내로 직접 대체본이 없다. 자동 선택한다. |
| algorithmic-art. | imagegen·playground와 인접하지만 p5.js 생성형 예술에 특화됐다. 자동 선택한다. |
| brand-guidelines. | 일반 브랜드·디자인 요청에 선택이 겹친다. Anthropic 브랜드용 명시 호출로 제한한다. |
| canvas-design. | imagegen과 정적 시각물 산출물이 일부 겹친다. 기존 사용자 지정 도구를 우선하고 자동 선택은 유지한다. |
| claude-api. | 자체 제작 API 스킬과 직접 겹친다. 공식 원본을 명시 호출로 구분한다. |
| discernment-nudge. | 후속 질문 기능·응답 형식에 영향을 준다. 명시 호출한다. |
| doc-coauthoring. | brainstorming·writing-plans·Pages와 문서 작업 일부가 겹친다. 기존 필수 설계 절차를 우선하고 자동 선택한다. |
| docx. | documents:documents와 겹치므로 명시 호출한다. |
| frontend-design. | 기존 전역 패키지와 전체 일치한다. 이전하고 자동 선택을 유지한다. |
| internal-comms. | daily-work-report·Notion digest와 부분 중첩한다. 지정 한국어 업무보고는 기존 전문 스킬을 우선하고 자동 선택한다. |
| mcp-builder. | mcp-integration과 관련되지만 서버 구현과 클라이언트 등록 역할이 다르다. 자동 선택한다. |
| pdf. | pdf:pdf와 겹치므로 명시 호출한다. |
| pptx. | presentations:Presentations와 겹치므로 명시 호출한다. |
| skill-creator. | 기존 Anthropic 항목을 이전하고 OpenAI 내장·writing-skills·skill-development와 구분해 명시 호출한다. |
| slack-gif-creator. | Slack GIF 제약·검증에 특화됐다. 자동 선택한다. |
| theme-factory. | 디자인과 인접하지만 테마 적용 보조 역할이다. 자동 선택한다. |
| web-artifacts-builder. | Sites와 웹 구축 요청이 겹치므로 명시 호출한다. |
| webapp-testing. | Chrome DevTools·verify와 브라우저 검증이 겹치므로 명시 호출한다. |
| xlsx. | spreadsheets:Spreadsheets와 겹치므로 명시 호출한다. |

초기 설계의 명시 호출 7개에서 전수조사로 확인한 brand-guidelines·web-artifacts-builder·webapp-testing을 추가해 총 10개를 제한하고 9개의 자동 선택을 유지했다. 현재 요청의 중복 방지 목적을 반영한 호출 정책 보강이다.

기존 `handover`와 `source-command-handover`, `delete-session`과 `source-command-delete-session`도 목적이 거의 겹친다. source-command 항목에는 수동 이식 필요 안내가 남아 있다. 다른 구현이며 이번 설치와 무관하므로 보존했다. review·code-review·review-pr·ponytail-review, verify·verification-before-completion, writing-skills·skill-development도 범위가 겹치지만 라우터·실행·게이트 역할이 달라 이름만으로 합치지 않았다.

## 구현과 검증.

Python 3.11 이상 표준 라이브러리와 Windows 기본 `icacls`를 사용하는 설치기를 추가했다. 공식 ZIP의 SHA256은 `e5b0c67dbfae471c013d0e03abe66db20ca70cc0c79ab6154a386c8b026e5195`다. 루트 SKILL.md 19개와 원본 440파일을 확인했다. 이름 변환은 frontmatter, 명시 호출과 확인된 형태의 패키지 경로에 한정하고 공개 URL·라이선스·일반 파일 형식 설명을 보존한다. 패키지 스크립트·의존성을 실행하거나 설치하지 않는다.

기존 frontend-design은 전체 원본과 일치했다. skill-creator는 LICENSE.txt의 저작권 표기 한 줄만 달랐으며, 기존 공식 플러그인 원본과 대조해 명세의 정확한 옛 라이선스 해시를 한정 허용했다. 라이선스 본문의 마지막 개행 차이도 구분했다. 개인 수정·추가 파일을 허용하는 예외가 아니다.

새 설치기 부재의 RED와 다음 반례 RED를 확인했다. 독립 전체 리뷰에서 확인한 4개 결함은 모두 수정하고 회귀를 통과했다.

| 발견·실패 조건. | 수정과 증거. |
|---|---|
| 사전 검사 뒤 사용자 대상이 생기는 경쟁. | 전체 스테이징 후 상태·대상·링크·전체 트리를 재검사해 이동 전에 거부한다. 합성 경쟁 반례 RED→GREEN이다. |
| 성공한 이전이 종료 코드 1을 반환함. | 완료 이전과 대기 이전을 구분했다. 실제 CLI 검사·적용·재검사 반례 RED→GREEN이다. |
| ZIP 빈 경로 성분으로 정규화 중복을 우회함. | 빈 성분을 거부했다. 유효한 frontmatter를 가진 중복 항목 반례 RED→GREEN이다. |
| `(docx/pptx/anything else)`가 경로로 잘못 치환됨. | 패키지 리소스 형태에만 변환을 적용했다. 실제 원본 설명 반례 RED→GREEN이다. |

추가로 라이선스·바이너리·공통 고지 보존, 원본 일치 2개 이전, 자체 제작 스킬 보호, 미관리 대상·로컬 수정·잘못된 ZIP·symlink·junction 거부, 실패 복구, 재실행·검사 모드 무변경을 검증했다. Windows에서 symlink 생성 권한이 없으면 실제 junction으로 검사해 제외 없이 통과한다. 기본 Python 3.11.9와 별도 Python 3.12.10을 확인했고 Windows ACL 상속 반례 RED→GREEN을 포함한 최종 전체 회귀는 Python 3.12.10으로 103개 통과했다. 저장소 기본 CI는 Python 3.12다.

## 배포 상태와 경계.

실제 사용자 계정에서 19개 패키지·469파일을 설치했다. 원본 440파일과 패키지별 공통 고지 19개·명시 호출 정책 10개를 대조했다. 기존 frontend-design·skill-creator는 전체를 탐색 경로 밖에 백업·이전했다. 자체 제작·내장·다른 활성 플러그인·설정·전역 지침 등 보호 대상 971파일의 SHA256이 전후 동일하다. 재설치와 검사 모드에서 설치 대상·상태·백업 파일의 내용과 수정 시각이 바뀌지 않았으며 기본 CLI 검사도 종료 코드 0이다.

설치 후 새 사용자 app-server에서 홈·대상 저장소·격리 worktree 모두 147개 enabled, user 142개와 system 5개, 오류 0개를 확인했다. 19개가 모두 사용자 범위의 실제 전역 경로로 발견됐고 이름과 본문을 읽었다. 기존 unprefixed 2개는 사라졌고 OpenAI 내장 skill-creator·자체 제작 claude-api는 남아 있다. 전체 147개에서 동명 그룹·원문 동일 그룹·정규화 본문 동일 그룹은 모두 0개다. 명시 호출 정책은 설정 파일을 대조했으며 모델의 자동 선택 행동까지 실행한 결과는 아니다.

실제 배포 뒤 현재 에이전트의 파일 읽기에서 Windows 임시 디렉터리의 비공개 ACL이 패키지와 상태 파일에 남는 실패를 확인했다. 기존 스킬 부모와 새 파일의 ACL 보호 여부를 대조해 원인을 확인했고, 부모 권한을 상속하는 설치기 동작을 실패 반례로 검증했다. 자동 승인 검토는 최초 권한 복원 명령을 설치 승인만으로는 범위가 충분하지 않다는 이유로 거부했다. 사용자가 새 anthropic-* 19개 폴더와 상태 JSON에 한정한 상속 복원을 명시적으로 승인한 뒤 그 범위만 적용했다. 다른 기존 파일의 권한은 변경하지 않았다. 이후 제한된 현재 에이전트에서 19개 SKILL.md를 모두 직접 읽고 검사 CLI 종료 코드 0을 확인했다.

전역 설명 복제본에는 이번 카탈로그·명세·설치기·설계·계획·검증 기록 8개만 동기화했다. 기존 개인 목차 절을 그대로 보존하고 개인 문서 2개의 해시를 대조했다. 기존 전역 지침·루트 README와 관련 없는 문서를 통째로 교체하지 않았다. 변경 전 문서와 원본 ZIP·이전 스킬·배포 검증 원문은 공개 저장소 밖에 보존한다.

전역 인덱스 링크 검사에서 기존 kordoc 카탈로그 문서 누락을 확인해 저장소의 설명 문서 1개만 추가로 보완했다. kordoc 실행 스킬이나 설정을 변경하지 않았다. 전역 카탈로그의 내부 링크·개인 목차와 보호 971파일 동일성을 다시 확인했다.

구현 커밋 `44e85c8`을 로컬 main에 fast-forward 통합한 뒤 전체 103개 회귀와 기본 검사 CLI를 다시 통과했다. 새 사용자 프로세스의 최종 홈·저장소 목록도 147개, Anthropic 19개, 동명·원문 중복 0개, 오류 0개다. 작업 트리가 깨끗하고 커밋이 main에 포함된 것을 확인한 뒤 이번 worktree·브랜치를 일반 삭제했다. 원격 main `1900d96`은 읽기 전용으로 확인했으며 push하지 않았다.

실제 모델에 의한 19개 기능 실행, 종속성 설치, 외부 서비스 로그인·게시, 원격 push는 수행하지 않았다. 독립 리뷰는 전원 중단·복구 자체 실패와 모델 실행을 검토 범위에서 제외했고, 이번 구현의 정상 오류 복구와 구분한다. 전원 중단 후 자동 복구를 보장하는 설치 관리자로 확장하지 않았다.
