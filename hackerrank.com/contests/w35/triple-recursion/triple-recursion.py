#!python3
n, m, k = [int(i) for i in input().strip().split(' ')]
M = [None] * n
for i in range(n):
    M[i] = [None] * n

from sys import stdout
M[0][0] = m
for i in range(n):
    if i > 0:
        M[i][i] = M[i-1][i-1] + k
    for j in range(i+1, n):
        M[i][j] = M[i][j-1] - 1
        M[j][i] = M[j-1][i] - 1
for i in range(n):
    print(' '.join(str(el) for el in M[i]))



