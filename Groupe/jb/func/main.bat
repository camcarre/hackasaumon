@echo off

cd "C:\Users\%username%\Desktop\Hackasaumon\hackasaumon"
cd "data"
del LastUsed.txt
type NUL > LastUsed.txt

del History.db
xcopy "C:\Users\%username%\AppData\Local\Google\Chrome\User Data\Default\History"

rename History History.db
cd "../func"
Powershell.exe -executionpolicy remotesigned -File power.ps1

python3 mainPY.py

pause