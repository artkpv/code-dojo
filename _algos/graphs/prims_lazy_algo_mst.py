#!python3

"""
Grow mst by taking closest to a tree. Lazy version.

Time: O(E*logE)
Space: ~V

"""

import unittest
from collections import namedtuple
from heapq import heappush, heappop

class Point(object):
    def __init__(self, x, y, e=None):
        self.x = x
        self.y = y
        self.e = None

    def __repr__(self):
        return '(%d,%d)' % (self.x, self.y)

    def __lt__(self, other):
        return self.x < other.x or self.y < other.y


def LazyPrimsMST(vertices, adj, weight):
    assert vertices
    q = []  # min queue
    marked = set()
    def visit(v):
        marked.add(v)
        for w in adj(v):
            if w not in marked:
                heappush(q, (weight(v, w), v, w))

    visit(vertices[0])
    mst = []
    while len(marked) < len(vertices):
        weightvw, v, w = heappop(q)
        if w in marked and v in marked:
            continue
        mst += [(v, w)]
        if w not in marked:
            visit(w)
        if v not in marked:
            visit(v)
    return mst


class Tests(unittest.TestCase):
    def test_one(self):
        field = """
.   .
  .   .  .
.

   . .
.
"""
        vertices = []
        for irow, row in enumerate(field.split('\n')):
            for icol, c in enumerate(row):
                if c == '.':
                    vertices += [Point(icol, irow, None)]
        def adj(v):
            yield from (w for w in vertices if w != v)

        def weight(v, w):
            return ((v.x - w.x)**2 + (v.y - w.y)**2)**0.5

        mst = LazyPrimsMST(vertices, adj, weight)
        self.assertEqual(
            '[((0,1), (0,3)), ((0,1), (2,2)), ((2,2), (4,1)), ((4,1), (6,2)), ((6,2), (9,2)), ((0,3), (0,6)), ((0,6), (3,5)), ((3,5), (5,5))]',
            repr(mst)
        )


unittest.main()

