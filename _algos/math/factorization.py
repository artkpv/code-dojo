#!/bin/python3

"""
Find all factors for N. Time: exponensial.
"""
import unittest
import math


def factors_easy(n):
    factors = []
    i = 2
    nn = n
    while n > 1 and i * i <= nn:
        q, r = divmod(n, i)
        if r == 0:
            n = q
            factors += [i]
        else:
            i += 1
    return factors


def factors(n):
    factors = []
    if n <= 3:
        return factors
    while n % 2 == 0:
        factors += [2]
        n //= 2
    while n % 3 == 0:
        factors += [3]
        n //= 3
    i = 1
    """
    Each following 6 numbers has only 2 candidates:
        5 7 11 13 17 19 23 25 ..
    """
    left_right = (-1,1)
    nn = n
    while n > 1 and pow(i*6 + 1, 2) <= nn:
        for j in left_right:
            k = i*6 + j
            if k > n:  # can be equal (45)
                assert(n == 1)
                break
            while True:
                q, r = divmod(n, k)
                if r != 0: break
                factors += [k]
                n = q
        i += 1
    return factors


class Tests(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(factors(1), [])
        self.assertEqual(factors(2), [])
        self.assertEqual(factors(3), [])
        self.assertEqual(factors(4), [2, 2])
        self.assertEqual(factors(5), [])
        self.assertEqual(factors(6), [2, 3])
        self.assertEqual(factors(12), [2, 2, 3])
        self.assertEqual(factors_easy(12), [2, 2, 3])

    def test_larger(self):
        self.assertEqual(factors(70560), [2, 2, 2, 2, 2, 3, 3, 5, 7, 7])
        self.assertEqual(factors_easy(70560), [2, 2, 2, 2, 2, 3, 3, 5, 7, 7])
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
