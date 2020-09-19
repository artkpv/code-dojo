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
10 2
10 1 2 3 4... 10
5  2 4 6 8 10
6  2 4 6 8 9 10  

2*k + p = n
(k + p) / m = q, int
k+p - min
q*m = k+p


n/2 = k1
k1%m = q1
if q1 == 0 : return
p1 = k1-q1
(n-p1)/2 = k2
(p1+k2)%m != 0

p = (n//2) % m
k = (n-p)/2

10 2
10//2 = 5
5%2 = 1
10 - (5-1)*2 = 2
4 + 2 = 6


435 9
435//2 = 217
217%9 = 1
435 - (217-1)*2 = 3
216+3  = 219 steps
216*2 + 3 = 432+3 = 

"""

n, m = read_int_array()
if m > n:
    print(-1)
else:
    k = n//2
    p = n-
    


