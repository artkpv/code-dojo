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
from math import sqrt
import unittest
import heapq


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

tests = read_int()

for test in range(tests):
    n, k = read_int_array()
    arr = read_int_array()
    arr.sort()
    if n == 1:
        print(0)
        break
    D = []
    for i in range(n-1):
        d = arr[i+1] - arr[i]
        if d > 1:
            heapq.heappush(D, -d)

    while k > 0 and D:
        d = -heapq.heappop(D)
        dd = d // 2
        if dd > 1:
            heapq.heappush(D, -dd)
        if d % 2 == 1:
            heapq.heappush(D, -(dd + 1))
        elif dd > 1:
            heapq.heappush(D, -dd)
        k -= 1

    max_ = -heapq.heappop(D) if D else 1
    print("Case #{}: {}".format(test+1, max_))


