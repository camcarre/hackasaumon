import subprocess

def runBat():
    subprocess.run([r"script.bat"])

def readTxt():
    listRecent = []
    with open("LastUsed.txt", "r", encoding="utf-16-le") as f:
        for line in f:
            folder = line.strip()
            folder_name = folder[:-4] if folder.endswith(".lnk") else folder
            listRecent.append(folder_name)
    listRecent.reverse()
    return listRecent


