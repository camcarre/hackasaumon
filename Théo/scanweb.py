import sqlite3
import time
import datetime

#checks for duplicate URLs and deletes them
def doublon(list):
    url = []
    final = []
    for i in list:
        if i[0] not in url:
            url.append(i[0])
            final.append(i)
    return final

#scans the database and retrieves URLs
def scanWeb():

    #database connection
    conn = sqlite3.connect("History.db")
    cursor = conn.cursor()

    start_of_day = int(datetime.datetime.combine(datetime.date.today(), datetime.time.min).timestamp())
    #Executing sql query
    cursor.execute("SELECT urls.url, urls.title FROM urls INNER JOIN visits ON urls.id = visits.url WHERE visits.visit_time >= ?", (start_of_day,))
    urls = cursor.fetchall()
    #extract only the last 20 urls
    urls = urls[-20:]

    urls = doublon(urls)

    unique_urls = set()
    
    #Parse the URLs so that it displays correctly without additional elements
    for url in urls:
        index_com = url[0].find(".com")
        if index_com != -1:
            modified_url = url[0][:index_com + 4]
            unique_urls.add((modified_url, url[1]))

    conn.close()

    return unique_urls
