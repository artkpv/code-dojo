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

n = read_int()
a = [[int(e) for e in input().strip().split(' ')] + [id] for id in range(1, n+1)]
a.sort(key=lambda e: (-sum(e[:-1]), e[-1]))
print(1 + list(e[-1] for e in a).index(1))
