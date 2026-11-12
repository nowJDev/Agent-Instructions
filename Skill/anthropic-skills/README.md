<!-- Anthropic 원본 스킬의 전역 설치 이름과 배포·호출 경계를 안내한다. -->
# Anthropic 스킬 설명 카탈로그.

이 문서는 설치 안내와 설명이며 타사 실행 원본을 포함하지 않는다. [원본 저장소](https://github.com/anthropics/skills)의 커밋 `2c5958ecac7cee2b583967a2c4981d0f4a75c579`에 있는 19개 패키지를 대상으로 한다. [설치 명세](../../references/anthropic-skills.lock.json)에 원본 커밋·ZIP SHA256·설치 이름·호출 정책을 고정한다. 라이선스와 공통 고지는 원본에서 내려받아 패키지와 함께 보존한다.

### 설치와 중복 처리.

Codex 실행본은 사용자 전역 `~/.agents/skills/anthropic-<원본명>`에 한 번 설치한다. 폴더와 `SKILL.md`의 `name`을 함께 바꾸고 필요한 호출·경로 참조도 변환한다. 지정 저장소에서 작업할 때도 전역 실행본을 사용하며 프로젝트 `.agents/skills`에 두 번째 복사본을 만들지 않는다. `skills`라는 저장소 이름은 설치 이름으로 쓰지 않는다.

저장소 루트에서 검사와 적용 명령을 구분한다. [설치기](../../scripts/install_anthropic_skills.py)는 Python 3.11 이상 표준 라이브러리와 Windows 기본 `icacls`를 사용하며 기본 실행에서 활성 파일을 변경하지 않는다. Windows에서는 게시한 패키지와 상태 파일이 대상 부모의 접근 권한을 상속하도록 처리하며 다른 기존 파일의 권한은 바꾸지 않는다. 저장소 전체 회귀에는 별도로 기존 Bash 도구가 필요하다.

```text
python -X utf8 -B scripts/install_anthropic_skills.py
python -X utf8 -B scripts/install_anthropic_skills.py --apply
```

| 기존 항목 | 이번 설치 정책. |
|---|---|
| Anthropic 전역 `frontend-design`. | 패키지 전체를 원본과 비교한 뒤 `anthropic-frontend-design`으로 이전한다. |
| Anthropic 전역 `skill-creator`. | 패키지 전체를 원본과 비교한 뒤 `anthropic-skill-creator`로 이전한다. |
| 자체 제작 `claude-api`. | 보존하고 공식 원본은 `anthropic-claude-api`로 구분한다. |
| OpenAI 내장 `skill-creator`와 다른 플러그인. | 보존하고 기존 설정을 변경하지 않는다. |

원본 ZIP·설치 상태·이전 백업은 스킬 탐색 경로와 공개 저장소 밖에 보관한다. Windows에서는 `%LOCALAPPDATA%/AgentSkills`, 다른 OS에서는 `~/.local/share/AgentSkills`를 사용한다. 공개 저장소에는 출처·명세·설치기·설명만 추적한다.

동일한 설치는 건너뛴다. 개인 수정·알 수 없는 추가 파일·미관리 동명 대상·junction·symlink·잘못된 ZIP이 발견되면 전역 변경 전에 중단하고 기존 파일을 보존한다. 전체 사전 검사와 백업 후 적용하며 게시 실패 시 이번 변경을 복구한다. 업데이트는 고정 커밋과 해시를 검토해 명세를 변경하는 별도 작업이다.

`skill-creator` 이전에서만 패키지의 나머지 전체 파일이 원본과 일치하고 `LICENSE.txt`가 설치 명세의 `legacy_license_sha256`과 정확히 일치하는 경우도 허용한다. 이는 고정된 공식 예전 원본의 저작권 표시 차이를 확인한 예외이며 일반적인 개인 수정 허용이 아니다.

### 호출과 검증 범위.

`anthropic-docx`, `anthropic-pdf`, `anthropic-pptx`, `anthropic-xlsx`, `anthropic-claude-api`, `anthropic-skill-creator`, `anthropic-discernment-nudge`, `anthropic-brand-guidelines`, `anthropic-web-artifacts-builder`, `anthropic-webapp-testing` 10개는 기존 기능과의 선택 중복을 줄이기 위해 `agents/openai.yaml`에 `allow_implicit_invocation: false`를 적용한다. 예를 들어 `$anthropic-pdf`처럼 명시적으로 호출한다. 나머지 9개는 원본의 자동 선택을 유지한다. 이름 구분과 자동 선택 제한은 별개의 정책이다.

패키지의 `scripts`·`references`·`assets`·예제와 상대경로 리소스를 함께 보존한다. 스킬 설치가 개별 작업에 필요한 Python·Node 패키지, 브라우저, 외부 서비스 인증이나 MCP 서버를 자동 준비하지는 않는다. 해당 작업에서 원본의 요구사항과 실제 가용 도구를 확인한다. Claude 전용 도구·환경은 Codex의 동등 기능으로 해석하고 지원되지 않는 부분은 명시한다.

설치 후 기본 검사 명령을 다시 실행하고 새 Codex 프로세스에서 19개 이름·실제 경로·본문·호출 정책을 확인한다. 파일 배치, 클라이언트 발견과 실제 기능 수행은 서로 다른 증거다. 이 설명만으로 특정 PC의 설치나 기능 검증 완료를 뜻하지 않는다. [승인 설계](../../docs/superpowers/specs/2026-11-12-anthropic-skills-design.md)와 [실행 계획](../../docs/superpowers/plans/2026-11-12-anthropic-skills.md)에 작업 범위를 기록한다.

## anthropic-academy-guide

Claude를 배우려는 목적에 맞는 Academy 과정·튜토리얼·사용 사례를 찾는 스킬이다. 학습 안내에 사용하며 제품 사용법의 최신성은 원본이 연결하는 공식 자료에서 확인한다. 자동 선택을 허용한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/academy-guide)를 따른다.

