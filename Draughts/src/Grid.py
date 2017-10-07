# imports
from __future__ import print_function

from Piece import Piece

__author__ = 'Emma'
__project__ = 'Draughts'


# Grid class
class Grid:

    # grid constructor
    def __init__(self, width, height, rows):

        self.rows = rows
        self.width = width
        self.setWidth(width)
        self.height = height
        self.setHeight(height)
        self.pieceNo = (self.width/2) * self.rows
        self.pieces = []
        self.usableSquares = []

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

    # Row Getter
    def getRows(self):
        return self.rows

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

    # Height Getter
    def getHeight(self):
        return self.height

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

    # Width Getter
    def getWidth(self):
        return self.width


    # create grid method
    def createGrid(self):

        # empty squares list
        self.squares = []
        self.pieces = []
        self.usableSquares = []

        # Create amount of rows needed
        for i in range(self.height):
            self.squares.append([])

        # loop through height and width
        for i in range(self.height):
            for j in range(self.width):
                # check if it should be a white square
                if (i % 2 and not j % 2) or (not i % 2 and j % 2):
                    self.squares[i].append(' ')
                # check if square should  contain black piece
                elif i < self.rows:
                    self.squares[i].append("b")
                    self.pieces.append(Piece([i, j], "b"))
                    self.usableSquares.append([i, j])
                # check if square should contain white piece
                elif i >= self.height - self.rows:
                    self.squares[i].append("w")
                    self.pieces.append(Piece([i, j], "b"))
                    self.usableSquares.append([i, j])
                # else square is black
                else:
                    self.squares[i].append(' ')
                    self.usableSquares.append([i, j])

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
            # new line
            print()



