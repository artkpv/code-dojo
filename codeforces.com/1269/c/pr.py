#!python3
"""
w1ld [dog] inbox dot ru

"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

numL, k = read_int_array()
num = input().strip()

found = True
i = 0
while i < k and i + k < numL and found:
    j = i
    while j + k < numL and found:
        if num[j] != num[j+k]:
            found = False
        j += k
    i += 1

if False and num[:15] == '763451441322205':
    print('numL',numL)
    print('k',k)
    print('num[0:10]',num[0:10])
    print('num[k-10:0+k+1]',num[k-10:k+1])
    print('num[:-10]',num[:-10])
    print(found)

if found:
    print(numL)
    print(num)
else:
    nineInx = k-1
    while nineInx >= 0 and num[nineInx] == '9':
        nineInx -= 1
    nineInx += 1
    print(numL)
    assert nineInx >= 0
    i = 0
    increased = (ord(num[nineInx-1]) - ord('0')) + 1
    while i < numL:
        if i%k + 1 < nineInx:
            print(num[i%k], end='')
        elif i%k + 1 == nineInx:
            print(increased, end='')
        else:
            print(0, end='')
        i += 1



