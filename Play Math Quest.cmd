@echo off
set "P=%~dp0src\index.html"
set "P=%P:\=/%"
set "Q="
if exist "%~dp0backups\sync-key.txt" set /p K=<"%~dp0backups\sync-key.txt"
if defined K set "Q=?sync=%K%"
start "" msedge --app="file:///%P%%Q%" --window-size=1300,900
