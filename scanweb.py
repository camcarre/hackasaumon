import sqlite3
import time
import datetime

conn = sqlite3.connect("History.db")
cursor = conn.cursor()

start_of_day = int(datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp())

cursor.execute("SELECT urls.url, urls.title, urls.visit_count FROM urls INNER JOIN visits ON urls.id = visits.url WHERE visits.visit_time >= ?", (start_of_day,))
urls = cursor.fetchall()

urls_today = [url for url in urls if url[2] >= start_of_day]
for i in urls[-20:]:
    print(i)
conn.close()



