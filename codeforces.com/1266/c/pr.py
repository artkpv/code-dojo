#!python3
"""
w1ld [dog] inbox dot ru

b1 b2 b3 b4

2 9
4 12
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, gcd
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

r, c = read_int_array()

if r == c == 1:
    print(0)
    exit()

if r == 1:
    print(' '.join(str(e) for e in range(2, c+2)))
    exit()

if c == 1:
    print('\n'.join(str(e) for e in range(2, r+2)))
    exit()

print('\n'.join(' '.join(str(i * j) for j in range(r+1, r+c+1)) for i in range(1, r + 1)))
