@echo off
chcp 65001 >nul
cd /d "%~dp0"
rename_translit.exe
pause

