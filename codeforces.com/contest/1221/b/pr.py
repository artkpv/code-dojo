#!python3

# from collections import deque, Counter
# import array
# from itertools import combinations, permutations
# from math import sqrt

# import sys

# sys.setrecursionlimit(99999)
def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

n = read_int()
B = [['.'] * n for _ in range(n)]
B[0][0] = 'W'
for i in range(1, n):
    B[0][i] = 'W' if B[0][i-1] == 'B' else 'B'

for i in range(1, n):
    for j in range(n):
        B[i][j] = 'W' if B[i-1][j] == 'B' else 'B'


# def fill(r, c):
    # p = 'W' if B[r][c] == 'B' else 'B'
    # for r2, c2 in (
        # (-1, -2), (-2, -1), (-2, 1), (-1, 2),
        # (1, 2), (2, 1), (2, -1), (1, -2)
        # ):
        # r2 = r + r2
        # c2 = c + c2
        # if not (0 <= r2 < n and 0<= c2 < n) or B[r2][c2] != '.':
            # continue
        # B[r2][c2] = p
        # fill(r2, c2)

# fill(0, 0)
# for r in range(n):
    # for c in range(n):
        # if B[r][c] == '.':
            # B[r][c] = 'B'
print('\n'.join(''.join(row) for row in B))


