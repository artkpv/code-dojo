#!python3
"""
x, y
x1, y1
x2, y2

(x1 - x)  = (y1 - y)
(x2 - x1)   (y2 - y1)

"""

import unittest
from collections import Counter


def maxline(points):
    if not points:
        return 0
    n = len(points)
    assert n > 0
    max_ = 0
    for i in range(n):
        x, y = points[i]
        counter = Counter()
        vertical = 0
        horizontal = 0
        same = 1
        j = i+1
        while j < n:
            x1, y1 = points[j]
            dx = x - x1
            dy = y - y1
            if dx == 0 and dy == 0:
                same += 1
            elif dx == 0:
                vertical += 1
            elif dy == 0:
                horizontal += 1
            else:
                counter[round(dx/dy, 5)] += 1
            j += 1

        count = max(vertical, horizontal) + same
        for v in counter.values():
            if count < v + same:
                count = v + same
        if count > max_:
            max_ = count
    return max_


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        return maxline([(x, y) for x, y in zip(A, B)])


class Tests(unittest.TestCase):
    def test_one(self):
        return
        self.assertEqual(maxline([]), 0)
        self.assertEqual(maxline([(0, 0)]), 1)
        self.assertEqual(maxline([(1, 1)]), 1)
        self.assertEqual(maxline([(1, 1), (2, 2)]), 2)
        self.assertEqual(maxline([(1, 1), (2, 2), (3, 3)]), 3)
        self.assertEqual(maxline([(1, 2), (2, 2), (3, 3)]), 2)
        self.assertEqual(maxline([(0, 0), (1, 1), (-1, -1)]), 3)
        self.assertEqual(maxline([(1, 0), (1, 4), (1, -1)]), 3)
        self.assertEqual(maxline([(4, -4), (8, -4), (-4, -4)]), 3)
        self.assertEqual(maxline([(1, 1), (1, 1), (1, 1)]), 3)
        self.assertEqual(maxline([(0, 0), (0, 0), (0, 0), (0, 1)]), 4)
        self.assertEqual(maxline(
            [(0, 0), (1, 1), (-1, -1), (-1, 1)]), 3
        )

    def test_other(self):
        A = [-6, -17, 5, -16, -18, -17]
        B = [2, -4, 5, -13, -2, 20]
        s = Solution().maxPoints(A, B)
        self.assertEqual(s, 2)


unittest.main()
