#!python3
"""
Author: w1ld [at] inbox [dot] ru
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

q, x = read_int_array()
counter = Counter()
while q > 0:
    q -= 1
    y = read_int()
    counter[y % x] += 1
    key, keycount = coutner.most_common()[-1]
    if key > 0:
        print(0)
    else:


