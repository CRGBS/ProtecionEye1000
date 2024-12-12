@echo on
setlocal enabledelayedexpansion

rem Initialize timer duration
set seconds=1800
set title=30-minute Timer

:timer
rem Set window title
title %title%

rem Start the timer
for /l %%i in (1,1,%seconds%) do (
    set /a remaining=%seconds%-%%i
    set /a minutes=remaining/60
    set /a secs=remaining%%60
    cls
    echo Remaining time: !minutes! minutes !secs! seconds
    timeout /t 1 /nobreak >nul
)

if "%title%"=="30-minute Timer" (
    set seconds=600
) else (
    set seconds=1800
)

:reset
if "%title%"=="30-minute Timer" (
    set seconds=1800
) else (
    set seconds=600
)
goto timer
