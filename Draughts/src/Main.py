# imports
from __future__ import print_function
from Grid import Grid
from Settings import Settings

__author__ = 'Emma'
__project__ = 'Draughts'


# ************** Menu ***************

# menu method
def menu(grid, settings):
    done = False
    # do while not done
    while not done:
        theIn = input("Play, NewGame, Settings, Rules, Exit: ")
        theIn = theIn.lower()
        # play game
        if theIn == "play":
            play(grid)
        # reset grid and play
        if theIn == "newgame":
            grid.createGrid()
            play(grid)
        # view settings
        elif theIn == "settings":
            settings.settings()
        # view rules
        elif theIn == "rules":
            settings.rules()
        # exit game
        elif theIn == "exit":
            done = True


# method to look for valid places to move to
def validPlaces(grid, x, y):
    if grid.squares[y][x].player == 1 or grid.squares[y][x].king != 0:
        # set i to row above
        i = y - 1
        # look in column before and column after
        for j in range(-1, 2, 2):
            # check if square is empty
            if grid.testAvailable(i, x + j):
                # set grid space to be a valid space
                grid.squares[i][x + j] = grid.validSpace
                # add grid space to valid spaces
                grid.validPlaces.update([(i, x + j)])
    # check if it's a black piece or any king
    if grid.squares[y][x].player == -1 or grid.squares[y][x].king != 0:
        # set i to row below
        i = y + 1
        # look in column before and column after
        for j in range(-1, 2, 2):
            # check if square is empty
            if grid.testAvailable(i, x + j):
                # set grid space to be a valid space
                grid.squares[i][x + j] = grid.validSpace
                # add grid space to valid spaces
                grid.validPlaces.update([(i, x + j)])


def setInput(theIn):
    if 65 <= ord(theIn[len(theIn) - 1].upper()) <= 90:
        # set x to int
        x = ord(theIn[len(theIn) - 1].upper())
        x -= ord('A')

        theIn = theIn[:-1]
        # set y to given int minus 1
        y = int(theIn) - 1
    elif 65 <= ord(theIn[0].upper()) <= 90:
        # set x to int
        x = ord(theIn[0].upper())
        x -= ord('A')

        theIn = theIn[1:]
        # set y to given int minus 1
        y = int(theIn) - 1
    return y, x


# move method
def move(grid, starty, startx):
    done = False
    # do while not done
    while not done:
        print()
        grid.printGrid()
        print()
        print(
            "Input the coordinates of the space you would like to move to \n(type cancel to select other piece, valid spaces shown with  ",
            end=grid.validSpace)
        theIn = input("): ")
        # check if player wanted to cancel
        if theIn.lower() == "cancel":
            done = True
        elif theIn.lower() == "no" and grid.more:
            grid.more = False
            grid.emptyValids()
            grid.ForcedPieces.clear()
            grid.DoubleTakes.clear()
        else:
            try:
                y, x = setInput(theIn)
                # check that move is valid
                if (y, x) in grid.validPlaces:
                    # move piece in grid
                    if not grid.completeMove(starty, startx, y, x):
                        if grid.more:
                            print("There are more pieces you can take, type cancel to end your turn")
                            starty = y
                            startx = x
                        else:
                            print("ERROR: there are multiple ways to get to this point please enter your route step by step")
                    else:
                        done = True
                else:
                    # give feedback for invalid input
                    print("\nERROR: invalid input\n")
            except:
                print("\nERROR: invalid input\n")


def checkForTakes(grid, pieces):
    for i in range(len(pieces)):
        grid.canTake(pieces[i], pieces[i].xy[1], pieces[i].xy[0])


def forceTakeMove(grid):
    print()
    grid.printGrid()
    print()
    print("\nType \"Quit\" to quit")
    print("FORCE TAKE:\nYou are able to take at least one of your enemies pieces.\nPlease input one of the following:")
    for f in grid.ForcedPieces:
        print(chr(65 + f[1]), end=str(f[0] + 1))
        print()
    theIn = input("Input: ")
    # check if player wants to quit
    if theIn.lower() == "quit":
        return True
    else:
        try:
            y, x = setInput(theIn)
            # check that there is a valid piece in that square
            if (y, x) not in grid.ForcedPieces:
                print("\nERROR: invalid input\n")
            else:
                grid.takes(grid.squares[y][x], x, y)
                # check that there where valid spaces
                if not grid.validPlaces:
                    print("\nERROR: No valid movements\n")
                    grid.printGrid()
                else:
                    # move piece
                    move(grid, y, x)
                    # check if piece was moved
                    if grid.validPlaces or grid.ForcedPieces:
                        grid.emptyValids()
                        grid.ForcedPieces.clear()
                    else:
                        return False
        except:
            print("\nERROR: Invalid input\n")
            return forceTakeMove(grid)
    return forceTakeMove(grid)


def choosePiece(grid):
    print()
    grid.printGrid()
    print()
    print("\nType \"Quit\" to quit")
    theIn = input("Input coordinates of piece you would like to move: ")
    # check if player wants to quit
    if theIn.lower() == "quit":
        return True
    else:
        try:
            y, x = setInput(theIn)
            # check that values are within grid boundaries
            if x not in range(0, grid.width) or y not in range(0, grid.height):
                print("\nERROR: invalid input\n")
            else:
                # check that there is a valid piece in that square
                if grid.squares[y][x].player == grid.player:
                    # call valid places method
                    validPlaces(grid, x, y)
                    # check that there where valid spaces
                    if not grid.validPlaces:
                        print("\nERROR: No valid movements\n")
                        grid.printGrid()
                    else:
                        # move piece
                        move(grid, y, x)
                        # check if piece was moved
                        if grid.validPlaces:
                            grid.emptyValids()
                        else:
                            return False
                else:
                    print("\nERROR: your piece is not on this square\n")
        except:
            print("\nERROR: invalid input\n")
            return choosePiece(grid)
    return choosePiece(grid)


# play method
def play(grid):
    print()

    done = False
    while not done:

        if grid.player == 1:
            print("\nPLAYER 1's TURN (" + grid.whitePiece + ")\n")
        else:
            print("\nPLAYER 2's TURN (" + grid.blackPiece + ")\n")

        if grid.player == 1:
            checkForTakes(grid, grid.whitePieces)
        else:
            checkForTakes(grid, grid.blackPieces)

        if not grid.ForcedPieces:
            done = choosePiece(grid)
        else:
            done = forceTakeMove(grid)

        grid.turn += 1

        if len(grid.blackPieces) == 0:
            print()
            grid.printGrid()
            print("\nPLAYER 1 WINS!\n")
            done = True
            main()
        elif len(grid.whitePieces) == 0:
            print()
            grid.printGrid()
            print("\nPLAYER 2 WINS\n")
            done = True
            main()
        else:
            # change player
            grid.player *= -1


# define main
def main():
    # create grid of width and height
    grid = Grid(8, 8, 3)
    settings = Settings(grid)
    # print rules
    settings.rules()
    # go to menu
    menu(grid, settings)


# run from main
if __name__ == "__main__":
    main()
