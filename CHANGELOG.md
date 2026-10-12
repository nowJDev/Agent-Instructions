<!-- 이 문서는 Agent-Instructions 저장소의 공개 변경 이력을 기록한다. -->
# Changelog

## 2026-10-12

### Added

- README에 구성 관계와 요청 처리 흐름을 설명하는 Mermaid 다이어그램 두 개를 추가했다.
- README 정리의 승인 범위와 구현·검증 계획을 기록했다.

### Changed

- 소개, 바로가기, 빠른 시작과 문서 안내를 정리하고 긴 카탈로그·디렉터리 맵·환경 주의사항을 펼쳐보기로 구성했다.
- 기존 섹션 번호와 전체 스킬 목록을 보존하고, 지침 적용과 실제 도구 설치·실행의 경계를 명확히 했다.

## 2026-08-28

### Changed

- `handover` 파일명을 `HANDOVER_{project-name}_{YYYYMMDD}_{topic-slug}.md`로 정하고, 명시값·Git 루트·현재 작업 폴더 순의 프로젝트명 결정과 작업 슬러그 내 프로젝트명 중복 방지 규칙을 추가했다.

## 2026-07-29

### Added

- 상태 변경 요청을 설계·계획·구현·검증·리뷰·문서화·통합 순서로 통제하는 자체 제작 `design-driven-delivery` Skill 원본을 `Owned-Skills/`에 추가했다.
- `design-driven-delivery` 개인 글로벌 Skill 카탈로그와 설치·이식 안내를 추가했다.

### Changed

- 루트와 Codex 전역 `AGENTS.md`에 상태 변경 라우팅, 전문 Skill 재사용, 읽기 전용 예외 규칙을 반영했다.
- README, Skill 인덱스와 사람용 설명서의 노출 Skill 수를 99개, 개인 글로벌 Skill 수를 6개로 갱신했다.
- 타사 Skill 비재배포 원칙은 유지하고 직접 작성한 Skill 원본만 저장소에 둘 수 있도록 이식 정책을 명확히 했다.

## 2026-07-08

### Added

- Windows에서 바탕화면 `Codex.bat` 실행 방식을 공식 Codex 아이콘을 쓰는 `Codex.lnk` 바로가기로 전환하는 절차를 `references/codex-windows-shortcut.md`에 추가했다.

### Changed

- README의 `references/` 설명에 Windows Codex 바로가기 가이드를 반영했다.

## 2026-07-02

### Added

- `hexagonal-code-review` 개인 글로벌 스킬 카탈로그를 추가해 헥사고날 아키텍처 / Ports and Adapters 기준의 코드 리뷰와 리팩토링 적용 기준을 문서화했다.

### Changed

- 스킬 인덱스와 README의 노출 스킬 수를 98개, 개인 글로벌 스킬 수를 5개로 갱신했다.
- `hexagonal-code-review`의 구현 모드는 계획 보고와 사용자 승인 후 수정하도록 보강하고, 결과 보고 시 출력 포맷 참조를 적용하도록 문서화했다.

## 2026-06-18

### Added

- `GETTING_STARTED.md`를 추가해 다른 AI에게 저장소를 적용시키는 프롬프트와 AI별 사용법을 분리했다.
- `SECURITY.md`를 추가해 토큰, 인증 헤더, 개인 설정 파일, 내부 프로젝트 지식의 공개 금지 기준을 명시했다.
- `LICENSE`를 추가해 직접 작성한 문서의 재사용 범위와 타사 자료의 별도 라이선스 적용 범위를 구분했다.
- Codex CLI의 `AGENTS.md` 로딩 방식과 `rules/*.md` 문서, `~/.codex/rules/*.rules` 승인 정책의 차이를 `GETTING_STARTED.md`에 추가했다.
- 핵심 검증·보안·파일 읽기·중단 조건을 `AGENTS.md` 본문에 직접 추가해 링크 문서를 읽지 않아도 최소 규칙이 적용되도록 했다.
- Codex 전역 `~/.codex/AGENTS.md`에 복사하기 위한 `codex-global-AGENTS.md`를 추가했다.

### Changed

- `README.md` 상단을 공개 저장소 첫 화면에 맞게 정리하고 Quick Start 프롬프트를 추가했다.
- `README.md`에서 `GETTING_STARTED.md`, `SECURITY.md`, `CHANGELOG.md`로 이어지는 온보딩 흐름을 명확히 했다.
- Notion 토큰 저장 언급을 일반 보안 주의 문구로 바꿨다.

### Removed

- 개인 프로젝트 지식인 `references/data2avatar.md`를 공개 대상에서 제외했다.
- 프로젝트 전용 흔적이던 `MCP/caveman-shrink.md`를 제거했다.
