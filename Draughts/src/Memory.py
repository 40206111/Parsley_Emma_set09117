from Piece import Piece


class Memory:

    def __init__(self, blackPieces, whitePieces):
        self.blackPieces = blackPieces
        self.whitePieces = whitePieces
        self.allPieces = blackPieces + whitePieces
        self.usedPieces = []
        self.usedPieces.append([])
        self.turn = 0

    def setPieces(self, blackPieces, whitePieces):
        self.blackPieces = blackPieces
        self.whitePieces = whitePieces
        self.allPieces = blackPieces + whitePieces
        self.usedPieces.clear()

    def updateUsed(self, piece, turn):
        if len(self.usedPieces) == turn + 1:
            self.usedPieces[turn].append(piece)
        else:
            self.usedPieces.append([])
            self.usedPieces[turn].append(piece)