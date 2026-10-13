# 추가 전체 리뷰 11건의 수정 계획.

For agentic workers: REQUIRED SUB-SKILL: executing-plans. 사용자는 전체 리뷰 결과의 11건 수정 실행을 승인했다.

## 목표와 설계.

기준선은 `0574a4a`다. 설정 병합 예제 전체 흐름·저장 실패·테마 백업, 프로젝트 경로 경계·실패 정리·Markdown 검사, hooks·Context7·Bash·Figma·HF 안내를 수정한다. 실제 전역 설정·서비스는 변경하지 않는다. 사용자의 추가 지시로 완료 후 커밋·병합·원격 push·임시 파일 정리와 지정 폴더 handover까지 진행한다. 기존 구조와 표준 라이브러리를 사용한다.

설정 예제는 승인된 항목 번호를 명시하고 선택한 섹션만 병합한다. `SessionStart`는 hooks 선택 때만 함께 적용한다. 저장은 같은 디렉터리의 임시 파일에 완성한 뒤 `os.replace`로 교체한다. 테마를 선택하면 홈의 세 파일도 백업한다.

초기화·검증의 모든 읽기·쓰기 대상은 실제 경로가 프로젝트 내부인지 확인한다. 초기화는 템플릿을 작업용 임시 파일에 복사한 뒤 `os.link`로 최종 이름을 배타적으로 게시한다. 이미 생성된 사용자 파일은 보존하고 실패 정리는 임시 파일에만 수행한다. 하드링크 미지원 파일시스템에서는 오류로 중단한다. 경로 검사는 기존 junction·symlink 우회를 차단하며, 다른 프로세스가 검사 후 디렉터리를 교체하는 공격을 차단하는 OS 샌드박스를 대신하지 않는다.

Markdown 완료 검사는 fenced 코드와 inline code를 제외하고 실제 `-`·`*`·`+` 목록의 미완료 표기를 확인한다. API 문서는 해당 클라이언트 인증 UI와 원격 서버 기능을 구분하고 실제 도구 스키마를 확인하도록 안내한다.

## Task 1. 회귀와 최소 구현.

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

## Task 2. 문서와 검증.

Files: `rules/02_tool-boundaries.md`, `index.html`, `Skill/plugin-dev/hook-development.md`, `Skill/huggingface-skills/*.md`, `MCP/{context7,figma,huggingface-skills,README}.md`, `Owned-Skills/design-driven-delivery/{SKILL.md,references/document-contracts.md,assets/templates/{plan,review,handover}-template.md}`, `CHANGELOG.md`.

- [x] 공식 입력·응답 계약과 MCP 도구 인자, 정상 Bash 변수 확장, 인증·기능 구분을 수정하고 관련 표를 맞춘다.
- [x] 문서의 경로 경계·초기화 지원 조건·Markdown 검사 범위를 실행 동작에 맞춘다.
- [x] 전체 링크·앵커·UTF-8·코드 블록·Python 문법과 `git diff --check`를 확인한다.
- [x] 독립 코드 리뷰에서 발견 사항을 검증하고 해결한 뒤 `docs/reviews/2026-10-13-review-followup.md`에 결과를 기록한다.
- [x] 한글 커밋·main 통합·일반 push·임시 작업 트리 정리 절차를 준비한다. 실행 후 최종 해시·원격 일치·정리 상태를 지정한 handover에 기록한다.
