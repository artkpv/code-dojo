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

for test in range(read_int()):
    a, b, c = read_int_array()
    a, b, c = sorted([a,b,c])
    if a == b == c:
        print(0)
    elif a == b or b == c:
        print(2*(min(abs(c-1 - a - 1), c - a - 1)))
    else:
        print(b - (a+1) + (c-1) - (a+1) + (c-1) - b)



