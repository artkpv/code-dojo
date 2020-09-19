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

n = read_int()
a = read_int_array()

oddnum = 0
coins = 0
k = int(1e9+7)
for e in a:
    coins += min(abs(e - -1), abs(e - 1))
    if e < 0:
        oddnum += 1
    else:
        k = min(k, abs(e - -1))

if oddnum % 2 != 0:
    coins += k
    coins -= abs(k - 2)

print(coins)


