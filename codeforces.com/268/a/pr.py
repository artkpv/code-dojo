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
teams = []
for i in range(n):
    teams += [read_int_array()]

count = 0
for i, t1 in enumerate(teams):
    for j, t2 in enumerate(teams):
        if i == j:
            continue
        if t1[0] == t2[1]:
            count += 1
print(count)

