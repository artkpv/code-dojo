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

a, b = read_int_array()
aw = 0
d = 0
bw = 0
for i in range(1, 7):
    c = abs(i - a) - abs(i - b)
    if c < 0:
        aw += 1
    elif c > 0:
        bw += 1
    else:
        d += 1

print(aw, d, bw)

