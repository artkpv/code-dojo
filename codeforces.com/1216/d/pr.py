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
x
y

a1 a2 ...

b1 b2 b3

sum(b_i) / z  = y
b1 / z = y1
b2 / z = y2
...
min y?


3 12 6
5 3
y z


13 52 0 13 26 52
12 13

52 52 26 13 13 0
0 0 26 39 39 52
13 12


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
g = a[0] - a[1]
for i in range(2, n):
    g = gcd(g, a[0] - a[i])
x = a[0]
y = sum((a[0] - a[i])//g for i in range(1, n))
print( y, g)






