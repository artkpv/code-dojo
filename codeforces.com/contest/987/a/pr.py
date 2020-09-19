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
s = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality',  'yellow': 'Mind'}
for i in range(n):
    k = input().strip()
    if k in s:
        del s[k]
print(len(s))
for k in s:
    print(s[k])


