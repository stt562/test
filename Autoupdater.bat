@Title Autoupdater
@echo off
@color 9f
cls
timeout 10
cls
echo Updating...
timeout 10 >nul /nobreak
Set /a %curl%=>>Autoupdater.bat

echo @title Updating>>tempfile.cmd
echo @echo off>>tempfile.cmd
echo @color 9f>>tempfile.cmd
echo cls>>tempfile.cmd
echo timeout 10>>tempfile.cmd
echo curl https://raw.githubusercontent.com/stt562/test/refs/heads/main/Autoupdater.bat %curl%>>tempfile.cmd
echo cmd /c exit tempfile.cmd>>tempfile.cmd

start tempfile.cmd

echo it worked
cls
