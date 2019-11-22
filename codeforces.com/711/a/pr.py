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
rows = []
sitted = False
for i in range(n):
    row = input().strip()
    if not sitted and 'OO' in row:
        rows += [row.replace('OO', '++', 1)]
        sitted = True
    else:
        rows += [row]

if sitted:
    print("YES")
    print('\n'.join(rows))
else:
    print("NO")

