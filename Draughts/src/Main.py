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
        if grid.memory.turn > 0:
            theIn = input("Play, Replay, NewGame, Rules, Exit: ")
        else:
            # set theIn to input
            theIn = input("Play, NewGame, Settings, Rules, Exit: ")
        # make theIn lowercase
        theIn = theIn.lower()
        # play game
        if theIn == "play":
            play(grid, settings)
        # reset grid and play
        elif theIn == "newgame":
            # reset grid
            grid.createGrid()
            play(grid, settings)
        elif theIn == "replay" and grid.memory.turn > 0:
            replay(grid)
        # view settings
        elif theIn == "settings":
            settings.settings()
        # view rules
        elif theIn == "rules":
            settings.rules()
        # exit game
        elif theIn == "exit":
            done = True


# ******** Helper Methods **********

# method to parse the input as x and y values
def setInput(theIn):
    # if last character is a letter in the english alphabet
    if 65 <= ord(theIn[len(theIn) - 1].upper()) <= 90:
        # set x to int
        x = ord(theIn[len(theIn) - 1].upper())
        x -= ord('A')

        # set the in to be the rest of the input
        theIn = theIn[:-1]
        # set y to given int minus 1
        y = int(theIn) - 1
    # if first character is a letter in the english alphabet
    elif 65 <= ord(theIn[0].upper()) <= 90:
        # set x to int
        x = ord(theIn[0].upper())
        x -= ord('A')

        # set the in to be the rest of the input
        theIn = theIn[1:]
        # set y to given int minus 1
        y = int(theIn) - 1
    # return x and y
    return y, x


# method to check if any pieces in a list can take
def checkForTakes(grid, pieces):
    for i in range(len(pieces)):
        grid.canTake(pieces[i], pieces[i].xy[0], pieces[i].xy[1])


# ************ Movement ***************

# move method
def move(grid, starty, startx):
    if len(grid.memory.usedPieces) > grid.turn:
        if 0 != grid.memory.turn >= grid.turn:
            for i in range(len(grid.memory.usedPieces)-1, grid.turn-1, -1):
                del grid.memory.usedPieces[i]
        else:
            del grid.memory.usedPieces[grid.turn]

    # initialise done to false
    done = False
    # do while not done
    while not done:
        # print grid
        print()
        grid.printGrid()
        print()
        # print instruction
        print(
            "Input the coordinates of the space you would like to move to \n(type cancel to select other piece, valid spaces shown with  ",
            end=grid.validSpace)
        # set theIn to input
        theIn = input("): ")
        # check if player wanted to cancel
        if (theIn.lower() == "cancel" or theIn.lower() == "undo") and not grid.more:
            # set done to true
            done = True
        elif theIn.lower() == "undo" and grid.more:
            grid.more = False
            grid.turn += 1
            undo(grid)
            grid.turn -= 1
            done = True
        # if player wants to finish there move and they have already moved
        elif theIn.lower() == "no" and grid.more:
            # set more moves to false
            grid.more = False
            # empty valid movements
            grid.emptyValids()
            # empty forced moved pieces
            grid.ForcedPieces.clear()
            # empty double takes
            grid.DoubleTakes.clear()
            done = True
        else:
            # try to complete move
            try:
                # parse the in to x and y
                y, x = setInput(theIn)
                # check that move is valid
                if (y, x) in grid.validPlaces:
                    # move piece in grid
                    if not grid.completeMove(starty, startx, y, x):
                        # if more moves
                        if grid.more:
                            # print explanation
                            print("There are more pieces you can take, type no to end your turn")
                            # set starty to y
                            starty = y
                            # set start x to x
                            startx = x
                        else:
                            # print error
                            print("ERROR: there are multiple ways to get to this point please enter your route step by step")
                    else:
                        # set done to true
                        done = True
                else:
                    # give feedback for invalid input
                    print("\nERROR: invalid input")
            except:
                # print error
                print("\nERROR: invalid input")


