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

n, m = read_int_array()
cs = set(('C', 'M', 'Y'))
for _ in range(n):
    if cs & set(input().strip().split(' ')):
        print('#Color')
        exit()
print('#Black&White')

