<!-- 조사한 출처·노출·호출 조건을 설명 항목으로 보존한다. -->
# 현재 제공 플러그인 스킬과 전문 가이드.

조사 세션이 제공한 17개 플러그인의 선택된 버전에서 직접 패키지 108개를 확인했다. 이 중 59개는 세션 목록에 노출됐고, 49개는 직접 비노출이다. 금융 44개는 라우터가 읽는 전문 가이드이며 Data 5개는 명시 정책이 있는 부속 항목이다. 캐시의 다른 버전이나 node_modules 내부 파일은 합산하지 않았다. 아래 `제공자:이름`은 출처를 구분하는 표시이며 호스트에서의 호출 명령을 보장하지 않는다. [조사 증거](../../references/skill-inventory-2026-11-12.json)의 버전은 설치 패키지 식별자이며 원격 최신 버전이라는 뜻이 아니다. 설명·메타데이터만 기록하고 실행 원본·개인 캐시 경로는 포함하지 않는다.

## spreadsheets-excel-live-control

**spreadsheets:excel-live-control** — 연결 세션에서 열려 있는 Microsoft Excel 통합문서를 제어한다.

출처는 OpenAI Spreadsheets · 패키지 버전 `26.1111.10934`다. 조사 세션 노출. Excel 앱 태그 또는 이미 연결된 live Excel 작업이 전제다. 독립 파일 편집과 구분한다.

## spreadsheets-spreadsheets

**spreadsheets:Spreadsheets** — XLSX·XLS·CSV·TSV 파일과 Google Sheets 대상 스프레드시트를 작성·편집·분석한다.

출처는 OpenAI Spreadsheets · 패키지 버전 `26.1111.10934`다. 조사 세션 노출. 파일 또는 Google Sheets 대상 작업에 사용한다. 열려 있는 Excel 제어는 live 스킬로 연결한다.

## documents-documents

**documents:documents** — DOCX·Word·Google Docs 대상 문서를 작성·편집하고 렌더링으로 확인한다.

출처는 OpenAI Documents · 패키지 버전 `26.1111.10934`다. 조사 세션 노출. 요청한 문서 형식과 기존 문서·템플릿을 확인하고 최종 렌더를 검증한다.

## pdf-pdf

**pdf:pdf** — PDF를 읽고 작성·렌더링·검증하며 양식 작업을 지원한다.

출처는 OpenAI PDF · 패키지 버전 `26.1111.10934`다. 조사 세션 노출. PDF 내용·화면·양식 중 요청 범위를 확인하고 해당 결과를 검증한다.

## presentations-presentations

**presentations:Presentations** — 발표자료를 읽고 작성·편집하며 PPTX·Google Slides 등 출력 경로를 안내한다.

출처는 OpenAI Presentations · 패키지 버전 `26.1111.10934`다. 조사 세션 노출. 기존 덱·템플릿·목표 형식을 확인하고 산출물 경로와 렌더를 검증한다.

## template-creator-template-creator

**template-creator:template-creator** — 개인용 산출물 템플릿을 재사용 가능한 Codex 스킬로 작성·갱신한다.

출처는 OpenAI Template Creator · 패키지 버전 `26.1111.10934`다. 조사 세션 노출. 재사용 개인 산출물 템플릿 스킬을 만들거나 갱신하는 요청에 사용한다.

## computer-use-computer-use

**computer-use:computer-use** — 사용자 컴퓨터의 Windows 앱을 화면 기반으로 조작한다.

출처는 OpenAI Computer Use · 패키지 버전 `26.1103.60933`다. 조사 세션 노출. 사용자가 지정한 앱·브라우저와 현재 가용 도구를 확인한다.

## visualize-visualize

**visualize:visualize** — 대화 안에서 시각화와 상호작용 도구를 만든다.

출처는 OpenAI Visualize · 패키지 버전 `1.0.84`다. 조사 세션 노출. 대화 내 상호작용 시각화에 사용한다. 내보낼 정량 차트와 구분한다.

## spotify-browse-collections

**app-68de829bf7648191acd70a907364c67c:browse-collections** — URI가 있는 Spotify 재생목록·앨범·팟캐스트의 내용을 조회한다.

