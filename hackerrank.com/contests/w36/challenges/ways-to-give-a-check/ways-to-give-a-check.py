#python3

import sys

def is_check(board, kp):  # kp - king position
    size = 8
    row = kp[0]
    col = kp[1]

    l = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for shift in l:
        y = row
        x = col
        while True:
            y += shift[0]
            x += shift[1]
            if not (0 <= y < size) or not (0 <= x < size):
                break
            if board[y][x] in 'RQ':
                return True
            if board[y][x] != '#':
                break

    l = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for shift in l:
        y = row
        x = col
        while True:
            y += shift[0]
            x += shift[1]
            if not (0 <= y < size) or not (0 <= x < size):
                break
            if board[y][x] in 'QB':
                return True
            if board[y][x] != '#':
                break

    l = [(2,1),(1,2),(-2,1),(1,-2),(2,-1),(-1,2),(-2,-1),(-1,-2)]
    y = row
    x = col
    for shift in l:
        y = row + shift[0]
        x = col + shift[1]
        if not (0 <= y < size) or not (0 <= x < size):
            continue
        if board[y][x] == 'N':
            return True

    return False

def waysToGiveACheck(board):
    size = 8
    pawn_row = 1
    checks = 0

    king_position = None
    for i in range(0, size):
        for j in range(0, size):
            if board[i][j] == 'k':
                king_position = (i, j)
                break

    for c in range(0, size):
        if board[pawn_row][c] != 'P':
            continue
        can_promote = board[0][c] == '#'
        if can_promote:
            # move and check:
            board[pawn_row][c] = '#'
            board[0][c] = 'R'
            isrook = is_check(board, king_position)
            if isrook:
                checks += 1
            board[0][c] = 'B'
            isbishop = is_check(board, king_position)
            if isbishop:
                checks += 1
            if isrook or isbishop:
                checks += 1
            board[0][c] = 'N'
            if is_check(board, king_position):
                checks += 1

            # move back:
            board[0][c] = '#'
            board[pawn_row][c] = 'P'
    return checks

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        board = []
        for board_i in range(8):
           board.append(list(input().strip()))
        result = waysToGiveACheck(board)
        print(result)
