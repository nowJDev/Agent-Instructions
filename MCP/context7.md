# context7

> 라이브러리·프레임워크·SDK·CLI의 **최신 공식 문서**를 실시간으로 가져오는 MCP 서버 (Upstash Context7).

## 📌 용도
학습 데이터 컷오프 이후 변경되었을 수 있는 라이브러리 문서를 실시간으로 조회한다. React, Next.js, Prisma, Express, Tailwind, Django, Spring Boot 같이 잘 알려진 것까지 포함해, API 문법·설정·버전 마이그레이션·라이브러리별 디버깅·설치 방법·CLI 사용법 등을 다룬다.

> 서버 자체 지침: 라이브러리/프레임워크/SDK/API/CLI/클라우드 서비스에 대한 질문이면 **이미 안다고 생각해도** 이 서버를 우선 사용. 라이브러리 문서는 웹 검색보다 이걸 우선할 것.
> 사용하지 말 것: 리팩터링, 처음부터 스크립트 작성, 비즈니스 로직 디버깅, 코드 리뷰, 일반 프로그래밍 개념.

## 🎯 트리거 조건 / 사용 맥락
- 특정 라이브러리/프레임워크의 API 시그니처, 옵션, 설정값을 물을 때
- 버전 업그레이드/마이그레이션 가이드가 필요할 때
- "이 라이브러리 최신 사용법 / 이 함수 인자 뭐였지?" 류 질문
- CLI 도구 명령어/플래그 확인

## 🛠️ 제공 도구 목록

| 도구명 | 기능 | 주요 파라미터 |
|--------|------|----------------|
| resolve-library-id | 라이브러리 이름(예: "next.js")과 질문으로 Context7 내부의 정식 라이브러리 ID를 찾는다. 문서 조회 전 선행 단계 | `libraryName`·`query` 필수 |
| query-docs | 해석된 라이브러리 ID에 대해 문서를 질의해 관련 문서 스니펫 반환 | `libraryId`(resolve 결과)·`query` 필수, `language` 선택 |

[공식 도구 계약](https://github.com/upstash/context7#available-tools)을 기준으로 하며 설치 버전의 런타임 스키마도 확인한다.

### 표준 사용 흐름
1. `resolve-library-id`에 `libraryName`과 구체적인 `query`를 넣어 정식 ID를 찾는다. 여러 후보가 나오면 질문·버전에 맞는 것을 선택한다.
2. `query-docs`에 `libraryId`와 알고 싶은 내용을 담은 `query`를 넣어 최신 문서를 조회한다.

## 💻 사용 예시

**예시 1 — Next.js App Router 라우팅 최신 문법 확인**
1. `resolve-library-id`(`libraryName: "next.js"`, `query: "app router route handlers"`) → 예: `/vercel/next.js` ID 획득.
2. `query-docs`(`libraryId: "/vercel/next.js"`, `query: "app router route handlers"`) → 최신 예제 코드 수신 후 답변에 반영.

**예시 2 — Prisma 마이그레이션 명령어 확인**
1. `resolve-library-id`(`libraryName: "prisma"`, `query: "migrate dev command options"`).
2. `query-docs`(`libraryId: "<resolve 결과 ID>"`, `query: "migrate dev command options"`).

## 📦 출처 / 설치 상태
- 제공: **플러그인** `context7@claude-plugins-official`
- 활성화: ON (`settings.json` → `enabledPlugins["context7@claude-plugins-official"]: true`)
- 연결 방식: **stdio** — `npx -y @upstash/context7-mcp`
- 설정/캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/context7/unknown/.mcp.json`
- 세션 내 도구 식별자 접두사: `mcp__plugin_context7_context7__`
