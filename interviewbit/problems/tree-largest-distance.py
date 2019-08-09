#!/bin/python3

import unittest

class Solver(object):
    def solve(self, parents):
        if not parents:
            return 0
        adj = [[] for _ in range(len(parents))]
        root = None
        for c, p in enumerate(parents):
            if p == -1:
                root = c
            else:
                adj[p] += [c]
        res = 0
        def maxdistance(v):
            nonlocal res
            mhs = [maxdistance(c) for c in adj[v]]
            mhs.sort()
            if len(mhs) >= 2:
                res = max(res, mhs[-1] + mhs[-2])
            return 1 + (mhs[-1] if len(mhs) > 0 else 0)

        rd = maxdistance(root) - 1
        if res < rd:
            res = rd
        return res

class Tests(unittest.TestCase):
    def test_simple(self):
        P = [-1, 0, 0, 0, 3]
        self.assertEqual(Solver().solve(P), 3)

    def test_subtree(self):
        """
        0
         1
           2 4 5
           3 6 7
        """
        P = [-1, 0, 1, 1, 2, 4, 3, 6]
        self.assertEqual(Solver().solve(P), 6)

    def test_edge_cases(self):
        self.assertEqual(Solver().solve([]), 0)
        self.assertEqual(Solver().solve([-1]), 0)
        self.assertEqual(Solver().solve([-1, 0]), 1)



unittest.main()
