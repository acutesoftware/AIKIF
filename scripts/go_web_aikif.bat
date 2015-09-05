@echo off
echo Starting web server for AIKIF

start /min C:\python34\python.exe ..\aikif\web_app\web_aikif.py
echo Server started - press SPACE to start browser
pause
start  http://127.0.0.1:5000