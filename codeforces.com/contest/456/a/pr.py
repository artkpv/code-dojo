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

A = []
for _ in range(n):
    A += [read_int_array()]
A.sort()
max_ai = 0
has_cq = False
for c, q in A:
    if q < max_ai:
        has_cq = True
        break
    max_ai = q
print('Happy Alex' if has_cq else 'Poor Alex')


