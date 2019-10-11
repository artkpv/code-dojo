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

for query in range(read_int()):
    n, r = read_int_array()
    a = read_int_array()
    a.sort()
    i = n - 1
    count = 0
    while 0 <= i and 0 < a[i] - (r * count):
        count += 1
        i -= 1
        while 0 <= i and a[i] == a[i+1]:
            i -= 1
    print(count)

