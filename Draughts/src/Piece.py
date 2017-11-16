
__author__ = 'Emma'
__project__ = 'Draughts'


class Piece:
    def __init__(self, xy, col, king, player):
        # set piece current coords
        self.xy = xy
        # set piece colour
        self.col = col
        # set piece memory
        self.turnTaken = 0
        self.turn = {0: xy}
        self.king = 0
        # set piece king
        self.kingLetter = king
        # 1 for player 1 and -1 for player 2
        self.player = player

    def __str__(self):
        # return correct string depending on weather or not it's a king
        if self.king == 0:
            return self.col
        else:
            return self.kingLetter
