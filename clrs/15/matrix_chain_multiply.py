#!python3

from matrix_chain_order import matrix_chain_order as mco
import unittest
from numpy import matrix, testing
from functools import reduce


def matrix_chain_multiply(matrices):
    if not matrices:
        return None
    dimensions = [len(matrices[0])]
    dimensions += [len(m[0]) for m in matrices]
    order_value, order = mco(dimensions)
    def multiply(lo, hi):
        if lo == hi:
            return matrices[lo-1]
        A = multiply(lo, order[lo][hi])
        B = multiply(order[lo][hi]+1, hi)
        A_rows, A_cols, B_rows, B_cols  = \
            len(A), len(A[0]), len(B), len(B[0])
        assert A_cols == B_rows

        def A_row(row):
            for e in A[row]:
                yield e

        def B_col(col):
            for i in range(B_rows):
                yield B[i][col]

        C = [[sum(a*b for a, b in zip(A_row(i), B_col(j)))
              for j in range(B_cols)]
            for i in range(A_rows)
        ]
        return C
    return multiply(1, len(matrices))


class Tests(unittest.TestCase):
    def test_4_matrices(self):
        matrices = [
            [[1,2,3,4],
             [4,5,6,7]],
            [[1,2],
             [2,3],
             [3,4],
             [4,5]],
            [[100,100,100],
             [50,50,50]],
            [[2,2,2],
             [3,3,3],
             [1,1,1]]
        ]
        expected = reduce(
                lambda x, y: matrix(x) * matrix(y),
                matrices)
        print(expected)
        actual = matrix_chain_multiply(matrices)
        print(actual)

        testing.assert_array_equal(expected, actual)


if __name__ == '__main__':
    unittest.main()
