#!python3

import unittest


def fib_dynamic(n):
    if n == 0:
        return 0
    a = 1
    b = 1
    for _ in range(3, n+1):
        t = a
        a = a + b
        b = t
    return a


class Tests(unittest.TestCase):
    def test_tests(self):
        self.assertEqual(fib_dynamic(1), 1)
        self.assertEqual(fib_dynamic(2), 1)
        self.assertEqual(fib_dynamic(3), 2)
        self.assertEqual(fib_dynamic(4), 3)
        self.assertEqual(fib_dynamic(5), 5)
        self.assertEqual(fib_dynamic(6), 8)
        self.assertEqual(fib_dynamic(7), 13)
        self.assertEqual(fib_dynamic(8), 21)
        self.assertEqual(fib_dynamic(9), 34)
        self.assertEqual(fib_dynamic(10), 55)
        self.assertEqual(fib_dynamic(40), 102334155)
        self.assertEqual(fib_dynamic(100), 354224848179261915075)


unittest.main()
