# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

from functions import *

endGame = False

# On charge les maps existantes
maps = loadMaps()

# On propose de choisir une carte
map = chooseMap(maps)

while not endGame:
  # Tant que la partie n'est pas finie, on demande au joueur d'entrer une commande
  endGame = pickYourMove(map)