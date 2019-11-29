#!python3
"""
w1ld [dog] inbox dot ru


1 100 98
1 100 99


1 2
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
    r, b, k = read_int_array()
    r, b = (r, b) if r < b else (b, r)
    print('OBEY' if r == b or (b-2)//r+1 < k else 'REBEL')

