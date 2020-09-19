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
if n < 1:
    exit()
print('I hate ', end='')
for i in range(1, n):
    print('that I hate ' if i % 2 == 0 else 'that I love ', end='')
print('it', end='')
