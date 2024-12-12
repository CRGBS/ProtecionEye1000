@echo off
setlocal enabledelayedexpansion

rem Initialize timer duration
set seconds=1800
set title=30-minute work Timer

:timer
rem Set window title
title %title%

rem Start the timer
for /l %%i in (1,1,%seconds%) do (
    timeout /t 1 >nul
    set /a remaining=%seconds%-%%i
    set /a minutes=remaining/60
    set /a secs=remaining%%60
	cls
    echo Remaining time: !minutes! minutes !secs! seconds
    echo Press R to reset the timer, 1 for 10 minutes rest, 2 for 30 minutes work
    set "input="
    set /p "input=Enter command: " <nul
    if /i "!input!"=="R" goto reset
    if /i "!input!"=="1" goto set10
    if /i "!input!"=="2" goto set30
)

echo Timer finished!
pause
goto timer

:set10
set seconds=600
set title=10-minute rest Timer
goto timer

:set30
set seconds=1800
set title=30-minute work Timer
goto timer

:reset
goto timer
