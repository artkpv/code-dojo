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

n = read_int()
P = [int(input().strip()) for _ in range(n)]
H = [0] * n
max_h = 0
for i in range(n):
    v = P[i]
    h = 1
    while v != -1 and H[v-1] < h:
        H[v-1] = h
        v = P[v-1]
        h += 1
    h -= 1
    if h > max_h:
        max_h = h
print(max_h+1)

"""
-1 1 2 1 -1
2 1 0 0 0
1

0  -1 1
1  1 1  -1 2
2  2 1  1 2  -1 3
3  1 1
4  -1 1
max_h = 2



"""

