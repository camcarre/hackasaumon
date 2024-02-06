@echo off
DEL LastUsed.txt
type NUL > LastUsed.txt

Powershell.exe -executionpolicy remotesigned -File power.ps1