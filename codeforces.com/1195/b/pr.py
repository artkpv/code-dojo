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

n, k = read_int_array()

"""

m eaten
m turns when eats
n - m  turns when increases

k = 1 + 2 + 3 + 4 + .. + ? - m

(n-m) * (n-m+1) / 2  = (n^2 -nm + n -nm + m^2 - m) /2

2k = n^2 + m^2 - 2nm + n - m - 2m
2k = n^2 + m^2 - 2nm + n - 3m
2k = m^2 - 2nm - 3m + n + n^2
0 = m^2 - 2nm - 3m + n + n^2 - 2k
0 = m^2 + m(-2n - 3) + (n + n^2 - 2k)
               b               c

m1,2 = (-b +- sqrt(b^2 - 4c)) / 2

"""

b = -2*n - 3
c = n  + n**2 - 2*k
d = b**2 - 4*c
sqrt_d = sqrt(d)
m1 = (-b + sqrt_d)/2
m2 = (-b - sqrt_d)/2

# print(b, c, d, m1, m2)
ans = m1 if 0 <= m1 <= n else m2
assert 0 <= ans <= n
print(int(ans))

