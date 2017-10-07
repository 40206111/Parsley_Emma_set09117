# imports
from __future__ import print_function
from Grid import Grid

__author__ = 'Emma'
__project__ = 'Draughts'


# define Draughts rules
def rules(grid):
    print("Rules:", end="\n\n• ")
    print(grid.getWidth(), end="x")
    print(grid.getHeight(), end=" grid.\n")
    print("• Each player has", end=" ")
    print(grid.pieceNo, end=" pieces\n")
    print("• The counters go on the first", end=" ")
    print(grid.getRows(), end=" rows\n")
    print("• Pieces can only move Diagonally towards opponent")
    print("• An opponents piece is Captured by jumping your piece over it diagonally")
    print("• All landing spaces must be vacant")
    print("• If an opponents piece can be captured it must be")
    print("• multiple captures are possible if there's a blank space between each one")
    print("• Pieces that get to the other side of the board become Kings and can move forward and backwards")
    print()


def boardSets(grid):
    print("\nBoard Settings:\n")
    print("1. Board Size:", end=" ")
    print(grid.getWidth(), end="x")
    print(grid.getHeight())
    print("2. Starting rows:", end=" ")
    print(grid.getRows())
    print("3. White Spaces:  ")
    print("4. Black Spaces: ")
    print("5. Back")
    done = False
    while not done:
        theIn = input("enter number: ")
        if theIn == '1':
            while not done:
                try:
                    tempWidth = grid.getWidth()
                    print("Board width must be even and at least 4 and at most 26")
                    width = input("Input board width (Type Cancel to cancel): ")
                    if not width == "Cancel":
                        grid.setWidth(int(width))
                        print("Board Height must less than 1000 and at least 4")
                        height = input("Input board height (Type Cancel to cancel: ")
                        if not height == "Cancel":
                            grid.setHeight(int(height))
                            grid.createGrid()
                        else:
                            grid.setWidth(tempWidth)
                    done = True
                    boardSets(grid)
                except:
                    print("ERROR: please enter whole numbers")

        elif theIn == '2':
            while not done:
                try:
                    rows = input("Input number of rows (Type Cancel to cancel): ")
                    if not rows == "Cancel":
                        grid.setRows(int(rows))
                        grid.createGrid()
                    done = True
                    boardSets(grid)
                except:
                    print("ERROR: Please enter a whole number")
        elif theIn == '3':
            done = True
            print(3)
            boardSets(grid)
        elif theIn == '4':
            done = True
            print(4)
            boardSets(grid)
        elif theIn == '5':
            done = True
            settings(grid)


def pieceSets(grid):
    print("\nPiece Settings:\n")
    print("1. White pieces: w")
    print("2. Black pieces: b")
    print("3. White Kings: W")
    print("4. Black Kings: B")
    print("5. Back")
    done = False
    while not done:
        theIn = input("enter number: ")
        if theIn == '1':
            done = True
            print(1)
            pieceSets(grid)
        elif theIn == '2':
            done = True
            print(2)
            pieceSets(grid)
        elif theIn == '3':
            done = True
            print(3)
            pieceSets(grid)
        elif theIn == '4':
            done = True
            print(4)
            pieceSets(grid)
        elif theIn == '5':
            done = True
            settings(grid)


def settings(grid):
    print("\nSettings:\n")
    print("1. See Board Settings")
    print("2. Two Player: Om")
    print("3. See Piece settings")
    print("4. Back")
    done = False
    while not done:
        theIn = input("enter number: ")
        if theIn == "1":
            done = True
            boardSets(grid)
        elif theIn == '2':
            print(2)
        elif theIn == '3':
            done = True
            pieceSets(grid)
        elif theIn == '4':
            done = True
            menu(grid)


def menu(grid):
    done = False

    while not done:
        theIn = input("Play, Settings, Rules, Exit: ")
        if theIn == "Play":
            play(grid)
            done = True
        elif theIn == "Settings":
            settings(grid)
            done = True
        elif theIn == "Rules":
            rules(grid)
        elif theIn == "Exit":
            done = True


def play(grid):
    print()
    # print grid
    grid.printGrid()
    done = False

    while not done:
        print("Type \"Quit\" to quit")
        theIn = input("Input coordinates of piece you would like to move: ")

        if theIn == "Quit"
            done = True
        else:
            print("invalid input")


# define main
def main():
    # create grid of width and height
    grid = Grid(8, 8, 3)
    rules(grid)
    menu(grid)


# run from main
if __name__ == "__main__":
    main()
