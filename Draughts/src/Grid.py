# imports
from __future__ import print_function

__author__ = 'Emma'
__project__ = 'Draughts'


# Grid class
class Grid:

    # grid constructor
    def __init__(self, width, height, rows):
        # check that width isn't larger than the English alphabet
        if width > 26:
            # set width to 26
            self.width = 26
        else:
            # set width to given width
            self.width = width

        # check that height isn't greater than 999
        if height > 999:
            # set height to 999
            self.height = 999
        else:
            # set height to given height
            self.height = height

        # set amount of rows counters are on
        if rows <= self.height/2:
            self.rows = rows
        else:
            self.rows = int(self.height/2)

        # Create list of grid squares variable
        self.squares = []
        # Create Grid
        self.createGrid()

    # create grid method
    def createGrid(self):
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
                # check if square should contain white piece
                elif i >= self.height - self.rows:
                    self.squares[i].append("w")
                # else square is black
                else:
                    self.squares[i].append(' ')

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



