#!python3
"""
Author: w1ld [at] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

class Node:
    def __init__(self, c):
        self.c = c
        self.l = None
        self.r = None


tests = read_int()

for test in range(tests):
    s = input().strip()
    left = Node(s[0])
    x = left
    found = True
    used = set([x.c])
    for c in s[1:]:
        if x.c == c:
            continue
        if x.l and x.l.c == c:
            x = x.l
        elif x.r and x.r.c == c:
            x = x.r
        elif not x.l and c not in used:
            x.l = Node(c)
            used.add(c)
            x.l.r = x
            x = x.l
            left = x
        elif not x.r and c not in used:
            x.r = Node(c)
            used.add(c)
            x.r.l = x
            x = x.r
        else:
            found = False
            break

    if not found:
        print("NO")
    else:
        ans = []
        x = left
        while x:
            ans.append(x.c)
            x = x.r
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if c not in used:
                ans.append(c)
        print("YES")
        print(''.join(ans))










