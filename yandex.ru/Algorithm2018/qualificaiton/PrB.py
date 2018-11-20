#!python3
"""
https://contest.yandex.ru/algorithm2018/contest/7491/problems/B/

4
1  6  14  7
5  4  1  13
13 16 12 10
8  3  6  16
11 2  7  10
15 9  14 12
4  3  9  2
5  8  15 11

> 5 4 1 13 | 8 3 6 16 | 15 9 14 12 | 11 2 7 10
"""

import sys, itertools

n = int(input().strip())
A = [None] * 2*n
ASets = [None] * 2*n  # to quicker check
for i in range(2*n):  ASets[i] = set()
for i in range(2*n):
    A[i] = [int(j) for j in input().strip().split(" ")]
    ASets[i] = set(A[i])

# 1) assume A[0] - is a row. 2) find all its columns
cols = [None] * n
cols_found = 0
x = 0
for y in range(1, 2*n):
    intersection = ASets[x].intersection(ASets[y])
    if intersection:
        assert len(intersection) == 1
        i = A[x].index(intersection.pop())
        cols[i] = y
        cols_found += 1
    if cols_found == n:
        break

# print matrix
for i in range(n):
    for j in range(n):
        sys.stdout.write(str(A[cols[j]][i]) + ' ')

