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

s = input().strip()
uc = sum(1 for c in s if c.isupper())
print(s.upper() if uc > len(s) - uc else s.lower())

