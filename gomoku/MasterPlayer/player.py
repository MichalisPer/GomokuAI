import math
from misc import winningTest, legalMove
from gomokuAgent import GomokuAgent
import numpy as np

PLUS_PATTERN = ["00000", "00001", "10000", "00010", "00100", "01000", "00011", "00101", "01001", "10001", "10010",
                "10100", "11000", "00110", "01010", "01100", "00111", "01011", "01101", "10011", "10101", "10110",
                "11001", "11010", "11100", "01110", "01111", "10111", "11011", "11101", "11110", "0011100", "01011010",
                "101010101", "010110", "011010", "011100", "001110", "011110", "11011011", "111010111"]

MINUS_PATTERN = ["00000", "0000-1", "-10000", "000-10", "00-100", "0-1000", "000-1-1", "00-10-1", "0-100-1", "-1000-1",
                 "-100-10", "-10-100", "-1-1000", "00-1-10", "0-10-10", "0-1-100", "00-1-1-1", "0-10-1-1", "0-1-10-1",
                 "100-1-1", "-10-10-1", "-10-1-10", "-1-100-1", "-1-10-10", "-1-1-100", "0-1-1-10", "0-1-1-1-1",
                 "-10-1-1-1", "-1-10-1-1", "-1-1-10-1", "-1-1-1-10", "00-1-1-100", "0-10-1-10-10", "-10-10-10-10-1",
                 "0-10-1-10", "0-1-10-10", "0-1-1-100", "00-1-1-10", "0-1-1-1-10", "-1-10-1-10-1-1", "-1-1-10-10-1-1-1"]

PATTERN_IDX_ZEROS = [None, [3], [1], [2, 4], [1, 3], [0, 2], [2], [1, 3], [0, 2, 3], [1, 2, 3], [1, 2, 4], [1, 3],
                     [2], [1, 4], [0, 2, 4], [0, 3], [1], [0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3],
                     [0, 4], [0], [1], [2], [3], [4], [1, 5], [2, 5], [3, 5], [2], [3], [4], [1], [0, 5], [2, 5],
                     [3, 5]]

PATTERN_IDX = [None, [4], [0], [3], [2], [1], [3, 4], [2, 4], [1, 4], [0, 4], [0, 3], [0, 2], [0, 1], [2, 3], [1, 3],
               [1, 2], [2, 3, 4], [1, 3, 4], [1, 2, 4], [0, 3, 4], [0, 2, 4], [0, 2, 3], [0, 1, 4], [0, 1, 3],
               [0, 1, 2], [1, 2, 3], [1, 2, 3, 4], [0, 2, 3, 4], [0, 1, 3, 4], [0, 1, 2, 4], [0, 1, 2, 3], [2, 3, 4],
               [1, 3, 4, 6], [0, 2, 4, 6, 8], [1, 3, 4], [1, 2, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4],
               [0, 1, 3, 4, 6, 7], [0, 1, 2, 4, 6, 7, 8]]

SEVERITY_IDX = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
                [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37], [38, 39, 40]]


