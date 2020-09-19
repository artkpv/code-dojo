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
count = 0
i = 0
for j in range(1, n):
    if s[i] == s[j]:
        count += 1
    else:
        i = j
print(count)


