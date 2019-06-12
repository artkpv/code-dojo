#!python3
"""
Next: Реализуй проверку на существование единичного решения и бесконечного множества решений.

"""
import unittest
from fractions import Fraction, gcd


def gauss_solve(original_matrix):
    n, m = len(original_matrix), len(original_matrix[0]) - 1
    # todo checks
    A = original_matrix.copy()

    def decrease_down():
        def decrease_equation(a, b):
            quotient = Fraction(A[b][a], A[a][a])
            for i in range(m+1):
                A[b][i] = (
                    Fraction(A[b][i])
                    - quotient * Fraction(A[a][i])
                )
            assert A[b][a] == 0

        for a in range(n-1):
            for b in range(a+1, n):
                decrease_equation(a, b)

    def calculate_up():
        for row in range(n-1, -1, -1):
            assert all(A[row][i] == 0 for i in range(row))
            assert all(
                    result[i] is not None
                    for i in range(row+1, m)
            )
            for i in range(row+1, m):
                x = A[row][i] * result[i]
                A[row][-1] -= x
                A[row][i] = 0
            result[row] = A[row][-1]/A[row][row]
        for i, e in enumerate(result):
            result[i] = float(e)

    decrease_down()
    result = [None] * m
    calculate_up()
    return result




class Tests(unittest.TestCase):
    def test_1(self):
        A = [[4, 2, 1, 1],
             [7, 8, 9, 1],
             [9, 1, 3, 2]]
        result = gauss_solve(A)
        expected = (
            0.2608695652173913,
            0.04347826086956526,
            -0.1304347826086957
        )
        self.assertEqual(len(result), len(expected))
        for i, result_e in enumerate(result):
            self.assertAlmostEqual(result_e, expected[i])


if __name__ == '__main__':
    n, m = [int(i) for i in input().strip().split(' ')]
    A = [
        [int(i) for i in input().strip().split(' ')]
        for _ in range(n)
    ]

    result = gauss_solve(A)
    if result is None:
        print('NO')
    elif result == float('inf'):
        print('INF')
    elif result:
        print('YES')
        print(' '.join(str(i) for i in result))

# py -m unittest 2.1_7_gauss_slau
