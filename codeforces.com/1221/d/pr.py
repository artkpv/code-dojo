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
    A = [read_int_array() for __ in range(n)]
    if n == 1:
        print(0)
        continue
    # TODO
    def f(i, cost, j):
        if i == 0:
            return cost
        j = i
        while 0 < j < n:
            a = A[j-1]
            b = A[j]
            if a[0] == b[0]:
                # 1:
                cost += b[1]
                b[0] += 1
                # 2:
                cost += a[1]
                a[0] += 1
                j -= 1

            else:
                j += 1


    cost = f(1, 0)







