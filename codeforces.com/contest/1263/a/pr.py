#!python3
"""
w1ld [dog] inbox dot ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt,ceil, floor
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

for test in range(read_int()):
    a,b,c = list(sorted(read_int_array()))

    days = a

    d = min(a, ceil((c - b + a) / 2))
    c -= d
    b -= (a - d)
    days += min(c, b)
    print(days)

