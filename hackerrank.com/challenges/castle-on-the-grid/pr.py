#!python3
"""
Grid: n*n
1 <= n <= 100
Castle: along x or y till end or blocked.

Find min moves.


Idea 1
Graph. Run shortest paths algo (Dijkstra's)
How many edges? n*n field. Edges: O(N^4) Vertices: O(N^2)

Time: O(V*log(V) + E*Log(V)) == O(N^4*log(N^2)) = O(N^4*log(N)) ~= 10^8*7
Space: V + V + V

"""


class Heap(object):
    """
    Min heap.
    Invariant: top element is the min. For any child >= their parent.
    """
    def __init__(self):
        self._array = [None]  # 1 based
        self._indeces = {}  # item to its heap index

    def add(self, el):
        """
        Adds to min-heap and returns index of new element in the heap.
        """
        assert el not in self._indeces, 'elements should be unique'
        self._array += [el]
        i = len(self._array)-1
        self._indeces[el] = i
        self._siftup(i)

    def delete(self, el):
        if el not in self._indeces:
            raise ValueError
        i = self._indeces[el]
        a = self._array
        if i != len(a) - 1:
            a[i], a[-1] = a[-1], a[i]
            self._indeces[a[i]] = i
            del a[-1]
            self._siftdown(i)
        else:
            del a[-1]
        del self._indeces[el]

    def change(self, old, new):
        assert old in self._indeces
        assert new not in self._indeces
        i = self._indeces[old]
        del self._indeces[old]
        self._indeces[new] = i
        self._array[i] = new
        if old < new:
            self._siftdown(i)
        elif old > new:
            self._siftup(i)

    def get_min(self):
        if len(self._array) == 1:
            return None
        return self._array[1]

    def _siftup(self, i):
        a = self._array
        while True:
            j = i // 2  # parent
            if j == 0 or a[j] <= a[i]:
                break
            a[j], a[i] = a[i], a[j]
            self._indeces[a[j]] = j
            self._indeces[a[i]] = i
            i = j
        return i

    def _siftdown(self, i):
        a = self._array
        while i * 2 < len(a):
            k = i*2
            if k+1 < len(a) and a[k+1] < a[k]:
                k += 1
            if a[k] >= a[i]:
                break
            a[k], a[i] = a[i], a[k]
            self._indeces[a[k]] = k
            self._indeces[a[i]] = i
            i = k

    def __str__(self):
        return str(self._array) + ' ' + str(self._indeces)


def adj(field, starty, startx):
    """
    Returns connected from y, x cells: (y, x, moves)
    """
    size = len(field)
    if field[starty][startx] == 'X':
        return
    for to_y, to_x in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        moves = 1
        while True:
            y, x = starty + to_y*moves, startx + to_x*moves
            in_field = 0 <= y < size and 0 <= x < size
            if (not in_field or field[y][x] == 'X'):
                break
            yield (y, x, 1)  # castle flies over cells
            moves += 1


MAX = 100
INF = 999_999
n = int(input('').strip())
field = []
for row in range(n):
    field += [input('').strip()]
starty, startx, endy, endx = [int(i) for i in input('').strip().split(' ')]

assert field[endy][endx] != 'X'

queue = Heap()
edgeto = {}
distto = {}
for y, row in enumerate(field):
    for x, value in enumerate(row):
        queue.add((INF, y, x))
        edgeto[(y, x)] = None
        distto[(y, x)] = INF
queue.change((INF, starty, startx), (0, starty, startx))
distto[(starty, startx)] = 0

while queue.get_min():
    v = queue.get_min()
    moves, y, x = v
    queue.delete(v)
    for y2, x2, moves in adj(field, y, x):
        old = distto[(y2, x2)]
        new = distto[(y, x)] + moves
        if old > new:
            queue.change((old, y2, x2), (new, y2, x2))
            distto[(y2, x2)] = new
            edgeto[(y2, x2)] = (y, x)
print(distto[(endy, endx)])
