#!/usr/bin/python3

import random


def qs3w(arr):
    """
    Quick 3 way sort

       0 1 2 3 4 5 6 7 8
    lt                 gt
       i               p

       0 1 2 3 4 5 6 7 8
         lt      gt    p
                 i
             eq
    a[lo..lt] < a[lt+1..i-1] < a[gt..hi-1]

    Time: O(n log n)
    T(n) = 2 * T(n/b) + f(n)
    """
    def sort(lo, hi):
        if hi <= lo:
            return
        p = arr[hi]
        lt = lo - 1
        gt = hi
        i = lo
        while i < gt:
            if arr[i] == p:
                i += 1
            elif arr[i] < p:
                lt += 1
                arr[lt], arr[i] = arr[i], arr[lt]
                i += 1
            else:  # arr[i] > p:
                gt -= 1
                arr[gt], arr[i] = arr[i], arr[gt]
        arr[gt], arr[hi] = arr[hi], arr[gt]
        gt += 1
        sort(lo, lt)
        sort(gt, hi)
    sort(0, len(arr)-1)
    return arr


def qs3w_old(a, lo=None, hi=None):
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
    qs3w_old(a, lo, lt)
    qs3w_old(a, j, hi)
    return a


if __name__ == '__main__':
    assert qs3w([]) == []
    assert qs3w([2]) == [2]
    assert qs3w([1, 2]) == [1, 2]
    assert qs3w([1, 1]) == [1, 1]
    assert qs3w([1,9,2,8,3,7,4,6,5, 2, 2, 7, 7]) == [1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 9]

    ran = random.Random()
    arr = [ran.randint(1, 20) for _ in range(100)]
    assert sorted(arr[:]) == qs3w(arr)
    print('tests pass')
