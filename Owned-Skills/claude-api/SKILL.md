---
name: claude-api
description: "Use when Anthropic Claude API·SDK·Agent SDK의 코드, 모델·가격·제한, 스트리밍·도구 호출·인증·마이그레이션을 명시적으로 묻거나 수정할 때 사용한다. 다른 제공자 작업이나 단순 Claude Code 설정에는 자동 적용하지 않는다."
---

# Claude API와 SDK.

## 입력과 제공자 판별.
- 사용자가 지정한 제공자·모델·언어·배포 환경과 요청이 설명인지 코드 변경인지 확인한다. Anthropic이 아닌 작업에 이 스킬을 강제하지 않는다.
- 제공자가 불분명하면 프로젝트 manifest·import와 대화에서 근거를 확인한다. 모델명이나 가격을 추정해 Anthropic으로 바꾸지 않는다.
- 코드 변경이면 설치된 `design-driven-delivery`를 적용하고 새 Agent SDK 앱이면 `new-sdk-app`을 참고한다. 해당 스킬이 없어도 변경 범위·완료 조건·계획을 확인한 뒤 최소 구현과 정상·실패 검증을 수행한다.

## 필요한 원문만 읽기.
언어·버전에 맞는 공식 문서만 읽는다. 이 패키지는 타사 원문을 보관하지 않으며, 참고 링크는 [공개 출처](references/sources.md)에 정리한다. 공식 예제의 기본 모델·호스트 선택도 현재 요청·도구·권한에 맞춰 판단한다.

| 작업 | 읽을 원문 |
|---|---|
| Python API | [공식 Python SDK](https://github.com/anthropics/anthropic-sdk-python)의 선택 버전 문서·타입. |
| TypeScript API | [공식 TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript)의 선택 버전 문서·타입. |
| C# API | [공식 C# SDK](https://github.com/anthropics/anthropic-sdk-csharp)의 선택 버전 문서·타입. |
| 기타 언어·전체 목차 | [공식 SDK 안내](https://docs.claude.com/en/api/client-sdks)에서 해당 언어만 선택한다. |
| 도구 호출 | [공식 도구 호출 안내](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview). |
| 오류·재시도 | [공식 오류 안내](https://docs.claude.com/en/api/errors). |
| 모델 변경 | [공식 모델 안내](https://docs.claude.com/en/docs/about-claude/models/overview)의 현재 ID·호환 범위. |
| 최신 모델·가격·한도 출처 | [공식 가격](https://docs.claude.com/en/docs/about-claude/pricing)과 [한도](https://docs.claude.com/en/api/rate-limits). |

## 수행 절차.
1. 조회 전에 설치 버전·lockfile·선택한 API 표면·인증 방식과 관련 호출자를 확인한다. 수정 파일은 전체를 읽고 기존 오류 처리·검증을 보존한다.
2. 모델 ID·가격·한도·최신 구문은 가용 검색·읽기 도구로 실제 공식 문서를 열어 검증한다. 캐시된 문서와 예제는 해당 버전의 자료이며 최신 사실의 증거로 단정하지 않는다.
3. 조회 불가 시 확인된 설치 버전·캐시 날짜와 불확실성을 명시한다. 현재 가격이나 모델을 만들어 답하지 말고 사용자가 확인할 공식 경로를 제공한다.
4. 사용자가 지정한 모델·호스팅 제공자를 보존한다. 예제의 기본 모델·상품 선택을 무조건 적용하거나 새 서비스·MCP를 도입하지 않는다.
5. 필요한 최소 요청·스트리밍 수명·오류·재시도·도구 입력 검증을 해당 버전의 타입·공식 예제와 대조해 구현한다. 다른 작업의 내부 데이터는 API 테스트에 보내지 않는다.
6. 키는 지원 환경변수·인증 경로로 주입하고 값은 출력·커밋하지 않는다. 키·네트워크가 없으면 mock·문법·타입 검사와 실제 원격 성공을 구분한다.
7. 정상·실패·도구 경계 입력을 프로젝트의 실제 검사로 확인하고, 요청된 원격 검증이 가능하면 최소 호출 결과를 확인한다.

## 결과.
선택 모델·SDK 버전·확인 날짜·정확한 공식 출처, 코드 변경·검증 명령·결과와 미검증 범위를 보고한다.
가격 질문에 네트워크가 없으면 숫자를 추측하지 않는 것이 올바른 결과다. 타입 검사가 통과해도 실제 인증·모델 응답까지 통과했다고 말하지 않는다.
