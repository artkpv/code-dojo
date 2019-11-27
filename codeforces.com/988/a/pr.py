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

n, k = read_int_array()
a = read_int_array()
d = dict()

for i, e in enumerate(a):
    l = d.get(e, [])
    l.append(i+1)
    d[e] = l

if len(d) < k:
    print("NO")
else:
    print("YES")
    print(' '.join([str(d[i][0]) for i in d.keys()][:k]))


