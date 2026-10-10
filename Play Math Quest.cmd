@echo off
set "P=%~dp0src\index.html"
set "P=%P:\=/%"
start "" msedge --app="file:///%P%" --window-size=1300,900
