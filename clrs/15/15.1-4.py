"""
15.1-4 Modify to return actual cut.

"""

import unittest


def cut_rod_bottom_up(rod, prices):
    def get_price(cut): return prices[cut-1] if cut > 0 else 0
    assert rod <= len(prices)
    revenue = [0] * (rod + 1)
    cuts = [None] * (rod + 1)
    for cut in range(1, rod+1):
        for j in range(cut):
            r = get_price(cut-j) + revenue[j]
            if r > revenue[cut]:
                revenue[cut] = r
                cuts[cut] = [cut-j] + (cuts[j] if cuts[j] else [])
    return revenue[rod], cuts[rod]


class Tests(unittest.TestCase):
    def test_1(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(cut_rod_bottom_up(1, prices), (1, [1]))
        self.assertEqual(cut_rod_bottom_up(2, prices), (5, [2]))
        self.assertEqual(cut_rod_bottom_up(3, prices), (8, [3]))
        self.assertEqual(cut_rod_bottom_up(4, prices), (10, [2, 2]))
        self.assertEqual(cut_rod_bottom_up(5, prices), (13, [3, 2]))
        self.assertEqual(cut_rod_bottom_up(6, prices), (17, [6]))
        self.assertEqual(cut_rod_bottom_up(7, prices), (18, [6, 1]))



unittest.main()
