#!python3
"""
w1ld [dog] inbox dot ru
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

n = read_int()
array = read_int_array()

count = 2 if array[0] < array[1] else 1
prevcount = 1
delcount = 0
maxcount = count
for i in range(2, n):
    if array[i-1] < array[i]:
        if delcount == 0 and array[i-2] < array[i]:
            delcount = prevcount + 1
        else:
            delcount += 1
        prevcount = count
        count += 1
    else:
        delcount = prevcount + 1 if array[i-2] < array[i] else 0
        prevcount = count
        count = 1

    maxcount = max(maxcount, count, delcount)

print(maxcount)

"""

1 2 5 3 4
    ^

1 2 


              v
0 1 2 3 4 5 6 7 8 9  10
6 5 5 6 7 1 8 9 1 10 11

i count prevcount maxcount
2 1 1 1
3 1 1 1
4 2 1 2
5 3 2 3
6 1 3 3
7 2 4 4


"""




