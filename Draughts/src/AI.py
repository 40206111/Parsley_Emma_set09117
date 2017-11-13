from Grid import Grid
import copy


class AI:
    def __init__(self, grid, player):
        self.grid = grid
        self.player = player
        self.takeScore = 3
        self.kingScore = 10
        self.win = 100
        self.takes = []
        self.move = []
        self.move.append([])
        self.depth = 1

    def calculateMove(self):
        self.grid.printGrid()
        newGrid = copy.deepcopy(self.grid)

        print(self.minimax(1, newGrid, self.player, [0]))
        theIn = input("input coordinate")

        x = ord(theIn[0].upper()) - 65
        y = int(theIn[1]) - 1
        x2 = ord(theIn[2].upper()) - 65
        y2 = int(theIn[3]) - 1

        self.grid.completeMove(y, x, y2, x2)
        self.move.clear()

    def minimax(self, depth, grid, player, score):
        if self.depth != depth:
            for p in grid.whitePieces:
                grid.canTake(p, p.xy[0], p.xy[1])

            for p in grid.whitePieces:
                if player == 1:
                    if p.xy in grid.ForcedPieces:
                        thisMove, thisScore = self.takeRoute(grid, set(), [[]], [0], p, p.xy[0], p.xy[1])
                        y1 = p.xy[0]
                        x1 = p.xy[1]
                        for i in range(0, thisMove):
                            if depth == 0:
                                self.move.append(thisMove[i])
                            for j in range(0, thisMove[i]):
                                grid.completeMove(y1, x1, thisMove[i][j][0], thisMove[i][j][1])
                                y1 = thisMove[i][j][0]
                                x1 = thisMove[i][j][1]
                            grid.turn += 1
                            if len(grid.blackPieces) == 0:
                                thisScore[i] += self.win
                            else:
                                thisScore[i] += min(self.minimax(depth + 1, grid, -player, score))
                            grid.undo()
                        score += max(thisScore)
                        score.append(0)
                    elif not grid.ForcedPieces:
                        grid.FindValids(p.xy[0], p.xy[1])
                        thisScore = [0]
                        if grid.validPlaces:
                            for i in range(0, len(grid.validPlaces)):
                                if depth == 0:
                                    self.move.append(grid.validPlaces[i])
                                grid.completeMove(p.xy[0], p.xy[1], grid.validPlaces[i][0], grid.validPlaces[i][1])
                                if p.king and p.king == grid.turn:
                                    thisScore[i] += self.kingScore
                                thisScore[i] += min(self.minimax(depth + 1, grid, -player, score))
                                thisScore.append(0)
                                grid.turn += 1
                                grid.undo()
                            score += max(thisScore)
                            score.append(0)
                        else:
                            score[len(score) - 1] += -self.win
                            score.append(0)
        return score


    def takeRoute(self, grid, jumped, move, score, piece, y, x):
        if piece.king:
            a = -1
            b = 2
        else:
            a = -piece.player
            b = -piece.player + 1

        for i in range(a, b, 2):
            for j in range(-1, 2, 2):
                if y + i + i in range(0, grid.height) and x + j + j in range(0, grid.width):
                    try:
                        if -piece.player == grid.squares[piece.xy[0] + i][piece.xy[1] + j].player:
                            if grid.testAvailable(y + i + i, x + j + j) and \
                                            (y + i, x + j) not in jumped:
                                jumped.add((y + i, x + j))

                                if not piece.king and (((y + i + i) == grid.height and piece.player == 1) or (
                                                (y + i + i) == 0 and piece.player == -1)):
                                    score[len(score) - 1] += self.kingScore * piece.player
                                move[len(move) - 1].append(grid.squares[piece.xy[0] + i + i][piece.xy[0] + j + j])
                                score[len(score) - 1] += self.takeScore * piece.player
                                score = self.takeRoute(grid, jumped, move, score, piece, y + i + i, x + j + j)
                                if score[len(score) - 1] != 0:
                                    score.append(0)
                                    move.append([])
                    except:
                        pass
        if score[len(score) - 1] == 0:
            del score[len(score) - 1]
            del move[len(move) - 1]
        return move, score
