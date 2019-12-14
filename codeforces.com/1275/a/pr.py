#!python3
"""
w1ld [dog] inbox dot ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

peoplenum = read_int()
aM = [[False] * peoplenum for _ in range(peoplenum)]
for i in range(1, peoplenum+1):
    row = read_int_array()
    for j in row[1:]:
        aM[i-1][j-1] = True

ans = []
for i in range(peoplenum):
    for j in range(i+1, peoplenum):
        if aM[j][i] != aM[i][j]:
            ans.append((i+1, j+1) if not aM[i][j] else (j+1, i+1))

print(len(ans))
for a, b in ans:
    print(a, b)


