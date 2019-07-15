#!python3

"""
Bellman-Ford shortest path with negative weights.
"""

from collections import deque
import unittest

INF = float('inf')

def bfsp(graph, source):
    def find_negative_cycle(edgeto, source):
        g = Graph(len(edgeto))
        for v, w in enumerate(edgeto):
            if w:
                g.add(v, w)

        onstack = [False] * g.V
        visited = [False] * g.V
        def find_cycle(v):
            onstack[v] = True
            visited[v] = True
            for w in g.adj[v]:
                if onstack[w]:
                    return True
                if not visited[w] and find_cycle(w):
                    return True
            onstack[v] = False
            return False

        for v in range(len(edgeto)):
            if find_cycle(v):
                return True
        return False

    q = deque()
    onQ = set()
    distto = [INF] * graph.V
    edgeto = [None] * graph.V
    distto[source] = 0
    q.append(source)
    onQ.add(source)

    cost = 0
    has_negative_cycle = False
    while q and not has_negative_cycle:
        v = q.pop()
        onQ.remove(v)
        for w in graph.adj[v]:
            if distto[w] > distto[v] + graph.weight(v, w):
                distto[w] = distto[v] + graph.weight(v, w)
                edgeto[w] = v  # MST
                if w not in onQ:
                    q.append(w)
                    onQ.add(w)
            cost += 1
            if cost % graph.V == 0:
                has_negative_cycle = find_negative_cycle(edgeto, source)
    return lambda t: distto[t] if not has_negative_cycle else -INF


class Graph(object):
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.weights = {}

    def add(self, from_, to_, weight=0):
        self.adj[from_] += [to_]
        self.weights[(from_, to_)] = weight

    def weight(self, v, w):
        return self.weights[(v, w)]


class Tests(unittest.TestCase):
    def test_4_correct(self):
        g = Graph(4)
        g.add(0, 1, 2)
        g.add(0, 2, 3)
        g.add(0, 3, 2)
        g.add(1, 2, -3)
        g.add(2, 3, 2)

        f = bfsp(g, 0)

        self.assertEqual(f(0), 0)
        self.assertEqual(f(1), 2)
        self.assertEqual(f(2), -1)
        self.assertEqual(f(3), 1)

    def test_negative_cycle(self):
        g = Graph(4)
        g.add(0, 1, 2)
        g.add(0, 2, 3)
        g.add(0, 3, 2)
        g.add(1, 2, -3)
        g.add(2, 1, 1)
        g.add(2, 3, 2)

        f = bfsp(g, 0)

        self.assertEqual(f(0), -INF)
        self.assertEqual(f(1), -INF)
        self.assertEqual(f(2), -INF)
        self.assertEqual(f(3), -INF)

unittest.main()
