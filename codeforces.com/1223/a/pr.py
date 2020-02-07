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

tests = read_int()
for test in range(tests):
    n = read_int()
    if n == 2:
        print(2);
    else:
        print(1 if n % 2 == 1 else 0)