def decide_comb(r, c, i, board, sign=1, diagonal=False):
    if not diagonal:
        if i == 18 and c + 5 <= 10 and board[r, c + 5] == 0:
            return 35
        elif i == 20 and c + 8 <= 10 and board[r, c + 5] == 0 and board[r, c + 6] == sign and board[r, c + 7] == 0 and \
                board[r, c + 8] == sign:
            return 33
        elif i == 17 and c + 7 <= 10 and board[r, c + 5] == 0 and board[r, c + 6] == sign and board[r, c + 7] == 0:
            return 32
        elif i == 17 and c + 5 <= 10 and board[r, c + 5] == 0:
            return 34
        elif i == 16:
            if c + 5 <= 10 and c + 6 <= 10 and board[r, c + 5] == 0 and board[r, c + 6] == 0:
                return 31
            elif c + 5 < 10 and board[r, c + 5] == 0:
                return 37
        elif i == 25 and c + 5 <= 10 and board[r, c + 5] == 0:
            return 36
        elif i == 26 and c + 5 <= 10 and board[r, c + 5] == 0:
            return 38
        elif i == 28 and c + 7 <= 10 and board[r, c + 5] == 0 and board[r, c + 6] == sign and board[r, c + 7] == sign:
            return 39
        elif i == 29 and c + 8 <= 10 and board[r, c + 5] == 0 and board[r, c + 6] == sign and board[
            r, c + 7] == sign and \
                board[r, c + 8] == sign:
            return 40
        return i
    else:
        if i == 18 and r + 5 <= 10 and c + 5 <= 10 and board[r + 5, c + 5] == 0:
            return 35
        if i == 20 and r + 8 <= 10 and c + 8 <= 10 and board[r + 5, c + 5] == 0 and board[r + 6, c + 6] == sign and \
                board[r + 7, c + 7] == 0 and board[r + 8, c + 8] == sign:
            return 33
        elif i == 17 and c + 7 <= 10 and r + 7 <= 10 and board[r + 5, c + 5] == 0 and board[r + 6, c + 6] == sign and \
                board[r + 7, c + 7] == 0:
            return 32
        elif i == 17 and r + 5 <= 10 and c + 5 <= 10 and board[r + 5, c + 5] == 0:
            return 34
        elif i == 16:
            if r + 6 <= 10 and r and c + 6 <= 10 and board[r + 5, c + 5] == 0 and board[r + 6, c + 6] == 0:
                return 31
            elif c + 5 < 10 and r + 5 <= 10 and board[r + 5, c + 5] == 0:
                return 37
        elif i == 25 and c + 5 <= 10 and r + 5 <= 10 and board[r + 5, c + 5] == 0:
            return 36
        elif i == 26 and r + 5 <= 10 and c + 5 <= 10 and board[r + 5, c + 5] == 0:
            return 38
        elif i == 28 and c + 7 <= 10 and r + 7 <= 10 and board[r + 5, c + 5] == 0 and board[r + 6, c + 6] == sign and \
                board[r + 7, c + 7] == sign:
            return 39
        elif i == 29 and r + 8 <= 10 and c + 8 <= 10 and board[r + 5, c + 5] == 0 and board[r + 6, c + 6] == sign and \
                board[r + 7, c + 7] == sign and board[r + 8, c + 8] == sign:
            return 40
        return i


def poss_moves(board, turnID):
    zero_threat, non_threats, force_threats, win_threat = [], [], [], []
    neighbours = [zero_threat, non_threats, force_threats, win_threat]

    for rot in range(2):
        for r in range(11):
            for c in range(7):
                for i, p in enumerate(zip(PLUS_PATTERN, MINUS_PATTERN)):
                    if 1 in [board[r, c], board[r, c + 1], board[r, c + 2], board[r, c + 3], board[r, c + 4]] and \
                            -1 in [board[r, c], board[r, c + 1], board[r, c + 2], board[r, c + 3], board[r, c + 4]]:
                        break
                    if i > 30:
                        break
                    if p[0] == str(board[r, c]) + str(board[r, c + 1]) + str(board[r, c + 2]) + str(
                            board[r, c + 3]) + str(board[r, c + 4]):
                        if i == 0:
                            break
                        i = decide_comb(r, c, i, board)
                        coord_idx = [j for j in range(4) if i in SEVERITY_IDX[j]][0]
                        if turnID == 1 and coord_idx == 3:
                            final = []
                            for offset in PATTERN_IDX_ZEROS[i]:
                                coord = (r, c + offset) if rot == 0 else (c + offset, 10 - r)
                                final.append(coord)
                            return final
                        for offset in PATTERN_IDX_ZEROS[i]:
                            coord = (r, c + offset) if rot == 0 else (c + offset, 10 - r)
                            if coord not in [xs for k in range(coord_idx, 4) for xs in neighbours[k]]:
                                neighbours[coord_idx].append(coord)
                                temp = [j for j in range(coord_idx - 1, -1, -1) if coord in neighbours[j]]
                                for x in temp:
                                    neighbours[x].remove(coord)
                        break
                    elif p[1] == str(board[r, c]) + str(board[r, c + 1]) + str(board[r, c + 2]) + str(
                            board[r, c + 3]) + str(board[r, c + 4]):
                        if i == 0:
                            break
                        i = decide_comb(r, c, i, board, -1)
                        coord_idx = [j for j in range(4) if i in SEVERITY_IDX[j]][0]
                        if turnID == -1 and coord_idx == 3:
                            final = []
                            for offset in PATTERN_IDX_ZEROS[i]:
                                coord = (r, c + offset) if rot == 0 else (c + offset, 10 - r)
                                final.append(coord)
                            return final
                        for offset in PATTERN_IDX_ZEROS[i]:
                            coord = (r, c + offset) if rot == 0 else (c + offset, 10 - r)
                            if coord not in [xs for k in range(coord_idx, 4) for xs in neighbours[k]]:
                                neighbours[coord_idx].append(coord)
                                temp = [j for j in range(coord_idx - 1, -1, -1) if coord in neighbours[j]]
                                for x in temp:
                                    neighbours[x].remove(coord)
                            if turnID == -1 and coord_idx == 3:
                                return win_threat
                        break
                if r > 6:
                    continue
                for i, p in enumerate(zip(PLUS_PATTERN, MINUS_PATTERN)):
                    if 1 in [board[r, c], board[r + 1, c + 1], board[r + 2, c + 2], board[r + 3, c + 3],
                             board[r + 4, c + 4]] and \
                            -1 in [board[r, c], board[r + 1, c + 1], board[r + 2, c + 2], board[r + 3, c + 3],
                                   board[r + 4, c + 4]]:
                        break
                    if i > 30:
                        break
                    if p[0] == str(board[r, c]) + str(board[r + 1, c + 1]) + str(board[r + 2, c + 2]) + str(
                            board[r + 3, c + 3]) + str(board[r + 4, c + 4]):
                        if i == 0:
                            break
                        i = decide_comb(r, c, i, board, diagonal=True)
                        coord_idx = [j for j in range(4) if i in SEVERITY_IDX[j]][0]
                        if turnID == 1 and coord_idx == 3:
                            final = []
                            for offset in PATTERN_IDX_ZEROS[i]:
                                coord = (r + offset, c + offset) if rot == 0 else (c + offset, 10 - (r + offset))
                                final.append(coord)
                            return final
                        for offset in PATTERN_IDX_ZEROS[i]:
                            coord = (r + offset, c + offset) if rot == 0 else (c + offset, 10 - (r + offset))
                            if coord not in [xs for k in range(coord_idx, 4) for xs in neighbours[k]]:
                                neighbours[coord_idx].append(coord)
                                temp = [j for j in range(coord_idx - 1, -1, -1) if coord in neighbours[j]]
                                for x in temp:
                                    neighbours[x].remove(coord)
                            if turnID == 1 and coord_idx == 3:
                                return win_threat
                        break
                    elif p[1] == str(board[r, c]) + str(board[r + 1, c + 1]) + str(board[r + 2, c + 2]) + str(
                            board[r + 3, c + 3]) + str(board[r + 4, c + 4]):
                        if i == 0:
                            break
                        i = decide_comb(r, c, i, board, -1, diagonal=True)
                        coord_idx = [j for j in range(4) if i in SEVERITY_IDX[j]][0]
                        if turnID == -1 and coord_idx == 3:
                            final = []
                            for offset in PATTERN_IDX_ZEROS[i]:
                                coord = (r + offset, c + offset) if rot == 0 else (c + offset, 10 - (r + offset))
                                final.append(coord)
                            return final
                        for offset in PATTERN_IDX_ZEROS[i]:
                            coord = (r + offset, c + offset) if rot == 0 else (c + offset, 10 - (r + offset))
                            if coord not in [xs for k in range(coord_idx, 4) for xs in neighbours[k]]:
                                neighbours[coord_idx].append(coord)
                                temp = [j for j in range(coord_idx - 1, -1, -1) if coord in neighbours[j]]
                                for x in temp:
                                    neighbours[x].remove(coord)
                            if turnID == -1 and coord_idx == 3:
                                return win_threat
                        break
        board = np.rot90(board)
    if win_threat:
        return win_threat
    elif force_threats:
        return force_threats[:5]
    elif non_threats:
        final = non_threats + zero_threat
        return final[:5]
    else:
        return zero_threat[:5]


