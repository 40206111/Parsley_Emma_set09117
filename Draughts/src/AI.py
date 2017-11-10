from Grid import Grid


class AI:
    def __init__(self, grid, player):
        self.grid = grid
        self.player = player
        self.takeScore = 3
        self.kingScore = 10
        self.takes = []
        self.move = []
        self.move.append([])

    def calculateMove(self):
        self.grid.printGrid()
        print(self.takeRoute(set(), [[]], [0], self.grid.squares[2][0], 2, 0))
        theIn = input("input coordinate")

        x = ord(theIn[0].upper()) - 65
        y = int(theIn[1]) - 1
        x2 = ord(theIn[2].upper()) - 65
        y2 = int(theIn[3]) - 1

        self.grid.completeMove(y, x, y2, x2)

    def takeRoute(self, jumped, move, score, piece, y, x):
        cont = False
        if piece.king:
            a = -1
            b = 2
        else:
            a = -piece.player
            b = -piece.player + 1

        for i in range(a, b, 2):
            for j in range(-1, 2, 2):
                if y + i + i in range(0, self.grid.height) and x + j + j in range(0, self.grid.width):
                    try:
                        if -piece.player == self.grid.squares[piece.xy[0] + i][piece.xy[1] + j].player:
                            if self.grid.testAvailable(y + i + i, x + j + j) and \
                                            (y + i, x + j) not in jumped:
                                jumped.add((y + i, x + j))

                                if not piece.king and (((y + i + i) == self.grid.height and piece.player == 1) or (
                                                (y + i + i) == 0 and piece.player == -1)):
                                    score[len(score) - 1] += self.kingScore
                                move[len(move) - 1].append(self.grid.squares[piece.xy[0] + i + i][piece.xy[0] + j + j])
                                score[len(score) - 1] += self.takeScore
                                score = self.takeRoute(jumped, move, score, piece, y + i + i, x + j + j)
                                if score[len(score) - 1] != 0:
                                    score.append(0)
                                    move.append([])
                    except:
                        pass
        if score[len(score) - 1] == 0:
            del score[len(score) - 1]
            del move[len(move) - 1]
        return score

