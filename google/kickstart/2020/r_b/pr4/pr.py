#!python3

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

tests = read_int()
MAX = int(1e5)
prb = [[None] * MAX for _ in range(MAX)]
for test in range(tests):
    w, h, l, u, r, d = read_int_array()

    for i in range(h):
        for j in range(w):
            if u - 1 <= i <= d - 1 and l - 1 <= j <= r -1:
                prb[i][j] = .0
            elif i == h -1 or j == w-1:
                prb[i][j] = 1.0
            else:
                prb[i][j] = None
    if r == w:
        for i in range(u-2, -1, -1):
            prb[i][w-1] = 0.0
    if d == h:
        for i in range(l-2, -1, -1):
            prb[h-1][i] = .0
    for i in range(h-2, -1, -1):
        for j in range(w-2, -1, -1):
            if u - 1 <= i <= d - 1 and l - 1 <= j <= r -1:
                continue
            prb[i][j] = .5*prb[i+1][j] + .5*prb[i][j+1]
    print("Case #{}: {:.5}".format(test + 1, prb[0][0]))

