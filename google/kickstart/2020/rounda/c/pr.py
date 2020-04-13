#!python3

"""

10 20

10 12 14 16 18 20

10 15 20
10 12 15 17 20
10 12 13 15 17 20
10 12 13 15 17 18 20
10 11 12 



b1 b2 b3 b4

6
10 6 4
2 2 2 2 2  6 4 


5 5    1
2 3 2 3    3
1 1 1 2 1 1 1 2     7
      1 1     1 1     9 

10 
2 2 2 2 2   4
1 1 ..       9 


f(b,



"""
from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, ceil
import unittest
import heapq


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

tests = read_int()

for test in range(tests):
    N, K = read_int_array()
    arr = read_int_array()
    arr.sort()
    if N == 1:
        print(0)
        break
    D = []
    hi = 1
    for i in range(N-1):
        d = arr[i+1] - arr[i]
        if d > 1:
            D.append(d)
            hi = max(hi, d)

    lo = 1
    while lo < hi:
        mid = (lo + hi) // 2
        k = 0
        for d in D:
            k += ceil(d / mid) - 1
        if k <= K:
            hi = mid
        else:
            lo = mid + 1

    print("Case #{}: {}".format(test+1, lo))


"""
2
10 13 15 16 17

3 2 

lo hi mid
1 3 3
3 3 


"""
