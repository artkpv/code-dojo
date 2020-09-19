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

n= read_int()
array = read_int_array()
d = deque(array)
a = 0
b = 0
turn = True
while d:
    x = max(d[0], d[-1])
    if turn:
        a += x
    else:
        b += x
    turn = not turn
    if d[0] > d[-1]:
        d.popleft()
    else:
        d.pop()
print(a, b)


