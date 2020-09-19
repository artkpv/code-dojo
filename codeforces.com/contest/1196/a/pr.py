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
from math import ceil, floor
"""
a+b+c

a + c1
b + c2

a+c1 == b+c-c1
(b+c-a)/2 = c1

a+c-c2 = b+c2
c2 = (a+c-b)/2

"""

for query in range(read_int()):
    a, b, c = sorted(read_int_array())
    print((a+b+c)//2)



