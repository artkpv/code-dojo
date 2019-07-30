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

kb = 'qwertyuiopasdfghjkl;zxcvbnm,./'
shift = input().strip()
text = input().strip()
print(''.join(kb[kb.index(c)+ (-1 if shift == 'R' else 1)] for c in text))

