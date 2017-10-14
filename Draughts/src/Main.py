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
                    print("Board width must be even and at least 4 and at most 26")
                    width = input("Input board width (Type Cancel to cancel): ")
                    if not width.lower() == "cancel":
                        print("Board Height must less than 1000 and at least 4")
                        height = input("Input board height (Type Cancel to cancel: ")
                        if not height.lower() == "cancel":
                            grid.setHeight(int(height))
                            grid.setWidth(int(width))
                            change = True
                            print(change)
                    done = True
                    boardSets(grid, change)
                except:
                    print("ERROR: please enter whole numbers")

        # Starting rows setting
        elif theIn == '2':
            print(change)
            while not done:
                try:
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
            done = True
            space = input("Input the character you want to represent white spaces\nOnly the first character you type will be used: ")
            try:
                grid.whiteSpace = space[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            boardSets(grid, change)
        # Black space setting
        elif theIn == '4':
            space = input("Input the character you want to represent black spaces\nOnly the first character you type will be used: ")
            try:
                grid.blackSpace = space[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            boardSets(grid, change)
        # valid space setting
        elif theIn == '5':
            space = input("Input the character you want to represent valid spaces\nOnly the first character you type will be used: ")
            try:
                grid.validSpace = space[0]
                change =True
            except:
                print("ERROR: you did not input anything")
            boardSets(grid)
        # back to settings
        elif theIn == '6':
            print(change)
            if change:
                grid.createGrid()
            done = True
            settings(grid)


# settings for pieces
def pieceSets(grid, change):
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
            piece = input("Input the character you want to represent white pieces\nOnly the first character you type will be used: ")
            try:
                grid.whitePiece = piece[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid, change)
        # black piece setting
        elif theIn == '2':
            done = True
            piece = input("Input the character you want to represent black pieces\nOnly the first character you type will be used: ")
            try:
                grid.blackPiece = piece[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid, change)
        # white king setting
        elif theIn == '3':
            done = True
            piece = input("Input the character you want to represent white kings\nOnly the first character you type will be used: ")
            try:
                grid.whiteKing = piece[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid)
        # black king setting
        elif theIn == '4':
            done = True
            piece = input("Input the character you want to represent black kings\nOnly the first character you type will be used: ")
            try:
                grid.blackKing = piece[0]
                change = True
            except:
                print("ERROR: you did not input anything")
            pieceSets(grid, change)
        elif theIn == '5':
            done = True
            if change:
                grid.createGrid()
            settings(grid)


# general settings
def settings(grid):
    print("\nSettings:\n")
    print("WARNING: Changing any settings will reset your game")
    print("1. See Board Settings")
    print("2. See Piece settings")
    print("3. Two Player: On")
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
            pieceSets(grid, False)
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
    # check if it's a white piece or any king
    if grid.squares[y][x] == grid.whitePiece or grid.squares[y][x] == grid.whiteKing or grid.squares[y][x] == grid.blackKing:
        # set i to row above
        i = y - 1
        # look in column before and column after
        for j in range(-1, 2, 2):
            # check if square is empty
            if grid.testAvailable(i, x+j):
                # set grid space to be a valid space
                grid.squares[i][x+j] = grid.validSpace
                # add grid space to valid spaces
                grid.validPlaces.update([(i, x + j)])

    # check if it's a black piece or any king
    if grid.squares[y][x] == grid.blackPiece or grid.squares[y][x] == grid.blackKing or grid.squares[y][x] == grid.whiteKing:
        # set i to row below
        i = y + 1
        # look in column before and column after
        for j in range(-1, 2, 2):
            # check if square is empty
            if grid.testAvailable(i, x+j):
                # set grid space to be a valid space
                grid.squares[i][x+j] = "o"
                # add grid space to valid spaces
                grid.validPlaces.update([(i, x + j)])


# move method
def move(grid, starty, startx):

    done = False
    # do while not done
    while not done:
        print("Input the coordinates of the space you would like to move to (valid spaces shown with  ", end=grid.validSpace)
        theIn = input("): ")
        try:
            # set x to be int value
            x = ord(theIn[1].upper())
            x -= ord('A')
            # set y to be input - 1
            y = int(theIn[0]) - 1

            # check that move is valid
            if (y, x) in grid.validPlaces:
                # move piece in grid
                grid.completeMove(starty, startx, y, x)
                # print the grid again
                grid.printGrid()
                done = True
            else:
                # give feedback for invalid input
                print("\nERROR: invalid input\n")
                grid.printGrid()
        except:
            # check if player wanted to quit
            if theIn.lower() == "quit":
                done = True
                # go back to menu
                menu(grid)
            # give feedback for invalid input
            else:
                print("\nERROR: invalid input\n")
                grid.printGrid()


# play method
def play(grid):
    print()
    # print grid
    grid.printGrid()
    done = False
    while not done:
        # get piece type for current player
        piece = grid.getPieceType()
        king = grid.getKingType()

        print("\nType \"Quit\" to quit")
        theIn = input("Input coordinates of piece you would like to move: ")
        try:
            # set x to int
            x = ord(theIn[1].upper())
            x -= ord('A')
            # set y to given int minus 1
            y = int(theIn[0]) - 1
            # check that values are within grid boundaries
            if x < 0 or x > grid.width or y < 0 or y > grid.height:
                print("\nERROR: invalid input\n")
                grid.printGrid()
            else:
                # check that there is a valid piece in that square
                if grid.squares[y][x] == piece or grid.squares[y][x] == king:
                    # call valid places method
                    validPlaces(grid, x, y)
                    # check that there where valid spaces
                    if not grid.validPlaces:
                        print("\nERROR: No valid movements\n")
                        grid.printGrid()
                    else:
                        # print gid and move piece
                        grid.printGrid()
                        move(grid, y, x)
                        # change player
                        grid.player *= -1
                        print("\nNEXT PLAYER")
                        grid.printGrid()
                else:
                    print("\nERROR: your piece is not on this square\n")
                    grid.printGrid()
        except:
            # check if player wants to quit
            if theIn.lower() == "quit":
                done = True
                menu(grid)
            # give feedback for invalid input
            else:
                grid.printGrid()
                print("\nERROR: invalid input\n")


# define main
def main():
    # create grid of width and height
    grid = Grid(8, 8, 3)
    # print rules
    rules(grid)
    # go to menu
    menu(grid)


# run from main
if __name__ == "__main__":
    main()
