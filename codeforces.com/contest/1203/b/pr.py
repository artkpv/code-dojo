#!python3

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
    a = read_int_array()
    a.sort()
    def allgood():
        if a[0] != a[1] or a[-2] != a[-1]:
            return False
        s = a[0]*a[-1]
        for i in range(1, n):
            if a[i*2] != a[i*2+1] or a[-i*2-1] != a[-i*2-2]:
                return False
            if a[i*2] * a[-i*2-1] != s:
                return False
        return True
    print('YES' if allgood() else 'NO')



