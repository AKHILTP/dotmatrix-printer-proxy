@echo off
echo Installing Python 3.8.20 silently...

REM Run Python installer silently and add to PATH
installers\python-3.8.20.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

REM Check Python version
python --version

pause
