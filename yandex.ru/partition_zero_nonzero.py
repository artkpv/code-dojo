#!python3

import unittest


def partition_zero_nonzero(a):
    i = 0
    j = -1
    while i < len(a) and j < len(a):
        if a[i] == 0:
            i += 1
        else:
            j += 1
            a[i], a[j] = a[j], a[i]
            i += 1
    return a


class Tests(unittest.TestCase):
    def test_tests(self):
        f = partition_zero_nonzero
        self.assertEqual([0], f([0]))
        self.assertEqual([1, 0], f([0, 1]))
        self.assertEqual([0], f([0]))
        self.assertEqual([1, 0, 0], f([0, 0, 1]))
        self.assertEqual([2, 1, 0], f([0, 2, 1]))
        self.assertEqual([2, 1, 0], f([2, 1, 0]))
        """
        0 2 1  0 -1
        0 2 1  1 -1
        2 0 1  1 0
        2 0 1  2 0
        2 1 0  2 1
        2 1 0  3 1
        exti
        """

