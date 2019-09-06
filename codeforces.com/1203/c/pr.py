#!python3

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, gcd, floor
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################


n = read_int()
a = read_int_array()

d = a[0]
for e in a[1:]:
    d = gcd(d, e)

factors = 0
x = 2
while d > 1:
    q, r = divmod(d, x)
    if r == 0:
        factors += 1
        d = q
    else:
        x += 1
print(2**factors)

"""
6
d x f
6 2 1
3 3 2
1 3 2


"""