## anthropic-algorithmic-art

코드와 매개변수로 생성형 시각 작품을 만드는 스킬이다. 예를 들어 조절 가능한 패턴이나 입자 작품을 만들 때 사용한다. 자동 선택을 허용하며 실행 환경·산출물은 작업별로 검증한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/algorithmic-art)를 따른다.

## anthropic-brand-guidelines

Anthropic의 브랜드 색상·타이포그래피를 산출물에 적용하는 스킬이다. 사용자 자신의 브랜드 지침과 구분하고 Anthropic 스타일이 필요한 경우에 `$anthropic-brand-guidelines`로 명시 호출한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/brand-guidelines)를 따른다.

## anthropic-canvas-design

포스터 등 정적인 시각 작품을 만드는 스킬이다. 이미지·PDF 산출물이 필요한 시각 디자인에 사용하며 폰트·렌더링 환경과 최종 표시를 확인한다. 자동 선택을 허용한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/canvas-design)를 따른다.

## anthropic-claude-api

공식 Claude API·SDK 원본 자료를 참고하는 스킬이다. 기존 자체 제작 `claude-api`와 구분해 `$anthropic-claude-api`로 명시 호출한다. 설치된 문서는 고정 스냅샷이므로 현재 모델·가격·API 계약은 공식 실시간 자료로 재확인한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/claude-api)를 따른다.

## anthropic-discernment-nudge

실질적인 답변 뒤에 사실·추론·누락을 점검하는 짧은 후속 질문을 제안하는 스킬이다. 자동으로 응답 형식을 바꾸지 않도록 `$anthropic-discernment-nudge`로 명시 호출한다. 사용자가 요청한 응답 형식과 원본의 적용 제외 조건을 확인한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/discernment-nudge)를 따른다.

## anthropic-doc-coauthoring

맥락 수집·초안 구성·독자 관점 검토를 거쳐 문서를 공동 작성하는 스킬이다. 제안서나 기술 설명을 함께 다듬는 요청에 사용하며 사용자가 제공한 사실과 작성자의 가정을 구분한다. 자동 선택을 허용한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/doc-coauthoring)를 따른다.

## anthropic-docx

Word 문서의 생성·편집을 안내하는 스킬이다. 기존 문서 도구와 구분해 `$anthropic-docx`로 명시 호출한다. 관련 리소스·변환 도구를 확인하고 최종 문서의 내용·레이아웃을 실제로 검증한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/docx)를 따른다.

