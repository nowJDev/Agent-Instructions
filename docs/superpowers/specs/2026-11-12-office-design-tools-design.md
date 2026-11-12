<!-- 요청한 세 도구의 전역 단일 설치와 공개 관리 경계를 정의한다. -->
# Office·디자인 도구 세 가지의 전역 설치.

## 요청과 범위.

사용자는 PPT Master·OfficeCLI·Huashu Design을 PC 사용자 전역과 Agent-Instructions에서 사용할 수 있게 설치하고 커밋·push하도록 요청했다. 이전 Anthropic 설치의 전역 단일 실행본·공개 관리 문서 분리를 이어간다. 아래 세부 방식은 기존 저장소 정책과 조사에 따른 구현 선택이다.

## 비교와 선택.

프로젝트마다 원본을 복사하면 중복·대형 자산·업데이트 불일치가 생긴다. 공식 일괄 설치는 다른 AI 클라이언트 스킬이나 MCP까지 변경할 수 있다. 따라서 고정 원본을 Codex 사용자 스킬 경로에 한 번 설치하고 실행 종속성은 비공개 사용자 도구 폴더에 격리한다. 이 공개 저장소에는 타사 원본을 넣지 않고 출처·버전·해시·설치 안내·검증 증거 요약만 관리한다.

## 책임과 설치 위치.

- `~/.agents/skills/ppt-master`에 공식 `skills/ppt-master` 전체를 보존한다. Python 의존성은 `%LOCALAPPDATA%/AgentTools/ppt-master`의 venv에 설치하고 해당 Python을 명시해 실행한다.
- `~/.agents/skills/huashu-design`에 저장소 루트 패키지 전체를 보존한다. Python 의존성은 `%LOCALAPPDATA%/AgentTools/huashu-design`의 venv를 사용한다. Node 의존성은 해당 패키지 내부에서 원본 lock으로 준비하며 생성물·개인 기억은 검증 폴더에 격리한다.
- OfficeCLI `v1.0.160`의 Windows x64 릴리스 바이너리는 `%LOCALAPPDATA%/OfficeCLI/officecli.exe`에 해시 검증 후 설치하고 사용자 PATH에 해당 폴더만 추가한다. `skills/officecli` 하나를 전역에 설치하고 전문 문서는 바이너리의 `load_skill`을 사용한다.
- OfficeCLI 전용 `OFFICECLI_SKIP_UPDATE=1`, `OFFICECLI_NO_AUTO_INSTALL=1` 사용자 환경변수로 고정 버전과 다른 클라이언트 스킬·MCP 보존을 유지한다. 검증 프로세스에서만 `OFFICECLI_NO_AUTO_RESIDENT=1`을 사용한다.
- 세 스킬은 이름을 유지하되 별도 `agents/openai.yaml`에서 명시 호출 전용으로 둔다. 원본 `SKILL.md`와 attribution guard·고지는 수정하지 않는다.

## 보호·실패·재실행.

기존 설치·동명 디렉터리·명령 충돌을 먼저 확인한다. 기존 사용자 파일은 덮어쓰지 않는다. 원본 SHA와 설치 파일 해시를 기록하고 같은 설치는 재검사로 끝낸다. 새 대상의 설치 실패 시 불완전 상태를 완료로 보고하지 않고 원인·복구 범위를 남긴다. 전역 권한·인증·다른 AI 설정·MCP·hooks는 변경하지 않는다. 세 도구의 이미지·음성·검색 등 유료 외부 API 기능은 실행하지 않는다.

## 검증과 완료 기준.

전체 리소스·원본 고지·부모 권한 상속·새 Codex 프로세스의 이름/경로/호출 정책을 확인한다. PPT Master의 guard와 품질 검사·편집 가능한 PPTX 생성, OfficeCLI의 DOCX/PPTX/XLSX 생성·수식 계산·재열기, Huashu의 원본 테스트·HTML 검증 또는 실제 변환 샘플을 수행한다. 사용한 경로와 미검증 기능은 구분한다. 기존 보호 파일 동일성·중복 조사·문서 링크·전체 회귀·독립 리뷰를 마친 뒤 한글 커밋·main 통합·일반 push·원격 SHA·CI를 확인하고 소유 worktree를 정리한다.

## 라이선스.

PPT Master는 MIT 고지와 SPONSORS·attribution을 유지한다. OfficeCLI는 Apache-2.0 및 NOTICE·제3자 고지를 보존한다. Huashu 루트는 MIT이나 일부 스티커는 PolyForm Shield 1.0.0 예외이므로 해당 고지도 보존한다. 종속성·원본·샘플은 공개 재배포하지 않는다.
