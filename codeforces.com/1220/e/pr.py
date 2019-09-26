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
vertex_weights = read_int_array()
def vweight(v):
    return vertex_weights[v]
graph_adj_l = [[] for _ in range(vn)]
for _ in range(en):
    v, w = read_int_array()
    graph_adj_l[v-1] += [w-1]
    graph_adj_l[w-1] += [v-1]

def graph_adj(v):
    return graph_adj_l[v]
source_vertex = read_int()-1

class Solution(object):
    def build_dg(self):
        """ Build directed graph. """
        # Reversed graph from DFS.
        self.rg = [[] for _ in range(vn)]
        # Reversed post order of DFS.
        self.rpo = []
        marked = set()
        def dfs(v, p):
            marked.add(v)
            for w in graph_adj(v):
                if w != p:
                    self.rg[w] += [v]
                if w in marked:
                    continue
                dfs(w, v)
            self.rpo += [v]

        dfs(source_vertex, None)
        self.rpo.reverse()

    def get_score(self):
        vtocc = [None] * vn  # # CC to vertices.
        # Merge CCs into one vertex but 1 size CCs.
        marked = set()
        cweight = []  # Weights of CCs.
        def visit(v, cid):  # Vertex, component id
            marked.add(v)
            vtocc[v] = cid
            weight = vweight(v)
            for w in self.rg[v]:
                if w in marked:
                    if vtocc[w] and vtocc[w] != cid:
                        weight += cweight[vtocc[w]]
                    continue
                wweight = visit(w, cid)
                weight += wweight
            return weight

        cid = 0  # component id
        score = 0
        for v in self.rpo:
            if v not in marked:
                cweight.append(visit(v, cid))
                score = max(score, cweight[-1])
                cid += 1
        print('cweight', cweight)
        print('vtocc', vtocc)
        return score

    def solve(self):
        self.build_dg()
        return self.get_score()


print(Solution().solve())
