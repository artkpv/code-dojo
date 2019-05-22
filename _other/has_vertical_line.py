#!python3

"""
Given (x,y) points determine whether there is a vertical line that
separates them all into to symmetrical groups where x1,y1 at left
has x2,y2 at right for all points at left.
"""

import unittest
from collections import defaultdict


def hasline(points):
    if not points:
        return False
    points = set(points)
    shift = min(p[0] for p in points)
    avg = shift + sum(p[0] - shift for p in points)/len(points)
    complement = defaultdict(set)
    for x, y in points:
        distance = x - avg
        if distance == 0:
            continue
        if -distance in complement:
            if y in complement[-distance]:
                complement[-distance].remove(y)
                if len(complement[-distance]) == 0:
                    del complement[-distance]
            else:
                complement[distance].add(y)
        else:
            complement[distance].add(y)
    print(complement)
    return len(complement) == 0


class TestHasLine(unittest.TestCase):
    def test_two_points(self):
        points = [(1,0), (3,0)]
        self.assertTrue(hasline(points))

    def test_two_points_no_line(self):
        points = [(1,1), (3,0)]
        self.assertFalse(hasline(points))

    def test_no_points(self):
        points = []
        self.assertFalse(hasline(points))

    def test_three_points(self):
        points = [(0,0), (1,0), (2,0)]
        self.assertTrue(hasline(points))

    def test_duplicate_points(self):
        points = [(0,0), (1,0), (2,0), (2,0)]
        self.assertTrue(hasline(points))


if __name__ == '__main__':
    unittest.main()
