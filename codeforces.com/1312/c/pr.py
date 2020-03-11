#!python3
"""
Author: w1ld [at] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

tests = read_int()
for t in range(tests):
    n, k = read_int_array()
    arr = read_int_array()
    used = [False] * 64
    can = True
    for ai in arr:
        if not can:
            break
        if ai == 0:
            continue
        power = 0
        while can and ai > 0:
            q, r = divmod(ai, k)
            if r > 1:
                can = False
            if r == 1:
                if used[power]:
                    can = False
                used[power] = True
            ai = q
            power += 1

    print("YES" if can else "NO")

