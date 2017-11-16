# imports
from Piece import Piece

__author__ = 'Emma'
__project__ = 'Draughts'

# Memory Class
class Memory:
    def __init__(self):
        # set memory variables
        self.usedPieces = []
        self.turn = 0

    # method to update used pieces
    def updateUsed(self, piece, turn):
        # if there's already a list for this turn append
        if len(self.usedPieces) == turn + 1:
            self.usedPieces[turn].append(piece)
        # else append new list
        else:
            self.usedPieces.append([])
            self.usedPieces[turn].append(piece)

    # method to delete last move
    def deleteLastMove(self):
        # remove movement from pieces
        for p in self.usedPieces[len(self.usedPieces) - 1]:
            p.turn.pop(len(self.usedPieces) - 1, None)
        # delete turn
        del self.usedPieces[len(self.usedPieces) - 1]


# Tree Class
class Tree:
    def __init__(self, value):
        # set tree variables
        self.nodes = []
        self.value = value
        self.score = 0
