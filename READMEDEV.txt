Tous d'abords nous devons récupérer tous les élements dont nous avons besoin:

-cela va inclure les dossier lu ces dernières 24h, en récuéprant les dossiers ouvert quand nous verouillons l'ordinateur

Pour récupérer cela nous avons réalisé un programme python qui va aller chercher le fichier ressent grâce à un chemin pour pouvoir accéder au drnier fichier visité.
Puis pour qu'il se mettent à jours nous avons utilisé un scripts pour que lorsque nous ouvrons de nouveaux fichier cela soit pris en compte autiomatiquement.


-nous allons égalements avoir les url lu ces dernières 24h

Pour cela nous avons réalisé un programme en python qui grâce à un chemin va aller chercher le dossier history où est contenu l'historique de mon navigateur chrome.
Nous avons ajouté une fonction pour que si les url ont été visité plusieurs fois il ne l'affiche seuelement une fois, en gros nous avons enlevé les doublons.
Pour finir pour que notre dossier history ce mettent à jours en continue en fonction de ce que nous allons voir sur chrome nous avons utilisé un script.

Toute nos données vont être lu et une IA, ici ChatGpt va résumé ce que nous avons visité grâce à un paragraphe d'une cinquentaine de mots:

-pour que ChatGpt fonctionne avec notre programme nous avons du importé sont API:
