# imports
from src.Grid import Grid

__author__ = 'Emma'
__project__ = 'Draughts'

# define Draughts rules
def rules(grid):
    print("Rules:", end="\n\n• ")
    print(grid.width, end="x")
    print(grid.height, end=" grid.\n")
    print("• Each player has", end=" ")
    print(int((grid.width/2 * grid.rows)), end=" pieces\n")
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
        print("board")
        theIn = input("enter number: ")
        if theIn == '1':
            print(1)
        elif theIn == '2':
            print(2)
        elif theIn == '3':
            print(3)
        elif theIn == '4':
            print(4)
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
        print("piece")
        theIn = input("enter number: ")
        if theIn == '1':
            print(1)
        elif theIn == '2':
            print(2)
        elif theIn == '3':
            print(3)
        elif theIn == '4':
            print(4)
        elif theIn == '5':
            done = True
            settings(grid)


def settings(grid):
    print("\nSettings:\n")
    print("1. See Board Settings")
    print("2. Toggle player Colour: white")
    print("3. See Piece settings")
    print("4. Back")
    done = False
    while not done:
        print("settings")
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
        theIn = input("Play, Settings, Exit: ")
        if theIn == "Play":
            print()
            # print grid
            grid.printGrid()
            done = True
        elif theIn == "Settings":
            settings(grid)
            done = True
        elif theIn == "Exit":
            done = True


# define main
def main():
    # create grid of width and height
    grid = Grid(8, 8, 3)
    rules(grid)
    menu(grid)


# run from main
if __name__ == "__main__":
    main()
