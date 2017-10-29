# imports
from __future__ import print_function

from Piece import Piece

__author__ = 'Emma'
__project__ = 'Draughts'


# Grid class
class Grid:
    # grid constructor
    def __init__(self, width, height, rows):
        self.debug = 0
        # set grid dimensions
        self.rows = rows
        self.width = width
        self.setWidth(width)
        self.height = height
        self.setHeight(height)

        # set piece information
        self.pieceNo = int((self.width / 2) * self.rows)
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

        self.more = False
        # create array for pieces
        self.whitePieces = []
        self.blackPieces = []
        # create a set of usable squares
        self.usableSquares = set([])
        # create a set of valid spaces
        self.validPlaces = set([])

        self.ForcedPieces = set([])
        self.DoubleTakes = set([])
        # Create list of grid squares variable
        self.squares = []
        # Create Grid
        self.createGrid()

    # Row Setter
    def setRows(self, rows):
        # set amount of rows counters are on
        if rows < self.height / 2:
            self.rows = rows
        elif rows == 0:
            self.rows = 1
        else:
            self.rows = int((self.height / 2) - 1)
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

    def normalMove(self, start1, start2, end1, end2):
        self.emptyValids()
        testpiece = self.squares[start1][start2]
        # check if should become king
        if end1 == 0 and testpiece.player == 1 and testpiece.king == 0:
            testpiece.king = self.turn
        elif end1 == self.height - 1 and testpiece.player == -1 and testpiece.king == 0:
            testpiece.king = self.turn
        self.squares[end1][end2] = testpiece
        self.squares[end1][end2].xy = (end1, end2)
        self.squares[start1][start2] = self.blackSpace

    def completeMove(self, start1, start2, end1, end2):
        if self.ForcedPieces:
            self.completeTakes(start1, start2, end1, end2)
            if self.ForcedPieces:
                return False
            else:
                self.canTake(self.squares[end1][end2], end2, end1)
                if self.ForcedPieces:
                    self.takes(self.squares[end1][end2], end2, end1)
                    self.more = True
                else:
                    self.more = False
        else:
            self.normalMove(start1, start2, end1, end2)
        return True

    def canTake(self, piece, x, y):
        # + 1 in direction piece is allowed to move
        i = y - piece.player
        # + 2 in direction piece is allowed to move
        k = - piece.player
        # + 1 in opposite direction from standard movement
        i2 = y + piece.player
        # + 2 in opposite direction from standard movement
        k2 = piece.player
        # for square before and square after
        for j in range(-1, 2, 2):
            # if space 2 away is within grid
            if x + j + j in range(0, self.width) or i + k in range(0, self.height):
                # try to check if there is a piece of opposite colour one away
                try:
                    if -piece.player == self.squares[i][x + j].player:
                        # test if space 2 away is empty
                        if self.testAvailable(i + k, x + j + j):
                            # add to forced pieces
                            self.ForcedPieces.add(piece.xy)
                except:
                    pass
                # try to check if there is a piece of opposite colour one away in non standard direction and piece is king
                try:
                    if piece.king and -piece.player == self.squares[i2][x + j].player:
                        # test if space 2 away is empty
                        if self.testAvailable(i2 + k2, x + j + j):
                            # add to forced pieces
                            self.ForcedPieces.add(piece.xy)
                except:
                    pass

    def takes(self, piece, x, y):
        # + 1 in direction piece is allowed to move
        i = y - piece.player
        # + 2 in direction piece is allowed to move
        k = - piece.player
        # + 1 in opposite direction from standard movement
        i2 = y + piece.player
        # + 2 in opposite direction from standard movement
        k2 = piece.player
        # for square one before and square one after
        for j in range(-1, 2, 2):
            # check if square + 2 within grid
            if x + j + j in range(0, self.width) or i + k in range(0, self.height):
                # try to check if there is a piece of opposite colour one away
                try:
                    if -piece.player == self.squares[i][x + j].player:
                        # test if square 2 away is empty
                        if self.testAvailable(i + k, x + j + j):
                            # set grid space to be a valid space
                            self.squares[i + k][x + j + j] = self.validSpace
                            # check if space already in valid spaces
                            if (i + k, x + j + j) in self.validPlaces:
                                # add space to double takes
                                self.DoubleTakes.add((i + k, x + j + j))
                            else:
                                # add space to valid spaces
                                self.validPlaces.update([(i + k, x + j + j)])
                            # call function again with new space
                            self.takes(piece, x + j + j, i + k)
                except:
                    pass
                # try to check if there is a piece of opposite colour one away in non standard direction and piece is king
                try:
                    if -piece.player == self.squares[i2][x + j].player and piece.king:
                        # set grid space to be a valid space
                        self.squares[i2 + k2][x + j + j] = self.validSpace
                        # check if space is already in valid spaces
                        if (i2 + k2, x + j + j) in self.validPlaces:
                            # add space to double takes
                            self.DoubleTakes.add((i2 + k2, x + j + j))
                        else:
                            # add grid space to valid spaces
                            self.validPlaces.update([(i2 + k2, x + j + j)])
                        # call function again with new space
                        self.takes(piece, x + j + j, i2 + k2)
                except:
                    pass

    def completeTakes(self, start1, start2, end1, end2):
        if end1 in range(start1 - 2, start1 + 3) and end2 in range(start2 - 2, start2 + 3):
            y = end1 + (start1 - end1) / 2
            x = end2 + (start2 - end2) / 2
            y = int(y)
            x = int(x)
            if self.squares[start1][start2].player == 1:
                self.blackPieces.remove(self.squares[y][x])
            else:
                self.whitePieces.remove(self.squares[y][x])
            self.squares[y][x] = self.blackSpace
            self.normalMove(start1, start2, end1, end2)
            self.ForcedPieces.clear()
            self.DoubleTakes.clear()
        else:
            if (end1, end2) not in self.DoubleTakes:
                removePieces = self.takeRoute(self.squares[start1][start2], start1, start2, end1, end2)
                print(removePieces)
                a = start1
                b = start2
                for p in removePieces:
                    tempPiece = self.squares[p[0]][p[1]]
                    self.squares[p[0]][p[1]] = self.blackSpace
                    if self.squares[a][b].player == 1:
                        self.blackPieces.remove(tempPiece)
                    else:
                        self.whitePieces.remove(tempPiece)
                    self.normalMove(a, b, p[0]+(p[0] - a), p[1] + (p[1] - b))
                    a = p[0]+(p[0] - a)
                    b = p[1] + (p[1] - b)
                    self.printGrid()
                if removePieces:
                    self.ForcedPieces.clear()
                    self.DoubleTakes.clear()

    def takeRoute(self, piece, start1, start2, end1, end2):
        # declare output
        output = []
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                if start1 == end1 and start2 == end2:
                    return output
                if start1 in range(0, self.height) and start2 in range(0, self.width):
                    try:
                        if -piece.player == self.squares[start1 + i][start2 + j].player:
                            if (start1 + i + i, start2 + j + j) in self.validPlaces:
                                if (start1 + i + i, start2 + j + j) in self.DoubleTakes:
                                    return []
                                else:
                                    output.append((start1 + i, start2 + j))
                                    output = output + self.takeRoute(piece, start1 + i + i, start2 + j + j, end1, end2)
                                    if output[len(output) - 1] != (start1 + i, start2 + j) or (start1 + i + i == end1 and start2 + j + j == end2):
                                        return output
                                    else:
                                        output.remove(output[len(output) - 1])
                    except:
                        pass
        return[]


    def resetGrid(self):
        for p in self.pieces:
            if p.player == 1:
                p.col = self.whitePiece
                p.kingLetter = self.whiteKing
            else:
                p.col = self.blackPiece
                p.kingLetter = self.blackKing
