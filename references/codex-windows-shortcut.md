<!-- 이 문서는 Windows에서 Codex 실행용 바로가기를 공식 아이콘 기반으로 구성하는 절차를 정리한다. -->
# Codex Windows Shortcut

Windows에서 "이 저장소대로 Codex 세팅해줘"를 요청하면 [전역 지침 배치](../GETTING_STARTED.md#41-windows-codex-환경-세팅)와 이 문서의 공식 아이콘 바로가기 생성·갱신·검증을 모두 수행한다. 단순 "지침 적용"은 규칙을 읽고 따르는 의미다.

`.bat`가 없어도 `Codex.lnk`를 새로 만들 수 있다. 기존 바로가기를 갱신할 때는 먼저 `TargetPath`, `Arguments`, `WorkingDirectory`, `IconLocation`을 출력해 기존 동작을 확인한다. 사용자 지정 작업 폴더를 우선하며, 기존 `.bat`는 삭제하지 않는다.

## 목표 상태

- 실제 Windows 바탕화면에 `Codex.lnk`를 실행 진입점으로 둔다.
- `Codex.lnk`는 `Codex.bat`를 호출하지 않고 `wt.exe`를 직접 실행한다.
- 아이콘은 사용자 전역 위치인 `%USERPROFILE%\.codex\assets\icons\codex-official.ico`에 보관한다.
- 시작 작업 폴더는 사용자가 지정한 폴더를 우선하고, 미지정이면 실제 바탕화면 아래 `Agent`를 사용한다.
- 실행 시 UTF-8 코드페이지를 적용한 뒤 확인된 `codex.cmd` 또는 `codex.exe`를 실행한다.

## 실행 전제와 공식 아이콘

- 바탕화면 경로는 `[Environment]::GetFolderPath('DesktopDirectory')`로 조회한다. `%USERPROFILE%\Desktop`을 고정하지 않으므로 OneDrive로 이동한 바탕화면도 지원한다.
- Codex CLI와 Windows Terminal이 이미 설치되어 있어야 한다. `Get-Command codex`는 `codex.ps1`을 반환할 수 있으므로 `cmd`용 `codex.cmd` 또는 `codex.exe`와 `wt.exe`의 실제 파일 경로를 별도로 확인한다. 버전 검사와 바로가기 모두 확인된 CLI의 `Source` 전체 경로를 실행해 작업 폴더의 동명 파일이 대신 실행되지 않게 한다.
- 기본 작업 폴더가 없으면 실제 바탕화면 아래 `Agent`를 만든다. 명시적으로 지정한 폴더가 없으면 임의 대체하지 않고 오류를 보고한다.
- `%USERPROFILE%\.codex\assets\icons\codex-official.ico`가 공식 출처에서 준비된 파일인지 확인하고 있으면 재사용한다. 파일명만 보고 공식 아이콘이라고 판단하지 않는다.
- 아이콘이 없거나 출처를 확인할 수 없으면 [OpenAI 공식 Codex 페이지](https://openai.com/codex/)에서 현재 공식 앱 아이콘의 원본·출처를 확인한 뒤 사용자 전역 아이콘 폴더에 준비한다. 원본이 PNG면 아래 변환 예시를 사용할 수 있다. 출처를 확인할 수 없거나 ICO 준비에 실패하면 바로가기 작업은 미완료로 보고한다.
- 전제가 없으면 중단하고 미완료 항목을 보고한다. 이 요청에 CLI·Terminal 자동 설치, 개인 설정 배포, 저장소 내 아이콘 바이너리 배포는 포함하지 않는다.

원본 PNG를 확인·저장한 뒤, 이미 Pillow를 사용할 수 있는 환경에서는 다음처럼 변환할 수 있다. Pillow가 없으면 자동 설치하지 않고 변환이 미완료임을 보고한다.

```powershell
$ErrorActionPreference = 'Stop'
$pngPath = Join-Path $env:USERPROFILE '.codex\assets\icons\codex-official.png'
$icoPath = Join-Path $env:USERPROFILE '.codex\assets\icons\codex-official.ico'
if (-not (Test-Path -LiteralPath $pngPath -PathType Leaf)) {
    throw "공식 출처에서 준비한 PNG가 없습니다: $pngPath"
}
python -c "import sys; from PIL import Image; img=Image.open(sys.argv[1]).convert('RGBA'); img.save(sys.argv[2], format='ICO', sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])" $pngPath $icoPath
if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $icoPath -PathType Leaf)) {
    throw 'Codex 공식 아이콘 ICO 변환에 실패했습니다.'
}
```

## 다른 PC에서 요청할 프롬프트

다른 PC의 에이전트에게는 아래처럼 요청한다.

```text
이 저장소대로 Windows Codex 환경을 세팅해줘.
전역 지침 배치와 공식 아이콘 Codex.lnk 생성·검증까지 진행해줘.
GETTING_STARTED.md와 references/codex-windows-shortcut.md를 따라줘.

요구사항.
- .bat 자체 아이콘 변경이 아니라 Codex.lnk 바로가기를 만들거나 갱신해줘.
- 바로가기는 bat 파일을 호출하지 말고 Windows Terminal(wt.exe)을 직접 실행하게 해줘.
- 기존 바로가기를 수정하기 전에 속성을 출력해 확인하고, bat가 없어도 새로 만들어줘.
- 바탕화면은 Windows가 반환하는 실제 경로를 쓰고, 작업 폴더는 내가 지정한 폴더를 우선해줘. 미지정이면 실제 바탕화면 아래 Agent를 사용해줘.
- 실행은 Windows Terminal 새 탭 제목 "Codex CLI"에서 cmd /k로 UTF-8 코드페이지를 적용한 뒤 확인된 codex.cmd 또는 codex.exe를 실행해줘.
- 공식 Codex 아이콘은 %USERPROFILE%\.codex\assets\icons\codex-official.ico 에 저장해줘.
- 아이콘 원본이 필요하면 OpenAI 공식 Codex 페이지에서 현재 공식 Codex 앱 아이콘을 확인해서 PNG를 저장한 뒤 ICO로 변환해줘.
- 완료 전 실행 파일·작업 폴더·아이콘·인자를 검증하고 Codex.lnk가 Codex.bat를 참조하지 않는지 확인해줘.
- 기존 bat는 삭제하지 말고, 전제가 없거나 검증에 실패하면 미완료 항목을 보고해줘. CLI와 Terminal은 자동 설치하지 마.
```

## PowerShell 구성 예시

아래 스크립트는 공식 출처가 확인된 ICO가 준비되어 있을 때 독립적으로 실행해 바로가기를 생성하거나 갱신한다. `$workingDir`에 사용자 지정 폴더를 넣고, 미지정이면 빈 문자열을 유지한다. 기존 바로가기 속성이 요청과 충돌하면 변경 전에 원인을 확인한다.

사용자 지정 폴더가 `C:\` 같은 드라이브 루트여도 인자가 깨지지 않도록 WT의 `-d`에는 끝의 `\`를 정리한 뒤 `\.`을 붙여 전달한다. 작업 폴더·CLI 경로의 세미콜론은 WT의 명령 구분자로 해석되지 않도록 `\;`로 전달한다. 바로가기의 `WorkingDirectory`와 버전 검사는 원래 확인된 경로를 유지한다.

```powershell
$ErrorActionPreference = 'Stop'
$workingDir = '' # 사용자 지정 폴더가 있으면 입력한다.
$desktopDir = [Environment]::GetFolderPath('DesktopDirectory')
if (-not $desktopDir -or -not (Test-Path -LiteralPath $desktopDir -PathType Container)) {
    throw '실제 바탕화면 폴더를 확인할 수 없습니다.'
}
$shortcutPath = Join-Path $desktopDir 'Codex.lnk'
$iconTarget = Join-Path $env:USERPROFILE '.codex\assets\icons\codex-official.ico'
$wtCommand = Get-Command wt.exe -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
$codexCommand = Get-Command codex.cmd, codex.exe -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $wtCommand -or -not (Test-Path -LiteralPath $wtCommand.Source -PathType Leaf)) {
    throw 'Windows Terminal(wt.exe)이 없습니다. 자동 설치하지 않습니다.'
}
if (-not $codexCommand -or -not (Test-Path -LiteralPath $codexCommand.Source -PathType Leaf)) {
    throw 'cmd에서 실행할 Codex CLI(codex.cmd 또는 codex.exe)가 없습니다.'
}
& $env:ComSpec /d /c ('chcp 65001 > nul & "{0}" --version' -f $codexCommand.Source)
if ($LASTEXITCODE -ne 0) { throw 'cmd에서 codex --version 실행에 실패했습니다.' }
if (-not (Test-Path -LiteralPath $iconTarget -PathType Leaf)) {
    throw "Codex 공식 아이콘 ICO가 없습니다: $iconTarget"
}
$wtPath = $wtCommand.Source

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
$arguments = '-w 0 nt --title "Codex CLI" -d "{0}" cmd /d /k "chcp 65001 > nul & \"{1}\""' -f ($workingDir.TrimEnd('\') + '\.').Replace(';', '\;'), $codexCommand.Source.Replace(';', '\;')
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $wtPath
$shortcut.Arguments = $arguments
$shortcut.WorkingDirectory = $workingDir
$shortcut.IconLocation = "$iconTarget,0"
$shortcut.Description = 'Codex CLI'
$shortcut.WindowStyle = 1
$shortcut.Save()
```

## 검증

생성·갱신 후 아래 검증을 별도로 실행한다. `$workingDir`은 생성 시와 같은 사용자 지정값을 넣거나, 기본값이면 빈 문자열을 유지한다. 파일이 없거나 속성이 목표와 다르면 `throw`로 실패하며 완료로 보고하지 않는다. 아이콘 경로는 마지막 쉼표의 인덱스만 분리하므로 경로 자체에 쉼표가 있어도 검증한다.

```powershell
$ErrorActionPreference = 'Stop'
$workingDir = '' # 생성 시 지정한 사용자 폴더와 같게 입력한다.
$desktopDir = [Environment]::GetFolderPath('DesktopDirectory')
if (-not $desktopDir -or -not (Test-Path -LiteralPath $desktopDir -PathType Container)) {
    throw '실제 바탕화면 폴더를 확인할 수 없습니다.'
}
$shortcutPath = Join-Path $desktopDir 'Codex.lnk'
$iconTarget = Join-Path $env:USERPROFILE '.codex\assets\icons\codex-official.ico'
$wtCommand = Get-Command wt.exe -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
$codexCommand = Get-Command codex.cmd, codex.exe -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $wtCommand -or -not (Test-Path -LiteralPath $wtCommand.Source -PathType Leaf)) {
    throw 'Windows Terminal(wt.exe)을 확인할 수 없습니다.'
}
if (-not $codexCommand -or -not (Test-Path -LiteralPath $codexCommand.Source -PathType Leaf)) {
    throw 'cmd에서 실행할 Codex CLI를 확인할 수 없습니다.'
}
& $env:ComSpec /d /c ('chcp 65001 > nul & "{0}" --version' -f $codexCommand.Source)
if ($LASTEXITCODE -ne 0) { throw 'cmd에서 codex --version 실행에 실패했습니다.' }
if (-not (Test-Path -LiteralPath $shortcutPath -PathType Leaf)) {
    throw "Codex.lnk가 없습니다: $shortcutPath"
}
if (-not $workingDir) { $workingDir = Join-Path $desktopDir 'Agent' }
if (-not (Test-Path -LiteralPath $workingDir -PathType Container)) {
    throw "작업 폴더가 없습니다: $workingDir"
}
$workingDir = (Resolve-Path -LiteralPath $workingDir).Path
$expectedArguments = '-w 0 nt --title "Codex CLI" -d "{0}" cmd /d /k "chcp 65001 > nul & \"{1}\""' -f ($workingDir.TrimEnd('\') + '\.').Replace(';', '\;'), $codexCommand.Source.Replace(';', '\;')
$shell = New-Object -ComObject WScript.Shell
$check = $shell.CreateShortcut($shortcutPath)
if ($check.TargetPath -ne $wtCommand.Source -or -not (Test-Path -LiteralPath $check.TargetPath -PathType Leaf)) {
    throw 'TargetPath가 확인된 wt.exe 경로와 다릅니다.'
}
if ($check.Arguments -cne $expectedArguments -or $check.Arguments -match 'Codex\.bat') {
    throw 'Arguments가 UTF-8 Codex CLI 직접 실행 인자와 다르거나 Codex.bat를 참조합니다.'
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
[PSCustomObject]@{
    ShortcutPath = $shortcutPath
    TargetPath = $check.TargetPath
    Arguments = $check.Arguments
    WorkingDirectory = $check.WorkingDirectory
    IconLocation = $check.IconLocation
    ExistsTarget = Test-Path -LiteralPath $check.TargetPath -PathType Leaf
    ExistsIcon = Test-Path -LiteralPath $iconPath -PathType Leaf
    StillCallsBat = ($check.Arguments -match 'Codex\.bat')
}
```

속성 검증 후 바로가기를 열어 Windows Terminal의 `Codex CLI` 탭, 실제 시작 작업 폴더와 Codex CLI 실행을 확인한다. 실행 확인이 실패하거나 아직 수행하지 않았으면 해당 검증은 미완료로 보고한다. 전역 지침·바로가기 위치, 작업 폴더, 공식 아이콘 출처와 검증 결과를 함께 보고한다.

Windows가 예전 아이콘을 캐시하면 바탕화면에서 새로고침하거나 아래 명령을 실행한다.

```powershell
& "$env:WINDIR\System32\ie4uinit.exe" -show
```

## 삭제 기준

`Codex.lnk`가 `wt.exe`를 직접 실행하고 `StillCallsBat = False`로 확인되면 기존 `Codex.bat`는 실행에 필요하지 않다. 환경 세팅 요청만으로 삭제하지 않으며 사용자가 명시적으로 승인한 뒤 별도 작업으로 처리한다.
