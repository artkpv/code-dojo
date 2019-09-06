#!/bin/python3

def sort(a):
    a = [None] + a
    n = len(a)-1
    def sift_down(i):
        while 2*i <= n:
            k = 2*i
            if k + 1 <= n and a[k+1] > a[k]:
                k += 1
            if a[k] <= a[i]:
                break
            a[i], a[k] = a[k], a[i]
            i = k

    # Heapify
    for i in range(n//2, 0, -1):
        sift_down(i)

    # Sort
    for _ in range(n):
        a[1], a[n] = a[n], a[1]
        n -= 1
        sift_down(1)
    a = a[1:]
    return a



assert(sort([2,3,1]) == [1,2,3])
assert(sort([1]) == [1])
assert(sort([1,9,2,8,3,7,4,6,5]) == [1,2,3,4,5,6,7,8,9])
assert(sort([4, 4, 3, 2, 3, 2, 1, 1]) == [1, 1, 2, 2, 3, 3, 4, 4])
