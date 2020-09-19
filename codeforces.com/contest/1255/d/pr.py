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

for test in range(read_int()):
    rows, cols, ch = read_int_array()
    rice = 0
    field = []
    for r in range(rows):
        field += [list(input().strip())]
        rice += field[-1].count('R')
    code = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    i = 0
    j = 0
    count = 0
    ch_n = 1
    base = rice // ch
    rem = rice % ch
    base_num = ch - rem
    for i in range(rows):
        for j in range(cols):
            j = j if i % 2 == 0 else -j-1
            if field[i][j] == 'R':
                count += 1

            # If next chicken.
            if count > (base if ch_n <= base_num else base + 1):
                ch_n += 1
                count = 1

            field[i][j] = code[ch_n - 1]
    print('\n'.join(''.join(field[i]) for i in range(rows)))









