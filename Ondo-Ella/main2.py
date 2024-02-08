

import os

nom_fichier = input("Entrez le nom du fichier que vous souhaitez créer : ")

with open(nom_fichier, 'w') as fichier:
    contenu_utilisateur = input(f"Écrivez quelque chose dans le fichier {nom_fichier} : ")
   
    fichier.write(contenu_utilisateur)

print(f"Le fichier {nom_fichier} a été créé et le contenu a été écrit.")
