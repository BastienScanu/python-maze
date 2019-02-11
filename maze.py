# -*-coding:Utf-8 -*

from wall import Wall
from corridor import Corridor
from door import Door
from trap import Trap
from exit import Exit

"""Ce module contient la classe Maze."""

class Maze:

    """Classe représentant un labyrinthe."""

    def __init__(self, gridString):
        self.done = False  #labyrinthe réussi ou non

        def createSquare(char):
          """ fonction auxilliaire pour créer chaque case du labyrinthe
              à modifier si on veut ajouter des nouveaux types de cases
          """
          if char == 'O':
            return Wall()
          elif char == '.':
            return Door()
          elif char == 'U':
            return Exit()
          elif char == 'T':
            return Trap()
          else:
            # Tout autre caractère (y compris le X du robot) est un couloir
            # On part du principe que le robot commence forcément dans un couloir
            return Corridor()

        
        self.grid = []
        lines = gridString.splitlines()
        for i, line in enumerate(lines):
          # on parcourt chaque ligne de la carte
          self.grid.append([])
          for j, char in enumerate(line):
            # puis chaque caractère, pour créer chaque case
            if char == "X":
              # quand on tombe sur le robot, on sauvegarde sa position
              self.robot = (i, j)
            symbol = createSquare(char)
            self.grid[i].append(symbol)

    def __repr__(self):
      """ Affichage de la grille du labyrinthe
      """
      mazeString = ""
      for i, line in enumerate(self.grid):
        for j, square in enumerate(line):
          if (i, j) == self.robot:
            mazeString += "X"
          else:
           mazeString += square.symbol
        if i < len(self.grid) - 1:
          mazeString += "\n"
      return mazeString

    def moveRobot(self, direction):
      """ Fonction pour déplacer le robot d'une case
      """

      # calcul des coordonnées d'arrivée selon la direction choisie
      if direction.upper() == "E":
        i, j = self.robot[0], self.robot[1] + 1
      elif direction.upper() == "O":
        i, j = self.robot[0], self.robot[1] - 1
      elif direction.upper() == "N":
        i, j = self.robot[0] - 1, self.robot[1]
      elif direction.upper() == "S":
        i, j = self.robot[0] + 1, self.robot[1]
      else:
        print "You must enter a valid direction : E, O, N or S. To quit, press Q."

      try:
        # on vérifie à quel type de case correspond la destination
        destination = self.grid[i][j]
        if destination.canPass:
          # Si on peut passer, on déplace le robot
          self.robot = (i, j)
          print self
        if destination.message:
          # On affiche le message s'il y en a un
          print destination.message
        # Si la case met fin à la partie, on passe le labyrinthe à done
        self.done = destination.endGame
        # On renvoie un booléen : si la case est un obstacle, inutile de continuer d'aller dans cette direction
        return not destination.canPass

      except:
        print "You cannot go out of the map!"
        return True

      