from random import randrange as rand

def qs(a):
    return _qs(a, 0, len(a)-1)

def _qs(a, lo, hi):
    if lo < hi:  # > 1 elements
        mid = partition(a, lo, hi)
        _qs(a, lo, mid-1)
        _qs(a, mid+1, hi)
        print(' '.join(str(i) for i in a[lo:hi+1]))

def exch(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def partition(a, lo, hi):
    """
    x|    <x    |  =x  |    >x   |  ?  |
                      i           j
    """
    k = rand(lo, hi, 1)
    x = a[k]
    exch(a, lo, k)
    i = lo
    j = lo+1
    while j <= hi:
        if a[j] <= x:
            i += 1
            exch(a, i, j)
        # else a[j] > x: move on
        j += 1
    exch(a, i, lo)
    return i


n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
qs(a)
#print(' '.join(str(i) for i in a))

