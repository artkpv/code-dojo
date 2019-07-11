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
m = read_int()
a = []
for _ in range(n):
    a += [read_int()]
a.sort()
count = 0
while m > 0:
    m -= a.pop()
    count += 1
print(count)



