# -*-coding:Utf-8 -*

"""Ce fichier contient les fonctions utilisées par le serveur

"""

import os

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
  