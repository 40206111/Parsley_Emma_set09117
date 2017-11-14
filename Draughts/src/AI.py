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
        self.depth = 1

    def minIndex(self, theList):
        minimum = theList[0]
        minIndex = 0
        for i in range(1, len(theList)):
            if theList[i] < minimum:
                minimum = theList[i]
                minIndex = i
        return minIndex

    def maxIndex(self, theList):
        maximum = theList[0]
        maxIndex = 0
        for i in range(1, len(theList)):
            if theList[i] > maximum:
                maximum = theList[i]
                maxIndex = i
        return maxIndex

    def calculateMove(self):
        newGrid = copy.deepcopy(self.grid)
        #newGrid.turn += 1
        that = [0]
        if self.player == 1:
            index = self.maxIndex(self.minimax(0, newGrid, self.player, [0]))
        else:
            index = self.minIndex(self.minimax(0, newGrid, self.player, [0]))

        y = self.move[index][0][0]
        x = self.move[index][0][1]
        for i in range(1, len(self.move[index])):
            y2 = self.move[index][i][0]
            x2 = self.move[index][i][1]
            self.grid.squares[y2][x2] = self.grid.validSpace
            self.grid.printGrid()
            self.grid.completeMove(y, x, y2, x2)
            self.grid.emptyValids()
            self.grid.printGrid()
            y = y2
            x = x2
        self.move.clear()


    def minimax(self, depth, grid, player, score):
        if self.depth != depth:
            if player == 1:
                score = self.calculate(grid, grid.whitePieces, grid.blackPieces, player, depth, score)
            else:
                score = self.calculate(grid, grid.blackPieces, grid.whitePieces, player, depth, score)
        return score

    def calculate(self, grid, pieces, otherpieces, player, depth, score):
        for p in pieces:
            grid.canTake(p, p.xy[0], p.xy[1])
        forced = copy.copy(grid.ForcedPieces)
        for p in pieces:
            if p.xy in forced:
                thisScore, thisMove = self.takeRoute(grid, set(), [[]], [0], p, p.xy[0], p.xy[1])
                y1 = p.xy[0]
                x1 = p.xy[1]
                for i in range(0, len(thisMove)):
                    if depth == 0:
                        self.move.append([p.xy] + thisMove[i])
                    for j in range(0, len(thisMove[i])):
                        grid.completeMove(y1, x1, thisMove[i][j][0], thisMove[i][j][1])
                        y1 = thisMove[i][j][0]
                        x1 = thisMove[i][j][1]
                    if len(otherpieces) == 0:
                        thisScore[i] += self.win * player
                    else:
                        if player == 1:
                            thisScore[i] += min(self.minimax(depth + 1, grid, -player, [0]))
                        else:
                            thisScore[i] += max(self.minimax(depth + 1, grid, -player, [0]))
                    grid.turn += 1
                    grid.undo()
                score[len(score) - 1] += max(thisScore)
                score.append(0)
            elif not forced:
                grid.FindValids(p.xy[0], p.xy[1])
                if grid.validPlaces:
                    tempv = copy.copy(grid.validPlaces)
                    for v in tempv:
                        if depth == 0:
                            self.move.append([p.xy, v])
                        grid.completeMove(p.xy[0], p.xy[1], v[0], v[1])
                        grid.turn += 1
                        if p.king and p.king == grid.turn:
                            score[len(score) - 1] += self.kingScore
                        if player == 1:
                            score[len(score) - 1] += min(self.minimax(depth + 1, grid, -player, [0]))
                        else:
                            score[len(score) - 1] += max(self.minimax(depth + 1, grid, -player, [0]))
                        score.append(0)
                        grid.undo()
                        del grid.memory.usedPieces[grid.turn]
        del score[len(score) - 1]
        if not score:
            score.append(0)
            score[len(score) - 1] -= self.win * player
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
                        if -piece.player == grid.squares[y + i][x + j].player:
                            if grid.testAvailable(y + i + i, x + j + j) and \
                                            (y + i, x + j) not in jumped:
                                jumped.add((y + i, x + j))

                                if not piece.king and (((y + i + i) == grid.height and piece.player == 1) or (
                                                (y + i + i) == 0 and piece.player == -1)):
                                    score[len(score) - 1] += self.kingScore * piece.player
                                move[len(move) - 1].append((y + i + i, x + j + j))
                                score[len(score) - 1] += self.takeScore * piece.player
                                score, unneeded = self.takeRoute(grid, jumped, move, score, piece, y + i + i, x + j + j)
                                if score[len(score) - 1] != 0:
                                    score.append(0)
                                    move.append([])
                    except:
                        pass
        if score[len(score) - 1] == 0:
            del score[len(score) - 1]
            del move[len(move) - 1]
        return score, move
