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
"""
m - odds num

odds num in a seq: r1 + r2 + r3 + .. + r_k = m
r_1..r_k >=1, %2 == 1

if k odd
    m - odd
if k even:
    m - even

"""

for query in range(read_int()):
    n, k = read_int_array()
    a = [(i,e%2) for i, e in enumerate(int(x) for x in input().strip().split(' ')) if e % 2 == 1]
    m = len(a)
    if m < k or m % 2 != k % 2:
        print('NO')
        continue
    print('YES')
    print(' '.join(str(i+1) for i,e in a[:k-1]), str(n))


