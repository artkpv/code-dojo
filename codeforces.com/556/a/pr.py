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
1100
01010
11101111

0000001
0001000

I 1
Aux arr with deleted

I 2

"""

n = read_int()
a = input().strip()

zeroes = 0
ones = 0
for c in a:
    if c == '0':
        zeroes += 1
    else:
        ones += 1
print(n - min(zeroes, ones)*2)

