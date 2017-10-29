# imports
from __future__ import print_function
from Grid import Grid

__author__ = 'Emma'
__project__ = 'Draughts'


# define Draughts rules
def rules(grid):
    print("Rules:", end="\n\n• ")
    print(grid.width, end="x")
    print(grid.height, end=" grid.\n")
    print("• Each player has", end=" ")
    print(int(grid.pieceNo), end=" pieces\n")
    print("• The counters go on the first", end=" ")
    print(grid.rows, end=" rows\n")
    print("• Pieces can only move Diagonally towards opponent")
    print("• An opponents piece is Captured by jumping your piece over it diagonally")
    print("• All landing spaces must be vacant")
    print("• If an opponents piece can be captured it must be")
    print("• multiple captures are possible if there's a blank space between each one")
    print("• Pieces that get to the other side of the board become Kings and can move forward and backwards")
    print()


# settings for board
def boardSets(grid, change):
    print("\nBoard Settings:\n")
    print("1. Board Size:", end=" ")
    print(grid.width, end="x")
    print(grid.height)
    print("2. Starting rows:", end=" ")
    print(grid.rows)
    print("3. White Spaces: ", end=grid.whiteSpace)
    print("\n4. Black Spaces: ", end=grid.blackSpace)
    print("\n5. Valid movements: ", end=grid.validSpace)
    print("\n6. Back")

    done = False

    # loop while not done
    while not done:
        theIn = input("enter number: ")
        # Board Size Setting
        if theIn == '1':
            while not done:
                try:
                    print("WARNING: changing this setting will reset the game")
                    print("Board width must be even and at least 4 and at most 26")
                    width = input("Input board width (Type Cancel to cancel): ")
                    if not width.lower() == "cancel":
                        print("Board Height must less than 1000 and at least 4")
                        height = input("Input board height (Type Cancel to cancel: ")
                        if not height.lower() == "cancel":
                            grid.setHeight(int(height))
                            grid.setWidth(int(width))
                            change = True
                    done = True
                    boardSets(grid, change)
                except:
                    print("ERROR: please enter whole numbers")

        # Starting rows setting
        elif theIn == '2':
            while not done:
                try:
                    print("WARNING: changing this setting will reset the game")
                    rows = input("Input number of rows (Type Cancel to cancel): ")
                    if not rows.lower() == "cancel":
                        grid.setRows(int(rows))
                        change = True
                    done = True
                    boardSets(grid, change)
                except:
                    print("ERROR: Please enter a whole number")

        # White space setting
        elif theIn == '3':
            print("WARNING: changing this setting will reset the game")
            done = True
            space = input(
                "Input the character you want to represent white spaces\nOnly the first character you type will be used: ")
            try:
                grid.whiteSpace = space[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            boardSets(grid, change)
        # Black space setting
        elif theIn == '4':
            print("WARNING: changing this setting will reset the game")
            done = True
            space = input(
                "Input the character you want to represent black spaces\nOnly the first character you type will be used: ")
            try:
                grid.blackSpace = space[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            boardSets(grid, change)
        # valid space setting
        elif theIn == '5':
            done = True
            space = input(
                "Input the character you want to represent valid spaces\nOnly the first character you type will be used: ")
            try:
                grid.validSpace = space[0]
            except:
                print("ERROR: you did not input anything")
            boardSets(grid, change)
        # back to settings
        elif theIn == '6':
            if change:
                grid.createGrid()
            done = True
            settings(grid)


# settings for pieces
def pieceSets(grid):
    print("\nPiece Settings:\n")
    print("1. White pieces: ", end=grid.whitePiece)
    print("\n2. Black pieces: ", end=grid.blackPiece)
    print("\n3. White Kings: ", end=grid.whiteKing)
    print("\n4. Black Kings: ", end=grid.blackKing)
    print("\n5. Back")

    done = False
    # loop while not done
    while not done:
        theIn = input("enter number: ")

        # white pieces setting
        if theIn == '1':
            done = True
            piece = input(
                "Input the character you want to represent white pieces\nOnly the first character you type will be used: ")
            try:
                grid.whitePiece = piece[0]
                grid.resetGrid()
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid)
        # black piece setting
        elif theIn == '2':
            done = True
            piece = input(
                "Input the character you want to represent black pieces\nOnly the first character you type will be used: ")
            try:
                grid.blackPiece = piece[0]
                grid.resetGrid()
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid)
        # white king setting
        elif theIn == '3':
            done = True
            piece = input(
                "Input the character you want to represent white kings\nOnly the first character you type will be used: ")
            try:
                grid.whiteKing = piece[0]
                grid.resetGrid()
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid)
        # black king setting
        elif theIn == '4':
            done = True
            piece = input(
                "Input the character you want to represent black kings\nOnly the first character you type will be used: ")
            try:
                grid.blackKing = piece[0]
                grid.resetGrid()
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid)
        elif theIn == '5':
            done = True
            settings(grid)


# general settings
def settings(grid):
    print("\nSettings:\n")
    print("1. See Board Settings")
    print("2. See Piece settings")
    print("3. Two Player: On  (Changing this setting will reset your game)")
    print("4. Back")

    done = False
    # do while not done
    while not done:
        theIn = input("enter number: ")
        # board settings
        if theIn == "1":
            done = True
            boardSets(grid, False)
        # piece settings
        elif theIn == '2':
            done = True
            pieceSets(grid)
        # toggle 2 players
        elif theIn == '3':
            done = True
            print("This Setting cannot be changed yet")
            settings(grid)
        # back to menu
        elif theIn == '4':
            done = True
            menu(grid)


# menu method
def menu(grid):
    done = False
    # do while not done
    while not done:
        theIn = input("Play, NewGame, Settings, Rules, Exit: ")
        theIn = theIn.lower()
        # play game
        if theIn == "play":
            play(grid)
            done = True
        # reset grid and play
        if theIn == "newgame":
            grid.createGrid()
            play(grid)
            done = True
        # view settings
        elif theIn == "settings":
            settings(grid)
            done = True
        # view rules
        elif theIn == "rules":
            rules(grid)
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
    print(grid.validPlaces)
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
        menu(grid)
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
    return False


def choosePiece(grid):
    print()
    grid.printGrid()
    print()
    print("\nType \"Quit\" to quit")
    theIn = input("Input coordinates of piece you would like to move: ")
    # check if player wants to quit
    if theIn.lower() == "quit":
        menu(grid)
        return True
    else:
        try:
            y, x = setInput(theIn)
            # check that values are within grid boundaries
            if x < 0 or x > grid.width or y < 0 or y > grid.height:
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
    return False


# play method
def play(grid):
    print()
    print("\nPLAYER 1's TURN (" + grid.whitePiece + ")\n")

    done = False
    while not done:

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
            if grid.player == 1:
                print("\nPLAYER 1's TURN (" + grid.whitePiece + ")\n")
            else:
                print("\nPLAYER 2's TURN (" + grid.blackPiece + ")\n")


# define main
def main():
    # create grid of width and height
    grid = Grid(8, 8, 1)
    grid.setRows(1)
    grid.createGrid()
    # black
    # grid.normalMove(0, 6, 1, 7)
    # grid.normalMove(7, 1, 6, 2)
    # grid.normalMove(7, 3, 4, 4)
    # grid.normalMove(7, 5, 2, 6)
    # white
    grid.normalMove(0, 0, 6, 2)
    grid.normalMove(0, 2, 4, 4)
    grid.normalMove(0, 4, 2, 6)
    # print rules
    rules(grid)
    # go to menu
    menu(grid)


# run from main
if __name__ == "__main__":
    main()
