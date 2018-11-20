"""
https://contest.yandex.ru/hiring/contest/5187/problems/

3 x 2:
0 1
2 3
4 5

2 x 3. (2 1) : 3*(2-1) + 1 - 1
0 1 2
3 4 5


(r, c)
(2, 1) : field[r*rows + c - 1]

5 5
9
2 2
2 3
2 4
3 4
4 4
4 3
4 2
3 2
1 2

  1 2 3 4 5
1   x
2   x x x
3   x   x
4   x x x
5

"""

class UnionFind:
    """
    Weighted quick-union with path compression and connected components.
    """

    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n
        self.cc = n  # connected components

    def _root(self, i):
        j = i
        while (j != self._id[j]):
            self._id[j] = self._id[self._id[j]]
            j = self._id[j]
        return j

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        if (self._sz[i] < self._sz[j]):
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        self.cc -= 1

rows, cols = (int(i) for i in input().strip().split(' '))
k = int(input().strip())
if k == rows*cols:
    for i in range(k):  # read input and only then print
        input()
    print(0)
    exit()
elif k == 0:
    print(1)
    exit()

def get_inx(rc):
    global cols
    return cols*(rc[0] - 1) + rc[1] - 1

uf = UnionFind(rows * cols)  # 3 3
last_mine_inx = None
for i in range(k):
    m_i = get_inx([int(j) for j in input().strip().split(' ')])
    if i > 0:
        uf.union(m_i, last_mine_inx)
    last_mine_inx = m_i

def union_free(x_i, y_i):  # row,col; not index
    global last_mine_inx
    if not uf.find(y_i, last_mine_inx):
        uf.union(x_i, y_i)

for r in range(1, rows + 1):
    for c in range(1, cols + 1):
        x_i = get_inx((r, c))
        if not uf.find(x_i, last_mine_inx):
            if r + 1 <= rows: # down
                union_free(x_i, get_inx((r + 1, c)))
            if c + 1 <= cols: # right
                union_free(x_i, get_inx((r, c + 1)))

print(uf.cc - 1)


