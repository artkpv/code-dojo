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

at = input().strip()
a = int(at)
max_ = -1
max_i = None
mask = 0
MAX = 0xFFFFFFFF
for i in range(len(at)):
    x = ((a >> 1) & (MAX & mask) | (mask & a))
    if x  > max_:
        max_ = x
        max_i = i
    mask <<= 1
    mask |= 1
print(at[:max_i] + at[max_i+1:])



