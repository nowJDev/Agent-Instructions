<!-- 이 문서는 선택한 Windows CLI의 공식 아이콘 바로가기를 생성하고 독립 검증하는 절차를 안내한다. -->
# Windows CLI Shortcut

"이거대로 세팅해줘"의 대상 선택·CLI 준비·전역 기본 지침은 [GETTING_STARTED.md](../GETTING_STARTED.md#41-windows-codex-환경-세팅)를 따른다. 이 문서는 선택한 Codex 또는 Claude Code 하나의 공식 아이콘 `.lnk`를 생성·갱신·검증한다. 각 예제의 `$client`를 `'codex'` 또는 `'claude-code'`로 명시하고 같은 값을 사용한다. 그 밖의 값은 오류다.

| `$client` | 실행 파일 후보 | 바로가기 | 공식 ICO 위치 |
|---|---|---|---|
| `codex` | `codex.cmd`, `codex.exe` | `Codex.lnk` | `~/.codex/assets/icons/codex-official.ico` |
| `claude-code` | `claude.cmd`, `claude.exe` | `Claude Code.lnk` | `~/.claude/assets/icons/claude-code-official.ico` |

## 실행 전제와 공식 아이콘.

표의 `~/.codex`·`~/.claude`는 기본 위치다. `CODEX_HOME`·`CLAUDE_CONFIG_DIR`이 지정됐으면 해당 설정 홈의 `assets/icons/`를 사용하고 지침·복제본·CLI 실행도 같은 환경변수를 유지한다.

- CLI 전체 경로에 `%`가 있으면 CMD 재확장을 막기 위해 실행·생성·검증 전에 중단한다. `%`가 없는 설치 경로로 옮긴 뒤 다시 실행한다. CMD에는 `/v:off`를 명시해 `!`가 있는 경로도 지연 확장하지 않는다.
- CLI는 공식 설치 절차로 준비한 뒤 확인된 `Source` 전체 경로로 버전을 실행한다. `Get-Command codex`나 `claude`가 반환할 수 있는 `.ps1` 대신 CMD에서 실행할 `.cmd`·`.exe`를 확인한다. 버전 검사와 바로가기 모두 전체 경로를 사용해 작업 폴더의 동명 CLI가 대신 실행되지 않게 한다.
- 바탕화면은 `[Environment]::GetFolderPath('DesktopDirectory')`로 조회해 OneDrive 리디렉션을 지원한다. 사용자 지정 작업 폴더를 우선하고 미지정이면 실제 바탕화면 아래 `Agent`를 만든다. 지정 폴더가 없으면 임의 대체하지 않는다.
- Windows Terminal이 있으면 `wt.exe`를 재사용하고 없으면 `$env:ComSpec`의 CMD를 쓴다. Terminal은 자동 설치하지 않는다. 두 분기 모두 UTF-8 코드페이지를 적용한다.
- 기존 바로가기의 `TargetPath`, `Arguments`, `WorkingDirectory`, `IconLocation`을 먼저 확인한다. 기존 `.bat`는 삭제하지 않으며 배치 파일 없이 `.lnk`를 새로 만들 수 있다.
- 기존 ICO는 공식 출처를 확인한 경우에만 재사용한다. 파일명만으로 판단하지 않는다. 없거나 출처가 불명확하면 [OpenAI 공식 Codex 페이지](https://openai.com/codex/) 또는 [Anthropic 공식 Claude Code 제품 페이지](https://claude.com/product/claude-code)에서 현재 제품 아이콘의 원본·출처를 확인해 선택한 사용자 전역 아이콘 폴더에 준비한다. 폴더가 없으면 준비 단계에서 생성한다. 출처 확인 또는 ICO 준비에 실패하면 미완료다. 아이콘 바이너리는 저장소에 넣지 않는다.

확인한 원본 PNG를 해당 사용자 폴더에 저장했다면 아래 기존 변환 예시를 재사용할 수 있다. 이미 Pillow를 사용할 수 있는 환경에 한하며 의존성을 자동 설치하지 않는다.

```powershell
$ErrorActionPreference = 'Stop'
$client = 'codex' # Claude Code를 선택했으면 'claude-code'로 바꾼다.
$iconRelativePath = switch ($client) {
    'codex' {
        $clientHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
        'assets\icons\codex-official'
    }
    'claude-code' {
        $clientHome = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $env:USERPROFILE '.claude' }
        'assets\icons\claude-code-official'
    }
    default { throw 'client는 codex 또는 claude-code여야 합니다.' }
}
$pngPath = Join-Path $clientHome ($iconRelativePath + '.png')
$icoPath = Join-Path $clientHome ($iconRelativePath + '.ico')
if (-not (Test-Path -LiteralPath $pngPath -PathType Leaf)) {
    throw "공식 출처에서 준비한 PNG가 없습니다: $pngPath"
}
python -c "import sys; from PIL import Image; img=Image.open(sys.argv[1]).convert('RGBA'); img.save(sys.argv[2], format='ICO', sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])" $pngPath $icoPath
if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $icoPath -PathType Leaf)) {
    throw '공식 아이콘 ICO 변환에 실패했습니다.'
}
```

## PowerShell 구성 예시.

아래 생성 블록은 독립적으로 실행한다. `$workingDir`은 사용자 지정 폴더가 있으면 입력하고 기본값이면 빈 문자열을 유지한다. 기존 바로가기 속성이 요청과 충돌하면 원인을 확인한 뒤 갱신한다.

WT의 `-d`는 드라이브 루트에서도 인자가 깨지지 않도록 끝의 `\`를 정리하고 `\.`을 붙인다. 경로의 세미콜론은 WT 명령 구분자로 처리되지 않도록 `\;`로 전달하고 CLI 경로의 따옴표는 WT의 argv 해석을 거쳐 CMD까지 보존한다. **CMD 대체 분기는 원래 경로를 인용하며 WT의 `\;` 이스케이프를 적용하지 않는다.** 버전 확인과 `WorkingDirectory`도 원래 경로를 사용한다.

```powershell
$ErrorActionPreference = 'Stop'
$client = 'codex' # Claude Code를 선택했으면 'claude-code'로 바꾼다.
switch ($client) {
    'codex' {
        $shortcutName = 'Codex.lnk'
        $cliNames = @('codex.cmd', 'codex.exe')
        $clientHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
        $iconRelativePath = 'assets\icons\codex-official.ico'
        $title = 'Codex CLI'
    }
    'claude-code' {
        $shortcutName = 'Claude Code.lnk'
        $cliNames = @('claude.cmd', 'claude.exe')
        $clientHome = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $env:USERPROFILE '.claude' }
        $iconRelativePath = 'assets\icons\claude-code-official.ico'
        $title = 'Claude Code CLI'
    }
    default { throw 'client는 codex 또는 claude-code여야 합니다.' }
}
$workingDir = '' # 사용자 지정 폴더가 있으면 입력한다.
$desktopDir = [Environment]::GetFolderPath('DesktopDirectory')
if (-not $desktopDir -or -not (Test-Path -LiteralPath $desktopDir -PathType Container)) {
    throw '실제 바탕화면 폴더를 확인할 수 없습니다.'
}
$shortcutPath = Join-Path $desktopDir $shortcutName
$iconTarget = Join-Path $clientHome $iconRelativePath
$wtCommand = Get-Command wt.exe -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
$cliCommand = Get-Command $cliNames -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $cliCommand -or -not (Test-Path -LiteralPath $cliCommand.Source -PathType Leaf)) {
    throw 'cmd에서 실행할 선택한 CLI(.cmd 또는 .exe)가 없습니다.'
}
if ($cliCommand.Source.Contains('%')) {
    throw 'CLI 경로의 %는 CMD에서 재확장됩니다. %가 없는 설치 경로로 옮긴 뒤 다시 실행하세요.'
}
if (-not (Test-Path -LiteralPath $env:ComSpec -PathType Leaf)) { throw '기본 CMD 실행 파일이 없습니다.' }
$cliCommand.Source
& $env:ComSpec /d /v:off /c ('chcp 65001 > nul & "{0}" --version' -f $cliCommand.Source)
if ($LASTEXITCODE -ne 0) { throw '선택한 CLI 전체 경로의 --version 실행이 실패했습니다.' }
if (-not (Test-Path -LiteralPath $iconTarget -PathType Leaf)) {
    throw "선택한 CLI 공식 아이콘 ICO가 없습니다: $iconTarget"
}
if ($wtCommand) {
    if (-not (Test-Path -LiteralPath $wtCommand.Source -PathType Leaf)) { throw '확인된 Windows Terminal 실행 파일이 없습니다.' }
    $targetPath = $wtCommand.Source
} else {
    $targetPath = $env:ComSpec
}