## anthropic-frontend-design

의도적인 시각 방향을 가진 프런트엔드 UI를 만드는 스킬이다. 기존 전역 `frontend-design`의 이전 대상이며 새 명시 호출 이름은 `$anthropic-frontend-design`이다. 자동 선택을 허용한다. 실제 브라우저에서 표시·상호작용·접근성을 확인한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/frontend-design)를 따른다.

## anthropic-internal-comms

상태 보고·사내 공지 등 내부 커뮤니케이션 문서를 작성하는 스킬이다. 조직의 실제 문체·독자·공개 범위와 제공 자료를 확인한다. 자동 선택을 허용하며 작성과 외부 전송 권한은 구분한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/internal-comms)를 따른다.

## anthropic-mcp-builder

외부 서비스를 연결하는 MCP 서버를 설계·구현하는 스킬이다. 서버의 도구 계약·인증·오류 처리·검증을 다룬다. 자동 선택을 허용하며 서버 구현과 클라이언트 등록·권한 확대는 요청 범위에 따라 별도로 수행한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/mcp-builder)를 따른다.

## anthropic-pdf

PDF 읽기·작성·변환 작업을 안내하는 스킬이다. 기존 PDF 도구와 구분해 `$anthropic-pdf`로 명시 호출한다. 텍스트 추출과 화면 렌더링의 차이를 고려해 필요한 내용·레이아웃을 검증한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/pdf)를 따른다.

## anthropic-pptx

PowerPoint 슬라이드 생성·편집을 안내하는 스킬이다. 기존 프레젠테이션 도구와 구분해 `$anthropic-pptx`로 명시 호출한다. 패키지 도구의 실행 조건과 슬라이드 렌더링 결과를 확인한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/pptx)를 따른다.

## anthropic-skill-creator

스킬 작성·수정·평가를 안내하는 스킬이다. 기존 Anthropic 전역 `skill-creator`의 이전 대상이며 OpenAI 내장본과 구분해 `$anthropic-skill-creator`로 명시 호출한다. Claude 전용 평가 도구가 실제 환경에 있는지 확인한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/skill-creator)를 따른다.

## anthropic-slack-gif-creator

Slack에 사용할 애니메이션 GIF를 만드는 스킬이다. 크기·프레임·파일 용량과 실제 재생 결과를 확인한다. 자동 선택을 허용하며 GIF 생성은 Slack 게시 권한을 포함하지 않는다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/slack-gif-creator)를 따른다.

## anthropic-theme-factory

문서·슬라이드·웹 산출물에 일관된 시각 테마를 적용하는 스킬이다. 사용자 브랜드나 기존 디자인 규칙과 적용 범위를 확인한다. 자동 선택을 허용하며 테마 적용 후 가독성과 렌더링을 검증한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/theme-factory)를 따른다.

## anthropic-web-artifacts-builder

여러 UI 요소가 필요한 웹 산출물을 구성하는 스킬이다. 기존 Sites 도구와 선택이 겹치지 않도록 `$anthropic-web-artifacts-builder`로 명시 호출한다. 설치된 프런트엔드 도구와 배포 대상의 제약을 확인하고 생성·실행·게시를 구분한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/web-artifacts-builder)를 따른다.

## anthropic-webapp-testing

로컬 웹 앱의 브라우저 동작·화면·로그를 검증하는 스킬이다. 기존 Chrome DevTools 도구와 선택이 겹치지 않도록 `$anthropic-webapp-testing`으로 명시 호출한다. 원본의 Playwright 사용 절차와 실제 가용 브라우저 도구를 확인하고 사용자 지정 도구와 프로젝트의 브라우저 검증 규칙을 먼저 따른다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/webapp-testing)를 따른다.

## anthropic-xlsx

스프레드시트 작성·편집을 안내하는 스킬이다. 기존 스프레드시트 도구와 구분해 `$anthropic-xlsx`로 명시 호출한다. 수식·표시 형식·재계산 도구와 최종 셀 값을 확인한다. [원본 패키지](https://github.com/anthropics/skills/tree/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/xlsx)를 따른다.
