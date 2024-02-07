import sqlite3
import time
import datetime

def doublon(list):
    url = []
    final = []
    for i in list:
        if i[0] not in url:
            url.append(i[0])
            final.append(i)
    return final

def scanWeb():
    conn = sqlite3.connect("History.db")
    cursor = conn.cursor()

    start_of_day = int(datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp())

    cursor.execute("SELECT urls.url, urls.title FROM urls INNER JOIN visits ON urls.id = visits.url WHERE visits.visit_time >= ?", (start_of_day,))
    urls = cursor.fetchall()

    urls = urls[-20:]

    urls = doublon(urls)

    unique_urls = set()

    for url in urls:
        index_com = url[0].find(".com")
        if index_com != -1:
            modified_url = url[0][:index_com + 4]
            unique_urls.add((modified_url, url[1]))

    conn.close()

    return unique_urls
