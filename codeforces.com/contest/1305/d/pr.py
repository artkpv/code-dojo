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
size = V
def remove(u):
    p = adj[u][0]
    adj[u].clear()
    adj[p].remove(u)
    if len(adj[p]) == 1:
        leaves.append(p)

i = 0
root = None
for query in range(V//2):
    if root:
        print("? {} {}".format(1, 2))
        stdout.flush()
        p = int(input().strip())
        continue
    assert i + 1 < len(leaves)
    print("? {} {}".format(leaves[i], leaves[i+1]))
    stdout.flush()
    p = int(input().strip())
    if p == leaves[i] or p == leaves[i+1]:
        root = p
    else:
        remove(leaves[i])
        remove(leaves[i+1])
        size -= 2
        i += 2
        if size == 1:
            root = leaves[i]

print("! {}".format(root or p))

