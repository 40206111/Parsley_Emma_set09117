# imports
from __future__ import print_function

from Piece import Piece

__author__ = 'Emma'
__project__ = 'Draughts'


# Grid class
class Grid:
    # grid constructor
    def __init__(self, width, height, rows):
        # declare piece number, will be set when rows is set
        self.pieceNo = 0

        # declare rows
        self.rows = rows
        # set grid width
        self.width = width
        self.setWidth(width)
        # set grid height
        self.height = height
        self.setHeight(height)

        # set piece information
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

        # set more moves boolean
        self.more = False

        # create array for pieces
        self.whitePieces = []
        self.blackPieces = []

        # create a set of usable squares
        self.usableSquares = set([])

        # create a set of valid spaces
        self.validPlaces = set([])
        # create set of pieces for forced takes
        self.ForcedPieces = set([])
        # create set of squares that can be gotten to in multiple ways through takes
        self.DoubleTakes = set([])
        # Create list of grid squares variable
        self.squares = []

        # Create Grid
        self.createGrid()

# ********** Setters ************

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
        # set rows to be correct with new height
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

# *********** Methods **********

    # create grid method
    def createGrid(self):
        # set player to player 1
        self.player = 1
        # empty lists and sets
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

    # method to test if square is a blackspace and empty
    def testAvailable(self, i, j):
        # if it's a useable square and has no piece in it return true
        if (i, j) in self.usableSquares and (self.squares[i][j] == self.blackSpace):
            return True
        else:
            return False

    # empty all valid squares
    def emptyValids(self):
        # loop through valid pieces
        for v in self.validPlaces:
            # set valid square to be empty square
            self.squares[v[0]][v[1]] = self.blackSpace
        # clear valid spaces
        self.validPlaces.clear()

    # method to move normally
    def normalMove(self, start1, start2, end1, end2):
        # empty valid pieces
        self.emptyValids()
        # set tempPiece to piece in start square
        tempPiece = self.squares[start1][start2]
        # check if should become king
        if end1 == 0 and tempPiece.player == 1 and tempPiece.king == 0:
            tempPiece.king = self.turn
        elif end1 == self.height - 1 and tempPiece.player == -1 and tempPiece.king == 0:
            tempPiece.king = self.turn
        # put tempPiece in end square
        self.squares[end1][end2] = tempPiece
        # set pieces new coordinates
        self.squares[end1][end2].xy = (end1, end2)
        # set start square to be empty
        self.squares[start1][start2] = self.blackSpace

    # method to complete move
    def completeMove(self, start1, start2, end1, end2):
        # if there was a forced take use corresponding methods
        if self.ForcedPieces:
            # call complete takes method
            self.completeTakes(start1, start2, end1, end2)
            # check if it was successful
            if self.ForcedPieces or self.validPlaces:
                return False
            else:
                # check if it's possible to take more pieces
                self.canTake(self.squares[end1][end2], end1, end2)
                if self.ForcedPieces:
                    # add possible takes to appropriate variables
                    self.takes(set(), self.squares[end1][end2], end1, end2)
                    # set more moves to true
                    self.more = True
                    return False
                else:
                    self.more = False
        else:
            # else carry out a normal move
            self.normalMove(start1, start2, end1, end2)
        return True

    def jumpPiece(self, player, start1, start2, y, x):
        # tell piece it has been taken
        self.squares[y][x].turnTaken = self.turn
        # if remove pieces from opposite players list
        if player == 1:
            self.blackPieces.remove(self.squares[y][x])
        else:
            self.whitePieces.remove(self.squares[y][x])
        # set place where taken piece was to empty
        self.squares[y][x] = self.blackSpace
        # complete move as normal
        self.normalMove(start1, start2, y + (y-start1), x + (x - start2))

    # method for completing move if you can take
    def completeTakes(self, start1, start2, end1, end2):
        multi = False
        player = self.squares[start1][start2].player
        # if end space only 1 take away
        if end1 in range(start1 - 2, start1 + 3) and end2 in range(start2 - 2, start2 + 3):
            # set y and x to coordinates of square with piece to be taken in
            y = (end1 + start1) / 2
            x = (end2 + start2) / 2
            # make sure y and x are ints
            y = int(y)
            x = int(x)
            if self.testAvailable(y, x):
                multi = True
            else:
                self.jumpPiece(player, start1, start2, y, x)
                # clear forced pieces
                self.ForcedPieces.clear()
                # clear double takes
                self.DoubleTakes.clear()

        else:
            multi = True

        if multi:
            # if the end doesn't have multiple routes to get to it
            if (end1, end2) not in self.DoubleTakes:
                # set pieces to remove to return from take route
                removePieces = self.takeRoute(set(), self.squares[start1][start2], start1, start2, end1, end2)
                # check if pieces can be removed
                if removePieces:
                    # set a and b to start coordinates
                    a = start1
                    b = start2
                    # for all pieces that can be removed
                    for p in removePieces:
                        self.jumpPiece(player, a, b, p[0], p[1])
                        # set a and b to next end square
                        a = p[0]+(p[0] - a)
                        b = p[1] + (p[1] - b)
                        # print grid
                        self.printGrid()
                    # clear forced pieces
                    self.ForcedPieces.clear()
                    # clear double takes
                    self.DoubleTakes.clear()


    # method to calculate route that gets a piece from start to end through taking
    def takeRoute(self, jumped, piece, start1, start2, end1, end2):
        # declare output
        output = []
        # for square above and below start
        for i in range(-1, 2, 2):
            # for square left or right of start
            for j in range(-1, 2, 2):
                # if at the end return output
                if start1 == end1 and start2 == end2:
                    return output
                # if on the board
                elif start1 in range(0, self.height) and start2 in range(0, self.width):
                    try:
                        # if piece is in the right direction or can take both ways
                        if i == piece.player or piece.king:
                            # if there is the opponents piece
                            if -piece.player == self.squares[start1 + i][start2 + j].player and (start1 + i, start2 + j) not in jumped:
                                # if space is valid
                                if (start1 + i + i, start2 + j + j) in self.validPlaces:
                                    # if space has multiple routes
                                    if (start1 + i + i, start2 + j + j) in self.DoubleTakes:
                                        # return nothing
                                        return []
                                    else:
                                        jumped.add((start1 + i, start2 + j))
                                        # append piece to output
                                        output.append((start1 + i, start2 + j))
                                        # append other possible pieces to output
                                        output = output + self.takeRoute(jumped, piece, start1 + i + i, start2 + j + j, end1, end2)
                                        # if output is not equal to this one or end
                                        if output[len(output) - 1] != (start1 + i, start2 + j) or (start1 + i + i == end1 and start2 + j + j == end2):
                                            #return output
                                            return output
                                        else:
                                            jumped.clear()
                                            # remove last one added to output
                                            output.remove(output[len(output) - 1])
                    except:
                        pass
        return[]

    def canTake(self, piece, y, x):
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
            if x + j + j in range(0, self.width) and i + k in range(0, self.height):
                # try to check if there is a piece of opposite colour one away
                try:
                    if -piece.player == self.squares[i][x + j].player:
                        # test if space 2 away is empty
                        if self.testAvailable(i + k, x + j + j):
                            # add to forced pieces
                            self.ForcedPieces.add(piece.xy)
                except:
                    pass
            # if space 2 away is within grid
            if x + j + j in range(0, self.width) and i2 + k2 in range(0, self.height):
                # try to check if there is a piece of opposite colour one away in non standard direction and piece is king
                try:
                    if piece.king and piece.king != self.turn and -piece.player == self.squares[i2][x + j].player:
                        # test if space 2 away is empty
                        if self.testAvailable(i2 + k2, x + j + j):
                            # add to forced pieces
                            self.ForcedPieces.add(piece.xy)
                except:
                    pass

    # method for
    def takes(self, jumped, piece, y, x):
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
            if x + j + j in range(0, self.width) and i + k in range(0, self.height):
                # try to check if there is a piece of opposite colour one away
                try:
                    if -piece.player == self.squares[i][x + j].player and (i, x+ j) not in jumped:
                        if (i + k, x + j + j) in self.validPlaces:
                            # add space to double takes
                            self.DoubleTakes.add((i + k, x + j + j))
                        # test if square 2 away is empty
                        elif self.testAvailable(i + k, x + j + j):
                            # set grid space to be a valid space
                            self.squares[i + k][x + j + j] = self.validSpace
                            if (i + k, x + j + j) != piece.xy:
                                # add space to valid spaces
                                self.validPlaces.update([(i + k, x + j + j)])
                                jumped.add((i, x + j))
                                # call function again with new space
                                self.takes(jumped, piece, i + k, x + j + j)
                except:
                    pass
            # if space 2 away is within grid
            if x + j + j in range(0, self.width) and i2 + k2 in range(0, self.height):
                # try to check if there is a piece of opposite colour one away in non standard direction and piece is king
                try:
                    if -piece.player == self.squares[i2][x + j].player and piece.king and (i2, x + j) not in jumped:
                        if (i2 + k2, x + j + j) in self.validPlaces:
                            # add space to double takes
                            self.DoubleTakes.add((i2 + k2, x + j + j))
                        elif self.testAvailable(i2 + k2, x + j + j):
                            # set grid space to be a valid space
                            self.squares[i2 + k2][x + j + j] = self.validSpace
                            if (i2 + k2, x + j + j) != piece.xy:
                                # add grid space to valid spaces
                                self.validPlaces.update([(i2 + k2, x + j + j)])
                                jumped.add((i2, x + j))
                                # call function again with new space
                                self.takes(jumped, piece, i2 + k2, x + j + j)
                except:
                    pass

    def resetGrid(self):
        for p in self.whitePieces:
            p.col = self.whitePiece
            p.kingLetter = self.whiteKing
        for p in self.blackPieces:
            p.col = self.blackPiece
            p.kingLetter = self.blackKing

    # method to look for valid places to move to
    def FindValids(self, y, x):
        if self.squares[y][x].player == 1 or self.squares[y][x].king != 0:
            # set i to row above
            i = y - 1
            # look in column before and column after
            for j in range(-1, 2, 2):
                # check if square is empty
                if self.testAvailable(i, x + j):
                    # set grid space to be a valid space
                    self.squares[i][x + j] = self.validSpace
                    # add grid space to valid spaces
                    self.validPlaces.update([(i, x + j)])
        # check if it's a black piece or any king
        if self.squares[y][x].player == -1 or self.squares[y][x].king != 0:
            # set i to row below
            i = y + 1
            # look in column before and column after
            for j in range(-1, 2, 2):
                # check if square is empty
                if self.testAvailable(i, x + j):
                    # set grid space to be a valid space
                    self.squares[i][x + j] = self.validSpace
                    # add grid space to valid spaces
                    self.validPlaces.update([(i, x + j)])
