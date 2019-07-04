#!python3

"""
Graham's scan algorithm for finding the convex hull for a given
set of points on 2D area.
"""
import unittest
from collections import namedtuple
from math import sqrt, atan2


Point = namedtuple('Point', ['x', 'y'])
Point.__repr__ = lambda p: '(%d, %d)' % (p.x, p.y)


def angle(a, b):
    """ Angle between two points """
    dx = b.x - a.x
    dy = b.y - a.y
    assert not (dx == dy == 0)
    return atan2(dy, dx)


def ccw(a, b, c):
    """
    Is counterclockwise turn.
    Given a, b, c points. Returns
    1 counterclockwise,
    0 collinear,
    -1 clockwise
    """
    area = ((b.x - a.x) * (c.y - a.y) -
            (b.y - a.y) * (c.x - a.x))
    if area < 0:
        return -1
    if area > 0:
        return 1
    return 0


def graham_scan(points):
    if not points:
        return []
    points = list(set(points))
    bottom = min(points, key=lambda p: p.y)
    ordered = list(sorted(
        (p for p in points if p != bottom),
        key=lambda p: angle(bottom, p),
        reverse=True
    ))
    hull = [bottom]
    while ordered:
        if len(hull) < 2:
            hull += [ordered.pop()]
        else:
            c = ordered[-1]
            a = hull[-2]
            b = hull[-1]
            if ccw(a, b, c) >= 0:
                hull += [ordered.pop()]
            else:
                hull.pop()
    return hull


class Tests(unittest.TestCase):
    def test_tests(self):
        dots_picture = """
  .  .
.  .   .
  .  .
.   .      .
 .  .
   .    ."""
        points = []
        dots_picture_lines = dots_picture.split('\n')
        n = len(dots_picture_lines)
        m = 0
        for i, line in enumerate(dots_picture_lines):
            m = max(len(line), m)
            for j, c in enumerate(line):
                if c == '.':
                    points += [Point(j, n-i-1)]
        hull = graham_scan(points)

        print('Dots:')
        print(dots_picture)
        print('Hull:')
        print(hull)
        hull_str = [[' '] * m for _ in range(n)]
        for x, y in hull:
            hull_str[n-y-1][x] = '.'
        print('\n'.join(
            ''.join(line) for line in hull_str)
        )

        expected = [Point(x, y) for x, y in (
            (3, 0), (8, 0), (11, 2), (7, 4),
            (5, 5), (2, 5), (0, 4), (0, 2), (1, 1))]
        self.assertEqual(hull, expected)


unittest.main()
