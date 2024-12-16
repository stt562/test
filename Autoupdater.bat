@Title Autoupdater
@echo off
@color 9f
cls
timeout 10
cls
echo Updating...
timeout 10 >nul /nobreak


echo timeout 10>>tempfile.cmd
echo curl https://raw.githubusercontent.com/stt562/test/refs/heads/main/Autoupdater.bat>>Autoupdater.bat>>tempfile.cmd
echo del tempfile.cmd>>tempfile.cmd

start tempfile.cmd
echo it worked
cls
