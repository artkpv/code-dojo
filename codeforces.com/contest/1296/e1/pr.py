#!python3
"""
Author: w1ld [at] inbox [dot] ru
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

n = read_int()
s = input().strip()
s1 = [s[0]]
s2 = []
for c in s[1:]:
    if s1[-1] <= c:
        s1.append(c)
    elif not s2 or s2[-1] <= c:
        s2.append(c)
    else:
        break

if len(s1) + len(s2) == len(s):
    i = 0
    j = 0
    out = []
    for c in s:
        if i < len(s1) and c == s1[i]:
            out.append('0')
            i += 1
        else:
            out.append('1')
            j += 1
    print("YES")
    print(''.join(out))
else:
    print('NO')

            


