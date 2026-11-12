<!-- 조사한 출처·노출·호출 조건을 설명 항목으로 보존한다. -->
# Codex 직접·시스템 패키지 보완.

기존 카탈로그·자체 제작 원본으로 연결되지 않았던 직접 패키지 16개의 설명이다. 설치된 실행본을 복사하지 않는다. 이름이 같은 이전 플러그인·내장 설명과 구분한다. [조사 증거](../../references/skill-inventory-2026-11-12.json)는 당시 파일 존재·노출·호출 정책을 구분하며, 현재 실행 성공을 뜻하지 않는다.

## user-firecrawl

**firecrawl** — 웹 검색·페이지 읽기·크롤링·상호작용을 작업에 맞는 Firecrawl 경로로 연결한다.

출처는 Firecrawl 전역 패키지다. 조사 세션 노출. 웹 작업의 최상위 안내이며 로컬 파일은 firecrawl-parse로 연결한다.

## user-paseo

**paseo** — Paseo의 호스트·프로젝트·작업 공간·에이전트·스케줄을 관리한다.

출처는 Paseo 스킬다. 조사 세션 노출. Paseo MCP 또는 CLI의 실제 가용성과 대상 작업 공간을 확인한다.

## user-paseo-advisor

**paseo-advisor** — 현재 작업에 대한 한 에이전트의 조언과 독립 의견을 구한다.

출처는 Paseo 스킬다. 조사 세션 노출. 사용자가 조언·두 번째 의견을 요청할 때 사용하며 작업 자체의 인수인계와 구분한다.

## user-paseo-committee

**paseo-committee** — 두 에이전트의 위원회로 원인과 어려운 계획을 검토한다.

출처는 Paseo 스킬다. 조사 세션 노출. 막힘·반복·어려운 계획에서 실제 다중 에이전트 기능을 확인한다.

## user-paseo-handoff

**paseo-handoff** — 현재 작업의 문맥을 다른 에이전트에게 인계한다.

출처는 Paseo 스킬다. 조사 세션 노출. 다른 에이전트로 작업을 넘기라는 요청과 실제 인계 기능을 확인한다.

## user-paseo-help

**paseo-help** — Paseo의 사용법·설정·연결·로그 문제를 설명한다.

출처는 Paseo 스킬다. 조사 세션 노출. Paseo 제품 질문에 사용하며 에이전트·작업 공간 조작은 paseo와 구분한다.

## user-paseo-plugin

**paseo-plugin** — Paseo의 신뢰된 로컬 플러그인을 제작·관리한다.

출처는 Paseo 스킬다. 조사 세션 노출. 플러그인 기능·허용 범위·수명주기와 실제 Paseo 환경을 확인한다.

## user-source-command-delete-session

**source-command-delete-session** — 현재 프로젝트의 세션 목록과 선택한 종료 세션의 제거를 다룬다.

출처는 원본 명령의 전역 변환본다. 조사 세션 노출. delete-session 자체 제작 패키지와 별개인 원본 명령 변환본이며 실제 대상 확인이 필요하다.

## user-source-command-handover

**source-command-handover** — 현재 세션을 다음 작업자가 이어갈 인수인계 문서로 정리한다.

출처는 원본 명령의 전역 변환본다. 조사 세션 노출. handover 자체 제작 패키지와 별개인 원본 명령 변환본이며 비공개 내용을 확인한다.

## user-unity-cli

**unity-cli** — CLI로 Unity Editor와 프로젝트·장면·빌드·테스트 작업을 제어한다.

출처는 Unity 스킬다. 조사 세션 노출. Unity CLI와 실행 중인 Editor의 연결·프로젝트·요청된 변경 범위를 확인한다.

## codex-user-migrate-to-codex

**migrate-to-codex** — 다른 도구의 지침·스킬·에이전트·MCP 설정을 Codex 형식으로 이전한다.

출처는 Codex 이전 도구다. 조사 세션 노출. 선택된 대상만 변환하고 원본 Claude 설정·인증 정보·관련 없는 파일은 보존한다.

## codex-system-imagegen

**imagegen** — 이미지 생성·편집·참조 변형으로 비트맵 시각 자산을 만든다.

출처는 Codex 시스템 스킬다. 조사 세션 노출. 비트맵 산출물에 사용하며 기존 SVG·코드 기반 자산을 고치는 작업과 구분한다.

## codex-system-openai-docs

**openai-docs** — Codex·OpenAI API·ChatGPT Work의 사용법과 설정 자료를 확인한다.

출처는 Codex 시스템 스킬다. 조사 세션 노출. OpenAI·Codex 관련 질문에 사용하며 일반 소프트웨어 작업과 구분한다.

## codex-system-review-agent

**review-agent** — 위임된 코드 변경을 읽기 전용으로 검토하고 재현 가능한 결함을 보고한다.

출처는 Codex 시스템 스킬다. 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 이번 세션 일반 스킬 목록에는 노출되지 않았다. 변경·커밋·푸시는 수행하지 않는다.

## codex-system-skill-creator

**skill-creator** — 범위가 명확한 Codex 스킬과 필요한 지원 리소스를 작성·갱신한다.

출처는 Codex 시스템 스킬다. 조사 세션 노출. Codex 시스템 구현이며 Anthropic 원본·기존 플러그인 동명 스킬과 구분한다.

## codex-system-skill-installer

**skill-installer** — 선정된 목록이나 저장소에서 Codex 스킬을 설치한다.

출처는 Codex 시스템 스킬다. 조사 세션 노출. 설치 대상·기존 패키지·리소스 보존과 실제 설치 경로를 확인한다.
