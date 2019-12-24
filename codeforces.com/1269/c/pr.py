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

numL, k = read_int_array()
num = input().strip()

found = True
i = 0
while i < k and found:
    j = i
    while j + k < numL and found:
        if num[j] != num[j+k]:
            found = False
        j += k
    i += 1

if found:
    print(numL)
    print(num)
else:
    nineInx = 0
    while nineInx < k and num[nineInx] != '9':
        nineInx += 1
    print(numL)
    i = 0
    while i < numL:
        if i%k + 1 < nineInx:
            print(num[i%k], end='')
        elif i%k + 1 == nineInx:
            print((ord(num[i%k]) - ord('0')) + 1, end='')
        else:
            print(0)
        i += 1



