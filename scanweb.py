import sqlite3

chrome_history_path = r"C:\Users\YourUsername\AppData\Local\Google\Chrome\User Data\Default\History"

conn = sqlite3.connect(chrome_history_path)
cursor = conn.cursor()

cursor.execute("SELECT url, title, visit_count FROM urls")
urls = cursor.fetchall()

for url in urls:
    print(url)

conn.close()
