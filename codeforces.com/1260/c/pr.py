#!python3
"""
w1ld [dog] inbox dot ru


1 100 98
1 100 99


6 16
2
3 8

0 6 12    18 24 30    36 42 48
0      16          32       48

0 3 6   9
0     8

"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, gcd
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

for test in range(read_int()):
    r, b, k = read_int_array()
    r, b = (r, b) if r < b else (b, r)
    d = gcd(b, r)
    if d != 1:
        r //= d
        b //= d
    print('OBEY' if r == b or (b-2)//r+1 < k else 'REBEL')


