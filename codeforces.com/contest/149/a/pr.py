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

k = read_int()
months = read_int_array()
months.sort(reverse=True)
h = 0
i = 0
while h < k and i < len(months):
    h += months[i]
    i += 1

print(i if h >= k else -1)

