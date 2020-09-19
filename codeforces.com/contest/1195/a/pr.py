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
"""
n k

m - odds
"""
n, k = read_int_array()
types = []
for _ in range(n):
    types += [read_int()]

odds = Counter(types)
odds_num = sum(1 for t, num in odds.items() if num % 2 == 1)

print(n - (odds_num//2))