# first method for movement if take has been forced
def forceTakeMove(grid):
    # print grid
    print()
    grid.printGrid()
    print()
    # print instruction
    print("\nType \"Quit\" to quit")
    print("FORCE TAKE:\nYou are able to take at least one of your enemies pieces.\nPlease input one of the following:")
    # output coordinates of all pieces that can take
    for f in grid.ForcedPieces:
        print(chr(65 + f[1]), end=str(f[0] + 1))
        print()
    # set theIn to input
    theIn = input("Input: ")
    if theIn.lower() == "undo":
        undo(grid)
        return 2
    elif theIn.lower() == "redo":
        redo(grid)
        return 2
    # check if player wants to quit
    elif theIn.lower() == "quit":
        return True
    else:
        # try to select piece to move
        try:
            # parse input to x and y
            y, x = setInput(theIn)
            # check that there is a valid piece in that square
            if (y, x) not in grid.ForcedPieces:
                # print error
                print("\nERROR: invalid input")
            else:
                # check for valid places piece can move
                grid.takes(set(), grid.squares[y][x], y, x)
                # check that there where valid spaces
                if not grid.validPlaces:
                    # program should not be able to get here without valid movements
                    print("\nERROR: Something has gone wrong")
                    # print grid
                    grid.printGrid()
                else:
                    # move piece
                    move(grid, y, x)
                    # check if piece was moved
                    if grid.validPlaces:
                        # empty valid pieces
                        grid.emptyValids()
                    else:
                        return False
        except:
            # print error
            print("\nERROR: Invalid input")
            return forceTakeMove(grid)
    return forceTakeMove(grid)


# first method for movement if there are no takes
def choosePiece(grid):
    # print grid
    print()
    grid.printGrid()
    print()
    # print instruction
    print("\nType \"Quit\" to quit")
    # set theIn to input
    theIn = input("Input coordinates of piece you would like to move: ")
    if theIn.lower() == "undo":
        undo(grid)
        return 2
    elif theIn.lower() == "redo":
        redo(grid)
        return 2
    # check if player wants to quit
    elif theIn.lower() == "quit":
        return True
    else:
        # try to select piece to move
        try:
            # parse input as y and x
            y, x = setInput(theIn)
            # check that values are within grid boundaries
            if x not in range(0, grid.width) or y not in range(0, grid.height):
                # print error
                print("\nERROR: invalid input")
            else:
                # check that there is a valid piece in that square
                if grid.squares[y][x].player == grid.player:
                    # call valid places method
                    grid.FindValids(y, x)
                    # check that there where valid spaces
                    if not grid.validPlaces:
                        # print error
                        print("\nERROR: No valid movements")
                        # print grid
                        grid.printGrid()
                    else:
                        # move piece
                        move(grid, y, x)
                        # check if piece was moved
                        if grid.validPlaces:
                            # empty valid pieces
                            grid.emptyValids()
                        else:
                            return False
                else:
                    # print error
                    print("\nERROR: your piece is not on this square")
        except:
            print("\nERROR: invalid input")
            return choosePiece(grid)
    return choosePiece(grid)


# ************* Play *************

