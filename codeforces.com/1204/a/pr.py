#!/bin/python3

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
10100 - 20

2^2*0  1
2^2*1  100
2^2*2  10000
2^2*3

n

"""

from math import log, ceil
s = input().strip()
n = len(s)
count = ceil(n/2)
if not any(c for c in s[1:] if c == '1') and n % 2 == 1:
    count -= 1
print(count)

