<!-- 세 외부 도구의 단일 전역 설치·호출·런타임과 검증 경계를 안내한다. -->
# Office·디자인 도구.

이 문서는 설명 카탈로그이며 타사 실행 원본·바이너리·대형 자산을 포함하지 않는다. 원본은 사용자 전역에 한 번 설치하고 이 저장소에서도 같은 실행본을 사용한다. 프로젝트 안에 두 번째 `.agents/skills` 복사본을 만들지 않는다. [고정 설치 명세](../../references/office-design-tools.lock.json), [설치 설계](../../docs/history/2026-11-12-office-design-tools.md#spec), [검증 기록](../../docs/history/2026-11-12-office-design-tools.md#review)을 함께 따른다.

### 설치와 재실행.

Codex의 표준 `skill-installer/scripts/install-skill-from-github.py`를 사용한다. `--dest`는 실제 사용자 스킬 경로로 지정하며, 아래 PowerShell 예시는 Codex 기본 설치를 전제로 한다. 목적지가 이미 있으면 먼저 원본·개인 수정 여부를 대조하고 그대로 재검사한다. 폴더를 지우거나 덮어써서 재설치하지 않는다.

```powershell
$skillInstaller = Join-Path $env:USERPROFILE '.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py'
$skillsDestination = Join-Path $env:USERPROFILE '.agents/skills'
python $skillInstaller --repo hugohe3/ppt-master --ref e2820d326d049f1fcbe90523983def3d52280233 --path skills/ppt-master --dest $skillsDestination
python $skillInstaller --repo iOfficeAI/OfficeCLI --ref c56512c8c7b76fe284f09940e4cd492470099d3e --path skills/officecli --dest $skillsDestination
python $skillInstaller --repo alchaincyf/huashu-design --ref e8d1148a80d5a281d4247cffe320add3df017928 --path . --name huashu-design --dest $skillsDestination
```

설치 후 세 패키지에 원본과 구분되는 `agents/openai.yaml` 정책을 추가한다. 원본 본문·제작자·고지는 유지한다. 세 이름이 기존 문서·디자인 기능과 역할이 겹치므로 명시 호출을 사용한다.

```yaml
policy:
  allow_implicit_invocation: false
```

실행 종속성은 이 스킬 복사 명령이 자동 준비하지 않는다. 이 PC의 PPT Master Python은 `%LOCALAPPDATA%/AgentTools/ppt-master/.venv/Scripts/python.exe`, Huashu Python은 `%LOCALAPPDATA%/AgentTools/huashu-design/Scripts/python.exe`다. 원본 venv 자동 선택 기능은 없으므로 기본 `python`의 가용성과 혼동하지 않는다. Node 의존성은 Huashu 패키지의 원본 `package-lock.json`을 기준으로 `npm ci`로 준비한다. 이 설치는 별도 실행 스크립트를 재구현하지 않고 공식 도구를 사용한다.

## ppt-master

문서·주제를 SVG 기반의 편집 가능한 PowerPoint로 만드는 [PPT Master](https://github.com/hugohe3/ppt-master) 스킬이다. `$ppt-master`로 명시 호출한다. 고정 커밋의 `skills/ppt-master` 전체를 `~/.agents/skills/ppt-master`에 설치하며 아이콘·템플릿·스크립트·requirements를 함께 보존한다. MIT·SPONSORS·attribution guard를 삭제하거나 수정하지 않는다. 원본 metadata `6.9.0`과 실제 설치 커밋을 구분한다.

전용 Python venv에서 패키지의 `requirements.txt`를 설치한다. `project_manager.py init <이름> --dir <출력 위치> --quick-generate`처럼 실제 작업 폴더를 명시한다. 최종 `svg_quality_checker.py` 보고서와 현재 SVG의 fingerprint가 일치해야 `svg_to_pptx.py` export를 통과한다. 생성·품질 검사·PPTX 재열기를 각각 확인한다. 이미지·음성·웹 검색 등 외부 서비스는 작업별 인증과 데이터 전달 조건을 별도 확인한다. venv 설치는 기본 Python이나 시스템 PATH를 변경하지 않는다.

## officecli

[OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)는 Word·Excel·PowerPoint 없이 DOCX/XLSX/PPTX를 생성·읽기·편집하는 CLI와 연동 스킬이다. `$officecli`로 명시 호출한다. 스킬 하나와 같은 릴리스의 Windows x64 실행본을 맞추고 전문 규칙은 `officecli load_skill word|pptx|excel` 등으로 읽는다. 9개 전문 문서를 별도 전역 스킬로 중복 설치하지 않는다.

Windows 실행본은 [v1.0.160 릴리스](https://github.com/iOfficeAI/OfficeCLI/releases/tag/v1.0.160)의 `officecli-win-x64.exe`를 내려받아 명세의 SHA256과 대조한 뒤 `%LOCALAPPDATA%/OfficeCLI/officecli.exe`에 배치한다. LICENSE·NOTICE·THIRD-PARTY-NOTICES.txt를 같은 폴더에 보존한다. 기존 명령과 파일이 있으면 교체 전에 확인하고, 사용자 PATH에는 해당 폴더만 중복 없이 추가한다. 기계 전체 PATH는 바꾸지 않는다.

공식 일괄 설치·`officecli install`은 다른 클라이언트의 스킬·MCP를 변경할 수 있어 이 설치 방식에서는 실행하지 않는다. `OFFICECLI_SKIP_UPDATE=1`, `OFFICECLI_NO_AUTO_INSTALL=1`을 사용자 환경에 두어 고정 버전과 다른 클라이언트를 보존한다. 업데이트는 새 버전·해시·고지를 검토하는 별도 작업이다. 검증할 때만 `OFFICECLI_NO_AUTO_RESIDENT=1`을 프로세스 환경에 지정하면 상주 프로세스를 만들지 않는다. 스킬만 설치하면 실행 파일은 준비되지 않는다.

새 터미널에서 `officecli --version`을 확인한다. `validate`, `view issues`, 실제 `get --json`과 수식 캐시 값을 대조한다. Office 없는 렌더 경로는 `view <파일> screenshot --render html -o <PNG>`로 명시한다. 브라우저·PDF 플러그인 등은 기능별 추가 요구사항이며 바이너리 설치만으로 모두 준비됐다고 하지 않는다.

## huashu-design

웹·앱·PPTX·인포그래픽 등 HTML 기반 디자인을 만드는 [Huashu Design](https://github.com/alchaincyf/huashu-design) 스킬이다. `$huashu-design`으로 명시 호출한다. 고정 커밋 루트 전체를 `~/.agents/skills/huashu-design`에 설치하고 `SKILL.md`뿐 아니라 references·assets·scripts·demos를 보존한다. 루트 MIT와 별개로 스티커 22개에는 PolyForm Shield 1.0.0 고지가 있으므로 전체를 MIT라고 재분류하지 않는다.

전용 Python venv와 패키지 내부 Node 의존성을 사용한다. 원본 `scripts/capabilities.py --json`으로 실제 가용 기능을 확인하고 원본 테스트·HTML 검증·PPTX 재열기로 대표 흐름을 확인한다. 이 PC의 Python Playwright 1.59.0과 Node lock의 1.59.1은 같은 Chromium 1217을 사용한다. 해당 작업 프로세스에 `PLAYWRIGHT_BROWSERS_PATH=%LOCALAPPDATA%/AgentTools/huashu-design/browsers`를 지정한다. Chromium·ffmpeg·이미지 검색·클라우드 음성 등은 서로 다른 요구사항이다. 외부 서비스나 자동 hooks를 이 설치 범위에서 추가하지 않는다. 개인 기억은 기본 `~/.huashu-design`에 저장될 수 있으며 검증에서는 `HUASHU_DESIGN_HOME`을 비공개 검증 폴더로 지정한다.

설치·호출 정책은 새 Codex 세션에서 확인한다. 대표 샘플 성공을 모든 디자인의 품질이나 모든 변환 기능의 호환성으로 확대하지 않는다.
