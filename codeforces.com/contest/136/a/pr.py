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
"""

"""

n = read_int()
a = read_int_array()

b = [None] * n
for i, e in enumerate(a):
    b[e-1] = i+1
print(' '.join(str(i) for i in b))

"""
2 3 4 1

4 1 2 3


2 1 4 3 
2 1 

2 3 1 ...
3 1 2 .. 

"""