# play method
def play(grid, settings):
    print()

    # do while not done
    while True:
        # check if anyone has Won
        if len(grid.blackPieces) == 0:
            print()
            grid.printGrid()
            print("\nPLAYER 1 WINS!\n")
            theIn = input("Would you like to replay your game now(y/n): ").lower()
            if theIn == "y" or theIn == "yes" or theIn == "ok" or theIn == "go for it" or theIn == "replay":
                replay(grid)
            break
        elif len(grid.whitePieces) == 0:
            print()
            grid.printGrid()
            print("\nPLAYER 2 WINS\n")
            theIn = input("Would you like to replay your game now(y/n): ").lower()
            if theIn == "y" or theIn == "yes" or theIn == "ok" or theIn == "go for it" or theIn == "replay":
                replay(grid)
            break

        # print the player who's turn it is
        if grid.player == 1:
            print("\nPLAYER 1's TURN (" + grid.whitePiece + ")")
        else:
            print("\nPLAYER 2's TURN (" + grid.blackPiece + ")")

        # check if current player has any forced takes
        if grid.player == 1:
            checkForTakes(grid, grid.whitePieces)
        else:
            checkForTakes(grid, grid.blackPieces)

        if settings.coms > 0:
            if grid.player == settings.com1.player:
                settings.com1.calculateMove()
            elif settings.coms == 2 and grid.player == settings.com2.player:
                settings.com2.calculateMove()
        if (settings.coms == 1 and settings.com1.player != grid.player) or settings.coms == 0:

            # if player doesn't have forced takes move normally
            if not grid.ForcedPieces:
                if grid.player == 1:
                    for p in grid.whitePieces:
                        grid.FindValids(p.xy[0], p.xy[1])
                else:
                    for p in grid.blackPieces:
                        grid.FindValids(p.xy[0], p.xy[1])
                if grid.validPlaces:
                    grid.emptyValids()
                    done = choosePiece(grid)
                else:
                    print("NO LEGAL MOVES")
                    if grid.player == 1:
                        print("PLAYER 2 WINS!")
                    else:
                        print("PLAYER 1 WINS")
                    theIn = input("Would you like to replay your game now(y/n): ").lower()
                    if theIn == "y" or theIn == "yes" or theIn == "ok" or theIn == "go for it" or theIn == "replay":
                        replay(grid)
                    break
            else:
                done = forceTakeMove(grid)
        if not done:
            # change player
            grid.player *= -1

            if grid.memory.turn == grid.turn:
                grid.memory.turn += 1
                # increase turn
                grid.turn += 1
        elif done and done != 2:
            break


def replay(grid):
        for i in range(grid.turn, 0, -1):
            undo(grid)
        grid.printGrid()
        while True:
            input("press enter to continue: ")
            redo(grid)
            grid.printGrid()
            if grid.turn >= grid.memory.turn:
                break
        print("REPLAY FINISHED")
        input("press enter to go back to menu")


def redo(grid):
    nextTurn = grid.turn
    if nextTurn >= grid.memory.turn:
        print("NO MORE REDOs")
        play(grid)
    else:
        grid.ForcedPieces.clear()
        grid.DoubleTakes.clear()
        grid.emptyValids()
        for p in grid.memory.usedPieces[nextTurn]:
            if nextTurn in p.turn:
                xy = p.turn.get(nextTurn)
                grid.normalMove(p.xy[0], p.xy[1], xy[0], xy[1])
            else:
                p.turnTaken = nextTurn
                if p.player == 1:
                    grid.whitePieces.remove(p)
                else:
                    grid.blackPieces.remove(p)
                grid.squares[p.xy[0]][p.xy[1]] = grid.blackSpace
        grid.turn += 1
        grid.player *= -1


def undo(grid):
    if grid.turn == 0:
        print("NO MORE UNDOs")
        play(grid)
    else:
        lastTurn = grid.turn - 1
        grid.ForcedPieces.clear()
        grid.DoubleTakes.clear()
        grid.emptyValids()
        grid.turn -= 1
        for p in grid.memory.usedPieces[lastTurn]:
            if lastTurn in p.turn:
                xy = p.turn.get(lastTurn)
                grid.normalMove(p.xy[0], p.xy[1], xy[0], xy[1])
            if p.turnTaken == lastTurn:
                p.turnTaken = 0
                grid.squares[p.xy[0]][p.xy[1]] = p
                if p.player == 1:
                    grid.whitePieces.append(p)
                    p.col = grid.whitePiece
                    p.kingLetter = grid.whiteKing
                else:
                    grid.blackPieces.append(p)
                    p.col = grid.blackPiece
                    p.kingLetter = grid.blackKing
            if p.king == lastTurn:
                p.king = 0
        grid.player *= -1


# define main
def main():
    # create grid of width and height
    grid = Grid(8, 8, 3)
    settings = Settings(grid, 1)

    # print rules
    settings.rules()
    # go to menu
    menu(grid, settings)


# run from main
if __name__ == "__main__":
    main()