출처는 Spotify · 패키지 버전 `4.3.0`다. 조사 세션 노출. 조회할 Spotify URI가 이미 있는 경우에 사용한다.

## spotify-build-playlists

**app-68de829bf7648191acd70a907364c67c:build-playlists** — 사용자 요청에 따라 Spotify 재생목록을 생성·편집한다.

출처는 Spotify · 패키지 버전 `4.3.0`다. 조사 세션 노출. 재생목록 생성·편집을 명시적으로 요청한 경우에 사용한다.

## spotify-manage-library

**app-68de829bf7648191acd70a907364c67c:manage-library** — Spotify 콘텐츠 저장·좋아요·팔로우 등 라이브러리를 관리한다.

출처는 Spotify · 패키지 버전 `4.3.0`다. 조사 세션 노출. 저장·좋아요·팔로우 등 라이브러리 변경을 명시적으로 요청한 경우에 사용한다.

## spotify-now-playing

**app-68de829bf7648191acd70a907364c67c:now-playing** — 현재 Spotify에서 재생 중인 콘텐츠를 확인한다.

출처는 Spotify · 패키지 버전 `4.3.0`다. 조사 세션 노출. 현재 재생 중인 콘텐츠를 사용자가 직접 물을 때만 사용한다.

## spotify-search-spotify

**app-68de829bf7648191acd70a907364c67c:search-spotify** — Spotify 음악·팟캐스트·오디오북을 찾고 추천한다.

출처는 Spotify · 패키지 버전 `4.3.0`다. 조사 세션 노출. 발견·추천·제목 검색 요청에 사용하며 Spotify 도구와 계정 상태를 확인한다.

## data-analytics-analyze-data-quality

**data-analytics:analyze-data-quality** — 구조화 데이터의 누락·중복·조인·최신성 등 품질 위험을 조사한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-answers-follow-up

**data-analytics:answers-follow-up** — 분석 답변 다음에 유용한 후속 작업을 선택지로 제안한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 유용한 다음 작업이 있고 현재 호스트가 후속 선택지 UI를 지원할 때 사용한다.

## data-analytics-build-dashboard

**data-analytics:build-dashboard** — 데이터 출처에 근거한 탐색·모니터링용 상호작용 대시보드를 만든다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-build-report

**data-analytics:build-report** — 검토 가능한 근거를 갖춘 분석 보고서를 작성한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-convert-to-doc

**data-analytics:convert-to-doc** — 기존 Data 산출물을 DOCX·Google Docs 문서로 변환한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다.

## data-analytics-convert-to-slides

**data-analytics:convert-to-slides** — 기존 Data 산출물을 PowerPoint·Google Slides 발표자료로 변환한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다.

## data-analytics-customize-data-plugin

**data-analytics:customize-data-plugin** — 개인·팀의 데이터 작업 관례와 문맥을 재사용 스킬로 정리한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 사용자가 재사용 데이터 관례·문맥의 생성·변경을 요청한 경우에 사용한다.

## data-analytics-design-kpis

**data-analytics:design-kpis** — KPI 정의·목표·가드레일·측정 계획을 설계한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-index

**data-analytics:index** — 데이터·지표·분석 요청을 알맞은 Data 작업 흐름으로 연결한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 데이터·지표·분석 요청을 분류한다. 단순 글쓰기·일반 설명에 확대하지 않는다.

## data-analytics-jupyter-notebooks

**data-analytics:jupyter-notebooks** — 요청한 SQL·Python 노트북을 생성·편집·검증·내보낸다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 노트북 작업을 요청한 경우에 사용한다. 일반 분석에 불필요한 노트북을 만들지 않는다.

## data-analytics-kpi-reporting

**data-analytics:kpi-reporting** — KPI 성과·목표 대비 결과와 정기 운영 보고를 작성한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-market-sizing

**data-analytics:market-sizing** — 가정과 불확실성을 밝혀 시장·세그먼트·기회 규모를 추정한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-metric-diagnostics

**data-analytics:metric-diagnostics** — 지표 변화·이상·차이의 원인과 기여 요인을 진단한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-onboarding

**data-analytics:onboarding** — Data 연결·첫 작업·사용 시작을 안내한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. Data 사용 시작·연결·첫 작업 안내 요청에 사용한다.

## data-analytics-product-business-analysis

**data-analytics:product-business-analysis** — 제품·사업 의사결정에 필요한 데이터 분석을 수행한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-publish-artifact-to-sites

**data-analytics:publish-artifact-to-sites** — 기존 Data HTML 보고서·대시보드를 Sites에 게시한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 기존 Data HTML 산출물과 게시 요청 또는 해당 전달 정책이 있어야 한다.

## data-analytics-report-to-pdf

**data-analytics:report-to-pdf** — 기존 Data 보고서·대시보드를 PDF로 변환한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다.

## data-analytics-schedule-refresh-jobs

**data-analytics:schedule-refresh-jobs** — 기존 Data 산출물의 반복 갱신 클라우드 작업을 설정한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다.

## data-analytics-share-artifact-summary

**data-analytics:share-artifact-summary** — Data 보고서·대시보드·차트의 요약을 제공하거나 공유한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 미노출. 현재 번들에 파일이 있지만 직접 호출 가능 여부는 확인하지 않았다.

## data-analytics-validate-data

**data-analytics:validate-data** — 분석 방법·계산·시각화·결론과 보고서 완성도를 검증한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## data-analytics-visualize-data

**data-analytics:visualize-data** — 분석 산출물에 들어갈 정량 차트·그림을 제작·검증한다.

출처는 Data Analytics · 패키지 버전 `1.1.0-exp-homepage`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-build-my-engineering-wiki

**notion:notion-build-my-engineering-wiki** — 기술 자료와 프로젝트 문맥을 Notion 엔지니어링 위키로 정리한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-create-my-team-handbook

**notion:notion-create-my-team-handbook** — 흩어진 절차·문서를 Notion 팀 핸드북으로 구성한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-database-designer

**notion:notion-database-designer** — 반복 업무와 메모를 Notion 데이터베이스 추적기로 설계한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-knowledge-capture

**notion:notion-knowledge-capture** — 대화·메모를 Notion 지식 문서·FAQ·결정 기록으로 저장한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-meeting-prep

**notion:notion-meeting-prep** — Notion 문맥과 조사 근거로 회의 안건·사전 자료를 준비한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-organize-my-semester

**notion:notion-organize-my-semester** — 수업·과제·일정을 Notion 학기 관리 공간으로 정리한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-plan-marketing-campaigns

**notion:notion-plan-marketing-campaigns** — 캠페인 개요·콘텐츠·제작 업무를 Notion에서 정리한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-research-documentation

**notion:notion-research-documentation** — 여러 Notion 자료를 조사해 출처가 있는 설명·비교·보고서를 만든다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-set-up-my-project

**notion:notion-set-up-my-project** — Notion에 프로젝트 문서·업무·회의를 위한 초기 홈을 만든다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-setup

**notion:notion-setup** — Notion에서 선호·문맥을 보존하고 작업을 이어갈 초기 구성을 준비한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. Notion 연결과 사용자 문맥 보존·초기 구성 목적을 확인한다.

## notion-notion-spec-to-implementation

**notion:notion-spec-to-implementation** — Notion 제품·기술 사양을 구현 계획과 연결된 업무로 바꾼다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## notion-notion-weekly-project-digest

**notion:notion-weekly-project-digest** — Notion 업무·결정·장애 근거를 비교해 주간 프로젝트 소식을 작성한다.

출처는 Notion · 패키지 버전 `3.0.9`다. 조사 세션 노출. 현재 세션에 노출돼 있으며 작업 목적·입력 자료·출력 형식과 필요한 도구의 가용성을 확인한다.

## pages-maintain-space

**pages:maintain-space** — 새 근거를 기존 ChatGPT Pages·Space 내용에 반영해 유지한다.

출처는 ChatGPT Pages · 패키지 버전 `0.1.26`다. 조사 세션 노출. 기존 페이지·공간의 근거 반영과 유지 요청에 사용한다.

## pages-manage-schedules

