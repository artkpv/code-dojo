#!python3
"""
w1ld [dog] inbox dot ru
"""

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

for test in range(read_int()):
    s = input().strip()
    l = 0
    r = 0
    u = 0
    d = 0
    for c in s:
        if c == 'L':
            l += 1
        elif c == 'R':
            r += 1
        elif c == 'D':
            d += 1
        elif c == 'U':
            u += 1
    du = min(d,u)
    lr = min(l,r)
    if du == 0:
        lr = min(lr, 1)
    if lr == 0:
        du = min(du, 1)
    print(lr * 2 + du * 2)
    print('L' * lr + 'U' * du + 'R' * lr + 'D' * du)



