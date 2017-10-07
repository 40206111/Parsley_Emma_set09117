

class Piece:

    def __init__(self, xy, col):
        self.xy = xy
        self.col = col
        self.turnTaken = 0
        self.turn = {0: xy}
