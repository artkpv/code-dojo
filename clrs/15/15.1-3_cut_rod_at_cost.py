#!python3
"""

Ex 1
prices
1, 5, 8, 9, 10, 17, 17, 20, 24, 30

cost = 1
rod = 4
9-0 = 9
8+1-1 = 8
5+5-1 = 9
5+1+1-2=5
1+1+1+1-3=1
1+8-1 = 8
1+1+5-2


"""

import unittest


def cost_cut_rod(cost, rod, prices):
    def get_price(cut): return prices[cut-1] if cut > 0 else 0
    assert rod <= len(prices)
    revenue = [0] * (rod + 1)
    for cut in range(1, rod+1):
        revenue[cut] = max(
            get_price(cut-j) + (revenue[j] - cost if j > 0 else 0)
            for j in range(cut)
        )
    return revenue[rod]


class Tests(unittest.TestCase):
    def test_1(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(cost_cut_rod(1, 4, prices), 9)
        """
        revenue =
        0
        1
        5 1+1-1 = 5
        8 5+5-1 = 9
        9 8+1-1 5+5-1 1+9-1
        cut 1 2 3 4

        """



unittest.main()
