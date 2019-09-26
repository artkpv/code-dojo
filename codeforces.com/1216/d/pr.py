#!python3

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, gcd
import unittest
from fractions import Fraction


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

"""
3 12 6
5 3
y z


13 52 0 13 26 52
12 13

39 0 52 39


a_i
n

max(a_i) - a_i = b_i 
gcd(b_i) = z1


"""

n = read_int()
a = read_int_array()
a.sort(reverse=True)
if a[0] == 0:
    print("0 0")
    exit()
if a[1] == 0:
    print(1, a[1]*(n-1))
    exit()
x = a[0]*a[1]//gcd(a[0], a[1])
for e in a[2:]:
    d =
    x = x*e//gcd(x,e)
y = 0
z = 0
for e in a:
    d = x - e





