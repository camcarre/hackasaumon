Pour réaliser notre projet nous avons tous d'abords du récupérer les données qui sont ensuite lu par une IA qui est ChatGpt


-Nous avons du récupérer les fichiers lu ces dernièrs 24h, c'est a dire les fichiers ouvert quand nous vérouillons notre ordinateur pour qu'il puisent être récupéré le lendemain.

Il aura été necessaire de créer un programme python pour récupérer le fichier récent grpace à un chemin qui contiens tous les fichiers visité récemment
Nous avons utilisé un scripts pour que lorsque nous visitonsde nouveaux dossier cela soit pris en compte et s'affiche automatiquement.


-De plus il a été necessaire de récupérer les url lui sur notre navigateur chrome

Pour cela nous avons réalisé également ici un programme python qui va lire grâce à un chemin le dossier history qui contiens l'historique des url de mon navigateur chrome.
Là aussi grâce à un script nous avons pu mettre à jours ce dossier history automatiquement pour que lorsque nous visitons de nouveaux sites cela soit pris en compte.
Si les mêmes url on été visité plusieurs fois dans la journé nous avons fait une fonction qui suprimes les doublons.


-Ensuite nous avons récupéré l'API de ChatGpt pour qu'il puisent nous résumé en 50 mots ce à quoi nous avons accéder la veille à partir des données récupéré précedement.

Encore une fois un programme python à été utilisé ici pour récupérer l'API et utilisé celui-ci dans notre projet


-Pour finir tous cela va s'afficher dans une page html

Nous avons donc créer un serveur avec une page html et un css que nous avons relier à nos fonctions.
Et grâce aux plannificateur des tâches nous avons pu programmer quand notre page html s'ouvre chaque jours pour indiqué à l'utilisateur ce qu'il a fait la veille, ici en géneral on réalisera cela le matin.