**pages:manage-schedules** — Space 페이지와 예약을 검토하고 반복 자동화를 관리한다.

출처는 ChatGPT Pages · 패키지 버전 `0.1.26`다. 조사 세션 노출. 대상 Space 페이지와 기존 예약을 먼저 읽고 변경 범위를 확인한다.

## pages-organize-space

**pages:organize-space** — 기존 ChatGPT Pages·Space의 구조와 배치를 정리한다.

출처는 ChatGPT Pages · 패키지 버전 `0.1.26`다. 조사 세션 노출. 기존 페이지·공간의 구조 정리 요청에 사용한다.

## pages-write-page

**pages:write-page** — 요청한 ChatGPT Page·Space 내용을 작성·편집한다.

출처는 ChatGPT Pages · 패키지 버전 `0.1.26`다. 조사 세션 노출. Page·Space 저장 또는 내용 편집 의도가 있는 경우에 사용한다.

## sites-sites

**sites:sites** — 랜딩 페이지·대시보드·포털·내부 도구 등 웹사이트를 제작·수정한다.

출처는 Sites · 패키지 버전 `1.1.6`다. 조사 세션 노출. 사이트 제작·수정 요청과 대상 사이트·제공 기능을 확인한다.

## sites-sites-remix

**sites:sites-remix** — 지정된 기존 Sites 사이트를 바탕으로 새 사이트를 만든다.

출처는 Sites · 패키지 버전 `1.1.6`다. 조사 세션 노출. 원본 Sites 사이트가 특정되고 새 사이트로 리믹스하는 요청이 있어야 한다.

## work-pets-create-pet

**work-pets:create-pet** — ChatGPT Work용 애니메이션 펫을 제작·검증·미리보기·업로드한다.

출처는 ChatGPT Work Pets · 패키지 버전 `0.1.6`다. 조사 세션 노출. ChatGPT Work 펫 제작 맥락에 사용한다. 일반 이미지·실제 동물 요청과 구분한다.

## work-pets-pets

**work-pets:pets** — ChatGPT Work의 애니메이션 펫을 조회·선택·다운로드·삭제한다.

출처는 ChatGPT Work Pets · 패키지 버전 `0.1.6`다. 조사 세션 노출. ChatGPT Work 펫 관리의 명시적 맥락과 대상·변경 범위를 확인한다.

## work-pets-update-pet

**work-pets:update-pet** — ChatGPT Work 펫의 이름·설명·스프라이트 등 기존 구성을 갱신한다.

출처는 ChatGPT Work Pets · 패키지 버전 `0.1.6`다. 조사 세션 노출. ChatGPT Work의 기존 펫을 대상으로 원본과 변경 범위를 확인한다.

## investment-banking-buyer-investor-list

**investment-banking:buyer-investor-list** — 매수자·투자자·스폰서·대출자 후보를 근거에 따라 분류·우선순위화한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-capital-markets-issuance

**investment-banking:capital-markets-issuance** — 증자·채권·차환·자금 조달과 발행 대안을 분석한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-cim-builder

**investment-banking:cim-builder** — 거래 마케팅용 CIM·티저·경영진 발표 서사를 작성한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-cim-teardown

**investment-banking:cim-teardown** — CIM·티저·실사 자료의 주장과 근거를 검토한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-company-tearsheet

**investment-banking:company-tearsheet** — 기업의 신원·사업·재무·시장 사실을 출처와 함께 요약한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-comps-valuation

**investment-banking:comps-valuation** — 비교 기업·거래와 배수에 근거한 가치평가를 수행한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-covenant-package-analyzer

**investment-banking:covenant-package-analyzer** — 채무약정 정의·제약·여유·변경 가능성을 분석한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-dcf-model-builder

**investment-banking:dcf-model-builder** — 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-deal-process-tracker

**investment-banking:deal-process-tracker** — NDA·입찰·실사·마감 등 거래 진행 상태를 추적한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-distressed-recovery-waterfall

**investment-banking:distressed-recovery-waterfall** — 부실 자본구조·채권자 순위·회수금 배분을 분석한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-financials-normalizer

**investment-banking:financials-normalizer** — 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-ib-deck-qc

