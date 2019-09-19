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

n = read_int()
s = input().strip()
c = Counter(s)
while c['n'] > 0:
    print('1', end=' ')
    c['n'] -= 1
while c['z'] > 0:
    print('0', end=' ')
    c['z'] -= 1




