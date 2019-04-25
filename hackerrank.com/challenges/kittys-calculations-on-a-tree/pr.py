#!python3
"""
Next: see TODO

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


Idea 3
How to optimize sum of combinations multiplications ?
Precompute all factors for all till 2*10^5. For each two numbers, get
common divisors. ??? Extract most common de
TODO


Idea 4
Two vertices, v and u on a tree. If on the same branch: level(b) - level(a).
If on other branches: level(b) - 2 * level(parent(a,b)) + level(a).
TODO
Make balanced tree?

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


class TreeDistance(object):
    """
    TODO
    Given n - root
    Calc distance for any v, u on tree.
    Idea: traverse tree, calc distance to previously visited vertices
    from current:
        distance(u,v) = distto(u, root) + level(v) - disto(parent(u,v), root)
    where parent of u, v found from the upper stack till root.
    Time: ~n*(n-1)/2, all pairs
    Space: distto only, ~V
    """
    def __init__(self, tree):
        self.tree = tree
        size = tree.size
        self.root = self.tree.size // 2  # root is unknown, so take any
        self.distance = {}
        self.order = []
        self.inorder(self.root, set())

    def inorder(node, parents):
        pass
        # TODO

    def get_distance(self, v, u):
        a = v if v < u else u
        b = u if v < u else v
        return self.distance[(a-1, b-1)]


class Tree(object):
    def __init__(self, size):
        self.adj = [[] for _ in range(size)]
        self.distance = {}
        self.size = size

    def add(self, a, b):
        self.adj[a-1] += [b-1]
        self.adj[b-1] += [a-1]

    def calc_dist(self):
        # td = TreeDistance(self)
        # self.distance = td.distance

        for v in range(self.size):
            sp = SP(v, tree)
            for u, distance in enumerate(sp.distto):
                a = v if v < u else u
                b = u if v < u else v
                if (a, b) not in self.distance:
                    self.distance[(a, b)] = distance


def calc(set_, tree):
    sum_ = 0
    for c in combinations(set_, 2):
        sum_ += (c[0] * c[1] * tree.get_distance(c[0], c[1])) % MODULO
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
