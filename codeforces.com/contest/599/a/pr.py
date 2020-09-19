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

a, b, c = read_int_array()

x = 0
if a < b:
    x += a
    x += min(c, a+b)
    x += min(b, c+a)
else:
    x += b
    x += min(c, a+b)
    x += min(a, c+b)
print(x)




