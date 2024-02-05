import os
import json

indexed_db_path = "C:/Users/delpo/AppData/Local/Google/Chrome/User Data/Default/IndexedDB"

def parcourir_dossier(dossier):
    for element in os.listdir(dossier):
        chemin = os.path.join(dossier, element)
        if os.path.isdir(chemin):
            parcourir_dossier(chemin)
        else:
            try:
                with open(chemin, "r", encoding="utf-8") as fichier:
                    contenu = fichier.read()
                    try:
                        data = json.loads(contenu)
                        if 'entries' in data:
                            for entry in data['entries']:
                                if 'url' in entry:
                                    print(entry['url'])
                    except json.JSONDecodeError:
                        pass
            except UnicodeDecodeError:
                print(f"Ignoré le fichier {chemin} car il ne peut pas être décodé avec UTF-8")
                pass


parcourir_dossier(indexed_db_path)

