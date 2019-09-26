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

a, b = read_int_array()
print(min(a, b), (a+b - 2*min(a,b)) // 2)

