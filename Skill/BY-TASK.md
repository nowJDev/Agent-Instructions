<!-- 작업 분야에서 기존 스킬의 선택 조건과 상세 안내를 찾도록 연결한다. -->
# 분야별 스킬 선택 안내.

엑셀·PPT 등 **하려는 작업에서 출발해 도구를 고르는 목차**다. 대표 항목과 선택 조건을 안내하며, 전체 항목은 [전체 카탈로그](CATALOG.md), 출처·설치는 [스킬 인덱스](README.md), 자체 제작 패키지는 [원본 목록](../Owned-Skills/README.md)에서 확인한다.

이 문서의 등재는 설치·현재 노출·인증·실행 성공을 보장하지 않는다. 사용자 지정 도구와 현재 클라이언트에서 제공하는 기능을 먼저 확인하고, 상세 안내의 호출 정책·실행 조건을 따른다. 문서 정리가 자동 스킬 선택 정책을 변경하지는 않는다.

| 분야 | 대표 작업 |
|---|---|
| [엑셀·스프레드시트](#task-excel). | 표·수식·XLSX 작성과 편집. |
| [PPT·발표자료](#task-ppt). | 슬라이드 제작·편집·디자인. |
| [Word·한글·PDF·보고서](#task-documents). | 문서 작성·편집·추출·업무보고. |
| [이미지·시각 디자인](#task-visual-design). | 포스터·테마·GIF·생성형 시각 작품. |
| [웹·앱 UI·Figma](#task-web-ui). | 화면·디자인 시스템·프런트엔드. |
| [검색·자료 수집·리서치](#task-research). | 검색·크롤링·교차 검증·논문 조사. |
| [개발 설계·구현](#task-development). | 요구사항·계획·기능 개발·TDD. |
| [디버깅·테스트·리뷰](#task-debug-review). | 오류·성능·접근성·보안·변경 검토. |
| [AI 모델·데이터셋·학습](#task-ai-training). | 모델 선택·로컬 실행·학습·평가·데모. |
| [에이전트·스킬·MCP·Unity 연동](#task-agent-integration). | 스킬·플러그인·서버 제작과 연결. |
| [환경 설정·세션·반복 작업](#task-environment). | 지침·권한·인수인계·반복·예약. |
| [배포·인프라](#task-deployment). | 배포·DB·호스팅 운영. |

<a id="task-excel"></a>
## 엑셀·스프레드시트.

파일 작성·편집과 내용 추출을 구분해서 선택한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 표·수식·서식이 있는 XLSX 작성·편집. | [anthropic-xlsx](anthropic-skills/README.md#anthropic-xlsx). | `$anthropic-xlsx` 명시 호출. 재계산 도구와 최종 셀 값을 확인한다. |
| CLI로 XLSX 읽기·생성·편집. | [officecli](office-design-tools/README.md#officecli). | `$officecli` 명시 호출. 실행 파일과 Excel 전문 가이드를 확인한다. |
| XLSX 등 로컬 파일의 내용을 Markdown으로 추출. | [firecrawl-parse](firecrawl/README.md#firecrawl-parse). | 내용 추출용 보조 도구다. 수식·서식 편집이나 원본 보존 변환의 대체로 취급하지 않는다. |

<a id="task-ppt"></a>
## PPT·발표자료.

최종 편집 대상과 제작 방식을 기준으로 고른다. 아래 순서는 품질 순위가 아니다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| PPTX 생성·편집. | [anthropic-pptx](anthropic-skills/README.md#anthropic-pptx). | `$anthropic-pptx` 명시 호출. 보조 도구와 슬라이드 렌더링을 확인한다. |
| SVG 기반의 편집 가능한 PPTX 제작. | [ppt-master](office-design-tools/README.md#ppt-master). | `$ppt-master` 명시 호출. SVG 품질 검사 후 내보내기·재열기를 확인한다. |
| HTML 기반 디자인과 PPTX 제작. | [huashu-design](office-design-tools/README.md#huashu-design). | `$huashu-design` 명시 호출. 해당 제작 경로의 실제 가용 기능을 확인한다. |
| CLI로 PPTX 읽기·생성·편집. | [officecli](office-design-tools/README.md#officecli). | `$officecli` 명시 호출. PPTX 전문 가이드와 렌더 조건을 확인한다. |
| Figma Slides 편집. | [figma-use-slides](figma/README.md#figma-use-slides), [figma-use](figma/README.md#figma-use). | Figma Slides가 편집 대상일 때 선택한다. 기반 스킬과 도구·인증이 필요하다. |
| 슬라이드의 시각 테마 적용. | [anthropic-theme-factory](anthropic-skills/README.md#anthropic-theme-factory). | 제작 도구와 함께 쓰는 보조 스킬이다. 기존 브랜드와 가독성을 확인한다. |

<a id="task-documents"></a>
## Word·한글·PDF·보고서.

파일 형식과 문서 내용 작성의 목적을 함께 확인한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| Word 문서 생성·편집. | [anthropic-docx](anthropic-skills/README.md#anthropic-docx). | `$anthropic-docx` 명시 호출. 변환 도구와 최종 레이아웃을 확인한다. |
| CLI로 DOCX 읽기·생성·편집. | [officecli](office-design-tools/README.md#officecli). | `$officecli` 명시 호출. Word 전문 가이드를 확인한다. |
| HWP·HWPX와 한국 공문서 작업. | [kordoc](kordoc/README.md#kordoc). | 원본 형식과 지원하는 읽기·작성·검증 경로를 확인한다. |
| PDF 읽기·작성·변환. | [anthropic-pdf](anthropic-skills/README.md#anthropic-pdf). | `$anthropic-pdf` 명시 호출. 텍스트 추출과 화면 렌더링을 구분한다. |
| 제안서·기술 문서의 내용 공동 작성. | [anthropic-doc-coauthoring](anthropic-skills/README.md#anthropic-doc-coauthoring). | 초안·구조·독자 검토용이다. 파일 형식별 제작 도구와 조합한다. |
| 로컬 자료에 근거한 한국어 일일 업무보고. | [daily-work-report · 자체 제작](../Owned-Skills/daily-work-report/SKILL.md). | 지정 자료·업무명·형식을 기준으로 작성한다. |
| 사내 공지·상태 보고 등 내부 커뮤니케이션. | [anthropic-internal-comms](anthropic-skills/README.md#anthropic-internal-comms). | 독자·조직 문체·공개 범위를 확인한다. 작성과 외부 전송은 별개다. |

<a id="task-visual-design"></a>
## 이미지·시각 디자인.

정적인 시각 작품, 움직이는 이미지, 여러 산출물의 공통 테마를 구분한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 포스터 등 PNG·PDF 시각 작품. | [anthropic-canvas-design](anthropic-skills/README.md#anthropic-canvas-design). | 폰트·렌더링 환경과 최종 표시를 확인한다. |
| 코드와 매개변수로 생성형 시각 작품 제작. | [anthropic-algorithmic-art](anthropic-skills/README.md#anthropic-algorithmic-art). | 조절 가능한 패턴·시각 효과를 만들 때 사용한다. |
| Slack용 애니메이션 GIF 제작. | [anthropic-slack-gif-creator](anthropic-skills/README.md#anthropic-slack-gif-creator). | 크기·프레임·용량·재생을 확인한다. 게시 권한을 포함하지 않는다. |
| 문서·슬라이드·웹에 공통 테마 적용. | [anthropic-theme-factory](anthropic-skills/README.md#anthropic-theme-factory). | 기존 브랜드·가독성을 확인하는 보조 스킬이다. |
| Anthropic 브랜드 스타일 적용. | [anthropic-brand-guidelines](anthropic-skills/README.md#anthropic-brand-guidelines). | `$anthropic-brand-guidelines` 명시 호출. 해당 브랜드를 요청한 경우에 사용한다. |

<a id="task-web-ui"></a>
## 웹·앱 UI·Figma.

실행할 UI와 Figma 편집 산출물 중 무엇이 필요한지 먼저 확인한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 프런트엔드 화면의 시각 방향과 UI 구현. | [anthropic-frontend-design](anthropic-skills/README.md#anthropic-frontend-design). | 기존 `frontend-design` 배포 설명과 구분한다. 실제 브라우저로 검증한다. |
| Figma 화면·레이아웃 제작. | [figma-generate-design](figma/README.md#figma-generate-design). | 현재 Figma 파일·디자인 시스템과 필요한 도구를 확인한다. |
| Figma 디자인 시스템 구축. | [figma-generate-library](figma/README.md#figma-generate-library). | 변수·토큰·컴포넌트를 구축하거나 갱신할 때 사용한다. |
| Figma 기반 편집과 새 파일 생성. | [figma-use](figma/README.md#figma-use), [figma-create-new-file](figma/README.md#figma-create-new-file). | 편집·생성 도구의 필수 선행 가이드를 따른다. |
| 한 파일로 조절 가능한 HTML 탐색기 제작. | [playground](playground/README.md#playground). | 컨트롤과 라이브 미리보기가 필요한 작업에 사용한다. |
| HTML 기반 웹·앱 디자인. | [huashu-design](office-design-tools/README.md#huashu-design). | `$huashu-design` 명시 호출. 실제 제작 기능·브라우저 조건을 확인한다. |
| 여러 UI 요소가 있는 웹 산출물 제작. | [anthropic-web-artifacts-builder](anthropic-skills/README.md#anthropic-web-artifacts-builder). | `$anthropic-web-artifacts-builder` 명시 호출. 번들 실행·게시 조건을 따로 확인한다. |

<a id="task-research"></a>
## 검색·자료 수집·리서치.

소스 발견, 알려진 페이지 읽기, 여러 자료의 교차 검증을 구분한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 검색어로 웹 소스 발견. | [firecrawl-search](firecrawl/README.md#firecrawl-search). | 관련 페이지를 찾는 단계에 사용한다. |
| 알려진 웹페이지 읽기. | [firecrawl-scrape](firecrawl/README.md#firecrawl-scrape). | URL의 본문이나 구조화 결과가 필요할 때 사용한다. |
| URL 탐색·여러 페이지 수집. | [firecrawl-map](firecrawl/README.md#firecrawl-map), [firecrawl-crawl](firecrawl/README.md#firecrawl-crawl). | 주소 발견과 본문 일괄 수집을 구분한다. |
| 상호작용이 필요한 사이트 조사. | [firecrawl-interact](firecrawl/README.md#firecrawl-interact), [firecrawl-agent](firecrawl/README.md#firecrawl-agent). | 폼·페이지 이동 등 실제 상호작용이 필요한 경우에 선택한다. |
| 여러 자료를 비교·교차 검증한 조사. | [deep-research · 개인 분류 설명](_personal/README.md#deep-research). | 출처·불확실성과 근거가 있는 종합 답변이 필요할 때 사용한다. |
| Hugging Face 논문 조회. | [huggingface-papers](huggingface-skills/README.md#huggingface-papers). | 논문·저자·연결 모델과 데이터셋을 조사한다. |

<a id="task-development"></a>
## 개발 설계·구현.

프로젝트의 기존 운영 규칙 아래에서 작업 단계에 맞는 스킬을 사용한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 상태 변경 작업의 전체 흐름 조율. | [design-driven-delivery · 자체 제작](../Owned-Skills/design-driven-delivery/SKILL.md). | 설계·계획·구현·검증·통합의 상위 절차다. |
| 목적·범위·접근법을 설계로 정리. | [brainstorming](superpowers/README.md#brainstorming). | 새 작업의 의도와 승인 설계를 확인한다. |
| 승인 설계를 실행 가능한 태스크로 분해. | [writing-plans](superpowers/README.md#writing-plans). | 파일·테스트·검증·인터페이스를 계획한다. |
| 기존 코드베이스의 기능 개발. | [feature-dev · 자체 제작](../Owned-Skills/feature-dev/SKILL.md). | 호출자·요구사항·기존 구조를 조사하고 구현·검증한다. |
| 실패 테스트부터 기능·수정 구현. | [test-driven-development](superpowers/README.md#test-driven-development). | RED·GREEN으로 동작을 확인한다. |
| 승인 계획의 직접 실행·독립 태스크 위임. | [executing-plans](superpowers/README.md#executing-plans), [subagent-driven-development](superpowers/README.md#subagent-driven-development). | 현재 환경과 승인된 실행 방식에 따라 선택한다. |
| 작업 공간 격리와 브랜치 통합. | [using-git-worktrees](superpowers/README.md#using-git-worktrees), [finishing-a-development-branch](superpowers/README.md#finishing-a-development-branch). | 기존 격리·사용자 변경과 승인된 병합 범위를 확인한다. |

<a id="task-debug-review"></a>
## 디버깅·테스트·리뷰.

원인 조사, 실제 동작 검증, 변경 검토를 목적에 맞게 선택한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 버그·테스트 실패의 근본 원인 조사. | [systematic-debugging](superpowers/README.md#systematic-debugging). | 수정안을 내기 전에 재현·증거·패턴을 확인한다. |
| 앱 실행과 사용자 흐름 검증. | [run · 자체 제작](../Owned-Skills/run/SKILL.md), [verify · 자체 제작](../Owned-Skills/verify/SKILL.md). | 실행 준비와 실행 후 동작 확인을 구분한다. |
| 웹 디버깅·접근성·LCP·메모리 조사. | [chrome-devtools](chrome-devtools-mcp/README.md#chrome-devtools), [a11y-debugging](chrome-devtools-mcp/README.md#a11y-debugging), [debug-optimize-lcp](chrome-devtools-mcp/README.md#debug-optimize-lcp), [memory-leak-debugging](chrome-devtools-mcp/README.md#memory-leak-debugging). | 사용자 지정 도구와 브라우저 연결 조건을 확인한다. |
| 변경·PR 검토와 보안 조사. | [code-review · 자체 제작](../Owned-Skills/code-review/SKILL.md), [review-pr · 자체 제작](../Owned-Skills/review-pr/SKILL.md), [security-review · 자체 제작](../Owned-Skills/security-review/SKILL.md). | 검토 대상과 권한을 확인한다. 내장·플러그인 동명 항목과 구분한다. |
| 기존 동작을 유지하며 코드 단순화. | [simplify · 자체 제작](../Owned-Skills/simplify/SKILL.md). | 요청한 정리 범위와 동작·오류·부작용을 보존한다. |
| 완료 주장 전에 실행 증거 확인. | [verification-before-completion](superpowers/README.md#verification-before-completion). | 실제 검사 결과를 확인하며 실행 검증을 대체하지 않는다. |

<a id="task-ai-training"></a>
## AI 모델·데이터셋·학습.

모델 조사, 로컬 실행, 학습·평가·데모 배포를 구분한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 작업에 맞는 모델 선택·로컬 실행. | [huggingface-best](huggingface-skills/README.md#huggingface-best), [huggingface-local-models](huggingface-skills/README.md#huggingface-local-models). | 평가 근거와 실제 하드웨어·양자화 조건을 확인한다. |
| Hub 파일·데이터셋 조회와 관리. | [hf-cli](huggingface-skills/README.md#hf-cli), [huggingface-datasets](huggingface-skills/README.md#huggingface-datasets). | 다운로드·조회와 업로드 권한을 구분한다. |
| 언어 모델 학습·후학습. | [huggingface-llm-trainer](huggingface-skills/README.md#huggingface-llm-trainer), [trl-training](huggingface-skills/README.md#trl-training). | 데이터·학습 방식·실행 자원과 비용 범위를 확인한다. |
| 비전·임베딩 모델 학습. | [huggingface-vision-trainer](huggingface-skills/README.md#huggingface-vision-trainer), [train-sentence-transformers](huggingface-skills/README.md#train-sentence-transformers). | 태스크·데이터·평가 기준에 맞는 학습 경로를 선택한다. |
| 평가·학습 추적. | [huggingface-community-evals](huggingface-skills/README.md#huggingface-community-evals), [huggingface-trackio](huggingface-skills/README.md#huggingface-trackio). | 실제 하드웨어·평가 백엔드·로깅 조건을 확인한다. |
| ML 데모·Spaces·브라우저 추론. | [huggingface-gradio](huggingface-skills/README.md#huggingface-gradio), [huggingface-spaces](huggingface-skills/README.md#huggingface-spaces), [huggingface-zerogpu](huggingface-skills/README.md#huggingface-zerogpu), [transformers-js](huggingface-skills/README.md#transformers-js). | 로컬 UI·호스팅·GPU·브라우저 실행의 차이를 확인한다. |

<a id="task-agent-integration"></a>
## 에이전트·스킬·MCP·Unity 연동.

스킬 작성, 서버 구현, 클라이언트 연결은 서로 다른 작업 범위다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 스킬 설계·작성·검증. | [writing-skills](superpowers/README.md#writing-skills), [anthropic-skill-creator](anthropic-skills/README.md#anthropic-skill-creator). | 후자는 `$anthropic-skill-creator` 명시 호출. OpenAI 내장·다른 배포본과 구분한다. |
| Claude Code 에이전트·플러그인 제작. | [agent-development](plugin-dev/README.md#agent-development), [create-plugin](plugin-dev/README.md#create-plugin), [plugin-structure](plugin-dev/README.md#plugin-structure). | 해당 호스트의 플러그인·에이전트 형식에 맞춘다. |
| MCP 서버 구현과 플러그인 연동. | [anthropic-mcp-builder](anthropic-skills/README.md#anthropic-mcp-builder), [mcp-integration](plugin-dev/README.md#mcp-integration). | 서버 구현과 등록·인증·권한 변경을 구분한다. |
| Claude API·Agent SDK 작업. | [claude-api · 자체 제작](../Owned-Skills/claude-api/SKILL.md), [new-sdk-app · 자체 제작](../Owned-Skills/new-sdk-app/SKILL.md). | 제공자와 요청 범위를 확인한다. |
| Coplay·Funplay Unity MCP 설치·연결. | [coplay-funplay-unity-mcp-setup · 자체 제작](../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md). | 전역 도구와 프로젝트별 패키지·Editor 연결을 구분한다. |

<a id="task-environment"></a>
## 환경 설정·세션·반복 작업.

동명 내장 명령과 자체 제작 지침, 현재 세션 반복과 클라우드 예약을 구분한다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 프로젝트 지침 초기화와 환경 설정. | [init · 자체 제작](../Owned-Skills/init/SKILL.md), [update-config · 자체 제작](../Owned-Skills/update-config/SKILL.md). | 기존 개인 지침·설정을 보존한다. |
| 읽기 전용 승인 반복 줄이기·단축키 설정. | [fewer-permission-prompts · 자체 제작](../Owned-Skills/fewer-permission-prompts/SKILL.md), [keybindings-help · 자체 제작](../Owned-Skills/keybindings-help/SKILL.md). | 실제 클라이언트의 권한·단축키 지원을 확인한다. |
| 다음 세션에 작업 인수인계. | [handover · 개인 분류 설명](_personal/README.md#handover). | 프로젝트·현재 상태·미완료·재개 근거를 남긴다. |
| 세션 목록 정리. | [delete-session · 자체 제작](../Owned-Skills/delete-session/SKILL.md). | 실제 대상과 보관·제거 범위를 확인한다. |
| 현재 세션 반복·Ralph 작업. | [loop · 자체 제작](../Owned-Skills/loop/SKILL.md), [ralph-loop · 자체 제작](../Owned-Skills/ralph-loop/SKILL.md), [cancel-ralph · 자체 제작](../Owned-Skills/cancel-ralph/SKILL.md). | 승인된 반복 범위·완료·취소 조건을 확인한다. |
| 클라우드 에이전트 예약. | [schedule · 내장 분류 설명](_builtin/README.md#schedule). | 현재 호스트의 실제 예약 기능과 권한을 확인한다. 로컬 반복과 구분한다. |

<a id="task-deployment"></a>
## 배포·인프라.

아래 항목은 **작성 당시 비활성** 플러그인의 설명이다. 현재 설치·활성·인증·권한을 확인한 뒤 사용하며 목차 추가로 활성화되지 않는다.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| Vercel 배포·상태 확인. | [deploy](_disabled/vercel/README.md#deploy), [status](_disabled/vercel/README.md#status). | 조회와 배포를 구분하고 배포 대상·승인 범위를 확인한다. |
| Railway 앱·DB·호스팅 운영. | [use-railway](_disabled/railway/README.md#use-railway). | 실제 CLI·계정·프로젝트와 변경 권한을 확인한다. |
| Neon 데이터베이스 운영·전송량 조사. | [neon-postgres](_disabled/neon/README.md#neon-postgres), [neon-postgres-egress-optimizer](_disabled/neon/README.md#neon-postgres-egress-optimizer). | 원문·연결·인증 조건을 상세 안내에서 확인한다. |

## 선택과 유지보수.

- 같은 도구가 여러 분야에 등장해도 상세 설명은 같은 주소를 사용한다. 설치 명령·버전·실행 의존성을 이 표에 복제하지 않는다.
- 동명 항목은 자체 제작·내장·플러그인과 배포 이름을 구분한다. 명시 호출 정책은 해당 상세 문서에서 관리하고 이 안내도 함께 갱신한다.
- 새 항목은 기존 카탈로그나 자체 제작 원본에 먼저 설명한 뒤 필요한 분야에 연결한다. 모든 항목을 이 페이지에 반복해 싣지 않는다.
- 분야 제목을 다듬을 때도 `task-*` 앵커는 보존한다. 도구의 우열·실제 가용성은 별도 검증 없이 단정하지 않는다.
