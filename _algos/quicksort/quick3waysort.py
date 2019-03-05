#!/usr/bin/python3
""" Quick 3 way sort """

def sort(a, lo=None, hi=None):
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(a) - 1
    if lo >= hi:
        return a
    p = a[lo]
    lt = lo - 1
    i = lo
    j = hi
    while i <= j:
        if a[i] < p:
            lt += 1
            a[lt], a[i] = a[i], a[lt]
            i += 1
        elif a[i] > p:
            j -= 1
            a[i], a[j] = a[j], a[i]
        else:
            i += 1
    # now invariant: a[lo..lt] < p and a[lt+1..i] == p and a[j..hi] > p
    sort(a, lo, lt)
    sort(a, j, hi)
    return a

if __name__ == '__main__':
    assert(sort([]) == [])
    assert(sort([2]) == [2])
    assert(sort([1, 2]) == [1, 2])
    assert(sort([1, 1]) == [1, 1])
    assert(sort([1,9,2,8,3,7,4,6,5, 2, 2, 7, 7]) == [1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9])
    print('tests pass')
