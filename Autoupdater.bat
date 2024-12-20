@Title Autoupdater
@echo off
@color 9f
cls
set /a version=Alpha
timeout 10
cls
echo Updating... & echo: & curl https://raw.githubusercontent.com/stt562/test/refs/heads/main/Autoupdater.bat>Autoupdater.bat
time /T>>time.txt
set /a t=<time.txt
del time.txt
cls
echo Updated!
echo:
echo Infos to the Update
echo:
echo -------------------
echo:
echo Version: %version%
echo Updated at %t%
timeout 10
cls
exit
