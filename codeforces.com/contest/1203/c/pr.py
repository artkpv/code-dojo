#!python3

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, gcd, floor
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################


n = read_int()
a = read_int_array()

N = a[0]
for e in a[1:]:
    N = gcd(N, e)

if N == 1:
    print(1)
    exit()


divisors = 2
for x in range(2 if N % 2 == 0 else 3, int(N**.5)+1, 1 if N % 2 == 0 else 2 ):
    if N % x == 0:
        divisors += 2
if N**.5 % 1 == 0:
    divisors -= 1
print(divisors)

