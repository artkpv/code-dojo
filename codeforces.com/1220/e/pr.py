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
        cctov = []  # # CC to vertices.
        ccsize = []  # Sizes of CCs.
        # Merge CCs into one vertex but 1 size CCs.
        marked = set()
        count = 0
        def visit(v, c):  # Vertex, Count
            marked.add(v)
            cctov[c] += [v]
            ccsize[c] += 1
            for w in self.rg[v]:
                if w in marked:
                    continue
                visit(w, c)

        score = 0
        max_end_w = 0
        i = 0
        while i < len(self.rpo):
            v = self.rpo[i]
            if v not in marked:
                cctov.append([])
                ccsize.append(0)
                visit(v, count)
                if ccsize[-1] > 1 or i == 0:
                    for w in cctov[-1]:
                        score += vweight(w)
                else:
                    max_end_w = max(max_end_w, vweight(v))
                # print('cctov', cctov)
                # print('ccsize', ccsize)
                # print('score, max_end_w', score, max_end_w)
                count += 1
            i += 1
        return score + max_end_w

    def solve(self):
        self.build_dg()
        return self.get_score()


print(Solution().solve())