**investment-banking:ib-deck-qc** — 거래 자문 발표자료의 출처·모델·일관성과 배포 준비 상태를 점검한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-investment-banking

**investment-banking:investment-banking** — 거래·자금 조달·실사·가치평가 등 투자은행 작업을 전문 스킬로 연결한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 조사 세션 노출. 투자은행 거래·발행·실사·자문 맥락 또는 명시 호출이 필요하며 전문 원문을 읽고 연결한다.

## investment-banking-lbo-model-build

**investment-banking:lbo-model-build** — 인수 자금 조달·차입·수익률·회수 민감도를 포함한 LBO 모델을 작성한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-meeting-prep

**investment-banking:meeting-prep** — 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-memo-builder

**investment-banking:memo-builder** — 분석 담당 스킬의 결과를 의사결정 메모로 종합한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-merger-model-builder

**investment-banking:merger-model-builder** — 합병의 주당이익·구매회계·시너지·교환비율과 통합 재무를 모델링한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-model-audit-tieout

**investment-banking:model-audit-tieout** — 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-pitch-deck-builder

**investment-banking:pitch-deck-builder** — 거래·이사회·위원회용 피치덱의 이야기·페이지 계획·근거를 구성한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-private-credit-underwriting

**investment-banking:private-credit-underwriting** — 차입자 신용·담보·부채 수용력·하방 시나리오를 심사한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-scenario-sensitivity-generator

**investment-banking:scenario-sensitivity-generator** — 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-three-statement-model-builder

**investment-banking:three-statement-model-builder** — 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## investment-banking-user-context

**investment-banking:user-context** — 해당 금융 플러그인의 저장 선호·자료 설정·문맥을 관리한다.

출처는 Investment Banking · 패키지 버전 `0.1.29`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Investment Banking 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-catalyst-calendar

**public-equity-investing:catalyst-calendar** — 주가 촉매의 일정·확인 상태·투자 영향을 관리한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-company-tearsheet

**public-equity-investing:company-tearsheet** — 기업의 신원·사업·재무·시장 사실을 출처와 함께 요약한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-comps-valuation

**public-equity-investing:comps-valuation** — 비교 기업·거래와 배수에 근거한 가치평가를 수행한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-dcf-model-builder

**public-equity-investing:dcf-model-builder** — 가정·WACC·잔존가치·민감도를 포함한 DCF 모델을 작성한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-deck-report-qc

**public-equity-investing:deck-report-qc** — 투자 발표자료·보고서의 출처·모델·글쓰기 일관성을 점검한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-earnings-deep-dive

**public-equity-investing:earnings-deep-dive** — 발표 실적·가이던스·경영진 발언이 투자 논지에 미치는 영향을 분석한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-earnings-preview

**public-equity-investing:earnings-preview** — 실적 발표 전 기대·컨센서스·지표·시나리오를 정리한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-economic-impact-report

**public-equity-investing:economic-impact-report** — 거시·정책·원자재·금리·환율 변화의 상장주식 영향을 분석한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-equity-model-update

**public-equity-investing:equity-model-update** — 기존 주식 투자 모델의 실적·가이던스·가정·수식을 갱신한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-event-driven-analyzer

**public-equity-investing:event-driven-analyzer** — 합병·규제·특수 상황의 확률·보상·시기·하방을 평가한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-financials-normalizer

**public-equity-investing:financials-normalizer** — 원본 재무제표·지표를 출처가 있는 모델 입력 자료로 정규화한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-idea-generation

**public-equity-investing:idea-generation** — 투자 유니버스·테마·관심 종목에서 조사 후보를 발굴한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-initiating-coverage

**public-equity-investing:initiating-coverage** — 투자 논지·위험·목표주가·가치평가를 갖춘 최초 분석 보고서를 작성한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-long-short-pitch

**public-equity-investing:long-short-pitch** — 롱·숏·페어 투자 논지와 촉매·위험·진입·청산 조건을 구성한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-meeting-prep

**public-equity-investing:meeting-prep** — 업무 목적과 자료에 맞는 회의 브리프·질문·후속 계획을 준비한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-memo-builder

