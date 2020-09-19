#!python3
"""
w1ld [dog] inbox dot ru
"""

from collections import deque, Counter
import heapq
import array
from itertools import combinations, permutations
from math import sqrt
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

for test in range(read_int()):
    arrnum = read_int()
    even = set(e for e in read_int_array() if e % 2 == 0)
    heap = list(-e for e in even)
    heapq.heapify(heap)
    count = 0
    while heap:
        x = -heapq.heappop(heap)
        even.remove(x)
        count += 1
        x //= 2
        if x % 2 == 0 and x not in even:
            even.add(x)
            heapq.heappush(heap, -x)
    print(count)



