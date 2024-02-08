@echo off

cd C:\Users\%username%\OneDrive\Desktop\Hackasaumon\hackasaumon

del History.db
xcopy "C:\Users\%username%\AppData\Local\Google\Chrome\User Data\Default\History"

rename History History.db

python3 scanweb.py

start hello.txt