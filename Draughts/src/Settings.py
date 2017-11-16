# imports
from Grid import Grid
from AI import AI


__author__ = 'Emma'
__project__ = 'Draughts'


class Settings:
    def __init__(self, grid, coms):
        # set settings variables
        self.grid = grid
        self.com1 = AI(grid, -1)
        self.com2 = AI(grid, 1)
        self.coms = coms

# ************ Settings ***************

    # general settings
    def settings(self):
        # initialise done to false
        done = False
        # do while not done
        while not done:
            # print settings options
            print("\nSettings:\n")
            print("1. See Board Settings")
            print("2. See Piece settings")
            print("3. Players:", end=" ")
            # print What AI are playing
            if self.coms == 0:
                print("2 Humans")
            else:
                print(str(self.coms) + " Com(s)")
            if self.coms == 1:
                if self.com1.player == 1:
                    print("4. Com Player: 1")
                else:
                    print("4. Com Player: 2")
                print("5. Com Settings")
                print("6. Back")
            else:
                if self.coms == 2:
                    print("4. Com Settings")
                    print("5. Back")
                else:
                    print("4. Back")

            # set theIn to input
            theIn = input("enter number: ")
            # board settings
            if theIn == "1":
                self.boardSets(False)
            # piece settings
            elif theIn == '2':
                self.pieceSets()
            # toggle 2 players
            elif theIn == '3':
                self.coms += 1
                if self.coms > 2:
                    self.coms = 0
                elif self.coms == 2:
                    self.com1.player = -1
            # com1 player setting
            elif theIn == '4' and self.coms == 1:
                self.com1.player *= -1
            # ai settings
            elif theIn == '5' and self.coms == 1 or theIn == '4' and self.coms == 2:
                self.aiSets()
            # back to menu
            elif theIn == '4' or (theIn == '5' and self.coms == 2) or (theIn == '6' and self.coms == 1):
                done = True

    # settings for board
    def boardSets(self, change):
        while True:
            # print options for board settings
            print("\nBoard Settings:\n")
            print("1. Board Size:", end=" ")
            print(self.grid.width, end="x")
            print(self.grid.height)
            print("2. Starting rows:", end=" ")
            print(self.grid.rows)
            print("3. White Spaces: ", end=self.grid.whiteSpace)
            print("\n4. Black Spaces: ", end=self.grid.blackSpace)
            print("\n5. Valid movements: ", end=self.grid.validSpace)
            print("\n6. Back")

            # initialise done boolean to false
            done = False

            # get input
            theIn = input("enter number: ")
            # Board Size Setting
            if theIn == '1':
                # loop while action not complete
                while not done:
                    # try to set input to board height
                    try:
                        # print warning
                        print("WARNING: changing this setting will reset the game")
                        # print width disclaimer
                        print("Board width must be even and at least 4 and at most 26")
                        # set width to input
                        width = input("Input board width (Type Cancel to cancel): ")
                        # check if width equals cancel
                        if not width.lower() == "cancel":
                            # print height disclaimer
                            print("Board Height must less than 1000 and at least 4")
                            # set height to input
                            height = input("Input board height (Type Cancel to cancel: ")
                            # check if height equals cancel
                            if not height.lower() == "cancel":
                                # set height
                                self.grid.setHeight(int(height))
                                # set width
                                self.grid.setWidth(int(width))
                                # set change to true
                                change = True
                        # set done to true
                        done = True
                    except:
                        # print error
                        print("ERROR: please enter whole numbers")

            # Starting rows setting
            elif theIn == '2':
                # loop while action not complete
                while not done:
                    # try to set grid rows
                    try:
                        # print warning
                        print("WARNING: changing this setting will reset the game")
                        # set rows to input
                        rows = input("Input number of rows (Type Cancel to cancel): ")
                        # check if rows equal cancel
                        if not rows.lower() == "cancel":
                            # set rows
                            self.grid.setRows(int(rows))
                            # set change to true
                            change = True
                        # set done to true
                        done = True
                    except:
                        # print error
                        print("ERROR: Please enter a whole number")

            # White space setting
            elif theIn == '3':
                # print warning
                print("WARNING: changing this setting will reset the game")
                # set space to input
                space = input(
                    "Input the character you want to represent white spaces\nOnly the first character you type will be used: ")
                # try to set whitespace to space
                try:
                    # set whitespace
                    self.grid.whiteSpace = space[0]
                    # set change to true
                    change = True
                except:
                    # print error
                    print("ERROR: you did not input anything")
            # Black space setting
            elif theIn == '4':
                # warning
                print("WARNING: changing this setting will reset the game")
                # set space to input
                space = input(
                    "Input the character you want to represent black spaces\nOnly the first character you type will be used: ")
                # try to set blackspace to space
                try:
                    # set blackspace
                    self.grid.blackSpace = space[0]
                    # set change to true
                    change = True
                except:
                    # print error
                    print("ERROR: you did not input anything")
            # valid space setting
            elif theIn == '5':
                # set space to input
                space = input(
                    "Input the character you want to represent valid spaces\nOnly the first character you type will be used: ")
                # try to set validspace
                try:
                    # set valid space
                    self.grid.validSpace = space[0]
                except:
                    # print error
                    print("ERROR: you did not input anything")
            # back to settings
            if theIn == '6':
                # reset the grid if there have been major changes
                if change:
                    self.grid.createGrid()
                break

    # settings for pieces
    def pieceSets(self):
        while True:
            # print piece setting options
            print("\nPiece Settings:\n")
            print("1. White pieces: ", end=self.grid.whitePiece)
            print("\n2. Black pieces: ", end=self.grid.blackPiece)
            print("\n3. White Kings: ", end=self.grid.whiteKing)
            print("\n4. Black Kings: ", end=self.grid.blackKing)
            print("\n5. Back")

            theIn = input("enter number: ")

            # white pieces setting
            if theIn == '1':
                # set piece to input
                piece = input(
                    "Input the character you want to represent white pieces\nOnly the first character you type will be used: ")
                # try to set whitepiece to piece
                try:
                    # set whitepiece
                    self.grid.whitePiece = piece[0]
                    # reset grid
                    self.grid.resetGrid()
                except:
                    # print error
                    print("ERROR: you did not input anything")
            # black piece setting
            elif theIn == '2':
                # set piece to input
                piece = input(
                    "Input the character you want to represent black pieces\nOnly the first character you type will be used: ")
                # try to set blackpiece to piece
                try:
                    # set blackpiece
                    self.grid.blackPiece = piece[0]
                    # reset grid
                    self.grid.resetGrid()
                except:
                    # print error
                    print("ERROR: you did not input anything")
            # white king setting
            elif theIn == '3':
                # set piece to input
                piece = input(
                    "Input the character you want to represent white kings\nOnly the first character you type will be used: ")
                # try to set whiteking to piece
                try:
                    # set whiteking
                    self.grid.whiteKing = piece[0]
                    # reset grid
                    self.grid.resetGrid()
                except:
                    # print error
                    print("ERROR: you did not input anything")
            # black king setting
            elif theIn == '4':
                # set piece to input
                piece = input(
                    "Input the character you want to represent black kings\nOnly the first character you type will be used: ")
                # try to set blackking to piece
                try:
                    # set blackking
                    self.grid.blackKing = piece[0]
                    # reset grid
                    self.grid.resetGrid()
                except:
                    # print error
                    print("ERROR: you did not input anything")
            # back to settings
            if theIn == '5':
                break

    # settings for AI
    def aiSets(self):
        done = False
        change = False
        # set temp values to com1 values
        tempDepth = self.com1.depth
        tempKing = self.com1.kingScore
        tempTake = self.com1.takeScore
        tempWin = self.com1.win
        # loop while not done
        while not done:
            # print settings
            print("\n COM SETTINGS\n")
            print("1. Depth: " + str(tempDepth))
            print("2. King Score: " + str(tempKing))
            print("3. Take Score: " + str(tempTake))
            print("4. Win Score: " + str(tempWin))
            print("------------------------")
            print("5. Set Com1")
            print("6. set Com2")
            print("7. Set Both")
            print("------------------------")
            print("8. Back")

            # take input
            theIn = input("enter number: ")
            print()

            # depth setting
            if theIn == '1':
                while True:
                    print("This number represents how many moves the AI looks ahead before taking it's turn")
                    print("The higher this number is the harder the AI will be but the longer it will take to take it's turn")
                    print("type cancel to leave depth as it is")
                    newIn = input("enter new Depth: ")
                    if newIn.lower() == "cancel":
                        break
                    try:
                        # set temp depth to given depth
                        tempDepth = int(newIn)
                        break
                    except:
                        # print error
                        print("ERROR: please enter a valid number")
            # king score setting
            if theIn == '2':
                while True:
                    print("This number represents the value of getting a king to the AI")
                    print("The higher this value compared to the other scores the better it is considered to be")
                    print("type cancel to leave king score as it is")
                    newIn = input("enter new king score: ")
                    if newIn.lower() == "cancel":
                        break
                    try:
                        # set temp king score to given value
                        tempKing = int(newIn)
                        break
                    except:
                        # print error
                        print("ERROR: please enter a valid number")
            # take score setting
            if theIn == '3':
                while True:
                    print("This number represents the value of taking a piece to the AI")
                    print("The higher this value compared to the other scores the better it is considered to be")
                    print("type cancel to leave take score as it is")
                    newIn = input("enter new take score: ")
                    if newIn.lower() == "cancel":
                        break
                    try:
                        # set temp take score to given value
                        tempTake = int(newIn)
                        break
                    except:
                        # print error
                        print("ERROR: please enter a valid number")
            # win score setting
            if theIn == '4':
                while True:
                    print("This number represents the value of winning to the AI")
                    print("The higher this value compared to the other scores the better it is considered to be")
                    print("type cancel to leave win score as it is")
                    newIn = input("enter new win score: ")
                    if newIn.lower() == "cancel":
                        break
                    try:
                        # set temp score to given value
                        tempWin = int(newIn)
                        break
                    except:
                        # print error
                        print("ERROR: please enter a valid number")
            # set com 1
            if theIn == '5' or theIn == '7':
                # set com1s values to given values
                self.com1.depth = tempDepth
                self.com1.kingScore = tempKing
                self.com1.takeScore = tempTake
                self.com1.win = tempWin
                # print completed
                print("COMPLETE: Updated Com1")
                change = True
            # set com 2
            if theIn == '6' or theIn == '7':
                # set com2s values to given values
                self.com2.depth = tempDepth
                self.com2.kingScore = tempKing
                self.com2.takeScore = tempTake
                self.com2.win = tempWin
                # print completed
                print("COMPLETE: Updated Com2")
                change = True
            # back
            if theIn == '8':
                # check if something was changed
                if change:
                    done = True
                else:
                    # ask user if they're sure they want to exit without changing anything
                    while True:
                        print("You haven't set any changes you have made, are you sure you want to leave?")
                        newIn = input("Yes/No: ")
                        if newIn.lower() == "yes" or newIn.lower() == "y":
                            done = True
                            break
                        elif newIn.lower() == "no" or newIn.lower() == "n":
                            break


