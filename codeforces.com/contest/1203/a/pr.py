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

for _ in range(read_int()):
    n = read_int()
    p = read_int_array()
    if n == 1:
        print('YES')
        continue
    step = p[1] - p[0]
    if abs(step) != 1 and n > 2:
        step = p[2] - p[1]
    if abs(step) != 1:
        print('NO')
        continue
    breaks = 0
    for i in range(n):
        if p[i%n] + step != p[(i+1)%n]:
            breaks += 1
    print('YES' if breaks == 1 else 'NO')






