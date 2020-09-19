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
....
XXX

"""
for _ in range(read_int()):
    a, b = read_int_array()
    s = input().strip()
    g = []
    i = 0
    while i < len(s):
        if s[i] == '.':
            g += [1]
            i += 1
            while i < len(s) and s[i] == '.':
                g[-1] += 1
                i += 1
        else: 
            i += 1


            

