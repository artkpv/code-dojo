
import unittest


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

    def test_2(self):
        prices = [5, 10, 10, 10, 45, 45, 45, 45, 45, 100]
        self.assertEqual(cut_rod_bottom_up(10, prices), )



unittest.main()
