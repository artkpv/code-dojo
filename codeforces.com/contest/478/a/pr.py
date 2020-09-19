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

a = read_int_array()
n = sum(a)
print(n//5 if n != 0 and n%5 == 0 else -1)

