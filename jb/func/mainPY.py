import sqlite3
import time
import datetime
import subprocess

def runBat():
    subprocess.run([r"script.bat"])

def readTxt():
    listRecent = []
    with open("../data/LastUsed.txt", "r", encoding="utf-16-le") as f:
        for line in f:
            folder = line.strip()
            folder_name = folder[:-4] if folder.endswith(".lnk") else folder
            if "\ufeff" in folder_name:
                folder_name = folder_name.replace("\ufeff","")
            listRecent.append(folder_name)

    listRecent.reverse()
    return listRecent

def doublon(list):
    url = []
    final = []
    for i in list:
        if i[0] not in url:
            url.append(i[0])
            final.append(i)
    return final

def scanWeb():
    conn = sqlite3.connect("../data/History.db")
    cursor = conn.cursor()

    start_of_day = int(datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp())

    cursor.execute("SELECT urls.url, urls.title FROM urls INNER JOIN visits ON urls.id = visits.url WHERE visits.visit_time >= ?", (start_of_day,))
    urls = cursor.fetchall()

    urls = urls[-20:]

    urls = doublon(urls)

    unique_urls = []

    for url in urls:
        index_com = url[0].find(".com")
        if index_com != -1:
            modified_url = url[0][:index_com + 4]
            unique_urls.append((modified_url, url[1]))

    conn.close()

    return unique_urls

def WriteTxt(list,file):
    if type(list[0]) == str:
        with open(file,"w") as text:
            for i in list:
                text.write(str(i) + '\n')
    if type(list[0]) == tuple:
        with open(file,"w") as text:
            for i in range(len(list)):
                text.write(str(list[i][0]) + ' | ' + str(list[i][1] + "\n"))

    return
