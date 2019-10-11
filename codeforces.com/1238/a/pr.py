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

t = read_int()
for test in range(t):
    x, y = read_int_array()
    print('YES' if x - y > 1 else 'NO')

