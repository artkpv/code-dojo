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
count = 0
while True:
    n += 1
    count += 1
    if '8' in str(n):
        break
print(count)