def evaluation(board, turnID):
    plus_one_r = [[], [], [], []]
    plus_one_c = [[], [], [], []]
    plus_one_d1 = [[], [], [], []]
    plus_one_d2 = [[], [], [], []]
    minus_one_r = [[], [], [], []]
    minus_one_column = [[], [], [], []]
    minus_one_d1 = [[], [], [], []]
    minus_one_d2 = [[], [], [], []]
    plus_one_out = [plus_one_r, plus_one_c, plus_one_d1, plus_one_d2]
    minus_one_out = [minus_one_r, minus_one_column, minus_one_d1, minus_one_d2]
    comb_pattern = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25],
                    [31, 32, 33, 34, 35, 36, 37], [26, 27, 28, 29, 30, 38, 39, 40]]

    for rot in range(2):
        for r in range(11):
            for c in range(7):
                for i, p in enumerate(zip(PLUS_PATTERN, MINUS_PATTERN)):
                    if 1 in [board[r, c], board[r, c + 1], board[r, c + 2], board[r, c + 3], board[r, c + 4]] and \
                            -1 in [board[r, c], board[r, c + 1], board[r, c + 2], board[r, c + 3], board[r, c + 4]]:
                        break
                    if p[0] == str(board[r, c]) + str(board[r, c + 1]) + str(board[r, c + 2]) + str(
                            board[r, c + 3]) + str(board[r, c + 4]):
                        if i == 0:
                            break
                        neighbours = plus_one_r if rot == 0 else plus_one_c
                        qq = []
                        i = decide_comb(r, c, i, board)
                        coord_idx = [j for j in range(4) if i in comb_pattern[j]][0]
                        for offset in PATTERN_IDX[i]:
                            coord = (r, c + offset) if rot == 0 else (c + offset, 10 - r)
                            qq.append(coord)
                        flag = True
                        for ww in qq:
                            if ww in [xss for k in range(coord_idx, 4) for xs in neighbours[k] for xss in xs]:
                                flag = False
                                break
                        if flag:
                            neighbours[coord_idx].append(qq)
                            for ww in qq:
                                temp = [(j, neighbours[j][k]) for j in range(coord_idx - 1, -1, -1) for k in
                                        range(len(neighbours[j])) if ww in neighbours[j][k]]
                                if temp:
                                    neighbours[temp[0][0]].remove(temp[0][1])
                        break
                    if p[1] == str(board[r, c]) + str(board[r, c + 1]) + str(board[r, c + 2]) + str(
                            board[r, c + 3]) + str(board[r, c + 4]):
                        if i == 0:
                            break
                        m_neighbours = minus_one_r if rot == 0 else minus_one_column
                        qq = []
                        i = decide_comb(r, c, i, board, -1)
                        coord_idx = [j for j in range(4) if i in comb_pattern[j]][0]
                        for offset in PATTERN_IDX[i]:
                            coord = (r, c + offset) if rot == 0 else (c + offset, 10 - r)
                            qq.append(coord)
                        flag = True
                        for ww in qq:
                            if ww in [xss for k in range(coord_idx, 4) for xs in m_neighbours[k] for xss in xs]:
                                flag = False
                                break
                        if flag:
                            m_neighbours[coord_idx].append(qq)
                            for ww in qq:
                                temp = [(j, m_neighbours[j][k]) for j in range(coord_idx - 1, -1, -1) for k in
                                        range(len(m_neighbours[j])) if ww in m_neighbours[j][k]]
                                if temp:
                                    m_neighbours[temp[0][0]].remove(temp[0][1])
                        break
                if r > 6:
                    continue

                for i, p in enumerate(zip(PLUS_PATTERN, MINUS_PATTERN)):
                    if 1 in [board[r, c], board[r + 1, c + 1], board[r + 2, c + 2], board[r + 3, c + 3],
                             board[r + 4, c + 4]] and \
                            -1 in [board[r, c], board[r + 1, c + 1], board[r + 2, c + 2], board[r + 3, c + 3],
                                   board[r + 4, c + 4]]:
                        break
                    if p[0] == str(board[r, c]) + str(board[r + 1, c + 1]) + str(board[r + 2, c + 2]) + str(
                            board[r + 3, c + 3]) + str(board[r + 4, c + 4]):
                        if i == 0:
                            break
                        neighbours = plus_one_d1 if rot == 0 else plus_one_d2
                        qq = []
                        i = decide_comb(r, c, i, board, diagonal=True)
                        coord_idx = [j for j in range(4) if i in comb_pattern[j]][0]
                        for offset in PATTERN_IDX[i]:
                            coord = (r + offset, c + offset) if rot == 0 else (c + offset, 10 - (r + offset))
                            qq.append(coord)
                        flag = True
                        for ww in qq:
                            if ww in [xss for k in range(coord_idx, 4) for xs in neighbours[k] for xss in xs]:
                                flag = False
                                break
                        if flag:
                            neighbours[coord_idx].append(qq)
                            for ww in qq:
                                temp = [(j, neighbours[j][k]) for j in range(coord_idx - 1, -1, -1) for k in
                                        range(len(neighbours[j])) if ww in neighbours[j][k]]
                                if temp:
                                    neighbours[temp[0][0]].remove(temp[0][1])
                        break
                    if p[1] == str(board[r, c]) + str(board[r + 1, c + 1]) + str(board[r + 2, c + 2]) + str(
                            board[r + 3, c + 3]) + str(board[r + 4, c + 4]):
                        if i == 0:
                            break
                        m_neighbours = minus_one_d1 if rot == 0 else minus_one_d2
                        qq = []
                        i = decide_comb(r, c, i, board, -1, diagonal=True)
                        coord_idx = [j for j in range(4) if i in comb_pattern[j]][0]
                        for offset in PATTERN_IDX[i]:
                            coord = (r + offset, c + offset) if rot == 0 else (c + offset, 10 - (r + offset))
                            qq.append(coord)
                        flag = True
                        for ww in qq:
                            if ww in [xss for k in range(coord_idx, 4) for xs in m_neighbours[k] for xss in xs]:
                                flag = False
                                break
                        if flag:
                            m_neighbours[coord_idx].append(qq)
                            for ww in qq:
                                temp = [(j, m_neighbours[j][k]) for j in range(coord_idx - 1, -1, -1) for k in
                                        range(len(m_neighbours[j])) if ww in m_neighbours[j][k]]
                                if temp:
                                    m_neighbours[temp[0][0]].remove(temp[0][1])
                        break
        board = np.rot90(board)

    weights = [10, 200, 2000, 10000]
    sum_p = [0, 0, 0, 0]
    sum_m = [0, 0, 0, 0]
    for i in range(4):
        for j in range(4):
            sum_p[j] += len(plus_one_out[i][j])
            sum_m[j] += len(minus_one_out[i][j])
    return sum([(sum_p[i] - sum_m[i]) * weights[i] for i in range(4)]) * turnID


