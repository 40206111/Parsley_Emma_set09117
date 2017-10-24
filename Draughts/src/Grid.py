# imports
from __future__ import print_function

from Piece import Piece

__author__ = 'Emma'
__project__ = 'Draughts'


# Grid class
class Grid:

    # grid constructor
    def __init__(self, width, height, rows):
        # set grid dimensions
        self.rows = rows
        self.width = width
        self.setWidth(width)
        self.height = height
        self.setHeight(height)

        # set piece information
        self.pieceNo = int((self.width/2) * self.rows)
        self.blackPiece = "b"
        self.whitePiece = "w"
        self.blackKing = "B"
        self.whiteKing = "W"
        self.validSpace = "o"
        self.whiteSpace = " "
        self.blackSpace = " "

        # set current player
        self.player = 1
        # set current turn
        self.turn = 0

        # create array for pieces
        self.whitePieces = []
        self.blackPieces = []
        # create a set of usable squares
        self.usableSquares = set([])
        # create a set of valid spaces
        self.validPlaces = set([])

        self.ForcedPieces = set([])
        # Create list of grid squares variable
        self.squares = []
        # Create Grid
        self.createGrid()

    # Row Setter
    def setRows(self, rows):
        # set amount of rows counters are on
        if rows < self.height/2:
            self.rows = rows
        elif rows == 0:
            self.rows = 1
        else:
            self.rows = int((self.height/2)-1)
        self.pieceNo = (self.width / 2) * self.rows

    # Height Setter
    def setHeight(self, height):
        # check that height isn't greater than 999
        if height > 999:
            # set height to 999
            self.height = 999
        elif height < 4:
            self.height = 4
        else:
            # set height to given height
            self.height = height
        self.setRows(self.rows)

    # Width Setter
    def setWidth(self, width):
        # check that width isn't larger than the English alphabet
        if width > 26:
            # set width to 26
            self.width = 26
        elif width % 2:
            self.width = width - 1
        elif width < 4:
            self.width = 4
        else:
            # set width to given width
            self.width = width
        self.pieceNo = (self.width / 2) * self.rows

    # create grid method
    def createGrid(self):
        self.player = 1
        # empty squares list
        self.squares = []
        self.whitePieces = []
        self.blackPieces = []
        self.usableSquares = set([])

        # Create amount of rows needed
        for i in range(self.height):
            self.squares.append([])

        # loop through height and width
        for i in range(self.height):
            for j in range(self.width):
                # check if it should be a white square
                if (i % 2 and not j % 2) or (not i % 2 and j % 2):
                    self.squares[i].append(self.whiteSpace)
                # check if square should  contain black piece
                elif i < self.rows:
                    self.blackPieces.append(Piece((i, j), self.blackPiece, self.blackKing, -1))
                    self.squares[i].append(self.blackPieces[len(self.blackPieces) - 1])
                    self.usableSquares.update([(i, j)])
                # check if square should contain white piece
                elif i >= self.height - self.rows:
                    self.whitePieces.append(Piece((i, j), self.whitePiece, self.whiteKing, 1))
                    self.squares[i].append(self.whitePieces[len(self.whitePieces) - 1])
                    self.usableSquares.update([(i, j)])
                # else square is black
                else:
                    self.squares[i].append(self.blackSpace)
                    self.usableSquares.update([(i, j)])

    # print grid method
    def printGrid(self):

        # print gap before letters
        print(' ', end='\t')
        # loop through width
        for i in range(self.width):
            # print ascii letter for row
            print(chr(65 + i), end='  ')
        # new line
        print()
        # loop through height
        for i in range(self.height):
            # print column numbers
            print(i + 1, end='\t')
            # loop through width
            for j in range(self.width):
                # print square contents
                print(self.squares[i][j], end='  ')
            # print column numbers
            print(i + 1, end='\t')
            # new line
            print()
        # print gap before letters
        print(' ', end='\t')
        # loop through width
        for i in range(self.width):
            # print ascii letter for row
            print(chr(65 + i), end='  ')
        # new line
        print()

    def getKingType(self):
        if self.player == 1:
            return self.whiteKing
        else:
            return self.blackKing

    def testAvailable(self, i, j):
        if (i, j) in self.usableSquares and (self.squares[i][j] == self.blackSpace):
            return True
        else:
            return False

    def emptyValids(self):
        for v in self.validPlaces:
            self.squares[v[0]][v[1]] = " "
        self.validPlaces.clear()

    def completeMove(self, start1, start2, end1, end2):
        self.validPlaces.remove((end1, end2))
        testpiece = self.squares[start1][start2]
        # check if should become king
        if end1 == 0 and testpiece.player == 1 and testpiece.king == 0:
            testpiece.king = self.turn
        elif end1 == self.height - 1 and testpiece.player == -1 and testpiece.king == 0:
            testpiece.king = self.turn
        self.squares[end1][end2] = testpiece
        self.squares[end1][end2].xy = (end1, end2)
        self.squares[start1][start2] = self.blackSpace
        self.emptyValids()
        self.turn += 1

    def canTake(self, piece, x, y):
        i = y - piece.player
        k = - piece.player
        i2 = y + piece.player
        k2 = piece.player
        for j in range(-1, 2, 2):
            if x + j + j > 0 or x + j + j < self.width or i + k > 0 or i + k < self.height:
                try:
                    if -piece.player == self.squares[i][x+j].player:
                        if self.testAvailable(i + k, x+j+j):
                            # set grid space to be a valid space
                            self.ForcedPieces.add(piece.xy)
                        if -piece.player == self.squares[i2][x+j].player and piece.king:
                            # set grid space to be a valid space
                            self.ForcedPieces.add(piece.xy)
                except:
                    pass

    def takes(self, piece, x, y):
        i = y - piece.player
        k = - piece.player
        i2 = y + piece.player
        k2 = piece.player
        for j in range(-1, 2, 2):
            if x + j + j > 0 or x + j + j < self.width or i + k > 0 or i + k < self.height:
                try:
                    if -piece.player == self.squares[i][x+j].player:
                        if self.testAvailable(i + k, x+j+j):
                            # set grid space to be a valid space
                            self.squares[i + k][x+j + j] = self.validSpace
                            # add grid space to valid spaces
                            self.validPlaces.update([(i + k, x + j + j)])
                            self.takes(piece, i+k, x+j+j)
                    if -piece.player == self.squares[i2][x+j].player and piece.king:
                            # set grid space to be a valid space
                            self.squares[i2 + k2][x+j + j] = self.validSpace
                            # add grid space to valid spaces
                            self.validPlaces.update([(i2 + k2, x + j + j)])
                            self.takes(piece, i2+k2, x+j+j)
                except:
                    pass

    def resetGrid(self):
        for p in self.pieces:
            if p.player == 1:
                p.col = self.whitePiece
                p.kingLetter = self.whiteKing
            else:
                p.col = self.blackPiece
                p.kingLetter = self.blackKing
