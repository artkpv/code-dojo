#!python3
import unittest


def iter_multiply(A, B):
    return [
        [sum(el_a * el_b for el_a, el_b in zip(row_a, col_b))
         for col_b in zip(*B)] for row_a in A
    ]


def loop_multiply(A, B):
    assert len(A[0]) == len(B)
    C = []
    for i in range(len(A)):
        newrow = []
        for j in range(len(B[0])):
            newrow += [
                sum(
                    A[i][k] * B[k][j]
                    for k in range(min(len(A[0]), len(B)))
                )
            ]
        C += [newrow]
    return C


class Tests(unittest.TestCase):
    def test_simple(self):
        a = [[1, 2],
             [3, 4]]
        b = [[4, 3],
             [2, 1]]
        c = iter_multiply(a, b)
        expected = loop_multiply(a, b)
        self.assertEqual(c, expected)


if __name__ == '__main__':
    unittest.main()
