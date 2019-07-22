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

a, b, c, d = read_int_array()

misha = max(3*a/10, a - a//250 * c)
vasya = max(3*b/10, b - b//250 * d)

print('Misha' if misha > vasya else ('Vasya' if vasya > misha else 'Tie'))

