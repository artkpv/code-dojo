def sort(a):
    mergesort(a, [None] * len(a), 0, len(a) - 1)
    return a

def merge(a, aux, lo, m, hi):
    # combine, by copying to aux array and then back
    i = lo
    j = m+1
    for k in range(lo, hi + 1):
        if j > hi or (i <= m and a[i] <= a[j]):
            aux[k] = a[i]
            i += 1
        else:
            aux[k] = a[j]
            j += 1
    for i in range(lo, hi + 1):
        a[i] = aux[i]

def mergesort(a, aux, lo, hi):
    """
    Divide by middle. Sort recursively two parts.
    Combine results in ~n. Time all is ~n*log(n).
    """
    if lo >= hi: return
    m = (lo + hi)//2
    mergesort(a, aux, lo, m)
    mergesort(a, aux, m+1, hi)
    merge(a, aux, lo, m, hi)


def mergesort_iter(a):
    """
    Merge intervals starting with 2 till size < n.
    """
    n = len(a)
    aux = [None] * n
    size = 1
    while size < n:
        i = 0
        while i + size <= n:
            hi = i + 2*size - 1
            merge(a, aux, i, i + size - 1, min(hi, len(a)-1) )
            i += 2*size
        size *= 2
    return a

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self,other):
        return self.key <= other.key
    def __repr__(self):
        return "(%d,%d)" % (self.key, self.value)

if __name__ == '__main__':
    assert(sort([1]) == [1])
    assert(sort([9,1,8,2,7,3,6,4,5]) == [1,2,3,4,5,6,7,8,9])
    assert(mergesort_iter([9,1,8,2,7,3,6,4,5]) == [1,2,3,4,5,6,7,8,9])

    # test stable:
    a = [Node(i%4, i) for i in range(25, -1, -1)]
    mergesort_iter(a)
    assert all(i < 1 or a[i-1] <= e for i,e in enumerate(a))
    assert all(
        i < 1 or a[i-1].key != e.key or
        (a[i-1].key == e.key and a[i-1].value > e.value)
        for i,e in enumerate(a)), 'Not stable: %s' % repr(a)

    print('all tests pass')


