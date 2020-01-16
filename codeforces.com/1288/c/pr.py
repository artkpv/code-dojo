#!python3
"""
Author: w1ld [dog] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, factorial
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

n, m = read_int_array()

print( int(factorial(n + 2*m - 1) // (factorial(2*m) * factorial(n-1)) % (10**9 + 7)))

