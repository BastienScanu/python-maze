# -*-coding:Utf-8 -*

from square import Square

"""Ce module contient la classe Corridor."""


class Corridor(Square):
    """Classe représentant un couloir du labyrinthe"""

    def __init__(self):
        Square.__init__(self, "corridor", " ", "")
        self.canPass = True
