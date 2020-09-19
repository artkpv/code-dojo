#!/bin/python3
"""

w1ld [dog] inbox dot ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

n = read_int()
cols = read_int_array()
i = 0
blacks = 0
while i < n:
    if i % 2 == 0:
        blacks += cols[i] // 2
    else:
        blacks += cols[i] - cols[i] // 2
    i += 1

print(min(blacks, sum(cols) - blacks))