class Player(GomokuAgent):
    def move(self, board):
        if np.all(board == 0):
            return 5, 5
        bestScore = -math.inf
        moves = poss_moves(board, self.ID)
        if not moves:
            while True:
                moveLoc = tuple(np.random.randint(self.BOARD_SIZE, size=2))
                if legalMove(board, moveLoc):
                    return moveLoc
        moveLoc = moves[0]
        for move in moves:
            board[move] = self.ID
            score = self.alphabeta(board, 0, -math.inf, math.inf, False)
            board[move] = 0
            if score > bestScore:
                bestScore = score
                moveLoc = move
        return moveLoc

    # gomoku.py GomokuAgentRand Rambo
    def alphabeta(self, board, depth, alpha, beta, isAiTurn):
        if winningTest(self.ID, board, 5):
            return 99999
        if winningTest(-self.ID, board, 5):
            return -99999
        turnID = self.ID if isAiTurn else -self.ID

        if depth >= 3:
            return evaluation(board, self.ID)

        bestScore = -math.inf if isAiTurn else math.inf
        moves = poss_moves(board, turnID)
        for move in moves:
            board[move] = self.ID if isAiTurn else -self.ID

            score = self.alphabeta(board, depth + 1, alpha, beta, not isAiTurn)
            bestScore = max(score, bestScore) if isAiTurn else min(score, bestScore)
            board[move] = 0
            if isAiTurn:
                alpha = max(alpha, bestScore)
            else:
                beta = min(beta, bestScore)

            if alpha >= beta:
                break
        return bestScore
