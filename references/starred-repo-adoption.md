<!-- 검토한 공개 저장소 26개의 선별 반영 판단과 선택 도구 사용 조건을 기록한다. -->
# 공개 저장소 선별 반영과 선택 도구 안내.

2026-10-12 검토 목록의 공개 저장소 26개를 2026-10-13에 비교했다. 요구사항·구현·문서·컨텍스트·도구 선택의 다섯 영역을 함께 보완한다. 이 문서는 채택 근거와 참고 안내이며 정식 행동 규칙은 아래 반영 위치에서 관리한다.

## 읽을 조건과 적용 방식.

기존 지침을 보완하거나 현재 도구로 충족하지 못하는 요구가 있어 추가 도구를 검토할 때 읽는다. 후보 전체를 매 작업마다 읽거나 설치할 필요는 없다.

| 판정 | 의미 |
|---|---|
| 내부 원칙 채택 | 기존 규칙을 구체화할 원칙만 반영한다. 외부 스킬 설치를 전제하지 않는다. |
| 선택 도구 안내 | 실제 기능이 필요한 경우에만 지원 환경과 도입 조건을 검토한다. |
| 운영 참고 | 프로젝트 초기화·팀 운영 방식이 필요해질 때 다시 검토한다. |
| 작업별 보류 | 영상·알림·세션 관리 등 해당 작업에서 판단한다. |
| 분야 참고 / 반영 제외 | 이번 공통 운영 지침의 범위에 직접 해당하지 않는다. |
| 사용자 지정 제외 | 이번 검토에서 제외하도록 정해진 별도 도구다. |

판정은 설치·활성 상태와 별개다. 이번 변경은 후보 설치, hooks·권한·전역 설정 변경, 타사 실행 원본 복제와 스킬·MCP 카탈로그 확장을 포함하지 않는다. 기존 카탈로그 개수는 유지한다.

## 내부 원칙의 정식 위치.

| 영역 | 참고 출처 | 반영 위치와 기존 중복 |
|---|---|---|
| 요구사항·설계 | mattpocock/skills | [상태 변경 워크플로](../Owned-Skills/design-driven-delivery/references/change-workflow.md)의 DISCUSSING. 기존 목적·실패·성공 조건을 실제 시나리오·관찰 가능한 결과로 구체화한다. |
| 구현·영향 | ponytail, ECC | 같은 워크플로의 DISCOVERED·IMPLEMENTING. 기존 조사·최소 변경 항목에 해결책 재사용과 호출자·테스트·설정 영향을 반영한다. |
| 답변·문서 | humanizer, i-have-adhd, mattpocock/skills | [핵심 출력 규칙](../AGENTS.md)과 [문서 계약](../Owned-Skills/design-driven-delivery/references/document-contracts.md). 문체·참조 조건을 보완하며 기존 문서 구조를 재사용한다. |
| 컨텍스트·연속성 | context-mode, ECC | [컨텍스트 관리](../rules/04_garbage-collection.md). 기존 상태·결정·미완료 항목 보존에 큰 성공 출력의 취급을 보완한다. |
| 도구 선택 | ECC, archify, open-code-review, openai/plugins | [도구 경계](../rules/02_tool-boundaries.md). 가용성·대체·도입 판단을 관리하고 아래에서는 후보별 필요 상황만 안내한다. |

## 후보 26개의 판단.

확인 범위의 `소개`는 원본 저장소의 README·소개를 확인했다는 뜻이다. `스킬`은 관련 SKILL.md 원문까지 확인했다는 뜻이며 실행 검증과 다르다. `목록`은 검토 목록의 설명만 확인했고 원문·실행은 검증하지 않았다는 뜻이다. 모든 후보의 실제 설치·성능·다른 환경 호환성은 미검증이다.

