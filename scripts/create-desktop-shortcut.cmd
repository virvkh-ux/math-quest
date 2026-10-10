@echo off
set "ROOT=%~dp0.."
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$root=(Resolve-Path '%ROOT%').Path; $html=('file:///' + ($root + '\src\index.html').Replace('\','/'));" ^
  "$edge=(Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\msedge.exe').'(default)';" ^
  "$lnk=Join-Path ([Environment]::GetFolderPath('Desktop')) 'Play Math Quest.lnk';" ^
  "$s=(New-Object -ComObject WScript.Shell).CreateShortcut($lnk); $s.TargetPath=$edge; $s.Arguments=('--app=\"' + $html + '\" --window-size=1300,900');" ^
  "$s.IconLocation=($root + '\assets\math-quest.ico'); $s.Description='Math Quest'; $s.Save(); Write-Host ('Shortcut created: ' + $lnk)"
timeout /t 5
