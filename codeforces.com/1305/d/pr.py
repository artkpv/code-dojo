#!python3
"""
Author: w1ld [at] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
# import unittest
from sys import stdout


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

V = read_int()
adj = [[] for _ in range(V+1)]
leaves = set(list(range(1, V+1)))
for _ in range(V-1):
    v, w = read_int_array()
    adj[v].append(w)
    adj[w].append(v)
    if len(adj[v]) > 1 and v in leaves:
        leaves.remove(v)
    if len(adj[w]) > 1 and w in leaves:
        leaves.remove(w)

leaves = list(leaves)
i = 0

root = None
p = None
for query in range(V//2):
    print("? {} {}".format(leaves[i], leaves[i+1]))
    stdout.flush()
    p = int(input().strip())
    if p == leaves[i]:
        root = p
    elif p == leaves[i+1]:
        root = p
    elif i + 3 < len(leaves):
        i += 2
    elif i + 2 < len(leaves):
        i += 1

print("! {}".format(root or p))

