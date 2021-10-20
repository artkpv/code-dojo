'''
https://www.careercup.com/question?id=5715706939703296

Iterator over arrays. In asc order.


N elemen in each arr. M arrays.

I1. Points for each array and check next lowest in all at each step.
T: M * N * M 
S: M

I2. Heap with min elem. 
T: (N*M) * log (M) 
S: M
'''

from heapq import heappop, heappush
class MyIterator:
    def __init__(self, arrays):
        self.arrays = arrays
        self.mh = []
        for i, arr in enumerate(self.arrays):
            heappush(self.mh, (arr[0], 0, i))

    def next(self):
        if not self.hasNext():
            raise Exception()
        el, j, i = heappop(self.mh)
        if j + 1 < len(self.arrays[i]):
            heappush(self.mh, (self.arrays[i][j+1], j+1, i))
        return el

    def hasNext(self):
        return len(self.mh) > 0

def test(arrays, expected):
    mi = MyIterator(arrays)
    res = []
    while mi.hasNext():
        res += [mi.next()]
    print(f'test: {arrays} -> {res}')
    assert res == expected, f'{res} == {expected}'

test([[1], [2]], [1,2])
test([[2], [1]], [1,2])
test([[1,5,7], [2,3,10], [4,6,9]], [1,2,3,4,5,6,7,9,10])
test([[1,5,7], [2,3,10]], [1,2,3,5,7,10])



