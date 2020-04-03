#!python

"""
Prim's algo for MST using priority queue without decreasing a key (storing duplicates for edges).

Time: O(E*log(E))
Space: O(V+E)
"""

from heapq import heappop as hpop, heappush as hpush

INF = float('inf')


class PrimMST(object):
    def __init__(self, graph):
        s = 1
        q = [(0, s)]
        edgeto = [None] * (graph.V + 1)
        edgeto[s] = s
        dissto = [INF] * (graph.V + 1)
        dissto[s] = 0
        marked = set()
        while q:
            vweight, v = hpop(q)
            if v in marked:
                continue
            marked.add(v)
            for w in graph.adj(v):
                wweight = graph.weight(v, w)
                if dissto[w] > wweight:
                    dissto[w] = wweight
                    edgeto[w] = v
                    hpush(q, (wweight, w))
        self.edgeto = edgeto


class Graph(object):
    def __init__(self, V):
        self.V = V
        self._adj = [[] for _ in range(V + 1)]
        self._weight = dict()

    def adj(self, v):
        return self._adj[v]

    def add(self, v, w, weight):
        self._adj[v] += [w]
        self._adj[w] += [v]
        self._weight[tuple(sorted((v, w)))] = weight

    def weight(self, v, w):
        return self._weight[tuple(sorted((v, w)))]


def test_4_vertices():
    g = Graph(4)
    g.add(1, 2, 1)
    g.add(1, 3, 3)
    g.add(1, 4, 4)
    g.add(2, 3, 1)
    g.add(3, 4, 1)
    mst = PrimMST(g).edgeto

    assert mst[1] == 1
    assert mst[2] == 1
    assert mst[3] == 2
    assert mst[4] == 3


def test_5_vertices():
    g = Graph(5)
    g.add(1, 2, 1)
    g.add(1, 3, 2)
    g.add(1, 4, 3)
    g.add(1, 5, 4)
    g.add(2, 3, 1)
    g.add(2, 4, 2)
    g.add(2, 5, 3)
    g.add(3, 4, 1)
    g.add(3, 5, 2)
    g.add(4, 5, 1)
    mst = PrimMST(g).edgeto

    assert mst[1] == 1
    assert mst[2] == 1
    assert mst[3] == 2
    assert mst[4] == 3
    assert mst[5] == 4


if __name__ == "__main__":
    test_4_vertices()
    test_5_vertices()
    print('done')
