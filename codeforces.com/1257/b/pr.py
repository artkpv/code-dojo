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

for t in range(read_int()):
    x, y = read_int_array()
    if x == 1:
        print("YES" if y == 1 else "NO")
    elif x == 2 or x == 3:
        print("YES" if y <= 3 else "NO")
    else:
        print("YES")


