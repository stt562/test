ping www.google.com
if %errorlevel%==0
	curl -O https://raw.githubusercontent.com/stt562/test/refs/heads/main/Autoupdater.bat
	pause
