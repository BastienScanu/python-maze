# -*-coding:Utf-8 -*

from square import Square

"""Ce module contient la classe Exit."""


class Exit(Square):
    """Classe représentant une sortie du labyrinthe"""

    def __init__(self):

        Square.__init__(self, "exit", "U", "Congratulations, you won!")
        self.canPass = True
        self.endGame = True
