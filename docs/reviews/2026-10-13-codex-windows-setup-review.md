<!-- Windows Codex 세팅 안내 변경의 전체 리뷰와 검증 결과를 기록한다. -->
# Windows Codex 세팅 리뷰.

기준선은 1de591f83b252ec5ab9212c4f314517036f29b3d다. 승인된 안내 문서 7개와 설계·계획을 검토했다. 별도 스펙 리뷰 후 품질 리뷰를 수행했고 발견 사항 수정과 재리뷰가 통과했다.

## 해결한 발견 사항.

1. 확인한 CLI Source와 bare codex 호출이 달라 작업 폴더의 동명 파일이 실행될 수 있었다. 버전 검사와 생성·검증 인자 모두 확인된 CLI 전체 경로로 고정했다. 동명 cmd 파일의 실패 코드로 문제를 재현한 뒤 수정 후 통과를 확인했다.
2. 드라이브 루트의 끝 역슬래시가 WT의 닫는 따옴표를 이스케이프했다. WT 인자용 작업 폴더에 `\.`을 붙이고 COM WorkingDirectory는 원래 경로를 유지했다.
3. 경로 내 세미콜론이 WT 명령 분리자로 처리됐다. WT에 전달하는 작업 폴더·CLI 경로에 `\;` 이스케이프를 적용했다. 버전 검사는 WT를 거치지 않으므로 원래 Source를 사용한다.

인자 전달 검증은 [Microsoft Terminal 인자 파서](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/AppCommandlineArgs.cpp)와 [Commandline의 역변환](https://github.com/microsoft/terminal/blob/main/src/cascadia/TerminalApp/Commandline.cpp)을 확인한 뒤 Windows의 실제 argv 파싱과 숨긴 cmd 프로세스로 수행했다.

## 검증 결과.

- UTF-8·코드 펜스·로컬 링크·Markdown 및 HTML 앵커 검사 통과, 대상 7개 문서의 링크·앵커 81개 누락 0개다.
- PowerShell 예제 4개 구문 오류 0개다.
- 실제 Windows COM 생성·갱신·실패 검사 18건이 통과했다. 실제 바탕화면 바로가기의 해시와 기존 bat를 보존했다.
- 사용자 지정 폴더, 드라이브 루트, 공백·쉼표·작은따옴표·한글·세미콜론과 동명 CLI 사례를 확인했다. 인자 재구성 후 실제 Codex CLI 0.162.1 및 임시 CLI 실행이 통과했다.
- Chrome의 새 안내 배치와 링크를 확인했고 console warn/error는 0개다.
- git diff --check 통과, 스펙·품질 재리뷰의 미해결 고확신 발견 사항은 없다.

## 검증 범위.

별도 PC의 실제 OneDrive, Terminal GUI 새 탭·대화형 Codex 세션, 공식 아이콘 신규 다운로드·PNG 변환은 실행하지 않았다. 현재 전역 지침과 바탕화면은 변경하지 않았다. 실제 세팅 요청에서는 문서에 따라 새 세션·아이콘 출처를 확인하고 미검증 항목을 미완료로 보고한다.
