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

k2, k3, k5, k6 = read_int_array()

num256 = min(k2, k5, k6)
k2 -= num256
num32 = min(k2, k3)
print(256 * num256 + 32 * num32)


