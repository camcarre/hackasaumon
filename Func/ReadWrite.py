import sqlite3
import time
import datetime
import subprocess
from openai import OpenAI

def API(listUrls,listFiles):
  client = OpenAI()

  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
          {"role": "system", "content": "T'es un robot qui fait des résumé"},
          {"role": "user", "content": "voici les sites : " + str(listUrls) + " et les fichiers utilisés : " + str(listFiles) + ", fait moi un résumé de tout ça."},
      ]
  )
  WriteTxtAPI(completion.choices[0].message.content,"../Data/API.txt")

def WriteTxtAPI(response,file):
    with open(file,"w", encoding="utf-8") as text:
        text.write(response)
    return

def readTxt():
    listRecent = []
    with open("../data/LastUsed.txt", "r", encoding="utf-16-le") as f:
        for line in f:
            folder = line.strip()
            folder_name = folder[:-4] if folder.endswith(".lnk") else folder
            if "\ufeff" in folder_name:
                folder_name = folder_name.replace("\ufeff","")

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
    conn = sqlite3.connect("../Data/History.db")
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

def WriteTxtList(list,file):
    if type(list[0]) == str:
        with open(file,"w",encoding="utf-8") as text:
            for i in list:
                text.write(str(i) + '\n')
    if type(list[0]) == tuple:
        with open(file,"w",encoding="utf-8") as text:
            for i in range(len(list)):
                text.write(str(list[i][0]) + ' | ' + str(list[i][1] + "\n"))

    return

url = scanWeb()
files = readTxt()
WriteTxtList(url,"../Data/urls.txt")
WriteTxtList(files,"../Data/LastUsed.txt")
API(url,files)