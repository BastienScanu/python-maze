# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

from functions import *

endGame = False

# On charge les maps existantes
maps = loadMaps()

# Si il y a une partie sauvegardée, on la charge
map = loadGame(maps)
if map:
  # Partie trouvée en sauvegarde, on propose de continuer cette partie
  map = continueGame(map)
if not map:
  # S'il n'y a pas de partie sauvegardée, ou si le joueur ne veut pas continuer sa partie
  # Alors on propose de choisir une carte
  map = chooseMap(maps)

while not endGame:
  # Tant que la partie n'est pas finie, on demande au joueur d'entrer une commande
  endGame = pickYourMove(map)
  # Et on sauvegarde la partie
  saveGame(map)