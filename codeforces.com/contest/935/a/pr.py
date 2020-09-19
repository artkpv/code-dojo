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
for i in range(1, n//2 + 1):
    if (n - i) % i == 0:
        count += 1

print(count)

