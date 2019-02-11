# -*-coding:Utf-8 -*

from square import Square

"""Ce module contient la classe Door."""

class Door(Square):
 
 """Classe représentant une porte du labyrinthe"""

 def __init__(self):

    Square.__init__(self, "door", ".", "")
    self.canPass = True