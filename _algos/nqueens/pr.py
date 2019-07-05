#!python3

import unittest
# import pdb; pdb.set_trace()

def solveNQueens(n):
    # Queens rows. For i-th col a queen on qrows[i]-th row.
    qrows = [0] * n
    def solutions(m):
        """
        Generates solutions by getting next position
        for m-th queen on n*n field.
        m - column of a m-th queen.
        """
        for qrow in range(n):
            is_hit = any(
                row == qrow or abs(qrow - row) == abs(m - col)
                for col, row in enumerate(qrows[:m])
            )
            if is_hit:
                continue
            qrows[m] = qrow
            if m + 1 == n:
                yield qrows
            else:
                for s in solutions(m+1):
                    yield s

    boards = []
    for s in solutions(0):
        # To string:
        boards += [
            '\n'.join(''.join(
                'Q' if s[col] == row else '.' for col in range(n))
            for row in range(n))
        ]
    return boards


class Test(unittest.TestCase):
    def test_3queens(self):
        boards = solveNQueens(3)
        self.assertEqual(boards, [])

    def test_4queens(self):
        expected = [
"""..Q.
Q...
...Q
.Q..""",
""".Q..
...Q
Q...
..Q."""]
        boards = solveNQueens(4)
        for i, b in enumerate(boards):
            print()
            print(i+1)
            print(b)
        self.assertEqual(boards, expected)

    def test_8queens(self):
        expected = [
"""..Q.
Q...
...Q
.Q..""",
""".Q..
...Q
Q...
..Q."""]
        boards = solveNQueens(8)
        for i, b in enumerate(boards):
            print()
            print(i+1)
            print(b)
        self.assertEqual(boards, expected)


unittest.main()
