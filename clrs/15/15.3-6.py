#!python3

import unittest

def trade(d, rates):
    """
    Returns money we get in n-th currency, given money in 1-st currency.
    Time: N*N.
    """

    n = len(rates)
    units = [0] * n
    units[0] = d
    for i in range(1, n):
        for j in range(0, n-1):
            units[i] = max(units[i], rates[j][i] * units[j])
    return units[n-1]

class Tests(unittest.TestCase):
    def test_test(self):
        rates = [
            [1, 2, 4, 10],
            [1/2, 1, 1, 4],
            [1/4, 1, 1, 5],
            [1/10, 1/4, 1/5, 1]
        ]

        self.assertEqual(trade(10, rates), 200)


unittest.main()
