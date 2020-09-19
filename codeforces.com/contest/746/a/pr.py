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

a = read_int()
b = read_int()
c = read_int()

x = min(a, b//2, c//4)
print(x + x*2 + x*4)
