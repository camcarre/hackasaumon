import sqlite3

# Connexion à la base de données
conn = sqlite3.connect("History.db")
cursor = conn.cursor()

# Requête pour sélectionner les URL visitées
cursor.execute("SELECT url, title, visit_count FROM urls")
urls = cursor.fetchall()

# Affichage des URL visitées
for url in urls:
    print(url)

# Fermeture de la connexion
conn.close()