# ************ Rules ********************

    # define Draughts rules
    def rules(self):
        # rules printed based on the board settings
        print("\nRULES:", end="\n\n")
        print("Player 1: ", end="")
        if (self.coms > 0 and self.com1.player == 1) or self.coms == 2:
            print("COMPUTER")
        else:
            print("HUMAN")
        print("Player 2: ", end="")
        if (self.coms > 0 and self.com1.player == -1) or self.coms == 2:
            print("COMPUTER\n")
        else:
            print("HUMAN\n")
        print("• ", end="")
        print(self.grid.width, end="x")
        print(self.grid.height, end=" grid.\n")
        print("• Each player has", end=" ")
        print(int(self.grid.pieceNo), end=" pieces\n")
        print("• The counters go on the first", end=" ")
        print(self.grid.rows, end=" row(s)\n")
        print("• Player 1's pieces are shown by:", end=" ")
        print(self.grid.whitePiece, end="\n")
        print("• Player 2's pieces are shown by:", end=" ")
        print(self.grid.blackPiece, end="\n\n")

        print("• Pieces can only move Diagonally towards opponent")
        print("• An opponents piece is Captured by jumping your piece over it diagonally")
        print("• All landing spaces must be vacant")
        print("• If an opponents piece can be captured it must be")
        print("• multiple captures are possible if there's a blank space between each one")
        print("• Pieces that get to the other side of the board become Kings and can move forward and backwards")
        print()
