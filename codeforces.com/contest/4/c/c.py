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

n = read_int()
d = {}
while n > 0:
    s = input().strip()
    d[s] = d.get(s, 0) + 1
    if d[s] == 1:
        print('OK')
    else:
        print(s + str(d[s] - 1))
    n -= 1



