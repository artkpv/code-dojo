

def QS(a):
    if not a:
        return a
    def partition(lo, hi):
        if lo >= hi:
            return hi
        if hi - lo == 1:
            a[lo], a[hi] = min((a[lo], a[hi])), max((a[lo], a[hi]))
            return hi
        l = lo - 1
        r = hi
        i = lo
        p = a[hi]
        while i < r:
            if a[i] <= p:
                i += 1
                l += 1
            else:
                a[i], a[r-1] = a[r-1], a[i]
                r -= 1
        a[r], a[hi] = a[hi], a[r]
        return r
    def sort_(lo, hi):
        if hi <= lo:
            return
        m = partition(lo, hi)
        sort_(lo, m-1)
        sort_(m+1, hi)
    sort_(0, len(a) - 1)
    return a

def myassert(a):
    b = QS(a.copy())
    assert(sorted(a.copy()) == b)

myassert([])
myassert([1])
myassert([1,2])
myassert([2,1])
myassert([2,3,1])
myassert([4,2,3,1])
myassert([4,10,10,11,11,2,3,1])
print('WORKS')
