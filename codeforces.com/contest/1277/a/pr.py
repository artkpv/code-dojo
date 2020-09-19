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


tests = read_int()
for test in range(tests):
    n = read_int()

    nlen = 0
    x = n
    while x > 0:
        x //= 10
        nlen += 1

    ans = 9 * (nlen-1)

    ninc = 0
    for i in range(nlen):
        ninc = (ninc * 10 + 1)
    ans += (n // ninc)

    print(ans)





