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
adj = [[] for _ in range(k)]
edges = set()
vertices = set()
for _ in range(k):
    x, y = read_int_array()
    x, y = (y, x) if y < x else (x, y)
    if (x,y) not in edges:
        vertices.add(x)
        edges.add((x,y))
        adj[x-1] += [y-1]
        adj[y-1] += [x-1]

marked = set()
count = 0
def getpaths(v):
    marked.add(v)
    visitednum = 1
    for w in adj[v]:
        if w in marked:
            continue
        other = getpaths(w)
        if visitednum == 1:
            visitednum += 1 + other
        elif other > 1:
            visitednum += other
    return visitednum


while vertices:
    v = vertices.pop()
    count = getpaths(v)
    # if len(adj[v]) > 1:
        # count += 1
print(n - count)


