""" Classe BallGame herda de Game """

from game import Game 

class BallGame( Game ):
    def __init__(self):
        Game.__init__(self)

game = BallGame()