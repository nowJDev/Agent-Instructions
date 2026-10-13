<!-- 클라이언트별 최소 CLI 세팅 안내의 전체 리뷰와 검증 결과를 기록한다. -->
# 클라이언트별 최소 CLI 세팅 리뷰.

기준선은 dfac16764d14afce23fafd4a2a80fa6ad2ddabc1다. 승인된 안내 문서 10개와 설계·계획을 전체 검토했다. 별도 스펙 리뷰 후 품질 리뷰가 통과했으며 미해결 고확신 발견 사항은 없다. 독립 설치 프로그램을 추가하지 않고 기존 Codex 바로가기 예제를 공통 문서로 옮겨 Claude Code와 CMD 분기를 반영했다.

## 확인·해결한 사항.

- 명시 대상 우선, 신뢰할 수 있는 현재 세션의 클라이언트 정보와 판별 불가 시 한 번 질문 규칙을 모든 진입점에 맞췄다. 둘 다 설치돼 있어도 선택한 하나만 설정한다.
- 기존 전역 지침 백업·보존 병합, Claude import 중복 방지, 공식 아이콘, 실제 실행·지침 로드·인증과 미완료 보고를 확인했다. 기존 Codex 주소를 유지하고 Claude 확장은 명시적 추가 요청의 선택 항목으로 제한했다.
- 신규 공통 문서 일부가 작성 중 한글 인코딩을 잃어 UTF-8로 복구한 뒤 전체 인코딩·실행 검사를 다시 통과했다. 검증 도구의 횟수 집계 범위 오류도 수정하고 최종 횟수를 assert로 확인했다.
- 설치 명령은 [Codex 공식 원문](https://learn.chatgpt.com/docs/codex/cli.md), [Claude 공식 설치 안내](https://code.claude.com/docs/en/setup), 상대 import와 `/context`는 [Claude 공식 memory 문서](https://code.claude.com/docs/en/memory)로 대조했다. 실제 설치는 실행하지 않았다.

## 검증 결과.

- 구현 문서 10개 UTF-8·BOM 없음·코드 펜스·로컬 링크 및 앵커 94개 누락 0개다. 독립 품질 검사에서도 구현·과정 문서 12개 인코딩·펜스와 추가 내용의 시크릿 패턴 검사가 통과했다.
- GETTING_STARTED와 공통 바로가기의 PowerShell 블록 8개 파서 오류 0개다.
- Codex·Claude Code 각각 WT·CMD 4분기의 실제 Windows COM 생성·갱신·독립 속성 검증이 통과했다. 기본·사용자·드라이브 루트 작업 폴더와 실제 CLI·특수 경로 임시 CLI의 숨긴 실행 24회, 실패 조건 37개가 통과했다.
- CLI 버전은 Codex CLI 0.162.1과 Claude Code 2.1.181이다. 공백·쉼표·작은따옴표·한글·세미콜론·앰퍼샌드 경로와 동명 CLI를 확인했다. 확인된 Source 전체 경로가 실행되며 작업 폴더의 동명 CLI는 실행되지 않았다.
- 인자 검증은 Windows argv 파싱과 [Terminal 인자 파서](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/AppCommandlineArgs.cpp)·[역변환](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/Commandline.cpp)에 따른 숨긴 CMD 실행으로 수행했다. 실제 Terminal GUI 실행 증거와 구분한다.
- 기존 실제 Desktop 바로가기 해시와 임시 bat를 보존했다. Chrome에서 공통 요청과 두 클라이언트 결과 표를 확인했고 console warn/error는 0개다. 검증용 탭과 로컬 서버를 정리했다.
- 최종 관련 문서 13개의 인코딩·펜스·로컬 링크 및 앵커 95개 검사와 `git diff --check`가 통과했다. 스펙·품질 리뷰 PASS다.

## 검증 범위.

현재 PC의 CLI 설치·로그인·전역 지침·실제 Desktop을 변경하지 않았다. 실제 설치·인증 후 새 세션 지침 로드·대화형 CLI 실행·Terminal GUI·별도 PC의 OneDrive·공식 아이콘 신규 다운로드·PNG 변환은 미검증이다. ICO는 임시 fixture로 경로·속성을 검증했으며 Claude 공식 이미지 확인 증거가 아니다.

실제 사용자 세팅에서는 문서에 따라 공식 아이콘 출처·바로가기 실행·지침 로드·사용자 인증을 확인하고 남은 항목을 미완료로 보고해야 한다. 이번 완료 범위는 저장소 안내 구현과 위 검증이다.
