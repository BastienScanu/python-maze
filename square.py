# -*-coding:Utf-8 -*

"""Ce module contient la classe Maze."""


class Square:
    """Classe représentant une case du labyrinthe"""

    def __init__(self, name, symbol, message):
        self.name = name        # nom du symbole
        self.symbol = symbol    # caractère utilisé
        self.canPass = True     # est-ce qu'on peut passer par cette case ?
        self.message = message  # message affiché au passage sur la case
        self.endGame = False    # fin du jeu au passage sur la case ?

    def __repr__(self):
        return "<Square {}>".format(self.name)

    def __str__(self):
        return self.symbol or " "
