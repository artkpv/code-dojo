#!python3
import unittest


def lmis(X):
    n = len(X)
    c = [0] * n
    max_ = 0
    for i in range(n):
        c[i] = 1 + max((c[j] for j in range(n) if X[j] <= X[i]), default=0)
        max_ = max(max_, c[i])
    return max_


class Tests(unittest.TestCase):
    def test_first(self):
        self.assertEqual(lmis([1, 0, 2, 0, 3, 0, 3, 0, 4]), 5)
        self.assertEqual(lmis([1, 0, 1, 0, 1, 0, 1, 0, 0]), 5)
        self.assertEqual(lmis([1, 2, 3, 4, 5, 6, 7, 1]), 7)

unittest.main()
