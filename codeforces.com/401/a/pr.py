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

n, x = read_int_array()
arr = read_int_array()
y = sum(arr)
print(abs(y) // x + (1 if y % x > 0 else 0))

