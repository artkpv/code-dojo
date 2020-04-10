#!/bin/python3
from heapq import heappop, heappush

POS_INF = float('inf')


def dijkstra(graph, source):
    """
    Finds shortest path from S in G graph by expanding a tree
    with shortest edge to the source using. BFS and min-queue based.
    Time: O(V*log(E) + E*log(E))
    Space: E+V
    """
    q = [(0, source)]
    distto = [POS_INF] * (graph.V)
    distto[source] = 0
    edgeto = [None] * (graph.V)
    edgeto[source] = source
    marked = [False] * (graph.V)
    while q:
        vweight, v = heappop(q)
        if marked[v]:
            continue
        marked[v] = True
        for w in graph.adj(v):
            d = distto[v] + graph.weight(w, v)
            if distto[w] > d:
                distto[w] = d
                edgeto[w] = v
                heappush(q, (d, w))
    return edgeto


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
        v, w = (v, w) if v < w else (w, v)
        self._weight[(v,w)] = weight

    def adj(self, v):
        return self._adj[v] or []

    def weight(self, v, w):
        v, w = (v, w) if v < w else (w, v)
        return self._weight.get((v, w), POS_INF)


def test1():
    g = Graph(1)
    tree = dijkstra(g, 0)
    assert tree == [0], tree
    print("test 1 - YEAH")

def test2():
    g = Graph(2)
    g.add(0, 1, 1)
    tree = dijkstra(g, 0)
    assert tree == [0, 0], tree
    print("test 2 - YEAH")

def test3():
    g = Graph(3)
    g.add(0, 1, 1)
    g.add(0, 2, 2)
    tree = dijkstra(g, 0)
    assert tree == [0, 0, 0], tree
    print("test 3 - YEAH")

def test4():
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
    tree = dijkstra(g, 0)
    assert tree == [0, 0, 1, 2, 3, 4, 0, 6, 7, 8], tree
    print("test 4 - YEAH")

def test5():
    """
   1   2
     0
   3
   4   5
     6
    """
    g = Graph(7)
    g.add(0, 1, 1)
    g.add(0, 2, 1)
    g.add(0, 3, 3)
    g.add(0, 5, 4)
    g.add(3, 4, 3)
    g.add(4, 6, 3)
    g.add(5, 6, 4)
    tree = dijkstra(g, 0)
    assert tree == [0, 0, 0, 0, 3, 0, 5], tree
    print("test 5 - YEAH")

if __name__ == "__main__":
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()

    n, m = [int(e) for e in input().strip().split(' ')]
    g = Graph(n)
    for _ in range(m):
        v, w, vww = [int(e) for e in input().strip().split(' ')]
        g.add(v-1, w-1, vww)
    tree = dijkstra(g, 0)
    if tree[n-1] == None:
        print(-1)
    else:
        x = n-1
        ans = [x]
        while tree[x] != x:
            x = tree[x]
            ans.append(x)
        print(' '.join(str(x+1) for x in reversed(ans)))


