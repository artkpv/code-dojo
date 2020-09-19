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

n = read_int()
a = [(i,e) for i,e in enumerate(read_int_array())]
a.sort(key=lambda x: x[1], reverse=True)
x = 0
j = 0
for i, e in a:
    x += e*j + 1
    j += 1
print(x)
print(' '.join(str(i+1) for i, e in a))

