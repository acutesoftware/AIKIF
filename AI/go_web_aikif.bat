@echo off
echo Starting web server for AIKIF
echo call this from AIKIF folder, eg. T:\user\dev\src\python\AI\AI
rem echo "TODO - get flask working with Python 3.3"
start http://127.0.0.1:5000
C:\python34\python.exe web_app\web_aikif.py
