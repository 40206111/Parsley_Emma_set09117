from Piece import Piece


class Memory:

    def __init__(self):
        self.usedPieces = []
        self.turn = 0

    def updateUsed(self, piece, turn):
        if len(self.usedPieces) == turn + 1:
            self.usedPieces[turn].append(piece)
        else:
            self.usedPieces.append([])
            self.usedPieces[turn].append(piece)

    def deleteLastMove(self):
        for p in self.usedPieces[len(self.usedPieces) - 1]:
            p.turn.pop(len(self.usedPieces) - 1, None)
        del self.usedPieces[len(self.usedPieces) - 1]

class Tree:
    def __init__(self, value):
        self.nodes = []
        self.value = value
        self.score = 0
