from Grid import Grid


class AI:
    def __init__(self, grid, player):
        self.grid = grid
        self.player = player

    def calculateMove(self):
        self.grid.printGrid()
        theIn = input("input coordinate")

        x = ord(theIn[0].upper()) - 65
        y = int(theIn[1]) - 1
        x2 = ord(theIn[2].upper()) - 65
        y2 = int(theIn[3]) - 1

        self.grid.completeMove(y, x, y2, x2)
