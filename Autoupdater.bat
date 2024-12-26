@Title Autoupdater
@echo off
@color 9f
cls
timeout 10
cls
echo Updating... & echo: & curl https://raw.githubusercontent.com/stt562/test/refs/heads/main/Autoupdater.bat>Autoupdater.bat
set "ver=Alpha"
cls
echo Updated!
echo:
echo Infos to the Update
echo:
echo -------------------
echo:
echo Version: %ver%
echo Updated at %time%
timeout 10
cls
exit
