#!python3

from collections import deque, Counter
from itertools import combinations, permutations
from math import sqrt
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

_ = read_int()
a = read_int_array()
_ = read_int()
b = read_int_array()
a, b = (a, b) if len(a) < len(b) else (b, a)
n = len(a)
m = len(b)
a.sort()
b.sort()
i = 0
j = 0
pairs = 0
while i < n and j < m:
    if abs(a[i] - b[j]) <= 1:
        pairs += 1
        i += 1
        j += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(pairs)


