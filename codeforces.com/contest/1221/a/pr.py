#!python3

from bisect import bisect_left, insort_left
from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

for _ in range(read_int()):
    n = read_int()
    a = list(sorted(read_int_array()))
    bi = bisect_left(a, 2048)
    found = 0 <= bi < n and a[bi] == 2048
    while not found and len(a) > 1:
        n = len(a)
        i = 1
        while i < n:
            if a[i] == a[i-1]:
                break
            i += 1
        if i == n:
            break
        x = a[i] + a[i-1]
        if x == 2048:
            found = True
            break
        del a[i-1]
        del a[i-1]
        insort_left(a, x)
    print("YES" if found else "NO")


