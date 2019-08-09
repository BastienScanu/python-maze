# -*-coding:Utf-8 -*

from square import Square

"""Ce module contient la classe Wall."""


class Wall(Square):
    """Classe représentant un mur du labyrinthe"""

    def __init__(self):
        Square.__init__(self, "wall", "O", "You cannot go through walls!")
        self.canPass = False
