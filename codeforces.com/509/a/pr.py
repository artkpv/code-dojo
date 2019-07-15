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

a = [1] * n
b = [1] * n
for i in range(1, n):
    for j in range(1, n):
        b[j] = b[j-1] + a[j]
    a, b = b, a
print(a[-1])


