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

n, k, d = read_int_array()
MOD = int(1e9+7)

def c(n, k, d):
    if n == 0:
        return 1
    num = 0
    for i in range(1, k+1):
        if n - i < 0:
            break
        num += c(n - i, k, d)
"""
Следующее. Как учесть d? Если путь 2 2 2 2 2, d=3, k = 4, как отбросить этот путь?
"""


print(c(n, k, d))

