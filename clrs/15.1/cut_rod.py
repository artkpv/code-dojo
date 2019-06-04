
import unittest
import sys
sys.setrecursionlimit(10000)


def cut_rod_bottom_up(rod, prices):
    def get_price(cut): return prices[cut-1] if cut > 0 else 0
    assert rod <= len(prices)
    revenue = [0] * (rod + 1)
    for cut in range(1, rod+1):
        revenue[cut] = max(
            get_price(cut-j) + revenue[j] for j in range(cut)
        )
    return revenue[rod]


class Tests(unittest.TestCase):
    def test_1(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        self.assertEqual(cut_rod_bottom_up(1, prices), 1)
        self.assertEqual(cut_rod_bottom_up(2, prices), 5)
        self.assertEqual(cut_rod_bottom_up(3, prices), 8)
        self.assertEqual(cut_rod_bottom_up(4, prices), 10)
        self.assertEqual(cut_rod_bottom_up(5, prices), 13)
        self.assertEqual(cut_rod_bottom_up(6, prices), 17)
        self.assertEqual(cut_rod_bottom_up(7, prices), 18)
        """
        revenue = [0,1,5,8,9, 14, 17, 17 17+1 10+5 9 .. 18
        cut 1 2 3 4 5 6 7
        """



unittest.main()
