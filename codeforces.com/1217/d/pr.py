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

vn, en = read_int_array()
al = [[] for _ in range(vn)]  # adjacency list
def adj(v):
    return al[v]
itoe = [None for _ in range(en)]  # index to edge
for eid in range(en):  # eid - edge id
    v, w = read_int_array()
    v -= 1
    w -= 1
    al[v] += [w]
    itoe[eid] = (v, w)

marked = set()
stack = set()
etoc = {}  # edge to color
def dfs(v):  # vertex
    if v in marked:
        return
    marked.add(v)
    stack.add(v)
    hasbackedge = False
    for w in adj(v):
        if w in stack:  # back edge
            hasbackedge = True
            etoc[(v, w)] = 2
            continue
        if w in marked:
            continue
        if dfs(w):
            hasbackedge = True
    stack.remove(v)
    return hasbackedge

hasbackedge = False
for v in range(vn):
    if v not in marked:
        if dfs(v):
            hasbackedge = True

print(2 if hasbackedge else 1)
for ei in range(en):
    v, w = itoe[ei]
    c = etoc.get((v,w), 1)
    print(c, end=' ')





