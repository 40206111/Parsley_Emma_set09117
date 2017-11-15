from Grid import Grid
from Memory import Tree

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
        self.depth = 2

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
        newGrid.turn = 0
        newGrid.memory.usedPieces.clear()
        if self.player == 1:
            index = self.maxIndex(self.minimax(0, newGrid, self.player, [0]))
        else:
            index = self.minIndex(self.minimax(0, newGrid, self.player, [0]))

        print(self.move)
        print(index)
        print(self.move[index])
        y = self.move[index][0][0]
        x = self.move[index][0][1]
        print(self.move[index])
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
                if depth == 0:
                    print(self.move)
                    self.move.append([p.xy])
                treeRoute = Tree(p.xy)
                treeRoute = self.takeRoute(grid, set(), treeRoute, p, p.xy[0], p.xy[1])
                thisScore = self.moveThroughTreeNodes(treeRoute, grid, score, otherpieces, player, depth)
                del thisScore[-1]

                if player == 1:
                    score[len(score) - 1] += max(thisScore)
                else:
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

    def moveThroughTreeNodes(self, treeRoute, grid, score, otherpieces, player, depth):
        for t in treeRoute.nodes:
            if depth == 0:
                print("nyam")
                print(self.move)
                self.move[len(self.move) - 1].append(t.value)
                print(self.move)
            grid.printGrid()
            print(grid.turn)
            print(treeRoute.value)
            print(t.value)
            grid.completeMove(treeRoute.value[0], treeRoute.value[1], t.value[0], t.value[1])
            print("AFTERMOVE")
            grid.printGrid
            grid.turn += 1
            score[len(score) - 1] += t.score
            score = self.moveThroughTreeNodes(t, grid, score, otherpieces, player, depth)
            print("USIED")
            print(grid.turn)
            print(grid.memory.usedPieces)
            grid.undo()
            del grid.memory.usedPieces[grid.turn]
            score[len(score) - 1] -= t.score
            if depth == 0:
                print("del")
                print(self.move)
                if len(self.move[len(self.move) - 1]) > 1:
                    del self.move[len(self.move) - 1][-1]
                else:
                    del self.move[len(self.move) - 1]
                print(self.move)


        if not treeRoute.nodes:
            if len(otherpieces) == 0:
                score[len(score) - 1] += self.win * player
            else:
                score.append(score[len(score) - 1] - treeRoute.score)
                if depth == 0:
                    print("app")
                    print(self.move)
                    self.move.append(self.move[len(self.move) - 1][:-1])
                    print(self.move)

                if player == 1:
                    score[len(score) - 2] += min(self.minimax(depth + 1, grid, -player, [0]))
                else:
                    score[len(score) - 2] += min(self.minimax(depth + 1, grid, -player, [0]))

        return score

    def takeRoute(self, grid, jumped, move, piece, y, x):
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
                                move.nodes.append(Tree((y + i + i, x + j + j)))
                                if not piece.king and (((y + i + i) == grid.height and piece.player == 1) or (
                                                (y + i + i) == 0 and piece.player == -1)):
                                    move.nodes[len(move.nodes) - 1].score += self.kingScore * piece.player
                                move.nodes[len(move.nodes) - 1].score += self.takeScore * piece.player
                                self.takeRoute(grid, jumped, move.nodes[len(move.nodes) - 1], piece, y + i + i, x + j + j)

                    except:
                        pass
        return move
