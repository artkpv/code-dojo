

class RobotTests(unittest.TestCase):

    def test_2x2(self):
        r = Robot(2)
        self.assertEqual(r.draw(), """[ ][ ]
[ ][N]""")
        r.move("DF")
        self.assertEqual(r.draw(), """[ ][N]
[ ][ ]""")
        r.move("TR")
        self.assertEqual(r.draw(), """[ ][E]
[ ][ ]""")
        r.move("DB")
        self.assertEqual(r.draw(), """[E][ ]
[ ][ ]""")
        r.move("TL")
        self.assertEqual(r.draw(), """[N][ ]
[ ][ ]""")
        r.move("DB")
        self.assertEqual(r.draw(), """[ ][ ]
[N][ ]""")

    def test_3x3(self):
        r = Robot(3)
        self.assertEqual(r.draw(), """[ ][ ][ ]
[ ][ ][ ]
[ ][ ][N]""")

        r.move("DF", 1)
        self.assertEqual(r.draw(), """[ ][ ][ ]
[ ][ ][N]
[ ][ ][ ]""")

        r.move("TL")
        self.assertEqual(r.draw(), """[ ][ ][ ]
[ ][ ][W]
[ ][ ][ ]""")

        r.move("DF", 2)
        self.assertEqual(r.draw(), """[ ][ ][ ]
[W][ ][ ]
[ ][ ][ ]""")
