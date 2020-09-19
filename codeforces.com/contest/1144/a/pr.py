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


R = ord('z') - ord('a') + 1

def charat(c):
    return ord(c) - ord('a')

for test in range(read_int()):
    s = input().strip()
    d = [0] * R
    fail = False
    for c in s:
        if d[charat(c)] > 0:
            fail = True
            break
        else:
            d[charat(c)] = 1

    if fail:
        print("No")
        continue

    count = 0
    i = 0
    while i < R:
        if d[i] != 0:
            if count > 0:
                fail = True
                break
            while i < R and d[i] > 0:
                count += 1
                i += 1
        else:
            i += 1
    print("Yes" if not fail else "No")