**public-equity-investing:memo-builder** — 분석 담당 스킬의 결과를 의사결정 메모로 종합한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-model-audit-tieout

**public-equity-investing:model-audit-tieout** — 재무모델의 수식·출처·정합성과 수정 필요 사항을 감사한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-portfolio-risk-management

**public-equity-investing:portfolio-risk-management** — 포지션 크기·추가·축소·헤지·위험 예산과 운용 조치를 분석한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-public-equity-investing

**public-equity-investing:public-equity-investing** — 상장주식의 기업·실적·가치평가·포트폴리오 작업을 전문 스킬로 연결한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 조사 세션 노출. 상장주식 투자·기업·실적·가치평가·모델 맥락 또는 명시 호출이 필요하며 전문 원문을 읽고 연결한다.

## public-equity-investing-scenario-sensitivity-generator

**public-equity-investing:scenario-sensitivity-generator** — 기본·상방·하방 가정과 민감도·의사결정 영향을 분석한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-thesis-tracker

**public-equity-investing:thesis-tracker** — 투자 논지·촉매·반증 조건과 검토 주기를 추적한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-three-statement-model-builder

**public-equity-investing:three-statement-model-builder** — 손익·재무상태·현금흐름을 연결한 재무예측 모델을 작성한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## public-equity-investing-user-context

**public-equity-investing:user-context** — 해당 금융 플러그인의 저장 선호·자료 설정·문맥을 관리한다.

출처는 Public Equity Investing · 패키지 버전 `0.1.31`다. 명시 호출 정책. 현재 세션 직접 비노출. 명시 호출 전용 정책·현재 세션 직접 미노출. Public Equity Investing 라우터가 해당 업무를 선택할 때 전문 원문을 읽고 사용하며 실행 도구·자료 가용성을 확인한다.

## plugin-management-plugin-management

**plugin-management:plugin-management** — 관련 플러그인을 찾고 권한·의존성·연결·제거를 관리한다.

출처는 Plugin Management · 패키지 버전 `0.1.0`다. 조사 세션 노출. 관련 플러그인·권한·연결 요청을 확인한다. 제거는 명시적인 제거 의도가 있어야 한다.

## ponytail-ponytail

**ponytail:ponytail** — 요청을 완결하는 최소 변경과 간결한 보고 원칙을 적용한다.

출처는 Ponytail · 패키지 버전 `5.3.3`다. 조사 세션 노출. 코딩 작업에 최소 완결 변경 원칙을 적용한다.

## ponytail-ponytail-audit

**ponytail:ponytail-audit** — 저장소 전체의 결함·보안·부하·테스트·불필요한 코드를 감사한다.

출처는 Ponytail · 패키지 버전 `5.3.3`다. 조사 세션 노출. 저장소 전체 감사를 요청한 경우에 조사하며 구현 범위와 구분한다.

## ponytail-ponytail-debt

**ponytail:ponytail-debt** — shortcut·ponytail 주석을 찾아 기술 부채 목록으로 보여준다.

출처는 Ponytail · 패키지 버전 `5.3.3`다. 조사 세션 노출. 부채 주석 목록을 읽기 전용으로 보여준다.

## ponytail-ponytail-gain

**ponytail:ponytail-gain** — Ponytail 벤치마크에 기록된 코드·비용·속도 절감 결과를 보여준다.

출처는 Ponytail · 패키지 버전 `5.3.3`다. 조사 세션 노출. 기록된 벤치마크를 표시하며 현재 작업의 새 절감 측정으로 주장하지 않는다.

## ponytail-ponytail-help

**ponytail:ponytail-help** — Ponytail 수준·스킬·명령의 사용법을 안내한다.

출처는 Ponytail · 패키지 버전 `5.3.3`다. 조사 세션 노출. Ponytail 사용법·수준·명령 질문에 사용한다.

## ponytail-ponytail-review

**ponytail:ponytail-review** — 코드 변경의 정확성·안전·부하·테스트·필요성을 검토한다.

출처는 Ponytail · 패키지 버전 `5.3.3`다. 조사 세션 노출. 변경 범위를 정하고 품질·안전·필요성을 검토한다.
