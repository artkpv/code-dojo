#!python3

"""


"""

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

n, m = read_int_array()
s = input().strip()
ctopos = {}
ctopos[s[0]] = 0
moves = 0
pos = 0
for i in range(1, n):
    c = s[i]
    if c not in ctopos:
        if pos < len(ctopos) // 2:
            for e in ctopos:
                ctopos[e] += 1
            ctopos[c] = 0
            pos += 1
        else:
            ctopos[c] = len(ctopos)
    moves += abs(ctopos[c] - pos)
    pos = ctopos[c]
    # print(moves, pos)
print(moves)


"""
counter = Counter(s)
res = deque()
side = True
for c, cnum in counter.most_common():
    if not res:
        res.append((c, cnum))
    elif side:
        res.appendleft((c, cnum))
    else:
        res.append((c, cnum))
    side = not side
assert len(res) <= m
res = list(res)
# print(res)
ctopos = {}
pos = 0
for i, e in enumerate(res):
    c, cnum = e
    ctopos[c] = i
    if c == s[0]:
        pos = i
moves = 0
for k in range(1, n):
    nextpos = ctopos[s[k]]
    moves += abs(nextpos - pos)
    pos = nextpos
print(moves)
"""




