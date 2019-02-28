# -*-coding:Utf-8 -*

"""Ce fichier contient les fonctions nécessaires au déroulement du jeu

"""

import os
import pickle

from map import Map

def loadMaps():
  """ Chargement des cartes depuis le dossier maps """
  maps = []
  for fileName in os.listdir("maps"):
      if fileName.endswith(".txt"):
          chemin = os.path.join("maps", fileName)
          with open(chemin, "r") as file:
              content = file.read()
              map = Map(fileName, content)
              maps.append(map)
  return maps

def chooseMap(maps):
  """ Choix de la carte """
  print("Existing mazes:")
  for i, map in enumerate(maps):
      print("  {} - {}".format(i + 1, map.name))
  while 1:
    i = raw_input("Enter the number of the maze you want to play")
    try:
      i = int(i)
      print maps[i-1]
      if i <= len(maps):
        chosenMap = maps[i - 1]
        print "You chose the map {}:\n{}".format(chosenMap.name, chosenMap.maze)
        return chosenMap
      else:
        print "The number must be between 1 and {}.".format(len(maps))
    except:
      print "You must enter a digit between 1 and {}.".format(len(maps))
      
def pickYourMove(map):
  """ Tour de jeu : on demande au joueur d'entrer sa commande """
  done = False    # True quand le tour de jeu est fini
  endGame = False # True si le joueur quitte la partie
  while not done:
    move = raw_input("What is your move?")

    if move.upper() == "Q":
      # Fin du jeu
      print "Thanks for playing ! Your game has been saved, see you later !"
      endGame = True
      done = True

    else:
      direction = move.upper()[0]
      if direction in ["E", "O", "S", "N"]:
        # La première lettre doit forcément être une des 4 directions
        if len(move) > 1:
          # la commande contient plus d'une lettre
          i = 0
          try:
            distance = int(move[1:])
            # Si c'est un entier, on récupère cette distance X et on applique le déplacement X fois
            while i < distance and not done:
              done = map.maze.moveRobot(direction)
              # Si done est à True, c'est qu'on a rencontré un obstacle, pas la peine de continuer la boucle
              i += 1
            done = True
            print "c"
          except:
            print "You must enter a valid integer after the direction"
        else:
          # On déplace le robot d'une case dans la direction demandée
          map.maze.moveRobot(direction)
          done = True
      else:
        print "You must enter a valid direction : E, O, N or S. To quit, press Q."
  return endGame or map.maze.done
