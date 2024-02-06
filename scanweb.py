import sqlite3
import time
import datetime
import copy

conn = sqlite3.connect("History.db")
cursor = conn.cursor()

start_of_day = int(datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp())

cursor.execute("SELECT urls.url, urls.title, urls.visit_count FROM urls INNER JOIN visits ON urls.id = visits.url WHERE visits.visit_time >= ?", (start_of_day,))
urls = cursor.fetchall()
urls = urls[-20:]

def doublon(list):
    url = []
    final = []
    for i in list:
        if i[0] not in url:
            url.append(i[0])
            final.append(i)
    return final
urls = doublon(urls)

for i in urls:
    print(i[1])
    print(i[0])

