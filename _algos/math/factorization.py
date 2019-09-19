#!/bin/python3

import unittest

def factors(n):
    x = n
    i = 2
    prime_factors = []
    while 1 < x and i < n:
        q, r = divmod(x, i)
        if r == 0:
            prime_factors += [i]
            x = q
        else:
            i += 1
    return prime_factors


class Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(factors(1), [])
        self.assertEqual(factors(2), [])
        self.assertEqual(factors(3), [])
        self.assertEqual(factors(4), [2, 2])
        self.assertEqual(factors(5), [])
        self.assertEqual(factors(6), [2, 3])
        self.assertEqual(factors(12), [2, 2, 3])

    def test_larger(self):
        self.assertEqual(factors(70560), [2, 2, 2, 2, 2, 3, 3, 5, 7, 7])
        self.assertEqual(factors(100500), [2, 2, 3, 5, 5, 5, 67])

    def test_large(self):
        self.assertEqual(
            factors(100500100500100500100500100500),
            [2, 2, 3, 5, 5, 5, 31, 41, 67, 211, 241, 271, 2161, 9091, 2906161]
        )
        # self.assertEqual(
            # factors(100500100500100500100500100500100500100500100500100500100500100500100500),
            # [2, 2, 3, 3, 5, 5, 5, 19, 67, 73, 101, 137, 3169, 9901, 52579, 98641, 333667, 99990001, 999999000001, 3199044596370769]
        # )




unittest.main()
