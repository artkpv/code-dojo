#!python3

"""
Kosaraju's algorithm for computing strongly connected components on directed graph.
"""

import unittest
from collections import deque


class Graph(object):
    def __init__(self, vertices_num):
        self.adj = [[] for _ in range(vertices_num)]
        self.vertices_num = vertices_num

    def add(self, from_, to):
        self.adj[from_] += [to]


class ReversedGraph(Graph):
    def __init__(self, graph):
        self.vertices_num = graph.vertices_num
        self.adj = [[] for _ in range(self.vertices_num)]
        for v, adj in enumerate(graph.adj):
            for w in adj:
                self.adj[w] += [v]


class Kosaraju(object):
    def __init__(self, graph):
        def reversed_post_order():
            order = deque()
            visited = set()
            rg = ReversedGraph(graph)
            def dfs(v):
                if v in visited:
                    return
                visited.add(v)
                for w in rg.adj[v]:
                    dfs(w)
                order.appendleft(v)

            for v in range(rg.vertices_num):
                dfs(v)
            return order

        def count_cc():
            cc = list(range(graph.vertices_num))
            visited = set()
            def dfs(v, cc_num):
                visited.add(v)
                cc[v] = cc_num
                for w in graph.adj[v]:
                    if w in visited:
                        continue
                    dfs(w, cc_num)

            cc_num = 0
            for v in reversed_post_order():
                if v not in visited:
                    dfs(v, cc_num)
                    cc_num += 1
            return cc, cc_num

        self.scc, self.scc_number = count_cc()

    def find(self, v):
        return self.scc[v]


class Tests(unittest.TestCase):
    def test_simple_graph(self):
        """
        0 --> 1 --> 4 <--> 5
        ^     |
        |     |
        |     v
        2 <-- 3
        """
        g = Graph(6)
        g.add(0, 1)
        g.add(2, 0)
        g.add(1, 3)
        g.add(3, 2)
        g.add(1, 4)
        g.add(4, 5)
        g.add(5, 4)
        kosaraju = Kosaraju(g)
        self.assertEqual(kosaraju.scc_number, 2)
        self.assertEqual(kosaraju.find(0), kosaraju.find(3))
        self.assertEqual(kosaraju.find(4), kosaraju.find(5))
        self.assertNotEqual(kosaraju.find(2), kosaraju.find(4))

if __name__ == '__main__':
    unittest.main()
