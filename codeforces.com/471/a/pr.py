#!python3
"""
Author: w1ld [dog] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

a = read_int_array()

counter = [0] * 10
for e in a:
    counter[e] += 1

legs = 0
a = 0
b = 0
for i in range(1, 10):
    if counter[i] >= 4:
        legs = i
        counter[i] -= 4

    if counter[i] > 0 and a == 0:
        a = i
        counter[i] -= 1

    if counter[i] > 0:
        b = i
        counter[i] -= 1

if legs == 0:
    print('Alien')
else:
    print('Bear' if a != b else 'Elephant')
    

