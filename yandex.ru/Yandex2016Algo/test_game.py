from unittest import TestCase
from pr3_shashmati import Game,Position


class TestGame(TestCase):
    def test__add_moves(self):
        g = Game(Position((1,2), (3,8), False, None))
        self.assertEqual(g.winner(), "black")

    def test__next_moves(self):
        self.fail()

    def test_winner(self):
        self.fail()

    def test__winner(self):
        self.fail()

    def test_s(self):
        self.fail()
