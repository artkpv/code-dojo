
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
a = 0
b = 0
for _ in range(n):
    ai, bi = read_int_array()
    if bi < ai:
        a += 1
    elif ai < bi:
        b += 1
print('Mishka' if b < a else ('Chris' if a < b else 'Friendship is magic!^^'))

