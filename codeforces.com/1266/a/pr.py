#!python3
"""
w1ld [dog] inbox dot ru
"""

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

for test in range(read_int()):
    nStr = input().strip()

    sum_ = 0
    has_zero = False
    has_even = False
    for i, e in enumerate(nStr):
        sum_ += int(e)
        if not has_zero and e == '0':
            has_zero = True
        elif int(e) % 2 == 0:
            has_even = True
        
    print('red' if has_zero and has_even and sum_ % 3 == 0 else 'cyan')



