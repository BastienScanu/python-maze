# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from maze import Maze

class Map:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, name, string):
      self.name = name
      self.maze = Maze(string)

    def __repr__(self):
        return "<Map {}>".format(self.name)

    def __str__(self):
      return self.name + "\n" + self.maze.__repr__()


