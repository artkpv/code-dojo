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
count = 0
for _ in range(n):
    a, b, c = read_int_array()
    if a+b+c >= 2:
        count += 1
print(count)

