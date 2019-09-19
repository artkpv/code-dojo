#!python3
"""
11
 22
  33
   66
    11
     22
      33
       44
        55
12
23
34
"""

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
adj = [[] for _ in range(n)]
edges = set()
for _ in range(k):
    x, y = read_int_array()
    x, y = (y, x) if y < x else (x, y)
    if (x,y) not in edges:
        edges.add((x, y))
        adj[x-1] += [y-1]
        adj[y-1] += [x-1]

marked = set()

def bfs(s):
    queue = [s]
    count = 0
    while queue:
        v = queue.pop()
        if v in marked:
            continue
        count += 1
        marked.add(v)
        for w in adj[v]:
            if w not in marked:
                queue += [w]
    return count

count = 0
for v in range(n):
    if v not in marked:
        m = bfs(v)
        count += m - 1

print(k - count)

"""
0 1
3 2
0 3
2 3
"""

