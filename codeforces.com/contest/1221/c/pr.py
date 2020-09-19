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

for _ in range(read_int()):
    c, m, x = read_int_array()
    """
    1 1 ?
    y = min(c, m)
    z = x + c+m - y
    min(y, z, (c+m+x)//3)
    """
    y = min(c, m)
    print(min(y, (c+m+x)//3))

