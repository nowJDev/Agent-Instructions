<!-- 전체 등록 항목을 분야별로 연결하고 빠른 선택과 호출 상태를 구분한다. -->
# 분야별 전체 스킬 안내.

엑셀·PPT 등 **하려는 작업에서 전체 등록 항목을 찾는 목차**다. 각 분야의 빠른 선택 뒤에 전체 목록을 둔다. [전체 카탈로그](CATALOG.md)의 설명·원본 주소 294개 모두가 최소 한 분야에 있으며, 같은 도구는 여러 분야에 나타날 수 있다. 분야별 행 수를 더해 고유 스킬 수로 세지 않는다.

기존 설명·과거 배포·자체 제작 원본과 조사 당시의 직접 설치·플러그인 제공을 구분한다. 세션 노출은 실제 실행·인증 성공과 다르며, 명시 정책·직접 비노출·상위 라우터 조건을 각 행과 상세 설명에서 확인한다. 문서 추가는 설치·호출 정책을 변경하지 않는다. [출처·집계 안내](README.md)와 [조사 증거](../references/skill-inventory-2026-11-12.json)는 날짜가 있는 기준이며 이후 설치 변경은 다시 대조해야 한다.

| 분야 | 등록 주소 수 |
|---|---|
| [엑셀·스프레드시트](#task-excel). | 32개. |
| [PPT·발표자료](#task-ppt). | 13개. |
| [Word·한글·PDF·보고서](#task-documents). | 20개. |
| [이미지·시각 디자인·캐릭터](#task-visual-design). | 11개. |
| [웹·앱 UI·Figma](#task-web-ui). | 23개. |
| [데이터 분석·지표·시각화](#task-data-analysis). | 22개. |
| [검색·자료 수집·리서치](#task-research). | 20개. |
| [개발 설계·구현](#task-development). | 25개. |
| [디버깅·테스트·리뷰](#task-debug-review). | 38개. |
| [AI 모델·데이터셋·학습](#task-ai-training). | 18개. |
| [에이전트·스킬·MCP·Unity 연동](#task-agent-integration). | 35개. |
| [환경 설정·세션·반복 작업](#task-environment). | 42개. |
| [지식 관리·협업·Notion·Pages](#task-knowledge-management). | 19개. |
| [금융·투자·재무 모델](#task-finance). | 46개. |
| [음악·팟캐스트·Spotify](#task-music). | 5개. |
| [배포·인프라](#task-deployment). | 16개. |

<a id="task-excel"></a>
## 엑셀·스프레드시트.

파일 작성·편집, live Excel, 분석·변환을 구분한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| XLSX·CSV·TSV 등 파일 작성·편집·차트. | [spreadsheets:Spreadsheets](codex-plugins/README.md#spreadsheets-spreadsheets). | 파일 산출 작업에 사용하며 live Excel 제어와 구분한다. |
| 열려 있는 Excel 직접 제어. | [spreadsheets:excel-live-control](codex-plugins/README.md#spreadsheets-excel-live-control). | Excel 앱 태그 또는 연결된 live 세션이 필요하다. |
| 표·수식·서식이 있는 XLSX 작성·편집. | [anthropic-xlsx](anthropic-skills/README.md#anthropic-xlsx). | `$anthropic-xlsx` 명시 호출. 재계산 도구와 최종 셀 값을 확인한다. |
| CLI로 XLSX 읽기·생성·편집. | [officecli](office-design-tools/README.md#officecli). | `$officecli` 명시 호출. 실행 파일과 Excel 전문 가이드를 확인한다. |
| XLSX 등 로컬 파일의 내용을 Markdown으로 추출. | [firecrawl-parse](firecrawl/README.md#firecrawl-parse). | 내용 추출용 보조 도구다. 수식·서식 편집이나 원본 보존 변환의 대체로 취급하지 않는다. |

### 이 분야의 전체 목록.

분석·금융 전문 가이드는 일반 Excel 편집 도구와 구분한다. 파일 입력이 스프레드시트여도 결과가 XLSX라는 뜻은 아니다.

#### 스프레드시트 파일 작성·편집.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [spreadsheets:Spreadsheets](codex-plugins/README.md#spreadsheets-spreadsheets). | XLSX·XLS·CSV·TSV 파일과 Google Sheets 대상 스프레드시트를 작성·편집·분석한다. | OpenAI Spreadsheets · 조사 세션 노출. 파일 또는 Google Sheets 대상 작업에 사용한다. 열려 있는 Excel 제어는 live 스킬로 연결한다. |
| [anthropic-xlsx](anthropic-skills/README.md#anthropic-xlsx). | 스프레드시트 작성·편집을 안내하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [officecli](office-design-tools/README.md#officecli). | Office 없는 DOCX·XLSX·PPTX CLI와 명시 호출 전용 연동 스킬. | office-design-tools · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |

#### 열려 있는 Excel 제어.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [spreadsheets:excel-live-control](codex-plugins/README.md#spreadsheets-excel-live-control). | 연결 세션에서 열려 있는 Microsoft Excel 통합문서를 제어한다. | OpenAI Spreadsheets · 조사 세션 노출. Excel 앱 태그 또는 이미 연결된 live Excel 작업이 전제다. 독립 파일 편집과 구분한다. |

#### 데이터 분석·품질·시각화.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [data-analytics:analyze-data-quality](codex-plugins/README.md#data-analytics-analyze-data-quality). | 구조화 데이터의 누락·중복·조인·최신성 등 품질 위험을 조사한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:design-kpis](codex-plugins/README.md#data-analytics-design-kpis). | KPI 정의·목표·가드레일·측정 계획을 설계한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:index](codex-plugins/README.md#data-analytics-index). | 데이터·지표·분석 요청을 알맞은 Data 작업 흐름으로 연결한다. | Data Analytics · 조사 세션 노출. 데이터·지표·분석 요청을 분류한다. 단순 글쓰기·일반 설명에 확대하지 않는다. |
| [data-analytics:kpi-reporting](codex-plugins/README.md#data-analytics-kpi-reporting). | KPI 성과·목표 대비 결과와 정기 운영 보고를 작성한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:market-sizing](codex-plugins/README.md#data-analytics-market-sizing). | 가정과 불확실성을 밝혀 시장·세그먼트·기회 규모를 추정한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:metric-diagnostics](codex-plugins/README.md#data-analytics-metric-diagnostics). | 지표 변화·이상·차이의 원인과 기여 요인을 진단한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:product-business-analysis](codex-plugins/README.md#data-analytics-product-business-analysis). | 제품·사업 의사결정에 필요한 데이터 분석을 수행한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:validate-data](codex-plugins/README.md#data-analytics-validate-data). | 분석 방법·계산·시각화·결론과 보고서 완성도를 검증한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:visualize-data](codex-plugins/README.md#data-analytics-visualize-data). | 분석 산출물에 들어갈 정량 차트·그림을 제작·검증한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |

#### 내용 추출·변환 보조.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [firecrawl-parse](firecrawl/README.md#firecrawl-parse). | 로컬 파일(PDF/DOCX/XLSX/HTML 등)을 클린 마크다운으로 변환해 디스크에 저장하는 스킬. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [kordoc](kordoc/README.md#kordoc). | HWP·HWPX·HWPML과 한국 공문서를 읽고, 생성·채움·편집·비교·검증·미리보기하는 스킬. | kordoc · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |

#### 금융 모델 관련 라우터·전문 가이드.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [investment-banking:comps-valuation](codex-plugins/README.md#investment-banking-comps-valuation). | 비교 기업·거래와 배수에 근거한 가치평가를 수행한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:dcf-model-builder](codex-plugins/README.md#investment-banking-dcf-model-builder). | 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:financials-normalizer](codex-plugins/README.md#investment-banking-financials-normalizer). | 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:investment-banking](codex-plugins/README.md#investment-banking-investment-banking). | 거래·자금 조달·실사·가치평가 등 투자은행 작업을 전문 스킬로 연결한다. | Investment Banking · 조사 세션 노출. 투자은행 거래·발행·실사·자문 맥락 또는 명시 호출이 필요하며 전문 원문을 읽고 연결한다. |
| [investment-banking:lbo-model-build](codex-plugins/README.md#investment-banking-lbo-model-build). | 인수 자금 조달·차입·수익률·회수 민감도를 포함한 LBO 모델을 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:merger-model-builder](codex-plugins/README.md#investment-banking-merger-model-builder). | 합병의 주당이익·구매회계·시너지·교환비율과 통합 재무를 모델링한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:model-audit-tieout](codex-plugins/README.md#investment-banking-model-audit-tieout). | 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:scenario-sensitivity-generator](codex-plugins/README.md#investment-banking-scenario-sensitivity-generator). | 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:three-statement-model-builder](codex-plugins/README.md#investment-banking-three-statement-model-builder). | 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:comps-valuation](codex-plugins/README.md#public-equity-investing-comps-valuation). | 비교 기업·거래와 배수에 근거한 가치평가를 수행한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:dcf-model-builder](codex-plugins/README.md#public-equity-investing-dcf-model-builder). | 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:equity-model-update](codex-plugins/README.md#public-equity-investing-equity-model-update). | 기존 주식 투자 모델의 실적·가이던스·가정·수식을 갱신한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:financials-normalizer](codex-plugins/README.md#public-equity-investing-financials-normalizer). | 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:model-audit-tieout](codex-plugins/README.md#public-equity-investing-model-audit-tieout). | 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:public-equity-investing](codex-plugins/README.md#public-equity-investing-public-equity-investing). | 상장주식의 기업·실적·가치평가·포트폴리오 작업을 전문 스킬로 연결한다. | Public Equity Investing · 조사 세션 노출. 상장주식 투자·기업·실적·가치평가·모델 맥락 또는 명시 호출이 필요하며 전문 원문을 읽고 연결한다. |
| [public-equity-investing:scenario-sensitivity-generator](codex-plugins/README.md#public-equity-investing-scenario-sensitivity-generator). | 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:three-statement-model-builder](codex-plugins/README.md#public-equity-investing-three-statement-model-builder). | 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |

<a id="task-ppt"></a>
## PPT·발표자료.

PPTX와 Figma Slides 등 편집 대상과 제작 방식을 확인한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 프레젠테이션 파일 작성·편집. | [presentations:Presentations](codex-plugins/README.md#presentations-presentations). | 요청한 파일·서비스 대상에 맞는 제공 도구를 확인한다. |
| PPTX 생성·편집. | [anthropic-pptx](anthropic-skills/README.md#anthropic-pptx). | `$anthropic-pptx` 명시 호출. 보조 도구와 슬라이드 렌더링을 확인한다. |
| SVG 기반의 편집 가능한 PPTX 제작. | [ppt-master](office-design-tools/README.md#ppt-master). | `$ppt-master` 명시 호출. SVG 품질 검사 후 내보내기·재열기를 확인한다. |
| HTML 기반 디자인과 PPTX 제작. | [huashu-design](office-design-tools/README.md#huashu-design). | `$huashu-design` 명시 호출. 해당 제작 경로의 실제 가용 기능을 확인한다. |
| CLI로 PPTX 읽기·생성·편집. | [officecli](office-design-tools/README.md#officecli). | `$officecli` 명시 호출. PPTX 전문 가이드와 렌더 조건을 확인한다. |
| Figma Slides 편집. | [figma-use-slides](figma/README.md#figma-use-slides), [figma-use](figma/README.md#figma-use). | Figma Slides가 편집 대상일 때 선택한다. 기반 스킬과 도구·인증이 필요하다. |
| 슬라이드의 시각 테마 적용. | [anthropic-theme-factory](anthropic-skills/README.md#anthropic-theme-factory). | 제작 도구와 함께 쓰는 보조 스킬이다. 기존 브랜드와 가독성을 확인한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [data-analytics:convert-to-slides](codex-plugins/README.md#data-analytics-convert-to-slides). | 기존 Data 산출물을 PowerPoint·Google Slides 발표자료로 변환한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [investment-banking:ib-deck-qc](codex-plugins/README.md#investment-banking-ib-deck-qc). | 거래 자문 발표자료의 출처·모델·일관성과 배포 준비 상태를 점검한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:pitch-deck-builder](codex-plugins/README.md#investment-banking-pitch-deck-builder). | 거래·이사회·위원회용 피치덱의 이야기·페이지 계획·근거를 구성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [presentations:Presentations](codex-plugins/README.md#presentations-presentations). | 발표자료를 읽고 작성·편집하며 PPTX·Google Slides 등 출력 경로를 안내한다. | OpenAI Presentations · 조사 세션 노출. 기존 덱·템플릿·목표 형식을 확인하고 산출물 경로와 렌더를 검증한다. |
| [public-equity-investing:deck-report-qc](codex-plugins/README.md#public-equity-investing-deck-report-qc). | 투자 발표자료·보고서의 출처·모델·글쓰기 일관성을 점검한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:long-short-pitch](codex-plugins/README.md#public-equity-investing-long-short-pitch). | 롱·숏·페어 투자 논지와 촉매·위험·진입·청산 조건을 구성한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [anthropic-pptx](anthropic-skills/README.md#anthropic-pptx). | PowerPoint 슬라이드 생성·편집을 안내하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [anthropic-theme-factory](anthropic-skills/README.md#anthropic-theme-factory). | 문서·슬라이드·웹 산출물에 일관된 시각 테마를 적용하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-use](figma/README.md#figma-use). | Figma Plugin API로 JavaScript를 실행해 노드를 생성/편집/조회하는 기반 스킬. 모든 `use_figma` 호출의 필수 선행 스킬. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-use-slides](figma/README.md#figma-use-slides). | Slides 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 Slides 특화 스킬. `figma-use`와 함께 사용. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huashu-design](office-design-tools/README.md#huashu-design). | HTML 기반 웹·앱·PPTX 디자인을 만드는 명시 호출 전용 스킬. | office-design-tools · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [officecli](office-design-tools/README.md#officecli). | Office 없는 DOCX·XLSX·PPTX CLI와 명시 호출 전용 연동 스킬. | office-design-tools · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [ppt-master](office-design-tools/README.md#ppt-master). | SVG에서 편집 가능한 PowerPoint를 만드는 명시 호출 전용 스킬. | office-design-tools · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |

<a id="task-documents"></a>
## Word·한글·PDF·보고서.

파일 형식과 문서 내용 작성 목적을 함께 확인한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| DOCX 문서 작성·편집·검토. | [documents:documents](codex-plugins/README.md#documents-documents). | 제공 문서 도구의 렌더·검증 절차를 따른다. |
| PDF 읽기·작성·검증. | [pdf:pdf](codex-plugins/README.md#pdf-pdf). | 제공 PDF 도구의 추출·렌더·검증 절차를 따른다. |
| Word 문서 생성·편집. | [anthropic-docx](anthropic-skills/README.md#anthropic-docx). | `$anthropic-docx` 명시 호출. 변환 도구와 최종 레이아웃을 확인한다. |
| CLI로 DOCX 읽기·생성·편집. | [officecli](office-design-tools/README.md#officecli). | `$officecli` 명시 호출. Word 전문 가이드를 확인한다. |
| HWP·HWPX와 한국 공문서 작업. | [kordoc](kordoc/README.md#kordoc). | 원본 형식과 지원하는 읽기·작성·검증 경로를 확인한다. |
| PDF 읽기·작성·변환. | [anthropic-pdf](anthropic-skills/README.md#anthropic-pdf). | `$anthropic-pdf` 명시 호출. 텍스트 추출과 화면 렌더링을 구분한다. |
| 제안서·기술 문서의 내용 공동 작성. | [anthropic-doc-coauthoring](anthropic-skills/README.md#anthropic-doc-coauthoring). | 초안·구조·독자 검토용이다. 파일 형식별 제작 도구와 조합한다. |
| 로컬 자료에 근거한 한국어 일일 업무보고. | [daily-work-report · 자체 제작](../Owned-Skills/daily-work-report/SKILL.md). | 지정 자료·업무명·형식을 기준으로 작성한다. |
| 사내 공지·상태 보고 등 내부 커뮤니케이션. | [anthropic-internal-comms](anthropic-skills/README.md#anthropic-internal-comms). | 독자·조직 문체·공개 범위를 확인한다. 작성과 외부 전송은 별개다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [data-analytics:build-report](codex-plugins/README.md#data-analytics-build-report). | 검토 가능한 근거를 갖춘 분석 보고서를 작성한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:convert-to-doc](codex-plugins/README.md#data-analytics-convert-to-doc). | 기존 Data 산출물을 DOCX·Google Docs 문서로 변환한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [data-analytics:report-to-pdf](codex-plugins/README.md#data-analytics-report-to-pdf). | 기존 Data 보고서·대시보드를 PDF로 변환한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [investment-banking:cim-builder](codex-plugins/README.md#investment-banking-cim-builder). | 거래 마케팅용 CIM·티저·경영진 발표 서사를 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:cim-teardown](codex-plugins/README.md#investment-banking-cim-teardown). | CIM·티저·실사 자료의 주장과 근거를 검토한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:meeting-prep](codex-plugins/README.md#investment-banking-meeting-prep). | 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:memo-builder](codex-plugins/README.md#investment-banking-memo-builder). | 분석 담당 스킬의 결과를 의사결정 메모로 종합한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [documents:documents](codex-plugins/README.md#documents-documents). | DOCX·Word·Google Docs 대상 문서를 작성·편집하고 렌더링으로 확인한다. | OpenAI Documents · 조사 세션 노출. 요청한 문서 형식과 기존 문서·템플릿을 확인하고 최종 렌더를 검증한다. |
| [pdf:pdf](codex-plugins/README.md#pdf-pdf). | PDF를 읽고 작성·렌더링·검증하며 양식 작업을 지원한다. | OpenAI PDF · 조사 세션 노출. PDF 내용·화면·양식 중 요청 범위를 확인하고 해당 결과를 검증한다. |
| [public-equity-investing:meeting-prep](codex-plugins/README.md#public-equity-investing-meeting-prep). | 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:memo-builder](codex-plugins/README.md#public-equity-investing-memo-builder). | 분석 담당 스킬의 결과를 의사결정 메모로 종합한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [anthropic-doc-coauthoring](anthropic-skills/README.md#anthropic-doc-coauthoring). | 초안·구조·독자 관점 검토를 거쳐 문서를 공동 작성하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-docx](anthropic-skills/README.md#anthropic-docx). | Word 문서 생성·편집을 안내하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [anthropic-internal-comms](anthropic-skills/README.md#anthropic-internal-comms). | 상태 보고·사내 공지 등 내부 커뮤니케이션 문서를 작성하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-pdf](anthropic-skills/README.md#anthropic-pdf). | PDF 읽기·작성·변환을 안내하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [anthropic-theme-factory](anthropic-skills/README.md#anthropic-theme-factory). | 문서·슬라이드·웹 산출물에 일관된 시각 테마를 적용하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-parse](firecrawl/README.md#firecrawl-parse). | 로컬 파일(PDF/DOCX/XLSX/HTML 등)을 클린 마크다운으로 변환해 디스크에 저장하는 스킬. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [kordoc](kordoc/README.md#kordoc). | HWP·HWPX·HWPML과 한국 공문서를 읽고, 생성·채움·편집·비교·검증·미리보기하는 스킬. | kordoc · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [officecli](office-design-tools/README.md#officecli). | Office 없는 DOCX·XLSX·PPTX CLI와 명시 호출 전용 연동 스킬. | office-design-tools · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [daily-work-report](../Owned-Skills/daily-work-report/SKILL.md). | 지정한 로컬 자료와 업무명·템플릿을 근거로 한국어 일일 업무보고를 작성한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |

<a id="task-visual-design"></a>
## 이미지·시각 디자인·캐릭터.

이미지·테마·GIF·애니메이션 캐릭터 작업을 찾는다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 포스터 등 PNG·PDF 시각 작품. | [anthropic-canvas-design](anthropic-skills/README.md#anthropic-canvas-design). | 폰트·렌더링 환경과 최종 표시를 확인한다. |
| 코드와 매개변수로 생성형 시각 작품 제작. | [anthropic-algorithmic-art](anthropic-skills/README.md#anthropic-algorithmic-art). | 조절 가능한 패턴·시각 효과를 만들 때 사용한다. |
| Slack용 애니메이션 GIF 제작. | [anthropic-slack-gif-creator](anthropic-skills/README.md#anthropic-slack-gif-creator). | 크기·프레임·용량·재생을 확인한다. 게시 권한을 포함하지 않는다. |
| 문서·슬라이드·웹에 공통 테마 적용. | [anthropic-theme-factory](anthropic-skills/README.md#anthropic-theme-factory). | 기존 브랜드·가독성을 확인하는 보조 스킬이다. |
| Anthropic 브랜드 스타일 적용. | [anthropic-brand-guidelines](anthropic-skills/README.md#anthropic-brand-guidelines). | `$anthropic-brand-guidelines` 명시 호출. 해당 브랜드를 요청한 경우에 사용한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [work-pets:create-pet](codex-plugins/README.md#work-pets-create-pet). | ChatGPT Work용 애니메이션 펫을 제작·검증·미리보기·업로드한다. | ChatGPT Work Pets · 조사 세션 노출. ChatGPT Work 펫 제작 맥락에 사용한다. 일반 이미지·실제 동물 요청과 구분한다. |
| [work-pets:pets](codex-plugins/README.md#work-pets-pets). | ChatGPT Work의 애니메이션 펫을 조회·선택·다운로드·삭제한다. | ChatGPT Work Pets · 조사 세션 노출. ChatGPT Work 펫 관리의 명시적 맥락과 대상·변경 범위를 확인한다. |
| [work-pets:update-pet](codex-plugins/README.md#work-pets-update-pet). | ChatGPT Work 펫의 이름·설명·스프라이트 등 기존 구성을 갱신한다. | ChatGPT Work Pets · 조사 세션 노출. ChatGPT Work의 기존 펫을 대상으로 원본과 변경 범위를 확인한다. |
| [imagegen](codex-local/README.md#codex-system-imagegen). | 이미지 생성·편집·참조 변형으로 비트맵 시각 자산을 만든다. | Codex 시스템 스킬 · 조사 세션 노출. 비트맵 산출물에 사용하며 기존 SVG·코드 기반 자산을 고치는 작업과 구분한다. |
| [visualize:visualize](codex-plugins/README.md#visualize-visualize). | 대화 안에서 시각화와 상호작용 도구를 만든다. | OpenAI Visualize · 조사 세션 노출. 대화 내 상호작용 시각화에 사용한다. 내보낼 정량 차트와 구분한다. |
| [anthropic-algorithmic-art](anthropic-skills/README.md#anthropic-algorithmic-art). | 코드와 조절 가능한 매개변수로 알고리즘 아트를 만드는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-brand-guidelines](anthropic-skills/README.md#anthropic-brand-guidelines). | Anthropic의 브랜드 색상·타이포그래피를 적용하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [anthropic-canvas-design](anthropic-skills/README.md#anthropic-canvas-design). | 포스터 등 정적인 시각 작품을 제작하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-slack-gif-creator](anthropic-skills/README.md#anthropic-slack-gif-creator). | Slack에 사용할 애니메이션 GIF를 만드는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-theme-factory](anthropic-skills/README.md#anthropic-theme-factory). | 문서·슬라이드·웹 산출물에 일관된 시각 테마를 적용하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huashu-design](office-design-tools/README.md#huashu-design). | HTML 기반 웹·앱·PPTX 디자인을 만드는 명시 호출 전용 스킬. | office-design-tools · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |

<a id="task-web-ui"></a>
## 웹·앱 UI·Figma.

실행할 UI와 디자인 편집 산출물을 구분한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 프런트엔드 화면의 시각 방향과 UI 구현. | [anthropic-frontend-design](anthropic-skills/README.md#anthropic-frontend-design). | 기존 `frontend-design` 배포 설명과 구분한다. 실제 브라우저로 검증한다. |
| Figma 화면·레이아웃 제작. | [figma-generate-design](figma/README.md#figma-generate-design). | 현재 Figma 파일·디자인 시스템과 필요한 도구를 확인한다. |
| Figma 디자인 시스템 구축. | [figma-generate-library](figma/README.md#figma-generate-library). | 변수·토큰·컴포넌트를 구축하거나 갱신할 때 사용한다. |
| Figma 기반 편집과 새 파일 생성. | [figma-use](figma/README.md#figma-use), [figma-create-new-file](figma/README.md#figma-create-new-file). | 편집·생성 도구의 필수 선행 가이드를 따른다. |
| 한 파일로 조절 가능한 HTML 탐색기 제작. | [playground](playground/README.md#playground). | 컨트롤과 라이브 미리보기가 필요한 작업에 사용한다. |
| HTML 기반 웹·앱 디자인. | [huashu-design](office-design-tools/README.md#huashu-design). | `$huashu-design` 명시 호출. 실제 제작 기능·브라우저 조건을 확인한다. |
| 여러 UI 요소가 있는 웹 산출물 제작. | [anthropic-web-artifacts-builder](anthropic-skills/README.md#anthropic-web-artifacts-builder). | `$anthropic-web-artifacts-builder` 명시 호출. 번들 실행·게시 조건을 따로 확인한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [data-analytics:build-dashboard](codex-plugins/README.md#data-analytics-build-dashboard). | 데이터 출처에 근거한 탐색·모니터링용 상호작용 대시보드를 만든다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:publish-artifact-to-sites](codex-plugins/README.md#data-analytics-publish-artifact-to-sites). | 기존 Data HTML 보고서·대시보드를 Sites에 게시한다. | Data Analytics · 조사 세션 노출. 기존 Data HTML 산출물과 게시 요청 또는 해당 전달 정책이 있어야 한다. |
| [computer-use:computer-use](codex-plugins/README.md#computer-use-computer-use). | 사용자 컴퓨터의 Windows 앱을 화면 기반으로 조작한다. | OpenAI Computer Use · 조사 세션 노출. 사용자가 지정한 앱·브라우저와 현재 가용 도구를 확인한다. |
| [sites:sites](codex-plugins/README.md#sites-sites). | 랜딩 페이지·대시보드·포털·내부 도구 등 웹사이트를 제작·수정한다. | Sites · 조사 세션 노출. 사이트 제작·수정 요청과 대상 사이트·제공 기능을 확인한다. |
| [sites:sites-remix](codex-plugins/README.md#sites-sites-remix). | 지정된 기존 Sites 사이트를 바탕으로 새 사이트를 만든다. | Sites · 조사 세션 노출. 원본 Sites 사이트가 특정되고 새 사이트로 리믹스하는 요청이 있어야 한다. |
| [anthropic-frontend-design](anthropic-skills/README.md#anthropic-frontend-design). | 의도적인 시각 방향을 가진 프런트엔드 UI를 만드는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-web-artifacts-builder](anthropic-skills/README.md#anthropic-web-artifacts-builder). | 여러 UI 요소가 필요한 웹 산출물을 구성하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [anthropic-webapp-testing](anthropic-skills/README.md#anthropic-webapp-testing). | 로컬 웹 앱의 브라우저 동작과 화면을 검증하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [figma-code-connect](figma/README.md#figma-code-connect). | Figma 컴포넌트를 코드 스니펫에 매핑하는 Code Connect 템플릿 파일(`.figma.ts`)을 생성·유지하는 스킬. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-create-new-file](figma/README.md#figma-create-new-file). | 새 빈 Figma 파일(design/figjam/slides)을 생성하는 스킬. `create_new_file` 호출의 필수 선행 스킬. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-generate-design](figma/README.md#figma-generate-design). | 코드/설명으로부터 디자인 시스템을 재사용해 Figma에 화면·뷰·다중 섹션 레이아웃을 구축/업데이트하는 스킬. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-generate-diagram](figma/README.md#figma-generate-diagram). | Mermaid.js 구문으로 편집 가능한 FigJam 다이어그램을 생성하는 스킬. `generate_diagram` 호출의 필수 선행 스킬. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-generate-library](figma/README.md#figma-generate-library). | 코드베이스로부터 Figma에 프로페셔널급 디자인 시스템(변수/토큰, 컴포넌트 라이브러리, 테마)을 구축/업데이트하는 스킬. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-generate-project-plan](figma/README.md#figma-generate-project-plan). | PRD(+선택적 코드베이스 컨텍스트)를 **FigJam 프로젝트 플랜 보드**로 변환하는 인터랙티브 워크플로 스킬. 섹션 후보 제안 → 사용자 선택 → 섹션별 콘텐츠·블록 확정 → FigJam 생성까지 단계마다 확인을 거친다. | figma · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [figma-use](figma/README.md#figma-use). | Figma Plugin API로 JavaScript를 실행해 노드를 생성/편집/조회하는 기반 스킬. 모든 `use_figma` 호출의 필수 선행 스킬. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-use-figjam](figma/README.md#figma-use-figjam). | FigJam 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 FigJam 특화 스킬. `figma-use`와 함께 사용. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-use-slides](figma/README.md#figma-use-slides). | Slides 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 Slides 특화 스킬. `figma-use`와 함께 사용. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [frontend-design](frontend-design/README.md#frontend-design). | 일반적인 "AI 슬롭" 미감을 피하고, 독창적이고 프로덕션급의 프론트엔드 인터페이스를 만드는 스킬. | frontend-design · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [huggingface-gradio](huggingface-skills/README.md#huggingface-gradio). | Python으로 Gradio 웹 UI와 ML 데모를 만드는 스킬 (Interface/Blocks/ChatInterface, 컴포넌트, 이벤트 리스너). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [transformers-js](huggingface-skills/README.md#transformers-js). | Transformers.js로 최신 ML 모델을 JavaScript/TypeScript에서 직접 실행하는 스킬 (브라우저·Node.js·Bun·Deno, WebGPU/WASM). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huashu-design](office-design-tools/README.md#huashu-design). | HTML 기반 웹·앱·PPTX 디자인을 만드는 명시 호출 전용 스킬. | office-design-tools · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [playground](playground/README.md#playground). | 컨트롤·라이브 프리뷰·프롬프트 출력을 갖춘 자기완결형 단일 HTML 인터랙티브 탐색기를 만드는 스킬. | playground · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-generate-project-plan](../Owned-Skills/figma-generate-project-plan/SKILL.md). | PRD를 FigJam 프로젝트 계획으로 정리하고 실제 도구 조건에 맞춰 반영한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |

<a id="task-data-analysis"></a>
## 데이터 분석·지표·시각화.

분석·품질·KPI·차트·대시보드와 파일 산출을 구분한다.

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [data-analytics:analyze-data-quality](codex-plugins/README.md#data-analytics-analyze-data-quality). | 구조화 데이터의 누락·중복·조인·최신성 등 품질 위험을 조사한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:answers-follow-up](codex-plugins/README.md#data-analytics-answers-follow-up). | 분석 답변 다음에 유용한 후속 작업을 선택지로 제안한다. | Data Analytics · 조사 세션 노출. 유용한 다음 작업이 있고 현재 호스트가 후속 선택지 UI를 지원할 때 사용한다. |
| [data-analytics:build-dashboard](codex-plugins/README.md#data-analytics-build-dashboard). | 데이터 출처에 근거한 탐색·모니터링용 상호작용 대시보드를 만든다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:build-report](codex-plugins/README.md#data-analytics-build-report). | 검토 가능한 근거를 갖춘 분석 보고서를 작성한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:convert-to-doc](codex-plugins/README.md#data-analytics-convert-to-doc). | 기존 Data 산출물을 DOCX·Google Docs 문서로 변환한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [data-analytics:convert-to-slides](codex-plugins/README.md#data-analytics-convert-to-slides). | 기존 Data 산출물을 PowerPoint·Google Slides 발표자료로 변환한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [data-analytics:customize-data-plugin](codex-plugins/README.md#data-analytics-customize-data-plugin). | 개인·팀의 데이터 작업 관례와 문맥을 재사용 스킬로 정리한다. | Data Analytics · 조사 세션 노출. 사용자가 재사용 데이터 관례·문맥의 생성·변경을 요청한 경우에 사용한다. |
| [data-analytics:design-kpis](codex-plugins/README.md#data-analytics-design-kpis). | KPI 정의·목표·가드레일·측정 계획을 설계한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:index](codex-plugins/README.md#data-analytics-index). | 데이터·지표·분석 요청을 알맞은 Data 작업 흐름으로 연결한다. | Data Analytics · 조사 세션 노출. 데이터·지표·분석 요청을 분류한다. 단순 글쓰기·일반 설명에 확대하지 않는다. |
| [data-analytics:jupyter-notebooks](codex-plugins/README.md#data-analytics-jupyter-notebooks). | 요청한 SQL·Python 노트북을 생성·편집·검증·내보낸다. | Data Analytics · 조사 세션 노출. 노트북 작업을 요청한 경우에 사용한다. 일반 분석에 불필요한 노트북을 만들지 않는다. |
| [data-analytics:kpi-reporting](codex-plugins/README.md#data-analytics-kpi-reporting). | KPI 성과·목표 대비 결과와 정기 운영 보고를 작성한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:market-sizing](codex-plugins/README.md#data-analytics-market-sizing). | 가정과 불확실성을 밝혀 시장·세그먼트·기회 규모를 추정한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:metric-diagnostics](codex-plugins/README.md#data-analytics-metric-diagnostics). | 지표 변화·이상·차이의 원인과 기여 요인을 진단한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:onboarding](codex-plugins/README.md#data-analytics-onboarding). | Data 연결·첫 작업·사용 시작을 안내한다. | Data Analytics · 조사 세션 노출. Data 사용 시작·연결·첫 작업 안내 요청에 사용한다. |
| [data-analytics:product-business-analysis](codex-plugins/README.md#data-analytics-product-business-analysis). | 제품·사업 의사결정에 필요한 데이터 분석을 수행한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:publish-artifact-to-sites](codex-plugins/README.md#data-analytics-publish-artifact-to-sites). | 기존 Data HTML 보고서·대시보드를 Sites에 게시한다. | Data Analytics · 조사 세션 노출. 기존 Data HTML 산출물과 게시 요청 또는 해당 전달 정책이 있어야 한다. |
| [data-analytics:report-to-pdf](codex-plugins/README.md#data-analytics-report-to-pdf). | 기존 Data 보고서·대시보드를 PDF로 변환한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [data-analytics:schedule-refresh-jobs](codex-plugins/README.md#data-analytics-schedule-refresh-jobs). | 기존 Data 산출물의 반복 갱신 클라우드 작업을 설정한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [data-analytics:share-artifact-summary](codex-plugins/README.md#data-analytics-share-artifact-summary). | Data 보고서·대시보드·차트의 요약을 제공하거나 공유한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [data-analytics:validate-data](codex-plugins/README.md#data-analytics-validate-data). | 분석 방법·계산·시각화·결론과 보고서 완성도를 검증한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [data-analytics:visualize-data](codex-plugins/README.md#data-analytics-visualize-data). | 분석 산출물에 들어갈 정량 차트·그림을 제작·검증한다. | Data Analytics · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [huggingface-datasets](huggingface-skills/README.md#huggingface-datasets). | Hugging Face Dataset Viewer API로 데이터셋 메타데이터·행 페이지네이션·검색·필터·parquet URL을 읽는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |

<a id="task-research"></a>
## 검색·자료 수집·리서치.

소스 발견·본문 수집·교차 검증을 구분한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 검색어로 웹 소스 발견. | [firecrawl-search](firecrawl/README.md#firecrawl-search). | 관련 페이지를 찾는 단계에 사용한다. |
| 알려진 웹페이지 읽기. | [firecrawl-scrape](firecrawl/README.md#firecrawl-scrape). | URL의 본문이나 구조화 결과가 필요할 때 사용한다. |
| URL 탐색·여러 페이지 수집. | [firecrawl-map](firecrawl/README.md#firecrawl-map), [firecrawl-crawl](firecrawl/README.md#firecrawl-crawl). | 주소 발견과 본문 일괄 수집을 구분한다. |
| 상호작용이 필요한 사이트 조사. | [firecrawl-interact](firecrawl/README.md#firecrawl-interact), [firecrawl-agent](firecrawl/README.md#firecrawl-agent). | 폼·페이지 이동 등 실제 상호작용이 필요한 경우에 선택한다. |
| 여러 자료를 비교·교차 검증한 조사. | [deep-research · 개인 분류 설명](_personal/README.md#deep-research). | 출처·불확실성과 근거가 있는 종합 답변이 필요할 때 사용한다. |
| Hugging Face 논문 조회. | [huggingface-papers](huggingface-skills/README.md#huggingface-papers). | 논문·저자·연결 모델과 데이터셋을 조사한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [firecrawl](codex-local/README.md#user-firecrawl). | 웹 검색·페이지 읽기·크롤링·상호작용을 작업에 맞는 Firecrawl 경로로 연결한다. | Firecrawl 전역 패키지 · 조사 세션 노출. 웹 작업의 최상위 안내이며 로컬 파일은 firecrawl-parse로 연결한다. |
| [claude-news](_personal/README.md#claude-news). | Claude Code 릴리스 노트 + Anthropic 모델/제품 소식을 **한국어로 요약**하는 개인 글로벌 스킬. 새 기능과 주요 변경을 카테고리별로 정리해 보여준다. | _personal · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [deep-research](_personal/README.md#deep-research). | 멀티소스 웹 검색 + 소스 fetch + **교차검증(adversarial verify)** + 인용 포함 리포트 합성을 수행하는 개인 글로벌 딥리서치 스킬. | _personal · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [anthropic-academy-guide](anthropic-skills/README.md#anthropic-academy-guide). | Claude 사용 목적에 맞는 Academy 과정·튜토리얼을 찾는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-discernment-nudge](anthropic-skills/README.md#anthropic-discernment-nudge). | 답변의 사실·추론·누락을 점검하는 후속 질문을 제안하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [firecrawl-agent](firecrawl/README.md#firecrawl-agent). | AI가 복잡한 사이트를 자율 탐색해 구조화된 JSON 데이터를 추출하는 스킬. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-cli](firecrawl/README.md#firecrawl-cli). | Firecrawl CLI로 웹을 검색·스크래핑·상호작용하는 최상위 워크플로우 스킬. LLM에 최적화된 클린 마크다운 반환. | firecrawl · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [firecrawl-crawl](firecrawl/README.md#firecrawl-crawl). | 웹사이트 전체 또는 섹션의 여러 페이지를 링크를 따라가며 대량 추출하는 스킬. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-download](firecrawl/README.md#firecrawl-download). | 웹사이트 전체를 로컬 파일(마크다운/스크린샷/다중 포맷)로 다운로드하는 스킬. (실험적). | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-interact](firecrawl/README.md#firecrawl-interact). | 스크래프한 페이지의 라이브 브라우저 세션을 자연어/코드로 제어하는 스킬 — 클릭, 폼 입력, 내비게이션, 로그인. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-map](firecrawl/README.md#firecrawl-map). | 웹사이트의 모든 URL을 발견·나열하는 스킬. 검색 필터로 특정 페이지 위치 파악. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-monitor](firecrawl/README.md#firecrawl-monitor). | 웹사이트 콘텐츠 변경을 감지해 웹훅/이메일로 알려주는 스킬 — cron·스크래퍼·diff 스크립트 불필요. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-parse](firecrawl/README.md#firecrawl-parse). | 로컬 파일(PDF/DOCX/XLSX/HTML 등)을 클린 마크다운으로 변환해 디스크에 저장하는 스킬. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-scrape](firecrawl/README.md#firecrawl-scrape). | 임의의 URL(JS 렌더링 SPA 포함)에서 클린 마크다운을 추출하는 스킬. WebFetch 대체. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-search](firecrawl/README.md#firecrawl-search). | 전체 페이지 콘텐츠 추출까지 지원하는 웹 검색 스킬. 스니펫이 아닌 실제 결과 + 풀페이지 마크다운. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [skill-gen](firecrawl/README.md#skill-gen). | Firecrawl로 문서 URL을 스크래핑해 완전한 Agent Skill을 자동 생성하는 슬래시 명령어. | firecrawl · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [huggingface-paper-publisher](huggingface-skills/README.md#huggingface-paper-publisher). | Hugging Face Hub에 연구 논문을 발행·관리하는 스킬 (페이지 생성, 모델/데이터셋 연결, 저자권 주장, 연구 아티클 생성). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-papers](huggingface-skills/README.md#huggingface-papers). | HF paper page를 마크다운으로 읽고, papers API로 저자·연결된 모델/데이터셋/스페이스 등 구조화 메타데이터를 조회하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [claude-news](../Owned-Skills/claude-news/SKILL.md). | Claude Code 릴리스와 Anthropic 제품의 최근 변경을 확인한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [deep-research](../Owned-Skills/deep-research/SKILL.md). | 여러 소스를 비교·교차 검증하고 출처·불확실성을 포함해 조사한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |

<a id="task-development"></a>
## 개발 설계·구현.

프로젝트 운영 규칙 아래에서 설계·구현 단계를 선택한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 상태 변경 작업의 전체 흐름 조율. | [design-driven-delivery · 자체 제작](../Owned-Skills/design-driven-delivery/SKILL.md). | 설계·계획·구현·검증·통합의 상위 절차다. |
| 목적·범위·접근법을 설계로 정리. | [brainstorming](superpowers/README.md#brainstorming). | 새 작업의 의도와 승인 설계를 확인한다. |
| 승인 설계를 실행 가능한 태스크로 분해. | [writing-plans](superpowers/README.md#writing-plans). | 파일·테스트·검증·인터페이스를 계획한다. |
| 기존 코드베이스의 기능 개발. | [feature-dev · 자체 제작](../Owned-Skills/feature-dev/SKILL.md). | 호출자·요구사항·기존 구조를 조사하고 구현·검증한다. |
| 실패 테스트부터 기능·수정 구현. | [test-driven-development](superpowers/README.md#test-driven-development). | RED·GREEN으로 동작을 확인한다. |
| 승인 계획의 직접 실행·독립 태스크 위임. | [executing-plans](superpowers/README.md#executing-plans), [subagent-driven-development](superpowers/README.md#subagent-driven-development). | 현재 환경과 승인된 실행 방식에 따라 선택한다. |
| 작업 공간 격리와 브랜치 통합. | [using-git-worktrees](superpowers/README.md#using-git-worktrees), [finishing-a-development-branch](superpowers/README.md#finishing-a-development-branch). | 기존 격리·사용자 변경과 승인된 병합 범위를 확인한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [notion:notion-set-up-my-project](codex-plugins/README.md#notion-notion-set-up-my-project). | Notion에 프로젝트 문서·업무·회의를 위한 초기 홈을 만든다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-spec-to-implementation](codex-plugins/README.md#notion-notion-spec-to-implementation). | Notion 제품·기술 사양을 구현 계획과 연결된 업무로 바꾼다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [ponytail:ponytail](codex-plugins/README.md#ponytail-ponytail). | 요청을 완결하는 최소 변경과 간결한 보고 원칙을 적용한다. | Ponytail · 조사 세션 노출. 코딩 작업에 최소 완결 변경 원칙을 적용한다. |
| [ponytail:ponytail-audit](codex-plugins/README.md#ponytail-ponytail-audit). | 저장소 전체의 결함·보안·부하·테스트·불필요한 코드를 감사한다. | Ponytail · 조사 세션 노출. 저장소 전체 감사를 요청한 경우에 조사하며 구현 범위와 구분한다. |
| [ponytail:ponytail-debt](codex-plugins/README.md#ponytail-ponytail-debt). | shortcut·ponytail 주석을 찾아 기술 부채 목록으로 보여준다. | Ponytail · 조사 세션 노출. 부채 주석 목록을 읽기 전용으로 보여준다. |
| [ponytail:ponytail-gain](codex-plugins/README.md#ponytail-ponytail-gain). | Ponytail 벤치마크에 기록된 코드·비용·속도 절감 결과를 보여준다. | Ponytail · 조사 세션 노출. 기록된 벤치마크를 표시하며 현재 작업의 새 절감 측정으로 주장하지 않는다. |
| [ponytail:ponytail-help](codex-plugins/README.md#ponytail-ponytail-help). | Ponytail 수준·스킬·명령의 사용법을 안내한다. | Ponytail · 조사 세션 노출. Ponytail 사용법·수준·명령 질문에 사용한다. |
| [ponytail:ponytail-review](codex-plugins/README.md#ponytail-ponytail-review). | 코드 변경의 정확성·안전·부하·테스트·필요성을 검토한다. | Ponytail · 조사 세션 노출. 변경 범위를 정하고 품질·안전·필요성을 검토한다. |
| [design-driven-delivery](_personal/README.md#design-driven-delivery). | 모든 요청을 읽기 전용·진단·상태 변경·모니터링으로 분류하고, 상태 변경을 설계·계획·구현·검증·리뷰·문서화·통합 순서로 통제하는 자체 제작 최상위 전달 스킬. | _personal · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [feature-dev](feature-dev/README.md#feature-dev). | 코드베이스를 깊이 이해하고, 모호한 부분을 먼저 질문하고, 여러 아키텍처를 설계한 뒤 구현하는 7단계 가이드형 기능 개발 명령어. | feature-dev · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [cancel-ralph](ralph-loop/README.md#cancel-ralph). | 활성화된 Ralph 루프의 상태 파일을 제거해 루프를 취소하는 명령어. | ralph-loop · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [help](ralph-loop/README.md#help). | Ralph Loop 플러그인의 개념·명령어·핵심 메커니즘을 사용자에게 설명하는 도움말 명령어. | ralph-loop · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [ralph-loop](ralph-loop/README.md#ralph-loop). | 같은 프롬프트를 Stop 훅으로 반복 주입해 현재 세션 안에서 자기참조 반복 개발 루프(Ralph Wiggum 기법)를 시작하는 명령어. | ralph-loop · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [brainstorming](superpowers/README.md#brainstorming). | 새 작업의 목적·범위와 접근법을 확인하고, 규모에 맞는 승인 설계로 정리하는 대화형 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [dispatching-parallel-agents](superpowers/README.md#dispatching-parallel-agents). | 공유 상태와 순차 의존성이 없는 독립 작업을 각각의 에이전트에게 병렬 위임하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [executing-plans](superpowers/README.md#executing-plans). | 현재 세션에서 계획을 직접 구현하고 진행 원장과 태스크별 검증·최종 브랜치 리뷰를 유지하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [finishing-a-development-branch](superpowers/README.md#finishing-a-development-branch). | 전체 테스트를 확인한 뒤 병합·PR·유지 중 승인된 통합을 수행하고 소유한 작업 공간을 정리하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [subagent-driven-development](superpowers/README.md#subagent-driven-development). | 태스크마다 새 구현자와 스펙·품질을 함께 보는 리뷰어를 배치하고 최종 전체 브랜치 리뷰를 수행하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [test-driven-development](superpowers/README.md#test-driven-development). | 실패 테스트를 먼저 확인하고 최소 구현과 전체 회귀를 거쳐 동작을 보장하는 TDD 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [using-git-worktrees](superpowers/README.md#using-git-worktrees). | 기존 격리를 확인하고 네이티브 도구를 우선해 작업 공간을 준비하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [using-superpowers](superpowers/README.md#using-superpowers). | 응답과 탐색 전에 관련 스킬을 확인하고 현재 플랫폼의 도구로 적용하게 하는 진입 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [writing-plans](superpowers/README.md#writing-plans). | 승인 스펙을 정확한 인터페이스·테스트·검증 결과가 있는 실행 가능한 태스크로 나누는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [design-driven-delivery](../Owned-Skills/design-driven-delivery/SKILL.md). | 요청을 분류하고 상태 변경을 설계부터 검증·통합까지 조율한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [feature-dev](../Owned-Skills/feature-dev/SKILL.md). | 기존 코드베이스의 기능을 조사·설계·구현하고 실제 동작을 검증한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [figma-generate-project-plan](../Owned-Skills/figma-generate-project-plan/SKILL.md). | PRD를 FigJam 프로젝트 계획으로 정리하고 실제 도구 조건에 맞춰 반영한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |

<a id="task-debug-review"></a>
## 디버깅·테스트·리뷰.

원인 조사·실제 실행·변경 검토를 목적에 맞게 선택한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 버그·테스트 실패의 근본 원인 조사. | [systematic-debugging](superpowers/README.md#systematic-debugging). | 수정안을 내기 전에 재현·증거·패턴을 확인한다. |
| 앱 실행과 사용자 흐름 검증. | [run · 자체 제작](../Owned-Skills/run/SKILL.md), [verify · 자체 제작](../Owned-Skills/verify/SKILL.md). | 실행 준비와 실행 후 동작 확인을 구분한다. |
| 웹 디버깅·접근성·LCP·메모리 조사. | [chrome-devtools](chrome-devtools-mcp/README.md#chrome-devtools), [a11y-debugging](chrome-devtools-mcp/README.md#a11y-debugging), [debug-optimize-lcp](chrome-devtools-mcp/README.md#debug-optimize-lcp), [memory-leak-debugging](chrome-devtools-mcp/README.md#memory-leak-debugging). | 사용자 지정 도구와 브라우저 연결 조건을 확인한다. |
| 변경·PR 검토와 보안 조사. | [code-review · 자체 제작](../Owned-Skills/code-review/SKILL.md), [review-pr · 자체 제작](../Owned-Skills/review-pr/SKILL.md), [security-review · 자체 제작](../Owned-Skills/security-review/SKILL.md). | 검토 대상과 권한을 확인한다. 내장·플러그인 동명 항목과 구분한다. |
| 기존 동작을 유지하며 코드 단순화. | [simplify · 자체 제작](../Owned-Skills/simplify/SKILL.md). | 요청한 정리 범위와 동작·오류·부작용을 보존한다. |
| 완료 주장 전에 실행 증거 확인. | [verification-before-completion](superpowers/README.md#verification-before-completion). | 실제 검사 결과를 확인하며 실행 검증을 대체하지 않는다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [review-agent](codex-local/README.md#codex-system-review-agent). | 위임된 코드 변경을 읽기 전용으로 검토하고 재현 가능한 결함을 보고한다. | Codex 시스템 스킬 · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 이번 세션 일반 스킬 목록에는 노출되지 않았다. 변경·커밋·푸시는 수행하지 않는다. |
| [ponytail:ponytail-audit](codex-plugins/README.md#ponytail-ponytail-audit). | 저장소 전체의 결함·보안·부하·테스트·불필요한 코드를 감사한다. | Ponytail · 조사 세션 노출. 저장소 전체 감사를 요청한 경우에 조사하며 구현 범위와 구분한다. |
| [ponytail:ponytail-review](codex-plugins/README.md#ponytail-ponytail-review). | 코드 변경의 정확성·안전·부하·테스트·필요성을 검토한다. | Ponytail · 조사 세션 노출. 변경 범위를 정하고 품질·안전·필요성을 검토한다. |
| [code-review](_builtin/README.md#code-review). | 현재 diff를 **정확성(버그) + 재사용/단순화/효율성** 관점에서 리뷰하는 빌트인 스킬. effort 레벨로 깊이를 조절하고, PR 코멘트나 워킹트리 적용까지 가능. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [review](_builtin/README.md#review). | PR / 코드 리뷰를 수행하는 빌트인 명령. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [run](_builtin/README.md#run). | 프로젝트 앱을 **실제로 띄워서** 변경이 동작하는지 확인하는 빌트인 스킬. 프로젝트 타입(CLI/server/TUI/Electron/browser/library)별 구동 패턴을 안다. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [security-review](_builtin/README.md#security-review). | **보안 취약점 관점**에서 코드를 리뷰하는 빌트인 명령. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [simplify](_builtin/README.md#simplify). | 변경된 코드를 **재사용·단순화·효율성·altitude(추상화 수준)** 관점에서 정리하고 그 수정을 직접 적용하는 빌트인 스킬. **품질 전용**이며 버그는 찾지 않는다. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [verify](_builtin/README.md#verify). | 코드 변경이 **실제로 의도대로 동작하는지** 앱을 직접 실행해 동작을 관찰하며 검증하는 빌트인 스킬. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [setup-semgrep-plugin](_disabled/semgrep/README.md#setup-semgrep-plugin). | Semgrep 설치·인증·버전 호환성 확인을 통해 Semgrep 플러그인을 셋업하는 커맨드. | _disabled/semgrep · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-agents](_disabled/vercel/README.md#benchmark-agents). | vercel-plugin의 스킬 주입을 고난도 AI 시스템 시나리오로 스트레스 테스트하는 내부 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-e2e](_disabled/vercel/README.md#benchmark-e2e). | vercel-plugin을 현실적 프로젝트로 돌려 스킬 주입·dev 서버 기동·검증·개선 리포트를 한 번에 생성하는 내부 E2E 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-sandbox](_disabled/vercel/README.md#benchmark-sandbox). | 로컬 WezTerm 대신 Vercel Sandbox(원격 microVM)에서 eval 시나리오를 돌리는 내부 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-testing](_disabled/vercel/README.md#benchmark-testing). | 현실적·기술명 비공개 프롬프트로 vercel-plugin 스킬 주입을 시험할 격리 테스트 프로젝트를 만드는 내부 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [plugin-audit](_disabled/vercel/README.md#plugin-audit). | 실제 Claude Code 세션 로그를 분석해 vercel-plugin 스킬 주입 성능과 패턴 커버리지 갭을 진단하는 내부 감사 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [vercel-plugin-eval](_disabled/vercel/README.md#vercel-plugin-eval). | 실제 Claude Code 세션을 띄워 vercel-plugin의 훅 발화·스킬 주입·dedup 정확성·커버리지를 검증하는 내부 eval 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [anthropic-webapp-testing](anthropic-skills/README.md#anthropic-webapp-testing). | 로컬 웹 앱의 브라우저 동작과 화면을 검증하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [a11y-debugging](chrome-devtools-mcp/README.md#a11y-debugging). | Chrome DevTools MCP를 활용해 web.dev 가이드라인 기반으로 웹 페이지의 접근성(a11y)을 디버깅·감사하는 스킬. | chrome-devtools-mcp · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [chrome-devtools](chrome-devtools-mcp/README.md#chrome-devtools). | Chrome DevTools를 MCP로 활용해 효율적으로 디버깅, 트러블슈팅, 브라우저 자동화를 수행하는 핵심 스킬. | chrome-devtools-mcp · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [chrome-devtools-cli](chrome-devtools-mcp/README.md#chrome-devtools-cli). | 터미널에서 셸 스크립트/명령으로 Chrome DevTools를 제어해 브라우저 작업을 자동화하는 스킬. | chrome-devtools-mcp · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [debug-optimize-lcp](chrome-devtools-mcp/README.md#debug-optimize-lcp). | Chrome DevTools MCP로 Largest Contentful Paint(LCP)를 디버깅하고 최적화하는 스킬. | chrome-devtools-mcp · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [memory-leak-debugging](chrome-devtools-mcp/README.md#memory-leak-debugging). | JavaScript/Node.js 애플리케이션의 메모리 누수를 진단·해결하는 스킬. | chrome-devtools-mcp · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [troubleshooting](chrome-devtools-mcp/README.md#troubleshooting). | Chrome DevTools MCP의 연결·타겟 문제를 단계별로 진단·해결하는 트러블슈팅 마법사 스킬. | chrome-devtools-mcp · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [review-pr](pr-review-toolkit/README.md#review-pr). | 변경된 코드(git diff)를 여러 전문 에이전트로 나눠 종합 PR 리뷰를 수행하고, 심각도별 액션 플랜으로 정리해주는 슬래시 명령어. | pr-review-toolkit · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [qodo-get-rules](qodo-skills/README.md#qodo-get-rules). | 현재 코딩 작업에 가장 관련 있는 Qodo 코딩 규칙을, 시맨틱 검색 쿼리를 생성해 `POST /rules/search`로 가져와 심각도별로 적용하는 스킬. | qodo-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [qodo-pr-resolver](qodo-skills/README.md#qodo-pr-resolver). | 현재 브랜치 PR/MR의 Qodo 리뷰 이슈를 가져와 심각도별로 보여주고, 대화형/일괄로 수정한 뒤 인라인 코멘트에 답글·요약을 다는 스킬. GitHub·GitLab·Bitbucket·Azure DevOps·Gerrit 지원. | qodo-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [diagnosing-superpowers](superpowers/README.md#diagnosing-superpowers). | Superpowers 세션의 반복 작업·계획 이탈·비용·실패를 대화 기록의 파일·줄 근거로 보고하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [receiving-code-review](superpowers/README.md#receiving-code-review). | 리뷰 피드백을 코드·요구사항·검증 근거와 대조한 뒤 항목별로 반영하거나 기술적으로 반박하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [requesting-code-review](superpowers/README.md#requesting-code-review). | 정확한 변경 범위와 요구사항을 전달해 작업 산출물의 독립 코드 리뷰를 요청하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [systematic-debugging](superpowers/README.md#systematic-debugging). | 수정안을 내기 전에 재현·증거·패턴 비교로 근본 원인을 찾는 네 단계 디버깅 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [verification-before-completion](superpowers/README.md#verification-before-completion). | 완료·수정·통과를 주장하기 전에 실제 검증 명령과 전체 결과를 확인하는 스킬. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [code-review](../Owned-Skills/code-review/SKILL.md). | 코드 변경의 정확성·상태·실패 경로·보안과 검증 근거를 검토한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [review](../Owned-Skills/review/SKILL.md). | 검토 대상을 정하고 코드·PR 리뷰의 적절한 절차로 연결한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [review-pr](../Owned-Skills/review-pr/SKILL.md). | PR의 테스트·오류 처리·주석·타입 등 여러 관점을 종합 검토한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [run](../Owned-Skills/run/SKILL.md). | 프로젝트의 앱·CLI·서버를 실제 실행하고 준비 상태를 확인한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [security-review](../Owned-Skills/security-review/SKILL.md). | 실제 공격 경로와 증거를 바탕으로 보안 문제를 조사한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [simplify](../Owned-Skills/simplify/SKILL.md). | 기존 동작·오류·부작용을 보존하며 요청한 코드를 단순화한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [verify](../Owned-Skills/verify/SKILL.md). | 변경 기능의 정상·실패 사용자 흐름과 실제 실행 증거를 확인한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |

<a id="task-ai-training"></a>
## AI 모델·데이터셋·학습.

모델 조사·학습·평가·데모 실행을 구분한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 작업에 맞는 모델 선택·로컬 실행. | [huggingface-best](huggingface-skills/README.md#huggingface-best), [huggingface-local-models](huggingface-skills/README.md#huggingface-local-models). | 평가 근거와 실제 하드웨어·양자화 조건을 확인한다. |
| Hub 파일·데이터셋 조회와 관리. | [hf-cli](huggingface-skills/README.md#hf-cli), [huggingface-datasets](huggingface-skills/README.md#huggingface-datasets). | 다운로드·조회와 업로드 권한을 구분한다. |
| 언어 모델 학습·후학습. | [huggingface-llm-trainer](huggingface-skills/README.md#huggingface-llm-trainer), [trl-training](huggingface-skills/README.md#trl-training). | 데이터·학습 방식·실행 자원과 비용 범위를 확인한다. |
| 비전·임베딩 모델 학습. | [huggingface-vision-trainer](huggingface-skills/README.md#huggingface-vision-trainer), [train-sentence-transformers](huggingface-skills/README.md#train-sentence-transformers). | 태스크·데이터·평가 기준에 맞는 학습 경로를 선택한다. |
| 평가·학습 추적. | [huggingface-community-evals](huggingface-skills/README.md#huggingface-community-evals), [huggingface-trackio](huggingface-skills/README.md#huggingface-trackio). | 실제 하드웨어·평가 백엔드·로깅 조건을 확인한다. |
| ML 데모·Spaces·브라우저 추론. | [huggingface-gradio](huggingface-skills/README.md#huggingface-gradio), [huggingface-spaces](huggingface-skills/README.md#huggingface-spaces), [huggingface-zerogpu](huggingface-skills/README.md#huggingface-zerogpu), [transformers-js](huggingface-skills/README.md#transformers-js). | 로컬 UI·호스팅·GPU·브라우저 실행의 차이를 확인한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [hf-cli](huggingface-skills/README.md#hf-cli). | Hugging Face Hub의 공식 CLI 도구 `hf`로 모델·데이터셋·스페이스·버킷·repo·논문·잡(Jobs) 등을 다운로드/업로드/관리하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-best](huggingface-skills/README.md#huggingface-best). | 특정 작업에 가장 좋은/추천 AI 모델을 HF 공식 벤치마크 리더보드로 찾아 비교표로 제시하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-community-evals](huggingface-skills/README.md#huggingface-community-evals). | 로컬 하드웨어에서 inspect-ai와 lighteval로 HF Hub 모델 평가(eval)를 실행하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-datasets](huggingface-skills/README.md#huggingface-datasets). | Hugging Face Dataset Viewer API로 데이터셋 메타데이터·행 페이지네이션·검색·필터·parquet URL을 읽는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-gradio](huggingface-skills/README.md#huggingface-gradio). | Python으로 Gradio 웹 UI와 ML 데모를 만드는 스킬 (Interface/Blocks/ChatInterface, 컴포넌트, 이벤트 리스너). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-llm-trainer](huggingface-skills/README.md#huggingface-llm-trainer). | TRL/Unsloth와 Hugging Face Jobs 클라우드 GPU로 언어·비전 모델을 학습/파인튜닝하는 스킬 (SFT/DPO/GRPO/Reward + GGUF 변환). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-local-models](huggingface-skills/README.md#huggingface-local-models). | llama.cpp + GGUF로 CPU/Mac Metal/CUDA/ROCm에서 모델을 로컬 실행하기 위한 모델 선택·실행 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-lora-space-builder](huggingface-skills/README.md#huggingface-lora-space-builder). | 사용자가 제공한 LoRA를 위한 Gradio 데모를 Hugging Face Spaces(ZeroGPU, 기본 private)에 빌드·발행하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-paper-publisher](huggingface-skills/README.md#huggingface-paper-publisher). | Hugging Face Hub에 연구 논문을 발행·관리하는 스킬 (페이지 생성, 모델/데이터셋 연결, 저자권 주장, 연구 아티클 생성). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-papers](huggingface-skills/README.md#huggingface-papers). | HF paper page를 마크다운으로 읽고, papers API로 저자·연결된 모델/데이터셋/스페이스 등 구조화 메타데이터를 조회하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-spaces](huggingface-skills/README.md#huggingface-spaces). | Hugging Face Spaces 앱(Gradio/Docker/Static, ZeroGPU·전용 하드웨어)을 빌드·배포·디버깅·유지보수하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-tool-builder](huggingface-skills/README.md#huggingface-tool-builder). | Hugging Face API 데이터를 fetch·가공·결합하는 재사용 가능한 CLI 스크립트/유틸리티를 만드는 스킬. | huggingface-skills · 조사 세션 노출. 반복하거나 여러 API 호출을 연결할 작업에 사용하며 실제 SDK·인증을 확인한다. |
| [huggingface-trackio](huggingface-skills/README.md#huggingface-trackio). | Trackio로 ML 학습 실험의 메트릭을 로깅·시각화하고, 알림 발화·메트릭 조회까지 다루는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-vision-trainer](huggingface-skills/README.md#huggingface-vision-trainer). | HF Transformers + HF Jobs 클라우드 GPU로 객체탐지·이미지분류·SAM/SAM2 분할 비전 모델을 학습/파인튜닝하는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [huggingface-zerogpu](huggingface-skills/README.md#huggingface-zerogpu). | Gradio Spaces의 ZeroGPU 하드웨어 코드 제약(`@spaces.GPU`, 프로세스 격리, duration/quota, CUDA 빌드)을 다루는 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [train-sentence-transformers](huggingface-skills/README.md#train-sentence-transformers). | sentence-transformers 모델(SentenceTransformer/CrossEncoder/SparseEncoder)을 학습/파인튜닝하는 라우터형 스킬. | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [transformers-js](huggingface-skills/README.md#transformers-js). | Transformers.js로 최신 ML 모델을 JavaScript/TypeScript에서 직접 실행하는 스킬 (브라우저·Node.js·Bun·Deno, WebGPU/WASM). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [trl-training](huggingface-skills/README.md#trl-training). | TRL(Transformers Reinforcement Learning) CLI 명령으로 LM을 학습/파인튜닝하는 스킬 (SFT/DPO/GRPO/KTO/RLOO/Reward). | huggingface-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |

<a id="task-agent-integration"></a>
## 에이전트·스킬·MCP·Unity 연동.

스킬·서버 구현과 클라이언트 연결을 구분한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 스킬 설계·작성·검증. | [writing-skills](superpowers/README.md#writing-skills), [anthropic-skill-creator](anthropic-skills/README.md#anthropic-skill-creator). | 후자는 `$anthropic-skill-creator` 명시 호출. OpenAI 내장·다른 배포본과 구분한다. |
| Claude Code 에이전트·플러그인 제작. | [agent-development](plugin-dev/README.md#agent-development), [create-plugin](plugin-dev/README.md#create-plugin), [plugin-structure](plugin-dev/README.md#plugin-structure). | 해당 호스트의 플러그인·에이전트 형식에 맞춘다. |
| MCP 서버 구현과 플러그인 연동. | [anthropic-mcp-builder](anthropic-skills/README.md#anthropic-mcp-builder), [mcp-integration](plugin-dev/README.md#mcp-integration). | 서버 구현과 등록·인증·권한 변경을 구분한다. |
| Claude API·Agent SDK 작업. | [claude-api · 자체 제작](../Owned-Skills/claude-api/SKILL.md), [new-sdk-app · 자체 제작](../Owned-Skills/new-sdk-app/SKILL.md). | 제공자와 요청 범위를 확인한다. |
| Coplay·Funplay Unity MCP 설치·연결. | [coplay-funplay-unity-mcp-setup · 자체 제작](../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md). | 전역 도구와 프로젝트별 패키지·Editor 연결을 구분한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [skill-creator](codex-local/README.md#codex-system-skill-creator). | 범위가 명확한 Codex 스킬과 필요한 지원 리소스를 작성·갱신한다. | Codex 시스템 스킬 · 조사 세션 노출. Codex 시스템 구현이며 Anthropic 원본·기존 플러그인 동명 스킬과 구분한다. |
| [skill-installer](codex-local/README.md#codex-system-skill-installer). | 선정된 목록이나 저장소에서 Codex 스킬을 설치한다. | Codex 시스템 스킬 · 조사 세션 노출. 설치 대상·기존 패키지·리소스 보존과 실제 설치 경로를 확인한다. |
| [data-analytics:customize-data-plugin](codex-plugins/README.md#data-analytics-customize-data-plugin). | 개인·팀의 데이터 작업 관례와 문맥을 재사용 스킬로 정리한다. | Data Analytics · 조사 세션 노출. 사용자가 재사용 데이터 관례·문맥의 생성·변경을 요청한 경우에 사용한다. |
| [template-creator:template-creator](codex-plugins/README.md#template-creator-template-creator). | 개인용 산출물 템플릿을 재사용 가능한 Codex 스킬로 작성·갱신한다. | OpenAI Template Creator · 조사 세션 노출. 재사용 개인 산출물 템플릿 스킬을 만들거나 갱신하는 요청에 사용한다. |
| [paseo](codex-local/README.md#user-paseo). | Paseo의 호스트·프로젝트·작업 공간·에이전트·스케줄을 관리한다. | Paseo 스킬 · 조사 세션 노출. Paseo MCP 또는 CLI의 실제 가용성과 대상 작업 공간을 확인한다. |
| [paseo-advisor](codex-local/README.md#user-paseo-advisor). | 현재 작업에 대한 한 에이전트의 조언과 독립 의견을 구한다. | Paseo 스킬 · 조사 세션 노출. 사용자가 조언·두 번째 의견을 요청할 때 사용하며 작업 자체의 인수인계와 구분한다. |
| [paseo-committee](codex-local/README.md#user-paseo-committee). | 두 에이전트의 위원회로 원인과 어려운 계획을 검토한다. | Paseo 스킬 · 조사 세션 노출. 막힘·반복·어려운 계획에서 실제 다중 에이전트 기능을 확인한다. |
| [paseo-handoff](codex-local/README.md#user-paseo-handoff). | 현재 작업의 문맥을 다른 에이전트에게 인계한다. | Paseo 스킬 · 조사 세션 노출. 다른 에이전트로 작업을 넘기라는 요청과 실제 인계 기능을 확인한다. |
| [paseo-plugin](codex-local/README.md#user-paseo-plugin). | Paseo의 신뢰된 로컬 플러그인을 제작·관리한다. | Paseo 스킬 · 조사 세션 노출. 플러그인 기능·허용 범위·수명주기와 실제 Paseo 환경을 확인한다. |
| [unity-cli](codex-local/README.md#user-unity-cli). | CLI로 Unity Editor와 프로젝트·장면·빌드·테스트 작업을 제어한다. | Unity 스킬 · 조사 세션 노출. Unity CLI와 실행 중인 Editor의 연결·프로젝트·요청된 변경 범위를 확인한다. |
| [claude-api](_builtin/README.md#claude-api). | Claude API / Anthropic SDK 레퍼런스 빌트인 스킬. model id·가격·파라미터·스트리밍·tool use·MCP·캐싱·토큰 카운팅·모델 마이그레이션을 다룬다. **Claude/Anthropic 관련 작업 시 파일을 열기 전에 먼저 읽는 트리거 스킬**. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [configure](_disabled/hookify/README.md#configure). | 기존 hookify 규칙을 인터랙티브하게 활성/비활성 토글하는 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [help](_disabled/hookify/README.md#help). | hookify 플러그인의 동작 원리와 사용법을 설명하는 도움말 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [hookify](_disabled/hookify/README.md#hookify). | 대화 분석이나 명시적 지시로부터 원치 않는 행동을 막는 hookify 규칙을 생성하는 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [list](_disabled/hookify/README.md#list). | 프로젝트에 설정된 모든 hookify 규칙을 표와 미리보기로 나열하는 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [writing-rules](_disabled/hookify/README.md#writing-rules). | hookify 규칙 파일(`.claude/hookify.*.local.md`)의 작성 문법과 패턴을 안내하는 스킬. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [new-sdk-app](agent-sdk-dev/README.md#new-sdk-app). | Claude Agent SDK 애플리케이션(Python / TypeScript)을 대화형으로 새로 만들고, 최신 SDK 설치·검증까지 끝내는 슬래시 명령어. | agent-sdk-dev · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [anthropic-claude-api](anthropic-skills/README.md#anthropic-claude-api). | 공식 Claude API·SDK 원본 자료를 참고하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [anthropic-mcp-builder](anthropic-skills/README.md#anthropic-mcp-builder). | 외부 서비스를 연결하는 MCP 서버를 설계·구현하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [anthropic-skill-creator](anthropic-skills/README.md#anthropic-skill-creator). | 스킬 작성·수정·평가를 안내하는 명시 호출 전용 스킬. | anthropic-skills · 명시 호출 전용. 설치 파일 확인·현재 세션 비노출. 명시 호출 전용이며 실제 실행 조건을 상세 안내에서 확인한다. |
| [claude-automation-recommender](claude-code-setup/README.md#claude-automation-recommender). | 코드베이스를 분석해 맞춤형 Claude Code 자동화(훅·서브에이전트·스킬·플러그인·MCP 서버)를 추천하는 스킬. | claude-code-setup · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [skill-gen](firecrawl/README.md#skill-gen). | Firecrawl로 문서 URL을 스크래핑해 완전한 Agent Skill을 자동 생성하는 슬래시 명령어. | firecrawl · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [agent-development](plugin-dev/README.md#agent-development). | Claude Code 플러그인용 서브에이전트의 구조·시스템 프롬프트·트리거 조건 설계를 안내하는 스킬. | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [command-development](plugin-dev/README.md#command-development). | Claude Code 슬래시 명령의 구조·YAML frontmatter·동적 인자·사용자 인터랙션 패턴을 안내하는 스킬. | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [create-plugin](plugin-dev/README.md#create-plugin). | 컴포넌트 설계·구현·검증을 아우르는, 가이드형 엔드투엔드 Claude Code 플러그인 생성 워크플로 (슬래시 명령). | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [hook-development](plugin-dev/README.md#hook-development). | Claude Code 플러그인의 이벤트 기반 훅을 생성·구현하는 스킬 (프롬프트 기반 훅 API 중심). | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [mcp-integration](plugin-dev/README.md#mcp-integration). | Claude Code 플러그인에 Model Context Protocol(MCP) 서버를 통합해 외부 도구·서비스를 연동하는 스킬. | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [plugin-settings](plugin-dev/README.md#plugin-settings). | `.claude/plugin-name.local.md` 패턴으로 플러그인별 설정·상태를 YAML frontmatter와 마크다운으로 저장하는 스킬. | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [plugin-structure](plugin-dev/README.md#plugin-structure). | Claude Code 플러그인의 디렉터리 레이아웃·매니페스트·컴포넌트 구성·자동 발견을 안내하는 스킬. | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [skill-development](plugin-dev/README.md#skill-development). | Claude Code 플러그인용 스킬의 구조·점진적 공개·작성 스타일 베스트 프랙티스를 안내하는 스킬. | plugin-dev · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [skill-creator](skill-creator/README.md#skill-creator). | 새 스킬을 만들고, 기존 스킬을 수정·개선하며, eval로 성능을 측정·최적화하는 메타 스킬. | skill-creator · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [writing-skills](superpowers/README.md#writing-skills). | 재사용 스킬의 설명·형태·실제 준수를 기준선과 비교해 검증하는 스킬 작성 절차. | superpowers · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [claude-api](../Owned-Skills/claude-api/SKILL.md). | Claude API·SDK·Agent SDK의 구현과 공식 사용 조건을 확인한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [coplay-funplay-unity-mcp-setup](../Owned-Skills/coplay-funplay-unity-mcp-setup/SKILL.md). | Coplay·Funplay Unity MCP의 설치·초기 연결·재연결을 수행한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [new-sdk-app](../Owned-Skills/new-sdk-app/SKILL.md). | Python 또는 TypeScript의 Claude Agent SDK 앱을 준비하고 실행을 검증한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |

<a id="task-environment"></a>
## 환경 설정·세션·반복 작업.

시스템 안내·지침·인수인계·자동화·반복을 찾는다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| 프로젝트 지침 초기화와 환경 설정. | [init · 자체 제작](../Owned-Skills/init/SKILL.md), [update-config · 자체 제작](../Owned-Skills/update-config/SKILL.md). | 기존 개인 지침·설정을 보존한다. |
| 읽기 전용 승인 반복 줄이기·단축키 설정. | [fewer-permission-prompts · 자체 제작](../Owned-Skills/fewer-permission-prompts/SKILL.md), [keybindings-help · 자체 제작](../Owned-Skills/keybindings-help/SKILL.md). | 실제 클라이언트의 권한·단축키 지원을 확인한다. |
| 다음 세션에 작업 인수인계. | [handover · 개인 분류 설명](_personal/README.md#handover). | 프로젝트·현재 상태·미완료·재개 근거를 남긴다. |
| 세션 목록 정리. | [delete-session · 자체 제작](../Owned-Skills/delete-session/SKILL.md). | 실제 대상과 보관·제거 범위를 확인한다. |
| 현재 세션 반복·Ralph 작업. | [loop · 자체 제작](../Owned-Skills/loop/SKILL.md), [ralph-loop · 자체 제작](../Owned-Skills/ralph-loop/SKILL.md), [cancel-ralph · 자체 제작](../Owned-Skills/cancel-ralph/SKILL.md). | 승인된 반복 범위·완료·취소 조건을 확인한다. |
| 클라우드 에이전트 예약. | [schedule · 내장 분류 설명](_builtin/README.md#schedule). | 현재 호스트의 실제 예약 기능과 권한을 확인한다. 로컬 반복과 구분한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [pages:manage-schedules](codex-plugins/README.md#pages-manage-schedules). | Space 페이지와 예약을 검토하고 반복 자동화를 관리한다. | ChatGPT Pages · 조사 세션 노출. 대상 Space 페이지와 기존 예약을 먼저 읽고 변경 범위를 확인한다. |
| [openai-docs](codex-local/README.md#codex-system-openai-docs). | Codex·OpenAI API·ChatGPT Work의 사용법과 설정 자료를 확인한다. | Codex 시스템 스킬 · 조사 세션 노출. OpenAI·Codex 관련 질문에 사용하며 일반 소프트웨어 작업과 구분한다. |
| [migrate-to-codex](codex-local/README.md#codex-user-migrate-to-codex). | 다른 도구의 지침·스킬·에이전트·MCP 설정을 Codex 형식으로 이전한다. | Codex 이전 도구 · 조사 세션 노출. 선택된 대상만 변환하고 원본 Claude 설정·인증 정보·관련 없는 파일은 보존한다. |
| [data-analytics:schedule-refresh-jobs](codex-plugins/README.md#data-analytics-schedule-refresh-jobs). | 기존 Data 산출물의 반복 갱신 클라우드 작업을 설정한다. | Data Analytics · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다. |
| [computer-use:computer-use](codex-plugins/README.md#computer-use-computer-use). | 사용자 컴퓨터의 Windows 앱을 화면 기반으로 조작한다. | OpenAI Computer Use · 조사 세션 노출. 사용자가 지정한 앱·브라우저와 현재 가용 도구를 확인한다. |
| [paseo](codex-local/README.md#user-paseo). | Paseo의 호스트·프로젝트·작업 공간·에이전트·스케줄을 관리한다. | Paseo 스킬 · 조사 세션 노출. Paseo MCP 또는 CLI의 실제 가용성과 대상 작업 공간을 확인한다. |
| [paseo-handoff](codex-local/README.md#user-paseo-handoff). | 현재 작업의 문맥을 다른 에이전트에게 인계한다. | Paseo 스킬 · 조사 세션 노출. 다른 에이전트로 작업을 넘기라는 요청과 실제 인계 기능을 확인한다. |
| [paseo-help](codex-local/README.md#user-paseo-help). | Paseo의 사용법·설정·연결·로그 문제를 설명한다. | Paseo 스킬 · 조사 세션 노출. Paseo 제품 질문에 사용하며 에이전트·작업 공간 조작은 paseo와 구분한다. |
| [plugin-management:plugin-management](codex-plugins/README.md#plugin-management-plugin-management). | 관련 플러그인을 찾고 권한·의존성·연결·제거를 관리한다. | Plugin Management · 조사 세션 노출. 관련 플러그인·권한·연결 요청을 확인한다. 제거는 명시적인 제거 의도가 있어야 한다. |
| [fewer-permission-prompts](_builtin/README.md#fewer-permission-prompts). | 트랜스크립트에서 자주 쓴 **read-only Bash·MCP 호출**을 스캔해, 프로젝트 `settings.json`에 우선순위 allowlist를 추가함으로써 권한 프롬프트를 줄이는 빌트인 스킬. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [init](_builtin/README.md#init). | 코드베이스를 분석해 **CLAUDE.md를 생성/초기화**하는 빌트인 명령. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [keybindings-help](_builtin/README.md#keybindings-help). | `~/.claude/keybindings.json`을 편집해 Claude Code의 키보드 단축키를 커스터마이즈하는 빌트인 스킬. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [loop](_builtin/README.md#loop). | 프롬프트나 슬래시 명령을 **주기적으로 반복 실행**하는 빌트인 스킬. 인터벌을 주면 그 간격으로, 생략하면 모델이 스스로 페이스를 정해 반복한다. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [schedule](_builtin/README.md#schedule). | **cron 스케줄로 도는 클라우드 에이전트(routines)**를 생성·수정·목록·실행하는 빌트인 스킬. 1회성 예약 실행도 지원. | _builtin · 조사 세션 노출. 현재 호스트의 실제 클라우드 예약 도구·권한을 별도로 확인한다. |
| [update-config](_builtin/README.md#update-config). | `settings.json` / `settings.local.json`을 직접 편집해 Claude Code 하네스(harness)를 설정하는 빌트인 스킬. 권한·환경변수·hook·자동 동작을 다룬다. | _builtin · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [configure](_disabled/hookify/README.md#configure). | 기존 hookify 규칙을 인터랙티브하게 활성/비활성 토글하는 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [help](_disabled/hookify/README.md#help). | hookify 플러그인의 동작 원리와 사용법을 설명하는 도움말 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [hookify](_disabled/hookify/README.md#hookify). | 대화 분석이나 명시적 지시로부터 원치 않는 행동을 막는 hookify 규칙을 생성하는 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [list](_disabled/hookify/README.md#list). | 프로젝트에 설정된 모든 hookify 규칙을 표와 미리보기로 나열하는 커맨드. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [writing-rules](_disabled/hookify/README.md#writing-rules). | hookify 규칙 파일(`.claude/hookify.*.local.md`)의 작성 문법과 패턴을 안내하는 스킬. | _disabled/hookify · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [delete-session](_personal/README.md#delete-session). | 현재 프로젝트의 **세션 목록을 보여주고**, 선택한 세션의 `jsonl` 파일을 삭제해 resume 리스트에서 제거하는 개인 글로벌 스킬. | _personal · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [handover](_personal/README.md#handover). | 현재 세션 전체 내용을 **다음 세션 인수인계용 md 파일**로 정리·저장하는 개인 글로벌 스킬. | _personal · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [anthropic-academy-guide](anthropic-skills/README.md#anthropic-academy-guide). | Claude 사용 목적에 맞는 Academy 과정·튜토리얼을 찾는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [claude-automation-recommender](claude-code-setup/README.md#claude-automation-recommender). | 코드베이스를 분석해 맞춤형 Claude Code 자동화(훅·서브에이전트·스킬·플러그인·MCP 서버)를 추천하는 스킬. | claude-code-setup · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [claude-md-improver](claude-md-management/README.md#claude-md-improver). | 저장소의 CLAUDE.md 파일들을 감사·평가하고 타겟 개선을 수행하는 스킬. | claude-md-management · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [revise-claude-md](claude-md-management/README.md#revise-claude-md). | 현재 세션에서 얻은 학습 내용을 CLAUDE.md에 반영해 업데이트하는 슬래시 명령. | claude-md-management · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [firecrawl-monitor](firecrawl/README.md#firecrawl-monitor). | 웹사이트 콘텐츠 변경을 감지해 웹훅/이메일로 알려주는 스킬 — cron·스크래퍼·diff 스크립트 불필요. | firecrawl · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [cancel-ralph](ralph-loop/README.md#cancel-ralph). | 활성화된 Ralph 루프의 상태 파일을 제거해 루프를 취소하는 명령어. | ralph-loop · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [help](ralph-loop/README.md#help). | Ralph Loop 플러그인의 개념·명령어·핵심 메커니즘을 사용자에게 설명하는 도움말 명령어. | ralph-loop · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [ralph-loop](ralph-loop/README.md#ralph-loop). | 같은 프롬프트를 Stop 훅으로 반복 주입해 현재 세션 안에서 자기참조 반복 개발 루프(Ralph Wiggum 기법)를 시작하는 명령어. | ralph-loop · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [source-command-delete-session](codex-local/README.md#user-source-command-delete-session). | 현재 프로젝트의 세션 목록과 선택한 종료 세션의 제거를 다룬다. | 원본 명령의 전역 변환본 · 조사 세션 노출. delete-session 자체 제작 패키지와 별개인 원본 명령 변환본이며 실제 대상 확인이 필요하다. |
| [source-command-handover](codex-local/README.md#user-source-command-handover). | 현재 세션을 다음 작업자가 이어갈 인수인계 문서로 정리한다. | 원본 명령의 전역 변환본 · 조사 세션 노출. handover 자체 제작 패키지와 별개인 원본 명령 변환본이며 비공개 내용을 확인한다. |
| [cancel-ralph](../Owned-Skills/cancel-ralph/SKILL.md). | 사용자가 요청한 현재 Ralph 반복 작업을 취소한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [delete-session](../Owned-Skills/delete-session/SKILL.md). | 현재 프로젝트의 세션 목록을 확인하고 승인된 종료 세션을 보관·제거한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [fewer-permission-prompts](../Owned-Skills/fewer-permission-prompts/SKILL.md). | 반복되는 읽기 전용 승인에서 좁은 허용 규칙 후보를 찾는다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [handover](../Owned-Skills/handover/SKILL.md). | 다음 세션이 작업을 이어갈 수 있도록 근거와 재개 방법을 문서로 남긴다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [help](../Owned-Skills/help/SKILL.md). | Ralph Loop의 개념·옵션·완료 신호와 취소 방법을 설명한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [init](../Owned-Skills/init/SKILL.md). | 코드베이스를 근거로 프로젝트 AGENTS.md·CLAUDE.md 초기 지침을 작성한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [keybindings-help](../Owned-Skills/keybindings-help/SKILL.md). | Claude Code 터미널 단축키 재할당·해제·설정 오류를 다룬다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [loop](../Owned-Skills/loop/SKILL.md). | 현재 세션에서 승인된 작업이나 상태 조회를 일정 간격으로 반복한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [ralph-loop](../Owned-Skills/ralph-loop/SKILL.md). | 명시적으로 요청한 Ralph 방식의 검증 가능한 개발 작업을 제한된 세션에서 반복한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |
| [update-config](../Owned-Skills/update-config/SKILL.md). | 지정한 클라이언트의 환경·권한·hook·동작 설정을 변경하거나 진단한다. | 자체 제작 공개 패키지 · 조사 세션 노출. 설치된 자체 제작 구현을 사용하며 실제 입력·호스트·도구 조건과 검증 절차를 확인한다. |

<a id="task-knowledge-management"></a>
## 지식 관리·협업·Notion·Pages.

위키·프로젝트·회의·학습 자료와 페이지를 정리한다.

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [pages:maintain-space](codex-plugins/README.md#pages-maintain-space). | 새 근거를 기존 ChatGPT Pages·Space 내용에 반영해 유지한다. | ChatGPT Pages · 조사 세션 노출. 기존 페이지·공간의 근거 반영과 유지 요청에 사용한다. |
| [pages:manage-schedules](codex-plugins/README.md#pages-manage-schedules). | Space 페이지와 예약을 검토하고 반복 자동화를 관리한다. | ChatGPT Pages · 조사 세션 노출. 대상 Space 페이지와 기존 예약을 먼저 읽고 변경 범위를 확인한다. |
| [pages:organize-space](codex-plugins/README.md#pages-organize-space). | 기존 ChatGPT Pages·Space의 구조와 배치를 정리한다. | ChatGPT Pages · 조사 세션 노출. 기존 페이지·공간의 구조 정리 요청에 사용한다. |
| [pages:write-page](codex-plugins/README.md#pages-write-page). | 요청한 ChatGPT Page·Space 내용을 작성·편집한다. | ChatGPT Pages · 조사 세션 노출. Page·Space 저장 또는 내용 편집 의도가 있는 경우에 사용한다. |
| [notion:notion-build-my-engineering-wiki](codex-plugins/README.md#notion-notion-build-my-engineering-wiki). | 기술 자료와 프로젝트 문맥을 Notion 엔지니어링 위키로 정리한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-create-my-team-handbook](codex-plugins/README.md#notion-notion-create-my-team-handbook). | 흩어진 절차·문서를 Notion 팀 핸드북으로 구성한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-database-designer](codex-plugins/README.md#notion-notion-database-designer). | 반복 업무와 메모를 Notion 데이터베이스 추적기로 설계한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-knowledge-capture](codex-plugins/README.md#notion-notion-knowledge-capture). | 대화·메모를 Notion 지식 문서·FAQ·결정 기록으로 저장한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-meeting-prep](codex-plugins/README.md#notion-notion-meeting-prep). | Notion 문맥과 조사 근거로 회의 안건·사전 자료를 준비한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-organize-my-semester](codex-plugins/README.md#notion-notion-organize-my-semester). | 수업·과제·일정을 Notion 학기 관리 공간으로 정리한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-plan-marketing-campaigns](codex-plugins/README.md#notion-notion-plan-marketing-campaigns). | 캠페인 개요·콘텐츠·제작 업무를 Notion에서 정리한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-research-documentation](codex-plugins/README.md#notion-notion-research-documentation). | 여러 Notion 자료를 조사해 출처가 있는 설명·비교·보고서를 만든다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-set-up-my-project](codex-plugins/README.md#notion-notion-set-up-my-project). | Notion에 프로젝트 문서·업무·회의를 위한 초기 홈을 만든다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-setup](codex-plugins/README.md#notion-notion-setup). | Notion에서 선호·문맥을 보존하고 작업을 이어갈 초기 구성을 준비한다. | Notion · 조사 세션 노출. Notion 연결과 사용자 문맥 보존·초기 구성 목적을 확인한다. |
| [notion:notion-spec-to-implementation](codex-plugins/README.md#notion-notion-spec-to-implementation). | Notion 제품·기술 사양을 구현 계획과 연결된 업무로 바꾼다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [notion:notion-weekly-project-digest](codex-plugins/README.md#notion-notion-weekly-project-digest). | Notion 업무·결정·장애 근거를 비교해 주간 프로젝트 소식을 작성한다. | Notion · 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다. |
| [anthropic-internal-comms](anthropic-skills/README.md#anthropic-internal-comms). | 상태 보고·사내 공지 등 내부 커뮤니케이션 문서를 작성하는 스킬. | anthropic-skills · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |
| [figma-generate-project-plan](figma/README.md#figma-generate-project-plan). | PRD(+선택적 코드베이스 컨텍스트)를 **FigJam 프로젝트 플랜 보드**로 변환하는 인터랙티브 워크플로 스킬. 섹션 후보 제안 → 사용자 선택 → 섹션별 콘텐츠·블록 확정 → FigJam 생성까지 단계마다 확인을 거친다. | figma · 기존 배포 설명. 현재 호스트의 실제 구현·노출·호출 조건을 확인한다. |
| [figma-use-figjam](figma/README.md#figma-use-figjam). | FigJam 컨텍스트에서 `use_figma` MCP 도구를 사용하기 위한 FigJam 특화 스킬. `figma-use`와 함께 사용. | figma · 조사 세션 노출. 현재 스킬 설명의 적용 조건과 실제 도구·인증 가용성을 확인한다. |

<a id="task-finance"></a>
## 금융·투자·재무 모델.

금융 라우터와 직접 비노출 전문 가이드를 구분한다.

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [investment-banking:buyer-investor-list](codex-plugins/README.md#investment-banking-buyer-investor-list). | 매수자·투자자·스폰서·대출자 후보를 근거에 따라 분류·우선순위화한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:capital-markets-issuance](codex-plugins/README.md#investment-banking-capital-markets-issuance). | 증자·채권·차환·자금 조달과 발행 대안을 분석한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:cim-builder](codex-plugins/README.md#investment-banking-cim-builder). | 거래 마케팅용 CIM·티저·경영진 발표 서사를 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:cim-teardown](codex-plugins/README.md#investment-banking-cim-teardown). | CIM·티저·실사 자료의 주장과 근거를 검토한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:company-tearsheet](codex-plugins/README.md#investment-banking-company-tearsheet). | 기업의 신원·사업·재무·시장 사실을 출처와 함께 요약한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:comps-valuation](codex-plugins/README.md#investment-banking-comps-valuation). | 비교 기업·거래와 배수에 근거한 가치평가를 수행한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:covenant-package-analyzer](codex-plugins/README.md#investment-banking-covenant-package-analyzer). | 채무약정 정의·제약·여유·변경 가능성을 분석한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:dcf-model-builder](codex-plugins/README.md#investment-banking-dcf-model-builder). | 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:deal-process-tracker](codex-plugins/README.md#investment-banking-deal-process-tracker). | NDA·입찰·실사·마감 등 거래 진행 상태를 추적한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:distressed-recovery-waterfall](codex-plugins/README.md#investment-banking-distressed-recovery-waterfall). | 부실 자본구조·채권자 순위·회수금 배분을 분석한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:financials-normalizer](codex-plugins/README.md#investment-banking-financials-normalizer). | 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:ib-deck-qc](codex-plugins/README.md#investment-banking-ib-deck-qc). | 거래 자문 발표자료의 출처·모델·일관성과 배포 준비 상태를 점검한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:investment-banking](codex-plugins/README.md#investment-banking-investment-banking). | 거래·자금 조달·실사·가치평가 등 투자은행 작업을 전문 스킬로 연결한다. | Investment Banking · 조사 세션 노출. 투자은행 거래·발행·실사·자문 맥락 또는 명시 호출이 필요하며 전문 원문을 읽고 연결한다. |
| [investment-banking:lbo-model-build](codex-plugins/README.md#investment-banking-lbo-model-build). | 인수 자금 조달·차입·수익률·회수 민감도를 포함한 LBO 모델을 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:meeting-prep](codex-plugins/README.md#investment-banking-meeting-prep). | 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:memo-builder](codex-plugins/README.md#investment-banking-memo-builder). | 분석 담당 스킬의 결과를 의사결정 메모로 종합한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:merger-model-builder](codex-plugins/README.md#investment-banking-merger-model-builder). | 합병의 주당이익·구매회계·시너지·교환비율과 통합 재무를 모델링한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:model-audit-tieout](codex-plugins/README.md#investment-banking-model-audit-tieout). | 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:pitch-deck-builder](codex-plugins/README.md#investment-banking-pitch-deck-builder). | 거래·이사회·위원회용 피치덱의 이야기·페이지 계획·근거를 구성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:private-credit-underwriting](codex-plugins/README.md#investment-banking-private-credit-underwriting). | 차입자 신용·담보·부채 수용력·하방 시나리오를 심사한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:scenario-sensitivity-generator](codex-plugins/README.md#investment-banking-scenario-sensitivity-generator). | 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:three-statement-model-builder](codex-plugins/README.md#investment-banking-three-statement-model-builder). | 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [investment-banking:user-context](codex-plugins/README.md#investment-banking-user-context). | 해당 금융 플러그인의 저장 선호·자료 설정·문맥을 관리한다. | Investment Banking · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:catalyst-calendar](codex-plugins/README.md#public-equity-investing-catalyst-calendar). | 주가 촉매의 일정·확인 상태·투자 영향을 관리한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:company-tearsheet](codex-plugins/README.md#public-equity-investing-company-tearsheet). | 기업의 신원·사업·재무·시장 사실을 출처와 함께 요약한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:comps-valuation](codex-plugins/README.md#public-equity-investing-comps-valuation). | 비교 기업·거래와 배수에 근거한 가치평가를 수행한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:dcf-model-builder](codex-plugins/README.md#public-equity-investing-dcf-model-builder). | 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:deck-report-qc](codex-plugins/README.md#public-equity-investing-deck-report-qc). | 투자 발표자료·보고서의 출처·모델·글쓰기 일관성을 점검한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:earnings-deep-dive](codex-plugins/README.md#public-equity-investing-earnings-deep-dive). | 발표 실적·가이던스·경영진 발언이 투자 논지에 미치는 영향을 분석한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:earnings-preview](codex-plugins/README.md#public-equity-investing-earnings-preview). | 실적 발표 전 기대·컨센서스·지표·시나리오를 정리한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:economic-impact-report](codex-plugins/README.md#public-equity-investing-economic-impact-report). | 거시·정책·원자재·금리·환율 변화의 상장주식 영향을 분석한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:equity-model-update](codex-plugins/README.md#public-equity-investing-equity-model-update). | 기존 주식 투자 모델의 실적·가이던스·가정·수식을 갱신한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:event-driven-analyzer](codex-plugins/README.md#public-equity-investing-event-driven-analyzer). | 합병·규제·특수 상황의 확률·보상·시기·하방을 평가한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:financials-normalizer](codex-plugins/README.md#public-equity-investing-financials-normalizer). | 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:idea-generation](codex-plugins/README.md#public-equity-investing-idea-generation). | 투자 유니버스·테마·관심 종목에서 조사 후보를 발굴한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:initiating-coverage](codex-plugins/README.md#public-equity-investing-initiating-coverage). | 투자 논지·위험·목표주가·가치평가를 갖춘 최초 분석 보고서를 작성한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:long-short-pitch](codex-plugins/README.md#public-equity-investing-long-short-pitch). | 롱·숏·페어 투자 논지와 촉매·위험·진입·청산 조건을 구성한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:meeting-prep](codex-plugins/README.md#public-equity-investing-meeting-prep). | 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:memo-builder](codex-plugins/README.md#public-equity-investing-memo-builder). | 분석 담당 스킬의 결과를 의사결정 메모로 종합한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:model-audit-tieout](codex-plugins/README.md#public-equity-investing-model-audit-tieout). | 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:portfolio-risk-management](codex-plugins/README.md#public-equity-investing-portfolio-risk-management). | 포지션 크기·추가·축소·헤지·위험 예산과 운용 조치를 분석한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:public-equity-investing](codex-plugins/README.md#public-equity-investing-public-equity-investing). | 상장주식의 기업·실적·가치평가·포트폴리오 작업을 전문 스킬로 연결한다. | Public Equity Investing · 조사 세션 노출. 상장주식 투자·기업·실적·가치평가·모델 맥락 또는 명시 호출이 필요하며 전문 원문을 읽고 연결한다. |
| [public-equity-investing:scenario-sensitivity-generator](codex-plugins/README.md#public-equity-investing-scenario-sensitivity-generator). | 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:thesis-tracker](codex-plugins/README.md#public-equity-investing-thesis-tracker). | 투자 논지·촉매·반증 조건과 검토 주기를 추적한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:three-statement-model-builder](codex-plugins/README.md#public-equity-investing-three-statement-model-builder). | 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |
| [public-equity-investing:user-context](codex-plugins/README.md#public-equity-investing-user-context). | 해당 금융 플러그인의 저장 선호·자료 설정·문맥을 관리한다. | Public Equity Investing · 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다. |

<a id="task-music"></a>
## 음악·팟캐스트·Spotify.

검색·추천·컬렉션·재생 확인·라이브러리 작업을 찾는다.

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [app-68de829bf7648191acd70a907364c67c:browse-collections](codex-plugins/README.md#spotify-browse-collections). | URI가 있는 Spotify 재생목록·앨범·팟캐스트의 내용을 조회한다. | Spotify · 조사 세션 노출. 조회할 Spotify URI가 이미 있는 경우에 사용한다. |
| [app-68de829bf7648191acd70a907364c67c:build-playlists](codex-plugins/README.md#spotify-build-playlists). | 사용자 요청에 따라 Spotify 재생목록을 생성·편집한다. | Spotify · 조사 세션 노출. 재생목록 생성·편집을 명시적으로 요청한 경우에 사용한다. |
| [app-68de829bf7648191acd70a907364c67c:manage-library](codex-plugins/README.md#spotify-manage-library). | Spotify 콘텐츠 저장·좋아요·팔로우 등 라이브러리를 관리한다. | Spotify · 조사 세션 노출. 저장·좋아요·팔로우 등 라이브러리 변경을 명시적으로 요청한 경우에 사용한다. |
| [app-68de829bf7648191acd70a907364c67c:now-playing](codex-plugins/README.md#spotify-now-playing). | 현재 Spotify에서 재생 중인 콘텐츠를 확인한다. | Spotify · 조사 세션 노출. 현재 재생 중인 콘텐츠를 사용자가 직접 물을 때만 사용한다. |
| [app-68de829bf7648191acd70a907364c67c:search-spotify](codex-plugins/README.md#spotify-search-spotify). | Spotify 음악·팟캐스트·오디오북을 찾고 추천한다. | Spotify · 조사 세션 노출. 발견·추천·제목 검색 요청에 사용하며 Spotify 도구와 계정 상태를 확인한다. |

<a id="task-deployment"></a>
## 배포·인프라.

배포·DB·호스팅 운영과 작성 당시 비활성 설명을 구분한다.

기존 `_disabled` 항목은 **작성 당시 비활성** 설명이다. 현재 설치·활성·인증을 별도 확인한다.

### 빠른 선택.

| 하려는 작업 | 도구와 상세 안내 | 선택·호출 조건 |
|---|---|---|
| Vercel 배포·상태 확인. | [deploy](_disabled/vercel/README.md#deploy), [status](_disabled/vercel/README.md#status). | 조회와 배포를 구분하고 배포 대상·승인 범위를 확인한다. |
| Railway 앱·DB·호스팅 운영. | [use-railway](_disabled/railway/README.md#use-railway). | 실제 CLI·계정·프로젝트와 변경 권한을 확인한다. |
| Neon 데이터베이스 운영·전송량 조사. | [neon-postgres](_disabled/neon/README.md#neon-postgres), [neon-postgres-egress-optimizer](_disabled/neon/README.md#neon-postgres-egress-optimizer). | 원문·연결·인증 조건을 상세 안내에서 확인한다. |

### 이 분야의 전체 목록.

| 스킬·설명과 상세 안내 | 역할 | 출처·호출 조건 |
|---|---|---|
| [neon-postgres](_disabled/neon/README.md#neon-postgres). | Neon 서버리스 Postgres 프로젝트와 데이터베이스를 관리하는 에이전트 스킬 (Neon MCP 서버와 연계). | _disabled/neon · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [neon-postgres-egress-optimizer](_disabled/neon/README.md#neon-postgres-egress-optimizer). | Neon Postgres의 데이터 송신(egress) 비용/트래픽을 최적화하는 에이전트 스킬 (neon 플러그인 동봉). | _disabled/neon · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [use-railway](_disabled/railway/README.md#use-railway). | Railway 인프라(계정 가입/로그인, 프로젝트·서비스·DB·버킷 생성, 배포, 환경/변수, 도메인, 장애 진단, 메트릭, 에이전트 도구 설정)를 CLI/MCP로 운영하는 스킬. | _disabled/railway · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [_conventions](_disabled/vercel/README.md#_conventions). | 이 플러그인의 모든 슬래시 커맨드가 따르는 일관된 구조를 정의하는 메타 문서. 사용자가 직접 호출하는 커맨드가 아님. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-agents](_disabled/vercel/README.md#benchmark-agents). | vercel-plugin의 스킬 주입을 고난도 AI 시스템 시나리오로 스트레스 테스트하는 내부 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-e2e](_disabled/vercel/README.md#benchmark-e2e). | vercel-plugin을 현실적 프로젝트로 돌려 스킬 주입·dev 서버 기동·검증·개선 리포트를 한 번에 생성하는 내부 E2E 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-sandbox](_disabled/vercel/README.md#benchmark-sandbox). | 로컬 WezTerm 대신 Vercel Sandbox(원격 microVM)에서 eval 시나리오를 돌리는 내부 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [benchmark-testing](_disabled/vercel/README.md#benchmark-testing). | 현실적·기술명 비공개 프롬프트로 vercel-plugin 스킬 주입을 시험할 격리 테스트 프로젝트를 만드는 내부 벤치마크 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [bootstrap](_disabled/vercel/README.md#bootstrap). | Vercel 연동 리소스로 저장소를 부트스트랩 — 사전 점검, 통합 프로비저닝, env 키 검증 후 db/dev 시작 명령을 안전하게 실행. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [deploy](_disabled/vercel/README.md#deploy). | 현재 프로젝트를 Vercel에 배포 — 사전 안전 점검, 프로덕션 명시 확인, 배포 후 검증 포함. 인자로 "prod"/"production" 전달 시 프로덕션 배포. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [env](_disabled/vercel/README.md#env). | Vercel 환경 변수 관리 — list, pull, add, remove, diff. Vercel과 로컬 개발 환경 간 env 변수 동기화. 시크릿 값은 절대 출력하지 않음. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [marketplace](_disabled/vercel/README.md#marketplace). | Vercel Marketplace 통합 발견·설치 — 데이터베이스, CMS, 인증, 결제, 옵저버빌리티 등 서비스를 가이드 셋업과 로컬 검증으로 추가. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [plugin-audit](_disabled/vercel/README.md#plugin-audit). | 실제 Claude Code 세션 로그를 분석해 vercel-plugin 스킬 주입 성능과 패턴 커버리지 갭을 진단하는 내부 감사 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [release](_disabled/vercel/README.md#release). | vercel-plugin을 릴리스 — 게이트 실행, 버전 범프, 아티팩트 생성, 커밋, 푸시까지 처리하는 내부 릴리스 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [status](_disabled/vercel/README.md#status). | 현재 Vercel 프로젝트의 상태 진단(Doctor) — 최근 배포, 링크 정보, env 개요, 도메인, 빌드 상태, 옵저버빌리티 점검. 읽기 전용. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |
| [vercel-plugin-eval](_disabled/vercel/README.md#vercel-plugin-eval). | 실제 Claude Code 세션을 띄워 vercel-plugin의 훅 발화·스킬 주입·dedup 정확성·커버리지를 검증하는 내부 eval 스킬. | _disabled/vercel · 작성 당시 비활성. 현재 설치·활성·인증을 별도 확인한다. |

## 선택과 유지보수.

- 상세 설명·설치 명령·버전은 출처별 문서에서 관리한다. 같은 항목은 분야가 달라도 같은 상세 주소를 연결한다.
- 새 조사 항목은 등록 주소 또는 구체적 제외 사유를 남긴다. 새 등록 주소는 최소 한 분야에 연결하고 조사 증거의 분야 배치와 함께 검사한다.
- 기존 이름이 같아도 자체 제작·내장 설명·시스템 패키지·플러그인 구현은 출처로 구분한다. 현재 노출과 실행 성공을 혼동하지 않는다.
- 제목을 바꾸어도 기존 `task-*` 앵커를 보존한다. 캐시의 다른 버전과 의존성 내부 가이드를 독립 노출 스킬로 세지 않는다.
