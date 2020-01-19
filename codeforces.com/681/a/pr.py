#!python3
"""
Author: w1ld [dog] inbox [dot] ru
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

n = read_int()
for i in range(n):
    n, b, a = input().strip().split(' ')
    before = int(b)
    after = int(a)
    if before >= 2400 and before < after:
        print("YES")
        exit()
print("NO")

