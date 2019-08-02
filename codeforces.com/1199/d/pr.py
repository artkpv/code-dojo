#!python3

from collections import deque, Counter
from heapq import heappush, heappop
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
a = read_int_array()
queries = read_int()
max_x = 0
ops = []
for query in range(queries):
    o = [int(i) for i in input().strip().split(' ')]
    if o[0] == 1:
        inx, val = o[1], o[2]
        heappush(ops, (val, inx))
    else:
        x = o[1]
        if x > max_x:
            max_x = x
            while ops and ops[0][0] < max_x:
                heappop(ops)
for i in range(n):
    if a[i] < max_x:
        a[i] = max_x
for val, inx in ops:
    a[inx-1] = val
print(' '.join(str(e) for e in a))






