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
os = [int(c) for c in input().strip()]  # original state
lc = [int(c) for c in input().strip()]  # lock combination

moves = 0
for i, d in enumerate(os):
    moves += min(abs(d - lc[i]), abs(d + 10 - lc[i]), abs(lc[i] + 10 - d))

print(moves)
"""
82195
64723

0 2,12,8  2
1 2,8,12  2
2 6,4,16  4
3 7,17,3  3
4 2
--
13
"""

