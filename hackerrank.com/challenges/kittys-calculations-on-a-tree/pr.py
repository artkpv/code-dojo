#!python3
"""
Idea 1
1) calc distance: n * (n-1)
2) calc sum: n*(n-1)
Time: O(n^2)
Space: tree + dissto = O(2E + V*V) = O(n^2) ~= 10^9 objects, >1 GB ?


Idea 2
TODO
How to quickly compute distance?
For any two v, u nodes their distance will be:
    distance(v,u) = level(v) - parent(v,u) + level(u) - parent(v,u)
Now how to traverse tree for this?


"""

from itertools import combinations
from collections import deque

MODULO = 10**9+7


class SP(object):  # shortest path
    def __init__(self, source, tree):
        distto = [None] * tree.size
        marked = [False] * tree.size
        queue = deque()
        queue += [source]
        distto[source] = 0
        while queue:
            v = queue.popleft()
            marked[v] = True
            for u in tree.adj[v]:
                if not marked[u]:
                    queue.append(u)
                    distto[u] = distto[v] + 1
        self.distto = distto


class Tree(object):
    def __init__(self, size):
        self.adj = [[] for _ in range(size)]
        self._dist = {}
        self.size = size

    def add(self, a, b):
        self.adj[a-1] += [b-1]
        self.adj[b-1] += [a-1]

    def calc_dist(self):
        for v in range(self.size):
            sp = SP(v, tree)
            for u, distance in enumerate(sp.distto):
                a = v if v < u else u
                b = u if v < u else v
                if (a, b) not in self._dist:
                    self._dist[(a, b)] = distance

    def dist(self, v, u):
        a = v if v < u else u
        b = u if v < u else v
        return self._dist[(a-1, b-1)]


def calc(set_, tree):
    sum_ = 0
    for c in combinations(set_, 2):
        sum_ += (c[0] * c[1] * tree.dist(c[0], c[1])) % MODULO
        sum_ = (sum_ % MODULO)
    return sum_


verticesnum, setsnum = [int(i) for i in input('').strip().split(' ')]
tree = Tree(verticesnum)
for edge in range(verticesnum-1):
    a, b = [int(i) for i in input('').strip().split(' ')]
    tree.add(a, b)
tree.calc_dist()

for _ in range(setsnum):
    size = int(input('').strip())
    set_ = [int(i) for i in input('').strip().split(' ')]
    print(calc(set_, tree))
