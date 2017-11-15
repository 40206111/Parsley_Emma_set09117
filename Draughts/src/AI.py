from Grid import Grid
from Memory import Tree

import copy


class AI:
    # AI constructor
    def __init__(self, grid, player):
        # tell AI what grid it's playing on
        self.grid = grid
        # tell AI weather it is player 1(1) or player 2(-1)
        self.player = player
        # set Scores for minmax calculation
        self.takeScore = 3
        self.kingScore = 10
        self.win = 100
        # list of possible moves for this turn
        self.move = []
        # amount of turns it looks at before deciding it's move
        self.depth = 3

    # return index of smallest value in list
    def minIndex(self, theList):
        minimum = theList[0]
        minIndex = 0
        # from second element in list onward
        for i in range(1, len(theList)):
            # check if smaller than current minimum
            if theList[i] < minimum:
                # change minimum and minimum index
                minimum = theList[i]
                minIndex = i
        # return the index of the minimum
        return minIndex

    # return index of largest value in list
    def maxIndex(self, theList):
        maximum = theList[0]
        maxIndex = 0
        # from second element in list onward
        for i in range(1, len(theList)):
            # check if larger than current maximum
            if theList[i] > maximum:
                # change maximum and maximum index
                maximum = theList[i]
                maxIndex = i
        # return index of the minimum
        return maxIndex

    # method to calculate and complete move
    def calculateMove(self):
        # copy the grid to a new grid
        newGrid = copy.deepcopy(self.grid)
        # index of the maximum or minimum score depending on the player
        if self.player == 1:
            index = self.maxIndex(self.minimax(0, newGrid, self.player, [0]))
        else:
            index = self.minIndex(self.minimax(0, newGrid, self.player, [0]))

        # set y to first part of first position at index
        y = self.move[index][0][0]
        # set x to second part of first position at index
        x = self.move[index][0][1]

        # from second move onward in that index
        for i in range(1, len(self.move[index])):
            # set y2 and x2 to next position coordinates
            y2 = self.move[index][i][0]
            x2 = self.move[index][i][1]
            # set end place to be a valid space
            self.grid.squares[y2][x2] = self.grid.validSpace
            # print grid
            self.grid.printGrid()
            # complete the move
            self.grid.completeMove(y, x, y2, x2)
            # empty valid places
            self.grid.emptyValids()
            y = y2
            x = x2
        # print grid after move
        self.grid.printGrid()
        # clear moves
        self.move.clear()

    # method to get minimax score for player given
    def minimax(self, depth, grid, player, score):
        # finish if reached depth
        if self.depth != depth:
            # give correct pieces to be calculated depending on player
            if player == 1:
                score = self.calculate(grid, grid.whitePieces, grid.blackPieces, player, depth, score)
            else:
                score = self.calculate(grid, grid.blackPieces, grid.whitePieces, player, depth, score)
        return score

    # method to calculate scores
    def calculate(self, grid, pieces, otherpieces, player, depth, score):
        # check if any pieces have to take
        for p in pieces:
            grid.canTake(p, p.xy[0], p.xy[1])
        # keep local copy of pieces that have to take
        forced = copy.copy(grid.ForcedPieces)

        # for all pieces
        for p in pieces:
            # check if piece is forced to take
            if p.xy in forced:
                # check if depth equals 0
                if depth == 0:
                    # add piece to start of self moves
                    self.move.append([p.xy])
                # set route of take tree to be piece
                takeTree = Tree(p.xy)
                # calculate take tree
                takeTree = self.takeRoute(grid, set(), takeTree, p, p.xy[0], p.xy[1])
                # calculate scores for take tree
                self.moveThroughTreeNodes(takeTree, grid, score, otherpieces, player, depth)
                # set last score to 0
                score[len(score) - 1] = 0
            # if pieces have not been forced to take
            elif not forced:
                # find all valid movements for this piece
                grid.FindValids(p.xy[0], p.xy[1])
                # if there are valid movements for this piece
                if grid.validPlaces:
                    # keep local copy of valid places
                    tempv = copy.copy(grid.validPlaces)
                    # for all valid places
                    for v in tempv:
                        # add to moves if at depth 0
                        if depth == 0:
                            self.move.append([p.xy, v])
                        # do move to that place
                        grid.completeMove(p.xy[0], p.xy[1], v[0], v[1])
                        # if piece wasn't king before but is now add to score
                        if p.king and p.king == grid.turn:
                            score[len(score) - 1] += self.kingScore
                        # add turn
                        grid.turn += 1
                        # test what next players best move is and add their score to score
                        if player == 1:
                            score[len(score) - 1] += min(self.minimax(depth + 1, grid, -player, [0]))
                        else:
                            score[len(score) - 1] += max(self.minimax(depth + 1, grid, -player, [0]))
                        # append score
                        score.append(0)
                        # undo
                        grid.undo()
                        # delete last turn from memory
                        del grid.memory.usedPieces[grid.turn]
        # delete last score
        del score[len(score) - 1]
        # if player cannot score other player has won
        if not score:
            # take away player win from score
            score.append(0)
            score[len(score) - 1] -= self.win * player
        # return score
        return score

    # do the moves in the take tree
    def moveThroughTreeNodes(self, treeRoute, grid, score, otherpieces, player, depth):
        # loop through nodes in tree route
        for t in treeRoute.nodes:
            # if depth is 0 add node to move
            if depth == 0:
                self.move[len(self.move) - 1].append(t.value)
            # move from tree route position to tree node position
            grid.completeMove(treeRoute.value[0], treeRoute.value[1], t.value[0], t.value[1])
            # add turn
            grid.turn += 1
            # add node score to score
            score[len(score) - 1] += t.score
            # calculate score for rest of take tree
            score = self.moveThroughTreeNodes(t, grid, score, otherpieces, player, depth)
            # undo move
            grid.undo()
            # delete last turn from memory
            del grid.memory.usedPieces[grid.turn]
            # take away node score from last score
            score[len(score) - 1] -= treeRoute.score
            # if depth is 0 remove nodes from last move
            if depth == 0:
                if len(self.move[len(self.move) - 1]) > 1:
                    del self.move[len(self.move) - 1][-1]
                else:
                    del self.move[len(self.move) - 1]

        # if there are no nodes under the treeRoute
        if not treeRoute.nodes:
            # if all of the other players pieces have been taken
            if len(otherpieces) == 0:
                # add win score to score
                score[len(score) - 1] += self.win * player
                # append new score equal to last score - this nodes score - win score
                score.append(score[len(score) - 1] - treeRoute.score - self.win)
            else:
                # append new score equal to last score - this nodes score
                score.append(score[len(score) - 1] - treeRoute.score)
            # if depth is 0 append new move equal to last move minus move to this node
            if depth == 0:
                self.move.append(self.move[len(self.move) - 1][:-1])

            # test what next players best move is and add their score to score
            if player == 1:
                score[len(score) - 2] += min(self.minimax(depth + 1, grid, -player, [0]))
            else:
                score[len(score) - 2] += min(self.minimax(depth + 1, grid, -player, [0]))
        # return score
        return score

    # method to calculate takes a piece can make
    def takeRoute(self, grid, jumped, move, piece, y, x):
        # check if player can move backwards and forwards or not
        if piece.king:
            a = -1
            b = 2
        else:
            a = -piece.player
            b = -piece.player + 1

        # loop through vertical ways piece can move
        for i in range(a, b, 2):
            # loop through left and right of piece
            for j in range(-1, 2, 2):
                # if 2 squares away is still on the board
                if y + i + i in range(0, grid.height) and x + j + j in range(0, grid.width):
                    try:
                        # piece next to this piece is opponents piece
                        if -piece.player == grid.squares[y + i][x + j].player:
                            # if square 2 away is free and piece has not already been jumped
                            if grid.testAvailable(y + i + i, x + j + j) and \
                                            (y + i, x + j) not in jumped:
                                # add to jumped
                                jumped.add((y + i, x + j))
                                # add space to take tree
                                move.nodes.append(Tree((y + i + i, x + j + j)))
                                # if piece becomes king from this move
                                if not piece.king and (((y + i + i) == grid.height and piece.player == 1) or (
                                                (y + i + i) == 0 and piece.player == -1)):
                                    # add king score to node score
                                    move.nodes[len(move.nodes) - 1].score += self.kingScore * piece.player
                                # add take score to node score
                                move.nodes[len(move.nodes) - 1].score += self.takeScore * piece.player
                                # call methods with next space
                                self.takeRoute(grid, jumped, move.nodes[len(move.nodes) - 1], piece, y + i + i, x + j + j)
                    except:
                        pass
        # return take tree
        return move
