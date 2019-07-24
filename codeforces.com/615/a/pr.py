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

n, m = read_int_array()
turned = set()
for i in range(n):
    xi, *yij = read_int_array()
    for b in yij:
        turned.add(b)
print('YES' if len(turned) == m else 'NO')


