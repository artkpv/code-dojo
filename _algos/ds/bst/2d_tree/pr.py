#!python
"""

(1, 0) (1,1) (0,1)

1.
x   1
       0 (1,0)

2.
    1
        0


"""

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Rect = namedtuple('Rect', ['tlx', 'tly', 'brx', 'bry'])  # Top left x / y. Bottom right x / y.

INF = float('inf')
class TwoDTree(object):

    class Node(object):
        def __init__(self, point):
            self.l_or_a = None  # Left or above.
            self.r_or_b = None  # Right or below.
            self.point = point

    def __init__(self):
        self.root = None

    def add(self, point):
        def node_add(point, n, byX):
            if not n:
                return TwoDTree.Node(point)
            if (byX and point.x < n.point.x) or (not byX and point.y >= n.point.y):
                n.l_or_a = node_add(point, n.l_or_a, not byX)
            else:
                n.r_or_b = node_add(point, n.r_or_b, not byX)
            return n

        self.root = node_add(point, self.root, byX=True)


    def range(self, rect):
        found = []
        def visit_node(n, r, byX):
            if not r or not n:
                return
            if contains(n.point, r):
                found.append(n.point)
            visit_node(n.l_or_a, intersection(left_or_above(n.point, byX), r), not byX)
            visit_node(n.r_or_b, intersection(right_or_below(n.point, byX), r), not byX)

        def contains(p, r):
            return (r.tlx <= p.x <= r.brx
                and r.bry <= p.y <= r.tly)

        def left_or_above(p, byX):
            if byX:
                return Rect(-INF, INF, p.x, -INF)
            return Rect(-INF, INF, INF, p.y)

        def right_or_below(p, byX):
            if byX:
                return Rect(p.x, INF, INF, -INF)
            return Rect(-INF, p.y, INF, -INF)

        def intersection(a, b):
            c = Rect(
                max(a.tlx, b.tlx), min(a.tly, b.tly),
                min(a.brx, b.brx), max(a.bry, b.bry)
            )
            if c.tlx <= c.brx and c.tly >= c.bry:
                return c
            return None

        visit_node(self.root, rect, byX=True)
        return found


def test1():
    t = TwoDTree()
    t.add(Point(1, 1))
    t.add(Point(9, 9))
    t.add(Point(1, 9))
    t.add(Point(9, 1))

    assert (t.range(Rect(0, 2, 2, 0)) == [Point(1, 1)],
        "Found {}".format(t.range(Rect(0, 2, 2, 0)))
    )
    assert (t.range(Rect(8, 10, 10, 8)) == [Point(9, 9)],
        "Found {}".format(t.range(Rect(8, 10, 10, 8)))
    )
    assert (t.range(Rect(0, 10, 2, 8)) == [Point(1, 9)],
        "Found {}".format(t.range(Rect(0, 10, 2, 8)))
    )
    assert (t.range(Rect(8, 2, 10, 0)) == [Point(9, 1)],
        "Found {}".format(t.range(Rect(8, 2, 10, 0)))
    )
    assert (t.range(Rect(0, 10, 10, 0)) ==
        [Point(1, 1), Point(9, 9), Point(1, 9), Point(9, 1)]), "All points: {}".format(t.range(Rect(0, 10, 10, 0)))
    assert t.range(Rect(0, 0, 0, 0)) == [], "None"
    print('Test 1 done')


if __name__ == "__main__":
    pointsnum = int(input().strip())
    t = TwoDTree()
    for _ in range(pointsnum):
        x, y = [int(e) for e in input().strip().split(' ')]
        t.add(Point(x, y))
    tests = int(input().strip())
    for _ in range(tests):
        tlx, tly, brx, bry = [int(e) for e in input().strip().split(' ')]
        ans = t.range(Rect(tlx, tly, brx, bry))
        if ans:
            print(len(ans))
            print('\n'.join(' '.join((str(p.x), str(p.y))) for p in sorted(ans)))
        else:
            print(0)


