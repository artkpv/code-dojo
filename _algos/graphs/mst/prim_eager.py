#!python3
"""
    Prim's algorithm for finding minimum spanning tree.
"""

import sys
from minqueue import MinPQ
POS_INF = 9e9

class Graph:
    def __init__(self, V):
        self.V = V
        self._adj = [None] * V
        self._weight = {}

    def add(self, v, w, weight):
        if not self._adj[v]:
            self._adj[v] = []
        if not self._adj[w]:
            self._adj[w] = []
        self._adj[v] += [w]
        self._adj[w] += [v]
        self._weight[(v,w)] = weight
    
    def adj(self, v):
        return self._adj[v] or []

    def weight(self, v, w):
        return self._weight.get((v, w), POS_INF)


class PrimMST:
    """
        Eager version of Prim's algorithm on non-negative connected graph
    """
    def __init__(self, graph, source):
        edgeTo = [None] * graph.V
        marked = [False] * graph.V
        distTo = [POS_INF] * graph.V
        distTo[source] = 0
        q = MinPQ()
        q.add(0, source)
        self._mst = []  # ve
        while q:
            v = q.pop()
            marked[v] = True
            self._mst += [(v, edgeTo[v])]
            for w in graph.adj(v):
                if not marked[w]:
                    weight = graph.weight(v, w)
                    if  distTo[w] > weight:
                        distTo[w] = weight
                        edgeTo[w] = v
                        if q.contains(w):
                            q.decrease(weight, w)
                        else:
                            q.add(weight, w)
    
    def get(self):
        return [i[0] for i in self._mst]


def test1():
    g = Graph(1)
    mst = PrimMST(g, 0)
    assert(mst.get() == [0])
    print("test 1 - YEAH")

def test2():
    g = Graph(2)
    g.add(0, 1, 1)
    mst = PrimMST(g, 0)
    assert(mst.get() == [0, 1])
    print("test 2 - YEAH")

def test3():
    g = Graph(3)
    g.add(0, 1, 1)
    g.add(0, 2, 2)
    mst = PrimMST(g, 0)
    assert(mst.get() == [0, 1, 2])
    print("test 3 - YEAH")

def test4():
    """
    5 4 3 2 1 0 6 7 8 9
    """
    g = Graph(10)
    g.add(0, 1, 1)
    g.add(1, 2, 1)
    g.add(2, 3, 1)
    g.add(3, 4, 1)
    g.add(4, 5, 1)
    g.add(0, 6, 2)
    g.add(6, 7, 2)
    g.add(7, 8, 2)
    g.add(8, 9, 2)
    mst = PrimMST(g, 0)
    assert(mst.get() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print("test 4 - YEAH")

def test5():
    """
   Path 0 3 4 6 > 0 5 6 but MST should be 4 6 not 5 6
   1   2 
     0 
   3
   4   5 
     6
    """
    g = Graph(10)
    g.add(0, 1, 1)
    g.add(0, 2, 1)
    g.add(0, 3, 3)
    g.add(0, 5, 4)
    g.add(3, 4, 3)
    g.add(4, 6, 3)
    g.add(5, 6, 4)
    mst = PrimMST(g, 0)
    assert(mst.get() == [0, 1, 2, 3, 4, 6, 5])

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()

    