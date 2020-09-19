#!python3
"""
Author: w1ld [at] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
from heapq import heappush as push, heappop as pop
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

n = read_int()
a = read_int_array()
t = read_int_array()
srt = list(sorted((a[i], t[i]) for i in range(n)))
cnt = [(-srt[0][1], 0)]
i = 1
cntValue = srt[0][0]
ans = 0
while cnt or i < n:
    if i < n and srt[i][0] == cntValue:
        push(cnt, (-srt[i][1], i))
        i += 1
    elif any(cnt):
        ti, inx = pop(cnt)
        ti = -ti
        ans += (cntValue - srt[inx][0]) * ti
        cntValue += 1
    else:
        cntValue = srt[i][0]
print(ans)





