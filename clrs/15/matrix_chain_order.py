#!python3
import unittest
import pdb

def matrix_chain_order(dimensions):
    """
    dimensions : [p0,p1,..,p_n]
        n matrcies, with
        p0xp1 for 1st matrix
        p1xp2 for 2nd matrix and so on
    Returns:
    value of solution,
    s - solution in form (1,(2,3))
    """
    n = len(dimensions)-1  # Number of matrices.
    # Memoization for solutions, ie. an item is
    # an optimal solution to multiply matrices in i..j range:
    m = [[float('inf')] * (n+1) for _ in range(n+1)]
    # Solution, s[i][j] - k-th matrix to choose to paranthesize.
    s = [[None] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        m[i][i] = 0  # No multiplications for one.
    # Compute in bottom-up way:
    d = dimensions
    for length in range(2, n+1):
        for i in range(1, n-length+2):
            j = i + length - 1
            for k in range(i, j):
                m_i_j = (
                    m[i][k] + m[k+1][j] + (d[i-1] * d[k] * d[j])
                )
                if m_i_j < m[i][j]:
                    m[i][j] = m_i_j
                    s[i][j] = k
    return m[1][n], s


def print_solution(solution):
    solution = []
    def build_solution(i, j):
        if i == j:
            solution.append(str(i))
            return
        solution.append('(')
        build_solution(i, s[i][j])
        solution.append('*')
        build_solution(s[i][j]+1, j)
        solution.append(')')
    build_solution(1, n)
    return ''.join(solution)


class Tests(unittest.TestCase):
    def test_simple(self):
        dimensions = [30, 35, 15, 5, 10, 20, 25]
        value, solution = matrix_chain_order(dimensions)
        print('test_simple', dimensions, value, solution)
        self.assertEqual(value, 15_125)
        self.assertEqual(print_solution(solution), '((1*(2*3))*((4*5)*6))')

    def test_15_2_1_exercies(self):
        dimensions = [5, 10, 3, 12, 5, 50, 6]
        value, solution = matrix_chain_order(dimensions)
        print('test_15.2-1', dimensions, value, solution)
        self.assertEqual(value, 2010)
        self.assertEqual(print_solution(solution), '((1*2)*((3*4)*(5*6)))')


if __name__ == '__main__':
    unittest.main()
