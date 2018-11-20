#!python3
def solve(board):
    color = board[0][0]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] != color:
                return False
            color = 1 if color == 0 else 0
        if n % 2 == 0:
            color = 1 if color == 0 else 0
    return True


tests = int(input().strip())
for test in range(tests):
    n = int(input().strip())
    board = []
    for i in range(n):
        board += [[int(c) for c in input().strip().split()]]
    print('Yes' if solve(board) else 'No')