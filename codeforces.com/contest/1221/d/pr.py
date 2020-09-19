#!python3

"""
2 4
2 1
3 5

2 0  3 4  4 8
2 4  3 1  4 2
3 2  4 6  5 11

1 6
1 5
1 4
1 3
1 2
1 1

1 0  2 6  3 12
1 6  2 5  3 10
1 5

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

CASES = 3
import pdb

INF = float('inf')
MAXANS = 10**18

def min_c(oc, h):
    return min(oc[i*2 + 1] for i in range(CASES) if oc[i*2] != h)

for _ in range(read_int()):
    n = read_int()
    A = [read_int_array() for __ in range(n)]
    if n == 1:
        print(0)
        continue

    oc = []
    for i in range(CASES):
        oc += [A[0][0] + i, A[0][1] * i]
    nextoc = [None] * (CASES*2)
    for i in range(1, n):
        a = A[i]
        for j in range(CASES):
            nextoc[j*2] = a[0] + j
            nextoc[j*2 + 1] = min_c(oc, a[0] + j) + j*a[1]
            if nextoc[j*2 + 1] > MAXANS:
                nextoc[j*2 + 1] = INF
        oc, nextoc = nextoc, oc
        # print(oc)
        # print(nextoc)

    ans = min(oc[i*2 + 1] for i in range(CASES))
    print(ans)

