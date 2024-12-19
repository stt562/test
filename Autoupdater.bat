@Title Autoupdater
@echo off
@color 9f
cls
timeout 10
cls
echo Updating... & curl https://raw.githubusercontent.com/stt562/test/refs/heads/main/Autoupdater.bat>Autoupdater.bat

echo Updated!
timeout 10
