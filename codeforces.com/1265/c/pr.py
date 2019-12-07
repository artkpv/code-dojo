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
    n = read_int()
    a = read_int_array()
    # a[0:g] - with golden
    # a[g:s] - with silver
    # a[s:b] - with bronze
    g = 1
    while g < n // 2 and a[g-1] == a[g]:
        g += 1
    s = g + 1 if g + 1 < n // 2 else n
    while s < n // 2 and (a[s-1] == a[s] or g >= (s - g)):
        s += 1
    if s >= n // 2:
        b = n
    else:
        b = n // 2
        while s < b and a[b] == a[b-1]:
            b -= 1

    if s == n or b == n or (b - s) <= g or (s - g) <= g:
        print(0, 0, 0)
    else:
        print(g, s - g, b - s)

"""
32
64 64 63 58 58 58 58 58 37 37 37 37 34 34 28 28 28 28 28 28 24 24 19 17 17 17 17 16 16 16 16 11
      g                 s                 b     16

g 1 2
s 3 4 5 6 7 8
b 16 15 14

"""
