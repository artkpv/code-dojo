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
s = [c for c in input().strip()]

count = 0
for i in range(1, n):
    if i % 2 == 1:
        if s[i] == s[i-1]:
            count += 1
            s[i] = 'a' if s[i] == 'b' else 'b'
print(count)
print(''.join(s))

