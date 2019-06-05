#!python3
"""
Shortest paths using topological sort. Only for DAG w/o negative weights.

Idea:
    TS = Get top. sorted vertices:

    for v in all vertices:
        dfs(v) if not visited

    dfs(v):
        v visited
        for w in adj(v):
            if w not visited: dfs(w)
        add v to stack / ts (reversed post order)

    for v in TS:
        for w in adj(v):
            relax(v,w)
"""

import unittest


class Graph(object):
    def __init__(self, vertices_num):
        self.adj = [[] for _ in range(vertices_num)]
        self.vertices_num = vertices_num
        self.weights = {}

    def add(self, from_, to, weight):
        self.adj[from_] += [to]
        self.weights[(from_, to)] = weight


class TSP(object):
    """
    TSP - topological shortest path.
    """
    def __init__(self, graph, source):
        self.graph = graph

        def tsort():
            order = []
            visited = set()

            def dfs(v):
                if v in visited:
                    return
                visited.add(v)
                for w in graph.adj[v]:
                    dfs(w)
                order.append(v)

            for v in range(graph.vertices_num):
                dfs(v)
            return list(reversed(order))

        order = tsort()

        distto = [float('inf')] * graph.vertices_num
        distto[source] = 0
        self.edgeto = {}
        self.edgeto[source] = source
        for v in order:
            for w in graph.adj[v]:
                if distto[w] > distto[v] + graph.weights[(v, w)]:
                    self.edgeto[w] = v
                    distto[w] = distto[v] + graph.weights[(v, w)]
        self.distto = distto

    def distanceto(self, v):
        return self.distto[v]

    def pathto(self, v):
        path = []
        while self.edgeto[v] != v:
            path += [v]
            v = self.edgeto[v]
        path += [v]
        return path

    def __repr__(self):
        s = ''
        for v in range(self.graph.vertices_num):
            s += '(%d: %f, %s)\n' % (v, self.distto[v], self.pathto(v))
        return s


class Tests(unittest.TestCase):
    def test_basic(self):
        """
        1 -1-> 2
        |      |
        4      1
        |      |
        v      v
        3 <-1- 4
        TS: 1 2 4 3
        SP:
            at 1:
                distto[1] = 0
                d[2] = 1
                d[3] = 4
            at 2:
                d[4] = 2
            at 4:
                d[3] = 3
            at 3:
                noop
            result: distto 1:0 2:1 4:2 3:3
        """
        g = Graph(4)
        g.add(0, 1, 1)
        g.add(0, 2, 4)
        g.add(1, 3, 1)
        g.add(3, 2, 1)
        sp = TSP(g, 0)
        self.assertEqual(sp.distanceto(0), 0)
        self.assertEqual(sp.distanceto(1), 1)
        self.assertEqual(sp.distanceto(2), 3)
        self.assertEqual(sp.distanceto(3), 2)

    def test_one_edge(self):
        g = Graph(1)
        sp = TSP(g, 0)
        self.assertEqual(sp.distanceto(0), 0)

    def test_tinyEWGraph(self):
        vertices = 8
        g = Graph(vertices)
        g.add(5, 4, 0.35)  # 13 edges
        g.add(4, 7, 0.37)
        g.add(5, 7, 0.28)
        g.add(5, 1, 0.32)
        g.add(4, 0, 0.38)
        g.add(0, 2, 0.26)
        g.add(3, 7, 0.39)
        g.add(1, 3, 0.29)
        g.add(7, 2, 0.34)
        g.add(6, 2, 0.40)
        g.add(3, 6, 0.52)
        g.add(6, 0, 0.58)
        g.add(6, 4, 0.93)
        sp = TSP(g, 5)

        self.assertAlmostEqual(sp.distanceto(0), 0.73)
        self.assertEqual(sp.pathto(0), [0, 4, 5])
        self.assertAlmostEqual(sp.distanceto(1), 0.32)
        self.assertEqual(sp.pathto(1), [1, 5])
        self.assertAlmostEqual(sp.distanceto(2), 0.62)
        self.assertEqual(sp.pathto(2), [2, 7, 5])
        self.assertAlmostEqual(sp.distanceto(3), 0.61)
        self.assertEqual(sp.pathto(3), [3, 1, 5])
        self.assertAlmostEqual(sp.distanceto(4), 0.35)
        self.assertEqual(sp.pathto(4), [4, 5])
        self.assertAlmostEqual(sp.distanceto(5), 0.00)
        self.assertEqual(sp.pathto(5), [5])
        self.assertAlmostEqual(sp.distanceto(6), 1.13)
        self.assertEqual(sp.pathto(6), [6, 3, 1, 5])
        self.assertAlmostEqual(sp.distanceto(7), 0.28)
        self.assertEqual(sp.pathto(7), [7, 5])


unittest.main()
