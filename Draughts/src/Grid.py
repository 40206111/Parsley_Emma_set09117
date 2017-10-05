#imports
from __future__ import print_function

__author__ = 'Emma'
__project__ = 'Draughts'


# Grid class
class Grid:

    # grid constructor
    def __init__(self, width, height):
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
        # Create list of grid squares for the grid height
        self.squares = []
        for i in range(self.height):
            self.squares.append([])
        self.createGrid()

    # create grid method
    def createGrid(self):
        # loop through height and width
        for i in range(self.height):
            for j in range(self.width):
                # check if it should be a white square
                if (i % 2 and not j % 2) or (not i % 2 and j % 2):
                    self.squares[i].append('0')
                # check if square should  contain black piece
                elif i < 3:
                    self.squares[i].append("b")
                # check if square should contain white piece
                elif i > self.height - 4:
                    self.squares[i].append("w")
                # else square is black
                else:
                    self.squares[i].append('1')

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



