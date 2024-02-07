@echo off
cd /d "%~dp0"
DEL LastUsed.txt
type NUL > LastUsed.txt

Powershell.exe -executionpolicy remotesigned -File power.ps1

python3 main.py

start LastUsed.txt