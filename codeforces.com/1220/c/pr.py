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

s = input().strip()
print('Mike')
min_ = s[0]
for i in range(1, len(s)):
    if min_ < s[i]:
        print('Ann')
    else:
        print('Mike')
    if s[i] < min_:
        min_ = s[i]


