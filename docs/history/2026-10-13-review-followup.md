<!-- 해당 작업의 설계·계획·검증 원문과 당시 상태를 보존한다. -->
# 2026-10-13-review-followup 작업 기록.

당시 결정·계획·검증 증거를 함께 보관한다. 과거의 미검증·보류·승인 경계를 원문대로 유지하며 현재 설치·인증 성공으로 확대하지 않는다.

[보관 목차](README.md)에서 다른 작업과 이전 주소를 찾을 수 있다.

<a id="plan"></a>
## 이전 계획 원문.

원본 경로: `docs/superpowers/plans/2026-10-13-review-followup.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/superpowers/plans/2026-10-13-review-followup.md).

<a id="plan--추가-전체-리뷰-11건의-수정-계획"></a>
### 추가 전체 리뷰 11건의 수정 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 사용자는 전체 리뷰 결과의 11건 수정 실행을 승인했다.

<a id="plan--목표와-설계"></a>
#### 목표와 설계.

기준선은 `0574a4a`다. 설정 병합 예제 전체 흐름·저장 실패·테마 백업, 프로젝트 경로 경계·실패 정리·Markdown 검사, hooks·Context7·Bash·Figma·HF 안내를 수정한다. 실제 전역 설정·서비스는 변경하지 않는다. 사용자의 추가 지시로 완료 후 커밋·병합·원격 push·임시 파일 정리와 지정 폴더 handover까지 진행한다. 기존 구조와 표준 라이브러리를 사용한다.

설정 예제는 승인된 항목 번호를 명시하고 선택한 섹션만 병합한다. `SessionStart`는 hooks 선택 때만 함께 적용한다. 저장은 같은 디렉터리의 임시 파일에 완성한 뒤 `os.replace`로 교체한다. 테마를 선택하면 홈의 세 파일도 백업한다.

초기화·검증의 모든 읽기·쓰기 대상은 실제 경로가 프로젝트 내부인지 확인한다. 초기화는 템플릿을 작업용 임시 파일에 복사한 뒤 `os.link`로 최종 이름을 배타적으로 게시한다. 이미 생성된 사용자 파일은 보존하고 실패 정리는 임시 파일에만 수행한다. 하드링크 미지원 파일시스템에서는 오류로 중단한다. 경로 검사는 기존 junction·symlink 우회를 차단하며, 다른 프로세스가 검사 후 디렉터리를 교체하는 공격을 차단하는 OS 샌드박스를 대신하지 않는다.

Markdown 완료 검사는 fenced 코드와 inline code를 제외하고 실제 `-`·`*`·`+` 목록의 미완료 표기를 확인한다. API 문서는 해당 클라이언트 인증 UI와 원격 서버 기능을 구분하고 실제 도구 스키마를 확인하도록 안내한다.

<a id="plan--task-1-회귀와-최소-구현"></a>
#### Task 1. 회귀와 최소 구현.

Files: `tests/test_review_regressions.py`, `Owned-Skills/design-driven-delivery/scripts/{bootstrap_workflow,validate_workflow,workflow_paths}.py`, `references/claude-code-cli-setup.md`.

- [x] junction 외부 쓰기·읽기, 경쟁 저장 후 복사 실패, Markdown 다른 목록 기호·코드 예시, 전체 설정 예제 선택·저장 실패, 테마 백업을 실패 테스트로 확인한다.
- [x] 실제 경로 검증과 임시 파일 게시·정리, 코드 예시 제외 및 목록 검사, 선택 항목 병합·원자적 설정 저장·테마 백업을 구현한다.
- [x] `python -X utf8 -B -m unittest discover -s tests -v`의 전체 통과와 기존 17개 회귀 보존을 확인한다.

구현 핵심은 다음과 같다.

```python
os.link(temporary_path, target_file)
os.replace(temporary_path, target_path)
```

첫 명령은 기존 최종 파일이 있으면 실패해 보존하며, 둘째 명령은 완성된 설정으로 교체한다. 두 명령 전에 복사를 완료하고 예외 시 임시 파일만 정리한다.

<a id="plan--task-2-문서와-검증"></a>
#### Task 2. 문서와 검증.

Files: `rules/02_tool-boundaries.md`, `index.html`, `Skill/plugin-dev/hook-development.md`, `Skill/huggingface-skills/*.md`, `MCP/{context7,figma,huggingface-skills,README}.md`, `Owned-Skills/design-driven-delivery/{SKILL.md,references/document-contracts.md,assets/templates/{plan,review,handover}-template.md}`, `CHANGELOG.md`.

- [x] 공식 입력·응답 계약과 MCP 도구 인자, 정상 Bash 변수 확장, 인증·기능 구분을 수정하고 관련 표를 맞춘다.
- [x] 문서의 경로 경계·초기화 지원 조건·Markdown 검사 범위를 실행 동작에 맞춘다.
- [x] 전체 링크·앵커·UTF-8·코드 블록·Python 문법과 `git diff --check`를 확인한다.
- [x] 독립 코드 리뷰에서 발견 사항을 검증하고 해결한 뒤 `docs/reviews/2026-10-13-review-followup.md`에 결과를 기록한다.
- [x] 한글 커밋·main 통합·일반 push·임시 작업 트리 정리 절차를 준비한다. 실행 후 최종 해시·원격 일치·정리 상태를 지정한 handover에 기록한다.

<a id="review"></a>
## 이전 리뷰·검증 원문.

원본 경로: `docs/reviews/2026-10-13-review-followup.md`

[원래 커밋의 문서](https://github.com/nowJDev/Agent-Instructions/blob/a559c66d71aee886e717ff91bffce6270accdb17/docs/reviews/2026-10-13-review-followup.md).

<a id="review--추가-전체-리뷰-11건의-수정-검증"></a>
### 추가 전체 리뷰 11건의 수정 검증.

기준선은 `0574a4a`다. 사용자는 전체 리뷰의 11건 수정과 완료 후 커밋·푸시·필요한 병합·임시 파일 정리 및 지정 폴더 handover를 승인했다. 저장소 원본만 수정하며 실제 전역 설정·MCP 서비스는 변경하지 않았다.

<a id="review--발견-사항-처리"></a>
#### 발견 사항 처리.

| 번호 | 문제 | 처리와 근거 |
|---|---|---|
| 1 | 설정 예제의 훅 호출 누락·미선택 권한 병합. | 두 Python 블록을 같은 프로세스에서 실행하고 선택한 훅·권한·상태줄·플러그인·언어만 적용한다. 기존 사용자 키와 플러그인을 보존한다. |
| 2 | 저장 실패 시 기존 JSON 절단. | 같은 디렉터리 임시 파일에 JSON을 완성하고 flush·fsync 후 원자적으로 교체한다. 쓰기 오류에서는 원본을 보존하고 임시 파일만 정리한다. |
| 3 | junction을 통한 프로젝트 외부 쓰기·읽기. | 기본·선택·상태·체크리스트의 실제 경로를 확인한다. Windows junction fixture에서 외부 생성·기본 검사 모두 거부했다. |
| 4 | 복사 실패 정리가 사용자의 경쟁 저장 파일 삭제. | 복사는 임시 파일에서 수행하고 완료 후 하드링크로 배타적으로 게시한다. 실패 시 임시 파일만 정리하며 경쟁 저장 문서는 보존한다. |
| 5 | 다른 목록 기호 누락·코드 예시 오탐. | `-`·`*`·`+` 실제 미완료 목록을 검사한다. fenced 코드·inline code 예시는 제외한다. |
| 6 | 테마 홈 파일 백업 누락. | 테마 선택 시 `.bashrc`·`.minttyrc`·`.elephant_walk.py`도 백업한다. Claude 디렉터리가 없는 경우의 홈 백업도 독립 fixture에서 확인했다. |
| 7 | 훅 입력 필드·치환 변수 오류. | `tool_response`·`prompt`·`$ARGUMENTS` 계약으로 수정했다. |
| 8 | Stop 훅 응답 유형 혼용. | 명령 훅의 `decision: block`과 프롬프트 훅의 `ok` 응답을 구분했다. |
| 9 | Context7 필수 인자·이름 오류. | resolve의 `libraryName`·`query`, 조회의 `libraryId`·`query`와 선택 `language`를 안내한다. |
| 10 | Bash 변수 확장을 미지원으로 일반화. | 정상 지원을 명시하고 바깥 PowerShell·CMD의 선확장·인용 문제와 구분했다. |
| 11 | Figma·HF 인증 화면을 서버 기능으로 단정. | 대표 기능과 실제 런타임 도구 확인을 안내한다. 인덱스와 HF 개별 카탈로그의 연결 안내도 공통 문서로 맞춘다. |

<a id="review--추가-독립-리뷰"></a>
#### 추가 독립 리뷰.

스크립트 검토자와 설정·API 검토자가 별도로 전체 관련 diff·연결 문서·테스트를 읽고 직접 회귀를 실행했다. 스크립트 리뷰에서 다음 두 결함을 추가로 재현하고 수정했다.

- 삼중 backtick inline code를 fence로 오인하거나 길이가 다른 구분자를 닫힘으로 처리하면 실제 미완료 항목을 놓쳤다. 유효한 fence 시작과 같은 길이 inline 구분자만 인정한다. 두 사례의 RED를 확인한 뒤 검출을 확인했다.
- 실제 필수 템플릿 필드가 inline code 안에 있어 예시로 제외됐다. plan·review·handover의 필수 필드를 코드 표시 밖으로 옮겼다. 세 템플릿의 RED를 확인한 뒤 자리표시자 검출을 확인했다.

최신 코드·템플릿에 대한 독립 재검증에서 추가 차단 사항을 발견하지 못했다. 설정·API 검토자는 선택 병합·원본 보존·테마 백업과 공식 계약의 일치를 확인했다.

<a id="review--검증"></a>
#### 검증.

`python -X utf8 -B -m unittest discover -s tests -v`에서 31개 통과, 실패·스킵 0개다. 기존 17개 회귀를 유지하고 전체 설정 예제·쓰기 실패·junction·경쟁 저장·Markdown·필수 템플릿 사례를 추가했다. 백업 테스트는 Git Bash와 임시 홈 fixture를 사용하며 실제 사용자 홈 설정을 변경하지 않는다.

전체 Markdown의 UTF-8·BOM·코드 블록·로컬 링크·앵커, Python 문법과 JSON 예제를 검사하고 `git diff --check`를 확인했다. 전역 배치용 문서는 실제 배치 기준 경로로 검사한다. 원격 fetch 결과 원격의 추가 분기는 없으며, 커밋 후 로컬 main으로 fast-forward 통합하고 승인된 원격 main에 일반 push한다.

<a id="review--공식-근거와-제한"></a>
#### 공식 근거와 제한.

[Claude hooks](https://code.claude.com/docs/en/hooks), [Context7 도구](https://github.com/upstash/context7#available-tools), [Figma 도구](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/), [HF MCP](https://huggingface.co/docs/hub/agents-mcp)를 기준으로 문서를 맞췄다.

하드링크를 지원하지 않는 파일시스템에서는 초기화가 오류로 중단한다. 미지원 게시 실패는 주입 시험으로 확인했고 실제 로컬 Windows 파일시스템의 정상 게시를 회귀로 확인했다. 경로 검사는 기존 외부 링크를 거부하며, 검사 후 다른 프로세스가 디렉터리를 교체하는 공격을 막는 OS 샌드박스는 아니다. 설정 예제는 동일 파일을 다른 프로세스가 동시에 편집하지 않는 상황에서 실행한다. 실제 전역 설치본 적용과 외부 서비스의 인증·실행은 검증하지 않았다.
