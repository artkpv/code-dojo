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

rows, cols = read_int_array()
field = [input().strip() for _ in range(rows)]

rows_taken = 0
for r in range(rows):
    rows_taken += (1 if 'S' not in field[r] else 0)

count = rows_taken * cols
for c in range(cols):
    count += (rows - rows_taken if 'S' not in (field[r][c] for r in range(rows)) else 0)
print(count)

