#!/bin/python

import random

def shsort(arr):
    n = len(arr)
    gap = 1  # 1 4 13 40 121 .. ; 121 40 13 4 1 0
    while 3 * gap + 1 < n:
        gap = 3 * gap + 1

    while gap >= 1:
        for i in range(gap):
            j = i + gap
            while j < n:
                k = j
                while k - gap >= 0 and arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                    k -= gap
                j += gap
        gap //= 3
    return arr


assert shsort([9, 1, 8, 2, 7, 3, 6, 4, 5]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

ran = random.Random()
test2 = []
for i in range(1000):
    test2.append(ran.randint(1, 1000))
sortedTest2 = list(sorted([e for e in test2]))
assert shsort(test2) == sortedTest2

print('done')
