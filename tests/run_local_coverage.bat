@echo off
REM run_local_coverage.bat
REM Thanks to nedbat @irc #python
coverage run run_tests.py
coverage html
start htmlcov/index.html
