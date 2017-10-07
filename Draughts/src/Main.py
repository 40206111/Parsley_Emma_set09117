# imports
from __future__ import print_function
from Grid import Grid

__author__ = 'Emma'
__project__ = 'Draughts'

turn = 0

# define Draughts rules
def rules(grid):
    print("Rules:", end="\n\n• ")
    print(grid.width, end="x")
    print(grid.height, end=" grid.\n")
    print("• Each player has", end=" ")
    print(grid.pieceNo, end=" pieces\n")
    print("• The counters go on the first", end=" ")
    print(grid.rows, end=" rows\n")
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
    print(grid.width, end="x")
    print(grid.height)
    print("2. Starting rows:", end=" ")
    print(grid.rows)
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
        theIn = theIn.lower()
        if theIn == "play":
            play(grid)
            done = True
        elif theIn == "settings":
            settings(grid)
            done = True
        elif theIn == "rules":
            rules(grid)
        elif theIn == "exit":
            done = True

def validPlaces(grid, x, y):
    if grid.squares[y][x] == grid.whitePiece or grid.squares[y][x] == grid.whiteKing or grid.squares[y][x] == grid.blackKing:
        i = y - 1
        for j in range (-1, 2, 2):
            grid.testAvailable(i, x+j)

    if grid.squares[y][x] == grid.blackPiece or grid.squares[y][x] == grid.blackKing or grid.squares[y][x] == grid.whiteKing:
        i = y + 1
        for j in range (-1, 2, 2):
            grid.testAvailable(i, x+j)

def play(grid):
    print()
    # print grid
    grid.printGrid()
    done = False
    player = -1
    while not done:
        player *= -1

        piece = grid.getPieceType(player)
        king = grid.getKingType(player)

        print("\nType \"Quit\" to quit")
        theIn = input("Input coordinates of piece you would like to move: ")
        try:
            x = ord(theIn[1].upper())
            x -= ord('A')
            y = int(theIn[0]) - 1
            if x < 0 or x > grid.width or y < 0 or y > grid.height:
                print("\nERROR: invalid input\n")
                grid.printGrid()
            else:
                if grid.squares[y][x] == piece or grid.squares[y][x] == king:
                    validPlaces(grid, x, y)
                    grid.printGrid()
        except:
            if theIn.lower() == "quit":
                done = True
                menu(grid)
            else:
                print("\nERROR: invalid input\n")
                grid.printGrid()


# define main
def main():
    # create grid of width and height
    grid = Grid(8, 8, 3)
    rules(grid)
    menu(grid)


# run from main
if __name__ == "__main__":
    main()
