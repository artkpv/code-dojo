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
"""
a1 * a1

1 2
  3  2 3    4/a2 * a3 = 6    a2 = a3*4/6
  4  3 4
  5
2 3         a2*a3 = 6    a2=6/a3     a3*4/6 = 6/a3 >  a3^2 = 4   a3 = 2
  4
  5
3 4  5 4
  5


"""

n = read_int()
M = []
for i in range(n):
    M += [read_int_array()]
a2 = int((M[1][2]*M[0][1]/M[0][2])**.5)
a1 = int(M[0][1]/a2)
A = [a1, a2]
for i in range(2, n):
    A += [int(M[0][i]/a1)]
print(' '.join(str(i) for i in A))

