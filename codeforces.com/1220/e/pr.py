#!python3

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
import unittest
from heapq import heappush, heappop


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

vn, en = read_int_array()
wl = read_int_array()
al = [[] for _ in range(vn)]

for _ in range(en):
    v, w = read_int_array()
    al[v-1] += [w-1]
    al[w-1] += [v-1]

s = read_int()-1

def adj(v):
    return al[v]
def weight(w):
    return wl[w]

def LazyPrimsMST():
    q = []  # min queue
    marked = set()
    def visit(v):
        marked.add(v)
        for w in adj(v):
            if w not in marked:
                heappush(q, (-weight(w), v, w))
        return weight(v)

    count = visit(s)
    while q:
        weightvw, v, w = heappop(q)
        if w in marked and v in marked:
            continue
        print(v+1, w+1, -weightvw)
        if w not in marked:
            count += visit(w)
        if v not in marked:
            count += visit(v)
    return count

print(LazyPrimsMST())
