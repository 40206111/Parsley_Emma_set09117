__author__ = 'Emma'
__project__ = 'Draughts'

class Piece:

    def __init__(self, xy, col, king, player):
        self.xy = xy
        self.col = col
        self.turnTaken = 0
        self.turn = {0: xy}
        self.king = 0
        self.kingLetter = king
        # 1 for player 1 and -1 for player 2
        self.player = player

    def __str__(self):
        if self.king == 0:
            return self.col
        else:
            return self.kingLetter
