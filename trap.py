# -*-coding:Utf-8 -*

from square import Square

"""Ce module contient la classe Trap."""

class Trap(Square):
 
 """Classe représentant un piège du labyrinthe"""

 def __init__(self):

    Square.__init__(self, "trap", "T", "It's a trap! You lost the game :(")
    self.canPass = False
    self.endGame = True