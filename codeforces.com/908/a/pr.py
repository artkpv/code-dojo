#!python3

from collections import deque, Counter
from itertools import combinations, permutations
from math import sqrt
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

s = input().strip()
vowels = 'aeiou'
evens = '02468'
print(sum(1 if (c in vowels or (c in '0123456789' and c not in evens) ) else 0 for c in s))

