#!python3
"""
w1ld [dog] inbox dot ru

b1 b2 b3 b4

2 9
4 12
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, gcd
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

r, c = read_int_array()

if r == c == 1:
    print(0)
    exit()

if r == 1:
    print(' '.join(str(e) for e in range(2, c+2)))
    exit()

if c == 1:
    print('\n'.join(str(e) for e in range(2, r+2)))
    exit()


B = [1]
while len(B) <= r:
    bi = B[-1] + 1
    while True:
        if all(gcd(e, bi) == 1 for e in B):
            break
        bi += 1
    B += [bi]

bi = next(e for e in range(1, B[-1] + 2) if e - 1 >= len(B) or B[e-1] != e)
B += [bi]

while len(B) <= r+c:
    bi = B[-1] + 1
    while True:
        if all(gcd(e, bi) == 1 for e in B[r:]) and bi not in B[:r]:
            break
        bi += 1
    B += [bi]

M = [[1] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        M[i][j] *= B[i]

for j in range(c):
    for i in range(r):
        M[i][j] *= B[r+j]

print('\n'.join(' '.join(str(e) for e in M[i]) for i in range(r)))



