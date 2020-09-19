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

n = read_int()
arr = read_int_array()

"""
levels[i] - num of cubes on that lvl

from right to left
 fill columns
"""

arr.sort()
print(' '.join(str(e) for e in arr))