| 번호 | 원본 저장소 | 판정 | 채택 내용과 위치 | 기존 중복·사용 조건 또는 제외 이유 | 확인 범위 |
|---:|---|---|---|---|---|
| 1 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 선택 도구 안내 | 탐색 가능한 HTML 다이어그램 후보다. 아래 사용 조건에서 안내한다. | Mermaid·FigJam·playground로 부족하고 관계·경로 탐색이 필요할 때 검토한다. | 소개·스킬. |
| 2 | [blader/humanizer](https://github.com/blader/humanizer) | 내부 원칙 채택 | 결론과 사실을 보존하는 문체를 AGENTS 출력 규칙에 반영한다. | 전체 문체 패턴을 전역 강제하지 않는다. 코드·인용·고유명사·로그를 임의 편집하지 않는다. | 소개·스킬. |
| 3 | [mattpocock/skills](https://github.com/mattpocock/skills) | 내부 원칙 채택 | 실제 시나리오·용어·완료 기준은 워크플로, 문서 포인터는 문서 계약에 반영한다. | brainstorming·TDD·디버깅·리뷰·handover와 겹치는 묶음 설치는 이번 범위에서 제외한다. | 소개·writing-for-agents·domain-modeling 스킬. |
| 4 | [bilawalsidhu/gods-eye-view](https://github.com/bilawalsidhu/gods-eye-view) | 분야 참고 | 공통 지침의 신규 규칙은 없다. | 3D 지구·공간 정보 프로젝트의 참고 자료로 필요할 때 검토한다. | 소개. |
| 5 | [openai/plugins](https://github.com/openai/plugins) | 선택 도구 안내 | 필요한 Codex 플러그인의 출처와 구성 참고다. 아래 사용 조건에서 안내한다. | 기존 플러그인·스킬·MCP로 충족하지 못하는 작업이 있을 때 해당 묶음만 검토한다. | 소개. |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 내부 원칙 채택 | 기존 해결책 확인은 워크플로, 도구 가용성과 설정 도입 점검은 rules/02에 반영한다. | TDD·리뷰·메모리 절차는 이미 있다. 검색·보안 점검은 해당 필요와 변경 범위에 적용한다. | 소개·search-first·security-scan 스킬. |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 내부 원칙 채택 | 기존 해결책·영향 범위·재사용 순서를 워크플로에 반영한다. | 최소 변경은 기존 규칙과 일치한다. 설치된 경우 활용하고 승인·필수 검증·기능/버그 TDD를 면제하지 않는다. | 소개·설치 원문 5.1.1 스킬·매니페스트. |
| 8 | [mksglu/context-mode](https://github.com/mksglu/context-mode) | 선택 도구 안내 | 큰 출력 취급은 rules/04에 보완하고 실제 출력·세션 관리 기능은 선택 후보로 안내한다. | 기존 인수인계로 해결되지 않는 컨텍스트 문제가 반복될 때 검토한다. 전체 파일 읽기와 실패 증거를 대체하지 않는다. | 소개·클라이언트별 안내. |
| 9 | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | 선택 도구 안내 | 특정 플랫폼 콘텐츠 조회 후보다. 아래 사용 조건에서 안내한다. | 기존 웹 조회로 부족할 때만 검토한다. 플랫폼별 로그인·권한·데이터 취급 조건을 확인한다. | 소개. |
| 10 | [mvschwarz/openrig](https://github.com/mvschwarz/openrig) | 운영 참고 | 이번 신규 행동 규칙은 없다. | 기존 서브에이전트로 부족하고 지속적인 여러 에이전트의 역할·공유 작업 운영이 필요할 때 검토한다. | 소개. |
| 11 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 작업별 보류 | 이번 신규 행동 규칙은 없다. | HTML 기반 영상 제작·렌더링 작업에서 검토한다. | 소개. |
| 12 | [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | 분야 참고 | 공통 지침의 신규 규칙은 없다. | AI 학습 자료로 필요할 때 검토한다. | 소개. |
| 13 | [moeru-ai/airi](https://github.com/moeru-ai/airi) | 분야 참고 | 공통 지침의 신규 규칙은 없다. | 음성·캐릭터·게임 연동 프로젝트에서 참고한다. | 소개. |
| 14 | [lyogavin/airllm](https://github.com/lyogavin/airllm) | 분야 참고 | 공통 지침의 신규 규칙은 없다. | 모델 추론 프로젝트에서 메모리·성능 조건을 검증하며 참고한다. | 소개. |
| 15 | [pascalorg/editor](https://github.com/pascalorg/editor) | 분야 참고 | 공통 지침의 신규 규칙은 없다. | 3D 건축 편집·CLI·MCP 연동 프로젝트에서 검토한다. | 소개. |
| 16 | [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | 선택 도구 안내 | 별도 CLI·CI 코드 분석 후보다. 아래 사용 조건에서 안내한다. | 기존 code-review·security-review·Qodo와 중복 여부를 확인하고 추가 분석이 필요할 때 검토한다. | 소개. |
| 17 | [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) | 내부 원칙 채택 | 결론·행동 우선을 AGENTS 출력 규칙에 반영한다. | 독자의 개인 상태를 추정하지 않는다. 고정 목록 수·시간 추정·매 응답 상태 반복을 강제하지 않는다. | 소개·스킬. |
| 18 | [DevinoSolutions/anotifier-for-claude-codex-cursor](https://github.com/DevinoSolutions/anotifier-for-claude-codex-cursor) | 작업별 보류 | 이번 신규 행동 규칙은 없다. | 데스크톱·휴대폰 알림이 필요한 작업에서 전달 내용·설정 범위를 확인한다. | 소개. |
| 19 | [MorpheApp/morphe-manager](https://github.com/MorpheApp/morphe-manager) | 반영 제외 | 공통 지침의 신규 규칙은 없다. | Android 앱 패치 도구로 이번 운영 지침 보완과 직접 관계가 없다. | 소개. |
| 20 | [0x90d/videoduplicatefinder](https://github.com/0x90d/videoduplicatefinder) | 반영 제외 | 공통 지침의 신규 규칙은 없다. | 중복 영상 탐색 도구로 이번 운영 지침 보완과 직접 관계가 없다. | 소개. |
| 21 | [Genymobile/scrcpy](https://github.com/Genymobile/scrcpy) | 반영 제외 | 공통 지침의 신규 규칙은 없다. | Android 화면·기기 제어 도구로 이번 운영 지침 보완과 직접 관계가 없다. | 소개. |
| 22 | [DOHA1012/pokemon-champions-pc](https://github.com/DOHA1012/pokemon-champions-pc) | 반영 제외 | 공통 지침의 신규 규칙은 없다. | 게임 런처로 이번 운영 지침 보완과 직접 관계가 없다. | 소개. |
| 23 | [glowElephant/snap-path](https://github.com/glowElephant/snap-path) | 사용자 지정 제외 | 이번 반영에서 제외한다. | 별도 Agent 폴더의 도구라는 사용자 결정에 따른다. | 목록·사용자 지정. 원문 조회 실패, 실행 미검증. |
| 24 | [glowElephant/claude-session-manager](https://github.com/glowElephant/claude-session-manager) | 작업별 보류 | 이번 신규 행동 규칙은 없다. | 세션 목록·재개·기기 간 동기화 수요가 생기면 데이터 저장·인증 조건을 확인한다. | 소개. |
| 25 | [glowElephant/context-forge](https://github.com/glowElephant/context-forge) | 운영 참고 | 기존 프로젝트 문서 구조를 우선하는 초기화 방식의 참고다. | 기존 document-contracts와 겹친다. 새 프로젝트 초기화 자동화가 필요할 때 검토한다. | 소개. |
| 26 | [jojoldu/junior-recruit-scheduler](https://github.com/jojoldu/junior-recruit-scheduler) | 반영 제외 | 공통 지침의 신규 규칙은 없다. | 채용 정보 자료로 이번 운영 지침 보완과 직접 관계가 없다. | 소개. |

## 선택 도구 사용 조건.

| 후보 | 검토할 상황 | 기존 수단으로 충분한 상황 | 실제 도입 시 확인 |
|---|---|---|---|
| archify | 관계·경로를 탐색하는 HTML 구조도를 공유해야 한다. | 간단한 Mermaid 또는 편집 가능한 FigJam이면 충분하다. | 실행 환경·부속 자원·출처 증거·산출물 검증을 확인한다. 그림만으로 실제 실행 영향이 검증됐다고 주장하지 않는다. |
| context-mode | 큰 출력과 긴 세션으로 컨텍스트 문제가 반복된다. | 출력 요약과 기존 인수인계 규칙으로 해결된다. | 클라이언트 지원·저장 데이터·MCP와 hooks 각각의 동작을 확인한다. |
| Agent-Reach | 기존 웹 도구로 특정 플랫폼의 필요한 콘텐츠를 조회하기 어렵다. | 일반 웹 조회와 연결 도구로 확인할 수 있다. | 플랫폼별 인증·권한·데이터 취급과 실제 조회 경로를 확인한다. |
| open-code-review | 별도 CLI·CI 분석 또는 추가 리뷰가 필요하다. | 기존 code-review로 필요한 검토가 가능하다. | 모델 엔드포인트에 전달되는 코드 범위·권한·분석 결과와 기존 리뷰 중복을 확인한다. |
| openai/plugins | 필요한 Codex 플러그인의 출처·구성을 찾고 있다. | 현재 도구로 작업을 수행할 수 있다. | 필요한 묶음의 매니페스트·부속 파일·인증·클라이언트 지원을 확인한다. |

## 원문 근거와 유지 기준.

- 문서 구조·참조 조건은 [writing-for-agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md), 용어·결정 기록은 [domain-modeling](https://github.com/mattpocock/skills/blob/main/skills/engineering/domain-modeling/SKILL.md)을 참고했다.
- 재사용·영향 확인은 [ponytail](https://github.com/DietrichGebert/ponytail/blob/main/skills/ponytail/SKILL.md)과 [ECC search-first](https://github.com/affaan-m/ECC/blob/main/skills/search-first/SKILL.md), 설정 도입 점검은 [ECC security-scan](https://github.com/affaan-m/ECC/blob/main/skills/security-scan/SKILL.md)을 참고했다.
- 사실 보존·문체 적용 범위는 [humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md), 행동 우선은 [i-have-adhd](https://github.com/ayghri/i-have-adhd/blob/main/skills/i-have-adhd/SKILL.md)을 참고했다.
- 다이어그램의 의미·검증 구분은 [archify](https://github.com/tt-a1i/archify/blob/main/archify/SKILL.md), 출력·세션 관리 후보는 [context-mode 안내](https://github.com/mksglu/context-mode#readme)를 참고했다.

상세 패턴·벤치마크 수치·원본 코드를 재배포하지 않고 독립적으로 정리한 판단과 출처를 남긴다. 공개 원본의 기능·경로·지원 조건은 이후 바뀔 수 있으므로 실제 도입 시 다시 확인하고 원본 라이선스 조건을 따른다. 저장소 자체의 문서 라이선스가 타사 자료에 자동 적용되는 것은 아니다.

내부 원칙을 바꾸면 정식 반영 위치를 먼저 수정하고 이 문서의 채택 근거·연결을 맞춘다. 새로운 실행 도구를 실제 도입한 경우에만 설치·노출 여부를 확인한 별도 카탈로그 갱신을 검토한다.
