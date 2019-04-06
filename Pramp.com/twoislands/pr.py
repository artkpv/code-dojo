#!python3
"""

I1. UF
Each el - union adj.
Time: ~N
Space: ~N

"""


class UnionFind:
    def __init__(self, N):
        self.components = N
        self.array = list(range(N))

    def find(self, a):
        if self.array[a] != a:
            self.array[a] = self.find(self.array[a])
        return self.array[a]

    def union(self, a, b):
        a_parent = self.find(a)
        b_parent = self.find(b)
        if a_parent == b_parent:
            return
        self.array[a_parent] = b_parent
        self.components -= 1
        print('union', a, b, a_parent, b_parent, ': ',
              ' '.join(str(i) for i in self.array))


def xy_to_num(x, y, cols):
    return x * cols + y


def adj(row, col, matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        x, y = row + i, col + j
        if 0 <= x < rows and 0 <= y < cols:
            if matrix[x][y] == 1:
                yield x, y


def get_number_of_islands(matrix):
    cols = len(matrix[0])
    uf = UnionFind(len(matrix) * len(matrix[0]))
    some_zero = None
    for row_i, row in enumerate(matrix):
        for cell_i, cell in enumerate(row):
            num = xy_to_num(row_i, cell_i, cols)
            if cell == 0:
                if some_zero is None:
                    some_zero = num
                else:
                    uf.union(some_zero, num)
            else:
                for x, y in adj(row_i, cell_i, matrix):
                    uf.union(num, xy_to_num(x, y, cols))
    return uf.components - (1 if some_zero is not None else 0)


if __name__ == '__main__':
    matrix = [[0,    1,    0,    1,    0],
              [0,    0,    1,    1,    1],
              [1,    0,    0,    1,    0],
              [0,    1,    1,    0,    0],
              [1,    0,    1,    0,    1]]
    print('running tests')
    assert get_number_of_islands(matrix) == 6

    print(get_number_of_islands(
         [[1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]))
    assert get_number_of_islands(
         [[1, 0, 1, 0], [0, 1, 1, 1], [0, 0, 1, 0]]) == 2
    print('all tests pass')
