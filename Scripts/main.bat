@echo off

cd "C:\Users\%username%\Desktop\Hackasaumon\hackasaumon"
cd "Data"
del LastUsed.txt
type NUL > LastUsed.txt

del History.db
xcopy "C:\Users\%username%\AppData\Local\Google\Chrome\User Data\Default\History"

rename History History.db
cd "../Func"
Powershell.exe -executionpolicy remotesigned -File GetFiles.ps1

python3 ReadWrite.py
go run server.go
pause