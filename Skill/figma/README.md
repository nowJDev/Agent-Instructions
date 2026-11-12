<!-- 같은 출처의 카탈로그 항목과 예제·실패 처리·출처를 모아 안내한다. -->
# figma 설명 카탈로그.

설명 문서이며 실행 스킬 설치본이 아니다. ON/OFF·캐시 표시는 작성 당시 Claude Code 환경의 기록이며 현재 클라이언트의 설치·노출·인증 상태와 구분한다. [전체 항목 목차](../CATALOG.md)에서 다른 분류를 찾는다.

- [figma-code-connect](#figma-code-connect).
- [figma-create-new-file](#figma-create-new-file).
- [figma-generate-design](#figma-generate-design).
- [figma-generate-diagram](#figma-generate-diagram).
- [figma-generate-library](#figma-generate-library).
- [figma-generate-project-plan](#figma-generate-project-plan).
- [figma-use-figjam](#figma-use-figjam).
- [figma-use-slides](#figma-use-slides).
- [figma-use](#figma-use).

## figma-code-connect

> Figma 컴포넌트를 코드 스니펫에 매핑하는 Code Connect 템플릿 파일(`.figma.ts`)을 생성·유지하는 스킬.

<a id="figma-code-connect---용도"></a>
### 📌 용도
Figma 컴포넌트를 코드 스니펫에 매핑하는 Code Connect **템플릿 파일**(`.figma.ts`)을 만든다. Figma URL을 받아 정해진 단계를 따라 템플릿을 생성한다. 이 스킬은 MCP 도구로 컴포넌트 컨텍스트를 가져오는 **템플릿 파일(`.figma.ts`)** 만 다룬다(파서 기반 `.figma.tsx` — `figma.connect()` + CLI 게시 — 는 범위 밖).

**6단계 워크플로우**
1. **Figma URL 파싱** — `fileKey`, `nodeId` 추출. nodeId 하이픈→콜론 변환(`1234-5678`→`1234:5678`).
2. **미매핑 컴포넌트 발견** — `get_code_connect_suggestions`(`excludeMappingPrompt: true`)로 미매핑 게시 컴포넌트 식별, `mainComponentNodeId` 추출.
3. **컴포넌트 속성 페치** — `get_context_for_code_connect`로 속성 정의(TEXT/BOOLEAN/VARIANT/INSTANCE_SWAP/SLOT) 확인.
4. **코드 컴포넌트 식별** — `figma.config.json`의 paths/importPaths로 코드 컴포넌트를 찾아 props 인터페이스 비교, 사용자 확인.
5. **템플릿 파일 생성**(`.figma.ts`) — 속성 매핑 메서드로 작성.
6. **검증** — 속성 커버리지, 유효·정확한 타입, 하드코딩 자식 없음, 보간 래핑 확인.

<a id="figma-code-connect---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: Code Connect 언급, Figma 컴포넌트 매핑, 디자인→코드 변환, `.figma.ts`/`.figma.js` 파일 생성/업데이트 요청.
- **언제 쓰지 않는가**: 파서 기반 `.figma.tsx`(CLI 게시) 작업, 컴포넌트 미게시 상태, Organization/Enterprise 플랜이 아닌 경우(Code Connect 미지원), Figma MCP 미연결 상태.

<a id="figma-code-connect---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
입력 예: `https://www.figma.com/design/QiEF6w564ggoW8ftcLvdcu/MyDesignSystem?node-id=4185-3778`
→ `fileKey = QiEF6w564ggoW8ftcLvdcu`, `nodeId = 4185:3778`

생성되는 템플릿 구조(`ComponentName.figma.ts`):
```ts
// url=https://www.figma.com/file/{fileKey}/{fileName}?node-id={nodeId}
// source={코드 컴포넌트 경로}
// component={코드 컴포넌트명}
import figma from 'figma'
const instance = figma.selectedInstance

const label = instance.getString('Label')
const variant = instance.getEnum('Variant', { 'Primary': 'primary', 'Secondary': 'secondary' })
const disabled = instance.getBoolean('Disabled')

export default {
  example: figma.code`<Button variant="${variant}" ${disabled ? 'disabled' : ''}>${label}</Button>`,
  imports: ['import { Button } from "primitives"'],
  id: 'button',
  metadata: { nestable: true }
}
```

<a id="figma-code-connect---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `get_code_connect_suggestions`, `get_context_for_code_connect` (Figma MCP).
- **속성 매핑 메서드**: `getString`(TEXT), `getBoolean`(BOOLEAN), `getEnum`(VARIANT, 모든 값 빠짐없이 매핑), `getInstanceSwap`(INSTANCE_SWAP), `getSlot`(SLOT 전용), `findInstance`/`findText`/`findConnectedInstance`(명명 자식 레이어).
- **보간 래핑**: 문자열→따옴표, 인스턴스/섹션(`executeTemplate().example`)→중괄호, 슬롯 섹션→`figma.code\`...\`` 내부 직접, boolean→조건식.
- **주요 규칙(Pitfalls)**: 템플릿 결과 문자열 연결 금지(`[object Object]` 발생), `hasCodeConnect()` 가드 사용 금지, `executeTemplate()` 전 `type === 'INSTANCE'` 체크, INSTANCE_SWAP엔 `getInstanceSwap()` 선호, 슬롯/자식 콘텐츠 하드코딩 금지, 속성명 대소문자 정확히, 코드 prop에 없는 속성 발명 금지.
- 부속 참조: `references/api.md`(전체 API), `references/advanced-patterns.md`(중첩·메타데이터 prop 전달).

<a id="figma-code-connect---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON (`disable-model-invocation: false`)
- 관련 MCP: Figma MCP 연동(`get_code_connect_suggestions`, `get_context_for_code_connect` 등). MCP 미연결 시 활성화 후 재시작 안내.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-code-connect/SKILL.md`

## figma-create-new-file

> 새 빈 Figma 파일(design/figjam/slides)을 생성하는 스킬. `create_new_file` 호출의 필수 선행 스킬.

<a id="figma-create-new-file---용도"></a>
### 📌 용도
`create_new_file` MCP 도구로 사용자 드래프트 폴더에 새 빈 Figma 파일을 만든다. 작업할 새 파일이 필요할 때(특히 `use_figma` 이전에) 사용한다. 이 스킬은 plan 해석 결정 트리, editorType 계약, 생성 후 `use_figma`로의 핸드오프를 인코딩한다.

> **필수(MANDATORY)**: 모든 `create_new_file` 호출 전에 이 스킬을 먼저 로드해야 한다. 직접 호출 금지.

**3단계 워크플로우**
1. **planKey 해석** — 사용자가 제공했으면 그대로 사용. 없으면 `whoami` 호출 → `plans` 배열에서 단일 플랜은 자동 사용, 복수면 사용자에게 어느 팀/조직인지 질문.
2. **create_new_file 호출** — `planKey`, `fileName`, `editorType` 전달.
3. **결과 사용** — `file_key`, `file_url` 반환. `file_key`를 후속 `use_figma` 등에 사용.

<a id="figma-create-new-file---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 새 빈 Figma 파일(design/figjam/slides)을 원할 때, 또는 `use_figma` 전에 새 파일이 필요할 때. `/figma-create-new-file [editorType] [fileName]`.
- **언제 쓰지 않는가**: 기존 파일에서 작업할 때, 다이어그램 생성(→ `generate_diagram`은 자체 파일 생성하므로 이 스킬 선행 불필요).

<a id="figma-create-new-file---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```
/figma-create-new-file                          # design 파일 "Untitled"
/figma-create-new-file figjam My Whiteboard     # FigJam 파일
/figma-create-new-file design My New Design     # design 파일
/figma-create-new-file slides Q3 Review         # Slides 프레젠테이션
```
- **인자**: `editorType`(`design` 기본 / `figjam` / `slides`), `fileName`(기본 "Untitled").

호출 페이로드 예:
```json
{ "planKey": "team:123456", "fileName": "My New Design", "editorType": "design" }
```

<a id="figma-create-new-file---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `create_new_file`, `whoami`(planKey 해석용).

| 파라미터 | 필수 | 설명 |
| --- | --- | --- |
| `planKey` | 예 | Step 1에서 얻은 플랜 키 |
| `fileName` | 예 | 새 파일 이름 |
| `editorType` | 예 | `"design"` / `"figjam"` / `"slides"` |

**주의**:
- 파일은 선택한 플랜의 **드래프트 폴더**에 생성.
- `use_figma`가 다음 단계면 `figma-use` 스킬을 먼저 로드.
- **Slides 특이사항**: 새로 만든 slides 파일은 행 0개·슬라이드 0개인 빈 그리드(`getSlideGrid()` → `[]`). 첫 `createSlide()`가 row 0과 슬라이드를 암묵 생성. 첫 슬라이드 존재를 가정하는 후속 스크립트는 빈 경우를 가드하거나 `createSlide()`를 먼저 호출(자세히는 `figma-use-slides → slide-grid`).

<a id="figma-create-new-file---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON (`disable-model-invocation: false`)
- 관련 MCP: Figma MCP 연동(`create_new_file`, `whoami`)
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-create-new-file/SKILL.md`

## figma-generate-design

> 코드/설명으로부터 디자인 시스템을 재사용해 Figma에 화면·뷰·다중 섹션 레이아웃을 구축/업데이트하는 스킬.

<a id="figma-generate-design---용도"></a>
### 📌 용도
게시된 디자인 시스템(컴포넌트·변수·스타일)을 **재사용**해 Figma에 화면·뷰·다중 섹션 UI 컨테이너를 만들거나 업데이트한다. 전체 페이지, 모달, 다이얼로그, 드로어, 사이드바, 패널 등 다중 섹션 합성 뷰가 대상이다. 핵심 인사이트: Figma 파일에는 코드의 UI 컴포넌트/토큰에 대응하는 게시 디자인 시스템이 있으므로, 박스에 hex 색을 칠하는 대신 그것을 찾아 사용한다.

> **필수**: 모든 `use_figma` 호출 전에 [figma-use](#figma-use)도 로드(색상 범위·폰트 로딩 등 핵심 규칙). `use_figma` 호출 시 `skillNames: "figma-generate-design"` 전달(로깅용).

**핵심 워크플로우**
- **Step 1**: 산출물 이해 — 소스 읽고 섹션/컴포넌트 식별, 이미지 포함 여부 확인.
- **Step 2**: 컴포넌트 키·변수·스타일 수집 — (2a-i) Code Connect 우선 확인 → (2a-ii) 기존 화면 인스펙트 → (2a-iii) 최후로 `search_design_system`. (2b) 변수, (2c) 스타일 발견.
- **Step 3**: 래퍼 프레임 먼저 생성(섹션을 페이지 자식으로 만들고 reparent 금지).
- **Step 4**: 래퍼 안에 섹션을 한 번에 하나씩 빌드(자체 `use_figma` 호출). 인스턴스 텍스트는 `setProperties()`로 오버라이드.
- **Step 5**: 전체 뷰 검증 + 이미지 전송(웹앱+이미지 시 `generate_figma_design` 병렬 캡처에서 `imageHash` 복사).
- **Step 6**: 기존 뷰 업데이트(`get_metadata`로 구조 확인, 변경 섹션만 수정).

<a id="figma-generate-design---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "write to Figma", "create in Figma from code", "push page to Figma", "create a screen", "build a landing page in Figma", "update the Figma screen to match code", "convert this modal/dialog/drawer/panel to Figma". 코드/설명에서 전체 페이지·모달·드로어·사이드바·패널 등 다중 섹션 뷰를 만들거나 업데이트.
- **언제 쓰지 않는가**: 새 재사용 컴포넌트/배리언트 생성(→ `figma-use` 직접), Code Connect 매핑 작성(→ `figma-code-connect`).

<a id="figma-generate-design---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```js
// 래퍼 먼저 생성(Step 3) — 빈 공간 찾아 배치, ID 반환
const wrapper = figma.createAutoLayout("VERTICAL");
wrapper.name = "Homepage"; wrapper.resize(1440, 100);
wrapper.layoutSizingHorizontal = "FIXED";
return { success: true, wrapperId: wrapper.id };
```
```js
// 섹션 빌드(Step 4) — 디자인 시스템 의존성 병렬 임포트
const [wrapper, buttonSet, bgColorVar] = await Promise.all([
  figma.getNodeByIdAsync("WRAPPER_ID"),
  figma.importComponentSetByKeyAsync("BUTTON_SET_KEY"),
  figma.variables.importVariableByKeyAsync("BG_COLOR_VAR_KEY"),
]);
```

<a id="figma-generate-design---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `use_figma`, `search_design_system`(+ `includeComponents`/`includeVariables`/`includeStyles`/`includeLibraryKeys`), `get_libraries`, `get_screenshot`, `get_metadata`, `generate_figma_design`(웹앱 픽셀퍼펙트 캡처, 이미지 필수 시 병렬).
- **하드 게이트**: 2a-i 완료 + 2a-ii 시도/로그 전 `search_design_system` 금지. Step 2 모든 행 완료 전 캔버스 변형 `use_figma` 금지.
- **변수 발견 주의**: `getLocalVariableCollectionsAsync()`는 로컬 변수만 — 비어 있어도 "변수 없음" 결론 금지. 라이브러리 변수는 `search_design_system`(`includeVariables: true`)로 확인.
- **빌드 vs 임포트**: 래퍼·섹션 컨테이너·레이아웃 그리드는 수동, 컴포넌트·변수(색/간격/반경)·텍스트/이펙트 스타일은 디자인 시스템에서 임포트. hex/픽셀 하드코딩 금지(`setBoundVariable`/`setBoundVariableForPaint`).
- 참조: `figma-use`의 component-patterns/variable-patterns/text-style-patterns/effect-style-patterns/gotchas.

<a id="figma-generate-design---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON (`disable-model-invocation: false`)
- 관련 MCP: Figma MCP 연동 필수(게시 디자인 시스템 있는 대상 파일 필요). `figma-use`와 함께 로드.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-generate-design/SKILL.md`

## figma-generate-diagram

> Mermaid.js 구문으로 편집 가능한 FigJam 다이어그램을 생성하는 스킬. `generate_diagram` 호출의 필수 선행 스킬.

<a id="figma-generate-diagram---용도"></a>
### 📌 용도
`generate_diagram` 도구는 Mermaid.js 구문을 받아 편집 가능한 FigJam 다이어그램을 만든다. 이 스킬은 타입별 가이드로 라우팅하고 보편 제약을 설정하며, 다른 다이어그램 타입을 써야 하거나 도구를 아예 건너뛰어야 할 때를 알려준다.

> **필수**: 모든 `generate_diagram` 호출 전에 이 스킬을 로드해야 한다. 스킵 시 렌더링 실패·저품질 발생.

**7단계 흐름**: (1) 도구가 적합한지 판단 → (2) 다이어그램 타입 선택 → (3) 보편 제약 적용 → (4) GIGO(맥락 충분히 수집) → (5) Mermaid 한계 초과 여부(하이브리드 워크플로우 판단) → (6) 도구 호출 → (7) 생성 후 처리.

<a id="figma-generate-diagram---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 다이어그램 생성/그리기 요청 — flowchart, architecture, sequence diagram, ERD, state diagram, gantt/timeline. Mermaid 구문 언급, 시스템 아키텍처·결정 트리·의존성 그래프·API 호출 흐름·인증 핸드셰이크·스키마·파이프라인을 FigJam에 시각화.
- **언제 쓰지 않는가(도구 호출 금지)**: pie chart, mindmap, venn, class diagram, journey, timeline, quadrant, C4, git graph, requirement diagram — 사용자에게 미지원임을 직접 알릴 것. 기존 다이어그램의 폰트 변경/개별 도형 이동/노드별 편집은 Figma에서 직접 편집 권장.

<a id="figma-generate-diagram---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
**지원 타입**: `flowchart`, `sequenceDiagram`, `stateDiagram`/`stateDiagram-v2`, `gantt`, `erDiagram`.

**타입 라우팅**(첫 매치 사용):
| 사용자 의도 | 타입 | 참조 |
| --- | --- | --- |
| 서비스+데이터스토어+큐+통합 | Architecture flowchart | `references/architecture.md` |
| 결정 트리/프로세스/파이프라인/의존성 | Flowchart | `references/flowchart.md` |
| 시간순 상호작용(API/인증/메시징) | Sequence | `references/sequence.md` |
| 데이터 모델/테이블/키/카디널리티 | ER | `references/erd.md` |
| 명명된 상태+전이 | State | `references/state.md` |
| 일정/마일스톤 | Gantt | `references/gantt.md` |

도구 호출(필수: `name`, `mermaidSyntax`; 선택: `userIntent`, `useArchitectureLayoutCode`(아키텍처 전용), `fileKey`).

<a id="figma-generate-diagram---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `generate_diagram`, 하이브리드 확장 시 `use_figma`(FigJam 전용 API), `get_figjam`/`get_design_context`(맥락 수집).
- **보편 제약**: 이모지 금지, 라벨 내 `\n` 금지, HTML 태그 금지, 예약어(`end`/`subgraph`/`graph`)를 노드 ID로 금지, 노드 ID camelCase·공백 금지, 특수문자 라벨은 따옴표, sequence의 `Note over/left/right`는 제거됨(하이브리드로), gantt 스타일링은 전처리에서 제거됨.
- **FigJam 전용 API 제약**: 출력이 FigJam(`figma.com/board/...`)이므로 `figma.createPage()` 호출 금지(Design 전용) — FigJam 섹션으로 정리.
- **하이브리드 워크플로우**: 스티키 주석, ERD 노드별 색상, 데이터 첨부 콜아웃 등 Mermaid가 못 하는 것은 `generate_diagram` + `use_figma`(`figma-use-figjam`) 조합. 사전 `references/workflow.md` 로드.
- **파일 재사용**: 반복/관련 다이어그램은 `fileKey` 전달로 기존 파일 재사용(매 호출이 새 드래프트 생성).

<a id="figma-generate-diagram---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON
- 관련 MCP: Figma MCP 연동(`generate_diagram` — 자체 FigJam 파일 생성, 따라서 `create_new_file` 선행 불필요).
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-generate-diagram/SKILL.md`

## figma-generate-library

> 코드베이스로부터 Figma에 프로페셔널급 디자인 시스템(변수/토큰, 컴포넌트 라이브러리, 테마)을 구축/업데이트하는 스킬.

<a id="figma-generate-library---용도"></a>
### 📌 용도
Figma에 코드와 일치하는 프로페셔널급 디자인 시스템을 구축한다. 20~100+회의 `use_figma` 호출에 걸친 다단계 워크플로우를 오케스트레이션하며, 실제 디자인 시스템(Material 3, Polaris, Figma UI3 등)의 품질 패턴을 강제한다. **무엇을 어떤 순서로** 만들지 가르치며, **어떻게** Plugin API를 호출하는지는 `figma-use`가 보완한다(둘 다 로드 필요).

> `use_figma` 호출 시 `skillNames: "figma-generate-library"` 전달(로깅용).

**가장 중요한 한 규칙**: 절대 원샷 작업이 아니다. 모든 작업을 최소 단위로 쪼개고, 검증하고, 피드백 받고, 진행한다.

**필수 페이즈 순서**
- **Phase 0 DISCOVERY** — 코드베이스 분석, Figma 인스펙트, 구독 라이브러리 검색, v1 스코프 락, 코드↔Figma 매핑. ✋체크포인트: 전체 계획 승인.
- **Phase 1 FOUNDATIONS** — 변수 컬렉션·모드, primitive/semantic 변수, scopes, code syntax, effect/text 스타일. ✋체크포인트.
- **Phase 2 FILE STRUCTURE** — 페이지 스켈레톤(Cover→Getting Started→Foundations→Components→Utilities), foundations 문서. ✋체크포인트.
- **Phase 3 COMPONENTS** — 컴포넌트를 하나씩(원자→분자 순서) 생성·배리언트·속성·문서·검증. ✋컴포넌트별 체크포인트.
- **Phase 4 INTEGRATION + QA** — Code Connect 마무리, 접근성·네이밍·바인딩 감사, 최종 스크린샷. ✋사인오프.

<a id="figma-generate-library---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 변수/토큰 생성, 컴포넌트 라이브러리 구축, 적절한 배리언트 세트·변수 바인딩의 개별 컴포넌트 생성, 테마(light/dark) 설정, 파운데이션 문서화, 코드↔Figma 갭 조정. "Figma에 컴포넌트 만들어/생성해" — 단일 컴포넌트라도 변수 파운데이션·배리언트 상태·토큰 바인딩이 필요하므로 이 스킬.
- **언제 쓰지 않는가**: 합성 화면/뷰 빌드(→ `figma-generate-design`), 단순 Plugin API 작업(→ `figma-use`).

<a id="figma-generate-library---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
표준 토큰 아키텍처:
```
Collection "Primitives"  modes: ["Value"]   blue/500 = #3B82F6, gray/900 = #111827
Collection "Color"       modes: ["Light","Dark"]
  color/bg/primary → Light: alias Primitives/white, Dark: alias Primitives/gray-900
Collection "Spacing"     modes: ["Value"]   spacing/xs = 4, spacing/md = 16
```
상태 영속(컨텍스트 truncation 대비): `/tmp/dsb-state-{RUN_ID}.json`에 ledger 기록, 매 턴 재독.

<a id="figma-generate-library---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `use_figma`(직렬만 — 절대 병렬 금지), `get_libraries`, `search_design_system`(`includeComponents`/`includeVariables`/`includeStyles`/`includeLibraryKeys`), `get_metadata`, `get_screenshot`.
- **핵심 규칙**: 변수 BEFORE 컴포넌트, 생성 전 인스펙트, 컴포넌트당 1페이지(기본), 시각 속성은 변수 바인딩, 모든 변수에 scopes(ALL_SCOPES 금지)·code syntax(WEB은 `var()` 래퍼), semantic은 primitive에 alias, combineAsVariants 후 배리언트 그리드 배치, 아이콘은 INSTANCE_SWAP(배리언트 폭증 방지), 결정적 네이밍, 비파괴 클린업, 검증 후 진행, 노드 ID 환각 금지.
- **상태 관리**: `getPluginData`/`setPluginData` 미지원 → `getSharedPluginData`/`setSharedPluginData` 또는 이름·ledger 사용. 재개 프로토콜·continuation 프롬프트 제공.
- 참조 문서: `discovery-phase.md`, `token-creation.md`, `component-creation.md`, `code-connect-setup.md`, `naming-conventions.md`, `error-recovery.md`. 헬퍼 스크립트: `scripts/`(inspectFileStructure, createVariableCollection, createComponentWithVariants 등).

<a id="figma-generate-library---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON (`disable-model-invocation: false`)
- 관련 MCP: Figma MCP 연동 필수. `figma-use`와 반드시 함께 로드.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-generate-library/SKILL.md`

## figma-generate-project-plan

> PRD(+선택적 코드베이스 컨텍스트)를 **FigJam 프로젝트 플랜 보드**로 변환하는 인터랙티브 워크플로 스킬. 섹션 후보 제안 → 사용자 선택 → 섹션별 콘텐츠·블록 확정 → FigJam 생성까지 단계마다 확인을 거친다.

아래 상세는 기존 Claude 플러그인 워크플로의 설명이다. 현재 Codex의 동명 실행 원본은 [자체 제작 figma-generate-project-plan](../../Owned-Skills/figma-generate-project-plan/SKILL.md)이며 외부 Figma 원본 8개와 구분한다. 실제 호출에서는 설치 원본과 필수 선행 스킬·도구·인증을 확인하고, 전제가 없으면 로컬 초안까지만 준비한다.

<a id="figma-generate-project-plan---용도"></a>
### 📌 용도
PRD를 받아 FigJam에 프로젝트 플랜 보드를 그린다. 섹션 집합은 고정이 아니라 리서치에서 **후보를 제안하고 사용자가 포함할 섹션을 고른다.** 선택된 각 섹션마다 콘텐츠 + 렌더링 블록(표/멀티컬럼/스티키 컬럼/다이어그램 등)을 제안하고 사용자가 확인한다. 전체 **9단계**로 진행한다:
1. 컨텍스트 수집(PRD·코드베이스 grounding) → 2. 섹션 후보 제안 → 3. 섹션별 심층 리서치(갭 도출) → 4. 콘텐츠 + 블록 제안 → 5. FigJam 파일 생성 → 6. 스켈레톤 → 7. 섹션별 채우기 → 8. 다이어그램 → 9. 최종 검토·리포트

각 단계는 Research(셀프체크) / Confirm(AskUserQuestion) / Write(스크린샷 + AskUserQuestion) 세 유형 중 하나이며, **확인 안 된 체크포인트를 지나쳐 쓰지 않는다.**

<a id="figma-generate-project-plan---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: "/generate-project-plan", "project plan in FigJam", "interactive project plan", "PRD to FigJam", PRD를 주며 섹션별 확인을 원할 때. `disable-model-invocation: false`라 모델이 자동 호출도 가능.
- **언제 쓰지 않는가**: 단순 다이어그램만(→ `figma-generate-diagram`), 디자인 시안 생성(→ `figma-generate-design`), 일반 FigJam 편집(→ `figma-use-figjam`).

<a id="figma-generate-project-plan---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
- `/generate-project-plan` + PRD 경로 또는 붙여넣기 → (선택) 코드베이스 진입점 지정
- 흐름: 컨텍스트 수집 → 섹션 후보 멀티셀렉트(≤4개씩 배치 질문) → 섹션별 갭 질문 → 콘텐츠·블록 확인 → 파일 생성(probe) → 스켈레톤(스크린샷 확인) → 섹션별 채우기(섹션마다 확인) → 다이어그램(생성·reparent) → 전체 스크린샷 최종 검토
- 0개 섹션 선택 시: 깔끔히 중단, 파일 생성 안 함.

<a id="figma-generate-project-plan---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **MCP 도구**: `create_new_file`, `use_figma`, `generate_diagram`, `whoami`(planKey 확인)
- **선행 필수 스킬**: `figma-use`와 `figma-use-figjam`(매 `use_figma` 호출 전 로드), `figma-generate-diagram`(매 `generate_diagram` 전 로드).
- **블록 서브스킬**(콘텐츠 타입별 reference): section / nested-section / intro-callout / text-primitives / table / multi-column-text / sticky-column / diagram-section / metadata-strip
- **STRICT 규칙**: `section.name = ""`(제목은 내부 H2 텍스트), 섹션 배경은 `ARCH_PALE` 팔레트(FigJam 표준 SECTION 팔레트 금지 — 다이어그램과 색 충돌), 표 셀은 `Inter Bold` 16px, 자식 위치는 `prevChild.y + height + 24`(고정 오프셋 금지), `use_figma` 1회당 ≤10 논리 연산, 모든 write 스크립트는 `createdNodeIds`/`mutatedNodeIds` 반환
- **다이어그램 주의**: reparent 후 커넥터는 **삭제·재생성**(stale elbow 방지), 커넥터 라벨은 `fontName`+`fontSize`+`characters`+`fills` 4개 모두 설정(기본 `fills=[]`라 투명)

<a id="figma-generate-project-plan---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON
- 관련 MCP: figma MCP (`create_new_file`·`use_figma`·`generate_diagram`·`whoami`)
- 과거 Claude 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/workflow-skills/generate-project-plan/SKILL.md` (※ 다른 figma 스킬과 달리 `skills/`가 아닌 `workflow-skills/` 하위). 현재 Codex 출처는 위 자체 제작 원본이다.

## figma-use-figjam

> FigJam 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 FigJam 특화 스킬. `figma-use`와 함께 사용.

<a id="figma-use-figjam---용도"></a>
### 📌 용도
`use_figma` MCP 도구를 FigJam(`figma.com/board/...`) 컨텍스트에서 쓰기 위한 FigJam 특화 컨텍스트를 제공한다. 기반 컨텍스트와 전체 Plugin API는 [figma-use](#figma-use)에 있고, 이 스킬은 FigJam만의 차이(인스펙션 도구, 이미지 업로드, 노드 타입, 색상 등)를 다룬다.

> `use_figma`를 FigJam 작업에 호출할 때 `skillNames: "figma-use-figjam"` 전달(로깅용).
> **FigJam에서 `figma.createPage()` 금지** — Design 전용 API. FigJam은 단일 암묵 페이지이며 섹션으로 콘텐츠를 정리.

<a id="figma-use-figjam---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: FigJam 보드(`figma.com/board/...`)에서 `use_figma`로 작업할 때 — 스티키/섹션/커넥터/도형/텍스트/표/코드블록/라벨 생성·수정, 보드 템플릿/레트로/브레인스토밍/회의 보드 구성, 마인드맵 등. `figma-use`와 함께 로드.
- **언제 쓰지 않는가**: Design 파일(→ `figma-use` 단독), Slides 파일(→ `figma-use-slides`).

<a id="figma-use-figjam---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
**인스펙션**: `get_figjam`이 FigJam 인스펙션 도구. 전체 노드 트리를 XML로 반환(페이지/섹션/스티키/커넥터 ID 포함). 후속 `use_figma`에서 ID 참조 전 먼저 호출. `console.log`는 반환되지 않으므로 인스펙션 스크립트로 ID 발견 금지 — `return` 또는 `get_figjam` 사용.
- `get_metadata`는 FigJam에서 **동작 안 함**(design 전용).
- `get_screenshot`은 유효한 `nodeId` 필요(`get_figjam`에서 먼저 획득).

**이미지 추가**: `upload_assets`가 FigJam에 이미지를 추가하는 **유일한** 지원 방법. `figma.createImage()`/`createImageAsync()`는 FigJam에서 미지원. FigJam `fileKey`로 호출 → 단일사용 업로드 URL 반환 → raw 바이트 POST. `nodeId`(+`count:1`) 전달 시 기존 노드에 fill로 부착, 생략 시 새 레이어로 배치.

```
ToolSearch query="select:use_figma,get_figjam,get_screenshot,get_metadata,create_new_file"
```

<a id="figma-use-figjam---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `use_figma`, `get_figjam`(인스펙션), `get_screenshot`, `create_new_file`, `upload_assets`(이미지). (`get_metadata`는 FigJam 미지원)
- **텍스트 mutation**: Design과 동일한 canonical recipe(폰트 로드→await→mutate→ID 반환). FigJam 서브레이어 기본 폰트가 다름(sticky/shape → `Inter Medium`, connector → 설정 전 invalid)이므로 하드코딩 대신 `node.text.fontName`에서 로드.
- **참조 문서**: `plan-board-content`(보드 콘텐츠 요청 시 필수), `create-section`/`create-sticky`/`create-connector`/`create-text`/`create-shape-with-text`/`create-code-block`/`create-table`/`create-label`, `position-figjam-nodes`, `edit-text`, `batch-modify`, `figjam-colors`(노드 타입별 팔레트 + `hex/255` 규칙·`h()` 헬퍼). 여러 참조가 필요하면 단일 병렬 배치로 읽기.

<a id="figma-use-figjam---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON (`disable-model-invocation: false`)
- 관련 MCP: Figma MCP 연동(FigJam 컨텍스트). `figma-use` 기반 위에서 동작.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-use-figjam/SKILL.md`

## figma-use-slides

> Slides 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 Slides 특화 스킬. `figma-use`와 함께 사용.

<a id="figma-use-slides---용도"></a>
### 📌 용도
`use_figma` MCP 도구를 Figma Slides(`figma.com/slides/...`) 컨텍스트에서 쓰기 위한 Slides 특화 컨텍스트를 제공한다. 기반 컨텍스트와 전체 Plugin API는 [figma-use](#figma-use)에 있고, 이 스킬은 Slides만의 차이(슬라이드 그리드, 좌표 오프셋, 스피커 노트, 디자인 씽킹 등)를 다룬다.

> `use_figma`를 Slides 작업에 호출할 때 `skillNames: "figma-use-slides"` 전달(로깅용).

<a id="figma-use-slides---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: Slides 파일(`figma.com/slides/...`)에서 `use_figma`로 작업할 때 — 슬라이드/섹션 생성·복제·삭제·재정렬, 슬라이드 내 콘텐츠(텍스트/도형/오토레이아웃) 빌드, 테마/팔레트 설정, 스피커 노트 작성, 덱 디자인. `figma-use`와 함께 로드.
- **언제 쓰지 않는가**: Design 파일(→ `figma-use` 단독), FigJam 파일(→ `figma-use-figjam`).

<a id="figma-use-slides---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
**슬라이드 목록 인스펙션**:
```js
const grid = figma.getSlideGrid();
return grid.map((row, rowIdx) =>
  row.map((slide, colIdx) => ({
    id: slide.id, name: slide.name, row: rowIdx, col: colIdx,
    isSkipped: slide.isSkippedSlide, speakerNotes: slide.speakerNotes,
  }))
);
```
**섹션 이름 변경**(SLIDE_ROW에 직접 — 그리드 내부 JS 배열에 `.name` 설정은 no-op):
```js
const slideGrid = figma.currentPage.children.find(c => c.type === "SLIDE_GRID");
slideGrid.children[0].name = "Intro";
```

<a id="figma-use-slides---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `use_figma`(읽기전용 인스펙션 포함), `get_screenshot` / `await node.screenshot()`(시각 컨텍스트). (`get_metadata`는 Slides 미지원 — 읽기전용 스크립트로 검증)
- **Slides 특화 Critical Rules**: ①새 Slides 파일은 기본 light 테마(스캐폴딩 — 자체 디자인으로 덮어쓰기). ②`x`/`y` 설정 전 슬라이드에 `appendChild` 먼저(좌표 오프셋 방지). ③SLIDE_GRID/SLIDE_ROW는 불투명 노드(`.fills`/`.effects`/레이아웃 접근 금지; `SLIDE_ROW.name`만 설정 가능). ④`get_metadata` 미동작. ⑤`figma.createPage()` 금지(Design 전용) — 슬라이드 그리드로 구조 구성.
- **디자인 씽킹 기어**: 콘텐츠/속성 편집(씽킹 스킵, 기존 매칭), 구조적 추가(inherit 모드 — 기존 덱 언어 매칭), 새 덱 생성(풀 디자인 프로세스 — 브리프 읽기, 디자인 언어 확인, 포지션 취하기, 시그니처 부여).
- **스피커 노트**: 요청 시/프레젠터 준비 덱에 작성. 슬라이드 반복 금지, 간결·스캔 가능, 전환·맥락 포함. `slide.speakerNotes`는 마크다운(리스트/볼드/이탤릭/취소선 지원; 헤딩/코드블록/링크 미지원). 무프롬프트 추가 금지.
- **레퍼런스 파일 읽기**: Slides 참조는 `get_screenshot`+읽기전용 스크립트, Design 참조는 `get_design_context`.
- 참조: `slide-gotchas`, `slide-lifecycle`, `slide-grid`, `slide-content`, `slide-properties`, `slide-design`.

<a id="figma-use-slides---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON (`disable-model-invocation: false`)
- 관련 MCP: Figma MCP 연동(Slides 컨텍스트). `figma-use` 기반 위에서 동작.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-use-slides/SKILL.md`

## figma-use

> Figma Plugin API로 JavaScript를 실행해 노드를 생성/편집/조회하는 기반 스킬. 모든 `use_figma` 호출의 필수 선행 스킬.

<a id="figma-use---용도"></a>
### 📌 용도
`use_figma` 도구로 Figma 파일 컨텍스트에서 JavaScript를 실행(Plugin API)한다. 노드 생성/편집/삭제, 변수·토큰 설정, 컴포넌트·배리언트 빌드, 오토레이아웃·fill 수정, 변수 바인딩, 파일 구조 프로그래밍적 인스펙트 등. 상세 레퍼런스는 모두 `references/`에 있다.

> **필수**: 모든 `use_figma` 호출 전에 이 스킬을 로드해야 한다. 스킵 시 디버깅 어려운 흔한 실패 발생. `use_figma` 호출 시 `skillNames: "figma-use"` 전달(로깅용).

- 전체 페이지/화면/다중 섹션 레이아웃을 코드에서 빌드/업데이트 → `figma-generate-design`도 로드.
- 컴포넌트(단일 포함) 생성/빌드 → `figma-generate-library`도 로드.

<a id="figma-use---트리거-조건"></a>
### 🎯 트리거 조건
- **언제 호출되는가**: 쓰기 액션 또는 JS 실행이 필요한 고유 읽기 액션 — 노드 생성/편집/삭제, 변수/토큰 설정, 컴포넌트·배리언트 빌드, 오토레이아웃/fill 수정, 변수 바인딩, 파일 구조 인스펙트.
- **언제 쓰지 않는가**: FigJam 전용 작업(→ `figma-use-figjam` 추가), Slides 전용 작업(→ `figma-use-slides` 추가). 단, 둘 다 이 스킬을 기반으로 함.

<a id="figma-use---사용-예시--명령어"></a>
### 💻 사용 예시 / 명령어
```js
// 페이지 전환(동기 setter는 throw — 반드시 async)
const targetPage = figma.root.children.find((p) => p.name === "My Page");
await figma.setCurrentPageAsync(targetPage);

// 오토레이아웃 컨테이너(권장 기본 컨테이너)
const frame = figma.createAutoLayout('VERTICAL', { name: 'Column', itemSpacing: 8 });

// CSS류 셀렉터 + 배치 속성
figma.currentPage.query('FRAME[name^=Card] TEXT').set({
  fills: [{ type: 'SOLID', color: { r: 0.2, g: 0.2, b: 0.8 } }]
});

// 모든 created/mutated 노드 ID 반환(필수)
return { createdNodeIds: [...], mutatedNodeIds: [...] };
```

<a id="figma-use---제공-도구--주요-파라미터"></a>
### 🛠️ 제공 도구 / 주요 파라미터
- **사용 MCP 도구**: `use_figma`, `get_screenshot`, `get_metadata`, `create_new_file` 등(deferred일 경우 단일 `ToolSearch query="select:..."`로 일괄 로드 권장).
- **Critical Rules(요약)**: `return`으로 출력(IIFE/`closePlugin` 금지), top-level `await`+`return`, `figma.notify()`/`console.log()` 출력 금지, `getPluginData`/`setPluginData` 미지원(→ shared 버전), 색상 0~1, fills/strokes 읽기전용(복제 후 재할당), 텍스트는 폰트 로드 후 mutate, 페이지는 `setCurrentPageAsync`(동기 setter throw), `setBoundVariableForPaint`는 새 paint 반환, `layoutSizingHorizontal/Vertical`의 HUG/FILL은 구조 제약(appendChild 후 설정), 새 top-level 노드는 (0,0) 회피, 모든 created/mutated ID 반환, 모든 Promise `await`.
- **에디터 모드**: design(`figma.com/design/`) 기본. FigJam(`/board/`)·Slides(`/slides/`)는 노드 타입이 다름. `figma.createPage()`는 Design 전용.
- **효율 API**: `node.query(selector)`, `node.set(props)`, `figma.createAutoLayout()`, `node.placeholder`(진행 중 셰이머), `await node.screenshot()`.
- **워크플로우**: 인스펙트 우선 → 스켈레톤(placeholder) → 섹션 증분 채우기 → 매 호출 ID 반환 → 단계별 검증. 호출당 최대 10 논리 연산. 에러 시 STOP(원자적 — 부분 변경 없음), 메시지 읽고 수정 후 재시도.
- 참조: gotchas/common-patterns/plugin-api-patterns/api-reference/validation-and-recovery/component·variable·text-style·effect-style-patterns, plugin-api-standalone(.index.md/.d.ts — grep으로 부분 로드), working-with-design-systems/wwds.md.

<a id="figma-use---출처--설치-상태"></a>
### 📦 출처 / 설치 상태
- 플러그인: figma@claude-plugins-official
- 활성화: ON (`disable-model-invocation: false`)
- 관련 MCP: Figma MCP 연동(`use_figma` 등). 모든 Figma 쓰기/JS 실행 작업의 기반 스킬.
- 캐시 경로: `~/.claude/plugins/cache/claude-plugins-official/figma/2.2.12/skills/figma-use/SKILL.md`
