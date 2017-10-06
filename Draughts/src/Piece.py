

class Piece:

    def __init__(self, xy, col):
        self.xy = xy
        self.col = col
        self.taken = False
        self.turn = {0: xy}
