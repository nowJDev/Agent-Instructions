<!-- 이 문서는 Windows에서 Codex 실행용 바로가기를 공식 아이콘 기반으로 구성하는 절차를 정리한다. -->
# Codex Windows Shortcut

Windows의 `.bat` 파일은 파일 자체에 개별 아이콘을 안정적으로 지정하기 어렵다. Codex를 바탕화면에서 실행할 때는 `.bat`를 직접 두기보다, 공식 Codex 아이콘을 쓰는 `.lnk` 바로가기가 Windows Terminal을 직접 실행하도록 만든다.

## 목표 상태

- 바탕화면에는 `Codex.lnk`만 실행 진입점으로 둔다.
- `Codex.lnk`는 `Codex.bat`를 호출하지 않고 `wt.exe`를 직접 실행한다.
- 아이콘은 사용자 전역 위치인 `%USERPROFILE%\.codex\assets\icons\codex-official.ico`에 보관한다.
- 시작 작업 폴더는 `%USERPROFILE%\Desktop\Agent`로 둔다.
- 실행 시 UTF-8 코드페이지를 적용한 뒤 `codex` 명령을 실행한다.

기존 배치 파일이 하던 일은 아래와 같다.

```bat
@echo off
start "" wt.exe -w 0 nt --title "Codex CLI" -d "%USERPROFILE%\Desktop\Agent" cmd /k "chcp 65001 > nul & codex"
exit /b
```

바로가기는 같은 동작을 아래 Target/Arguments 조합으로 수행한다.

```text
TargetPath: %LOCALAPPDATA%\Microsoft\WindowsApps\wt.exe
Arguments: -w 0 nt --title "Codex CLI" -d "%USERPROFILE%\Desktop\Agent" cmd /k "chcp 65001 > nul & codex"
WorkingDirectory: %USERPROFILE%\Desktop\Agent
IconLocation: %USERPROFILE%\.codex\assets\icons\codex-official.ico,0
```

## 다른 PC에서 요청할 프롬프트

다른 PC의 에이전트에게는 아래처럼 요청한다.

```text
바탕화면의 Codex 실행용 bat 파일을 공식 Codex 아이콘을 쓰는 Windows 바로가기로 바꿔줘.

요구사항.
- .bat 자체 아이콘 변경이 아니라 Codex.lnk 바로가기를 만들거나 갱신해줘.
- 바로가기는 bat 파일을 호출하지 말고 Windows Terminal(wt.exe)을 직접 실행하게 해줘.
- 실행 동작은 기존 bat와 같아야 해.
- 작업 폴더는 %USERPROFILE%\Desktop\Agent 야.
- 실행 명령은 Windows Terminal 새 탭 제목을 "Codex CLI"로 두고, cmd /k "chcp 65001 > nul & codex" 를 실행하는 형태야.
- 공식 Codex 아이콘은 %USERPROFILE%\.codex\assets\icons\codex-official.ico 에 저장해줘.
- 아이콘 원본이 필요하면 OpenAI 공식 Codex 페이지에서 현재 공식 Codex 앱 아이콘을 확인해서 PNG를 저장한 뒤 ICO로 변환해줘.
- 완료 전 Codex.lnk가 Codex.bat를 참조하지 않는지 확인해줘.
- 확인되면 기존 Codex.bat는 삭제해도 된다고 알려줘. 삭제는 내가 별도로 승인할 때만 해줘.
```

## PowerShell 구성 예시

아래 스크립트는 이미 `codex-official.ico`가 준비되어 있을 때 바로가기를 만든다.

```powershell
$shortcutPath = Join-Path $env:USERPROFILE 'Desktop\Codex.lnk'
$iconTarget = Join-Path $env:USERPROFILE '.codex\assets\icons\codex-official.ico'
$wtPath = Join-Path $env:LOCALAPPDATA 'Microsoft\WindowsApps\wt.exe'
$workingDir = Join-Path $env:USERPROFILE 'Desktop\Agent'

if (-not (Test-Path -LiteralPath $iconTarget)) {
    throw "Codex 공식 아이콘 ICO가 없습니다: $iconTarget"
}

$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $wtPath
$shortcut.Arguments = "-w 0 nt --title `"Codex CLI`" -d `"$workingDir`" cmd /k `"chcp 65001 > nul & codex`""
$shortcut.WorkingDirectory = $workingDir
$shortcut.IconLocation = "$iconTarget,0"
$shortcut.Description = 'Codex CLI'
$shortcut.WindowStyle = 1
$shortcut.Save()
```

아이콘 원본이 PNG라면 Pillow로 ICO를 만들 수 있다.

```powershell
$pngPath = Join-Path $env:USERPROFILE '.codex\assets\icons\codex-official.png'
$icoPath = Join-Path $env:USERPROFILE '.codex\assets\icons\codex-official.ico'

python -c "from PIL import Image; img=Image.open(r'$pngPath').convert('RGBA'); img.save(r'$icoPath', format='ICO', sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])"
```

## 검증

아래 검증에서 `StillCallsBat`가 `False`여야 한다.

```powershell
$shortcutPath = Join-Path $env:USERPROFILE 'Desktop\Codex.lnk'
$shell = New-Object -ComObject WScript.Shell
$check = $shell.CreateShortcut($shortcutPath)

[PSCustomObject]@{
    TargetPath = $check.TargetPath
    Arguments = $check.Arguments
    WorkingDirectory = $check.WorkingDirectory
    IconLocation = $check.IconLocation
    ExistsTarget = Test-Path -LiteralPath $check.TargetPath
    ExistsIcon = Test-Path -LiteralPath (($check.IconLocation -split ',')[0])
    StillCallsBat = ($check.Arguments -match 'Codex\.bat')
}
```

Windows가 예전 아이콘을 캐시하면 바탕화면에서 새로고침하거나 아래 명령을 실행한다.

```powershell
& "$env:WINDIR\System32\ie4uinit.exe" -show
```

## 삭제 기준

`Codex.lnk`가 `wt.exe`를 직접 실행하고 `StillCallsBat = False`로 확인되면 기존 `Codex.bat`는 실행에 필요하지 않다. 다만 삭제는 되돌리기 어려우므로 사용자가 명시적으로 승인한 뒤 별도 작업으로 처리한다.