$shell = New-Object -ComObject WScript.Shell
if (Test-Path -LiteralPath $shortcutPath) {
    if (-not (Test-Path -LiteralPath $shortcutPath -PathType Leaf)) {
        throw "바로가기 위치가 파일이 아닙니다: $shortcutPath"
    }
    $existing = $shell.CreateShortcut($shortcutPath)
    $existing | Select-Object TargetPath, Arguments, WorkingDirectory, IconLocation | Format-List
}
if (-not $workingDir) {
    $workingDir = Join-Path $desktopDir 'Agent'
    if (-not (Test-Path -LiteralPath $workingDir)) {
        New-Item -ItemType Directory -Path $workingDir -ErrorAction Stop | Out-Null
    }
}
if (-not (Test-Path -LiteralPath $workingDir -PathType Container)) {
    throw "작업 폴더가 없습니다: $workingDir"
}
$workingDir = (Resolve-Path -LiteralPath $workingDir).Path
# WT의 argv 해석을 거쳐 cmd까지 CLI 경로 따옴표를 보존한다.
if ($wtCommand) {
    $arguments = '-w 0 nt --title "{0}" -d "{1}" cmd /d /v:off /k "chcp 65001 > nul & \"{2}\""' -f $title, ($workingDir.TrimEnd('\') + '\.').Replace(';', '\;'), $cliCommand.Source.Replace(';', '\;')
} else {
    $arguments = '/d /v:off /k "chcp 65001 > nul & "{0}""' -f $cliCommand.Source
}
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $targetPath
$shortcut.Arguments = $arguments
$shortcut.WorkingDirectory = $workingDir
$shortcut.IconLocation = "$iconTarget,0"
$shortcut.Description = $title
$shortcut.WindowStyle = 1
$shortcut.Save()
```

## 검증.

생성·갱신 후 아래 검증을 별도로 실행한다. `$client`와 `$workingDir`은 생성 시와 같은 값을 사용한다. 파일 누락과 속성 불일치는 `throw`로 실패하며 완료로 보고하지 않는다. 아이콘 경로는 마지막 쉼표의 인덱스만 분리해 경로 자체의 쉼표도 처리한다.

```powershell
$ErrorActionPreference = 'Stop'
$client = 'codex' # 생성 시 선택한 값과 같게 입력한다.
switch ($client) {
    'codex' {
        $shortcutName = 'Codex.lnk'
        $cliNames = @('codex.cmd', 'codex.exe')
        $clientHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
        $iconRelativePath = 'assets\icons\codex-official.ico'
        $title = 'Codex CLI'
    }
    'claude-code' {
        $shortcutName = 'Claude Code.lnk'
        $cliNames = @('claude.cmd', 'claude.exe')
        $clientHome = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $env:USERPROFILE '.claude' }
        $iconRelativePath = 'assets\icons\claude-code-official.ico'
        $title = 'Claude Code CLI'
    }
    default { throw 'client는 codex 또는 claude-code여야 합니다.' }
}
$workingDir = '' # 생성 시 지정한 사용자 폴더와 같게 입력한다.
$desktopDir = [Environment]::GetFolderPath('DesktopDirectory')
if (-not $desktopDir -or -not (Test-Path -LiteralPath $desktopDir -PathType Container)) {
    throw '실제 바탕화면 폴더를 확인할 수 없습니다.'
}
$shortcutPath = Join-Path $desktopDir $shortcutName
$iconTarget = Join-Path $clientHome $iconRelativePath
$wtCommand = Get-Command wt.exe -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
$cliCommand = Get-Command $cliNames -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $cliCommand -or -not (Test-Path -LiteralPath $cliCommand.Source -PathType Leaf)) {
    throw 'cmd에서 실행할 선택한 CLI를 확인할 수 없습니다.'
}
if ($cliCommand.Source.Contains('%')) {
    throw 'CLI 경로의 %는 CMD에서 재확장됩니다. %가 없는 설치 경로로 옮긴 뒤 다시 실행하세요.'
}
if (-not (Test-Path -LiteralPath $env:ComSpec -PathType Leaf)) { throw '기본 CMD 실행 파일이 없습니다.' }
$cliCommand.Source
& $env:ComSpec /d /v:off /c ('chcp 65001 > nul & "{0}" --version' -f $cliCommand.Source)
if ($LASTEXITCODE -ne 0) { throw '선택한 CLI 전체 경로의 --version 실행이 실패했습니다.' }
if ($wtCommand) {
    if (-not (Test-Path -LiteralPath $wtCommand.Source -PathType Leaf)) { throw '확인된 Windows Terminal 실행 파일이 없습니다.' }
    $targetPath = $wtCommand.Source
} else {
    $targetPath = $env:ComSpec
}
if (-not (Test-Path -LiteralPath $shortcutPath -PathType Leaf)) {
    throw "바로가기가 없습니다: $shortcutPath"
}
if (-not $workingDir) { $workingDir = Join-Path $desktopDir 'Agent' }
if (-not (Test-Path -LiteralPath $workingDir -PathType Container)) {
    throw "작업 폴더가 없습니다: $workingDir"
}
$workingDir = (Resolve-Path -LiteralPath $workingDir).Path
if ($wtCommand) {
    $expectedArguments = '-w 0 nt --title "{0}" -d "{1}" cmd /d /v:off /k "chcp 65001 > nul & \"{2}\""' -f $title, ($workingDir.TrimEnd('\') + '\.').Replace(';', '\;'), $cliCommand.Source.Replace(';', '\;')
} else {
    $expectedArguments = '/d /v:off /k "chcp 65001 > nul & "{0}""' -f $cliCommand.Source
}
$shell = New-Object -ComObject WScript.Shell
$check = $shell.CreateShortcut($shortcutPath)
if ($check.TargetPath -ne $targetPath -or -not (Test-Path -LiteralPath $check.TargetPath -PathType Leaf)) {
    throw 'TargetPath가 확인된 실행 파일 경로와 다릅니다.'
}
if ($check.Arguments -cne $expectedArguments -or $check.Arguments -match '(Codex|Claude Code)\.bat') {
    throw 'Arguments가 UTF-8 CLI 직접 실행 인자와 다르거나 기존 배치 파일을 참조합니다.'
}
if ($check.WorkingDirectory -ne $workingDir) {
    throw 'WorkingDirectory가 지정한 작업 폴더와 다릅니다.'
}
if ($check.IconLocation -notmatch '^(.*),(-?\d+)$') {
    throw 'IconLocation의 파일 경로와 아이콘 인덱스를 확인할 수 없습니다.'
}
$iconPath = $Matches[1].Trim('"')
if ($check.IconLocation -ne "$iconTarget,0" -or -not (Test-Path -LiteralPath $iconPath -PathType Leaf)) {
    throw 'IconLocation이 준비한 공식 ICO와 다르거나 아이콘 파일이 없습니다.'
}
if ($check.Description -cne $title -or $check.WindowStyle -ne 1) {
    throw 'Description 또는 WindowStyle이 목표 값과 다릅니다.'
}
[PSCustomObject]@{
    Client = $client
    CliSource = $cliCommand.Source
    Description = $check.Description
    WindowStyle = $check.WindowStyle
    ShortcutPath = $shortcutPath
    TargetPath = $check.TargetPath
    Arguments = $check.Arguments
    WorkingDirectory = $check.WorkingDirectory
    IconLocation = $check.IconLocation
    ExistsTarget = Test-Path -LiteralPath $check.TargetPath -PathType Leaf
    ExistsIcon = Test-Path -LiteralPath $iconPath -PathType Leaf
    StillCallsBat = ($check.Arguments -match '(Codex|Claude Code)\.bat')
}
```

속성 검증 후 바로가기를 실제로 열어 WT의 선택한 CLI 탭 또는 CMD에서 실제 시작 작업 폴더·UTF-8·선택한 CLI 실행을 확인한다. 새 세션 지침 로드와 사용자 로그인은 [최소 세팅 완료 조건](../GETTING_STARTED.md#41-windows-codex-환경-세팅)을 따른다. 실행하지 않았거나 인증이 남으면 해당 항목은 미완료다. CLI 전체 경로·버전, 전역 지침·바로가기 위치, 작업 폴더, 공식 아이콘 출처와 검증 결과를 보고한다.

Windows가 예전 아이콘을 캐시하면 바탕화면을 새로고침하거나 아래 명령을 실행한다.

```powershell
& "$env:WINDIR\System32\ie4uinit.exe" -show
```

## 삭제 기준.

`StillCallsBat = False`여도 기존 `Codex.bat`·`Claude Code.bat`는 환경 세팅 요청만으로 삭제하지 않는다. 사용자가 명시적으로 승인한 뒤 별도 작업으로 처리한다.
