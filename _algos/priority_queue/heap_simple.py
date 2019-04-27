#!python3


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


"""
3
1 1
1 2
1 3
2 1
3
> 2


Array:
- 1
- 1 2
- 1 2 3
- 3 2 , - 2 3

"""

if __name__ == '__main__':
    h = Heap()
    h.add(1)
    assert h.get_min() == 1
    h.add(2)
    h.add(3)
    h.delete(1)
    assert h.get_min() == 2
    h.delete(2)
    assert h.get_min() == 3
    h.delete(3)
    assert h.get_min() is None

    h.add(1)
    h.add(2)
    h.add(3)
    h.add(4)
    h.add(5)
    h.change(1, 6)
    print(h)
    assert h.get_min() == 2
    h.change(5, 1)
    assert h.get_min() == 1

    print('tests pass')
