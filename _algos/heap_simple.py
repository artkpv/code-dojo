#!python3


class Heap(object):
    """
    Min heap.
    Invariant: top element is the min. For any child >= their parent.
    """
    def __init__(self):
        self._array = [None]  # 1 based

    def add(self, el):
        self._array += [el]
        self._siftup(len(self._array)-1)

    def delete(self, el):
        a = self._array
        i = a.index(el)  # raises ValueError
        a[i], a[-1] = a[-1], a[i]
        del a[-1]
        self._siftdown(i)

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
            i = j

    def _siftdown(self, i):
        a = self._array
        while i * 2 < len(a):
            k = i*2
            if k+1 < len(a) and a[k+1] < a[k]:
                k += 1
            if a[k] >= a[i]:
                break
            a[k], a[i] = a[i], a[k]
            i = k


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


heap = Heap()
for _ in range(int(input('').strip())):
    op_arg = input('').strip().split(' ')
    if op_arg[0] == '1':
        el = int(op_arg[1])
        heap.add(el)
    elif op_arg[0] == '2':
        el = int(op_arg[1])
        heap.delete(el)
    elif op_arg[0] == '3':
        print(heap.get_min())


