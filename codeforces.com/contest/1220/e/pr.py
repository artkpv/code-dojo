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

verticesnum, edgesnum = read_int_array()
vertex_weights = read_int_array()
def vweight(v):
    return vertex_weights[v]
graph_adj_l = [[] for _ in range(verticesnum)]
for _ in range(edgesnum):
    v, w = read_int_array()
    graph_adj_l[v-1] += [w-1]
    graph_adj_l[w-1] += [v-1]

def graph_adj(v):
    return graph_adj_l[v]
source_vertex = read_int()-1

class UF(object):
    def __init__(self, verticesnum):
        self.p = list(verticesnum)
        self.size = [1] * verticesnum
        self.score = [vweight(v) for v in range(verticesnum)]

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(p[v])
        return self.p[v]

    def union(self, v, w):
        pv = self.find(v)
        pw = self.find(w)

        if self.size[pv] > self.size[pw]:
            self.p[pw] = pv
            self.size[pw] += self.size[pv]
            self.score[pw] += self.score[pv]
        else:
            self.p[pv] = pw
            self.size[pv] += self.size[pw]
            self.score[pv] += self.score[pw]

class Solution(object):
    def get_ccs(self):
        """ Get connected components and their scores. """
        # Reversed graph from DFS.
        rg = [[] for _ in range(verticesnum)]
        # Reversed post order of DFS.
        rpo = []
        marked = set()
        def dfs(v, p):
            marked.add(v)
            for w in graph_adj(v):
                if w != p:
                    rg[w] += [v]
                if w in marked:
                    continue
                dfs(w, v)
            rpo += [v]

        dfs(source_vertex, None)
        rpo.reverse()

        uf = UF(verticesnum)
        marked.clear()
        def visit(v):  # v - vertex
            """ DFS to get CCs. """
            marked.add(v)
            for w in rg[v]:
                if w in marked:
                    continue
                uf.union(v, w)
                visit(w)

        for v in rpo:
            if v not in marked:
                visit(v)
        return uf

    def get_score(self, uf):
        # TODO. How to get score now?
        # 1 Idea. DFS? With DP on score? But that fails as we visit a leave close to
        # source first and then CCs hence score for the leave is less.
        marked = set()
        vscore = [0] * verticesnum
        max_score = -float('inf')
        q = deque()
        q += [source_vertex]
        while q:
            v = q.popleft()
            if v in marked:
                continue
            marked.add(v)
            for w in graph_adj(v):

        return score

    def solve(self):
        uf = self.get_ccs()
        return self.get_score(uf)


print(Solution().solve())
