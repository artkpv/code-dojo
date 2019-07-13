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

a, b = read_int_array()
step = 1
while a >= 0 and b >= 0:
    if step % 2 == 1:
        a -= step
    else:
        b -= step
    step += 1
print('Vladik' if a < 0 else 'Valera')



