@Title Autoupdater
@echo off
@color 9f
cls
set /a ver=Alpha
timeout 10
cls
echo Updating... & echo: & curl https://raw.githubusercontent.com/stt562/test/refs/heads/main/Autoupdater.bat>Autoupdater.bat
start "" /WAIT time /T>t.txt & timeout 10 >nul & exit
set /a t=<t.txt
del t.txt
cls
echo Updated!
echo:
echo Infos to the Update
echo:
echo -------------------
echo:
echo Version: %ver%
echo Updated at %t%
timeout 10
cls
exit
