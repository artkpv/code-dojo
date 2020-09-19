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

for test in range(read_int()):
    n = read_int()
    cards = []
    for card in range(n):
        cards += [[int(c) for c in input().strip()]]
    count = 0
    for i in range(n):
        isdup = False
        while cards.count(cards[i]) > 1:
            isdup = True
            cards[i][0] = (cards[i][0] + 1) % 10
        if isdup:
            count += 1

    print(count)
    print('\n'.join(''.join(str(c) for c in card) for card in cards))




