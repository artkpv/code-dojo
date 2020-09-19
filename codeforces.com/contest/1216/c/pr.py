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

W = read_int_array()
B1 = read_int_array()
B2 = read_int_array()

by_x = [W[0], W[2], B1[0], B1[2], B2[0], B2[2]]
by_x.sort()

found = False
for x in by_x:
    if not (W[0] <= x <= W[2]):
        continue
    interval = W[3] - W[1]
    for b in [B1, B2]:
        if b[0] <= x <= b[2]:
            interval -= max(0, min(b[3], W[3]) - max(b[1], W[1]))
    if interval > 0:
        found = True
        break

if not found:
    by_y = [W[1], W[3], B1[1], B1[3], B2[1], B2[3]]
    by_y.sort()
    for y in by_y:
        if not (W[1] <= y <= W[3]):
            continue
        interval = W[2] - W[0]
        for b in [B1, B2]:
            if b[1] <= y <= b[3]:
                interval -= max(0, min(b[2], W[2]) - max(b[0], W[0]))
        if interval > 0:
            found = True
            break
print("YES" if found else "NO")






