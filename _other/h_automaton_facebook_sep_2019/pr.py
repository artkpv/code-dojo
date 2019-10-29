#!python3

"""
Problem.
Given the lane with h cells, numbered from 1 to h. Automaton starts at cell 1 and can move left, stay or move right. Determine how many paths the automaton can make if it can move only m times and should return to cell 1.
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

class Solver(object):
    def solve(self, h, m):
        if h < 2:
            return 1
        # Num of paths can do at cell i with 1 move.
        pn = [0] * h
        pn[0] = 1  # Stay put.
        pn[1] = 1  # Move to left.
        nextpn = [0] * h
        # Calc other till m.
        for moves in range(2, m+1):
            for i in range(h):
                nextpn[i] = (pn[i-1] if 0 < i else 0) + pn[i] + (pn[i+1] if i + 1 < h else 0)
            pn, nextpn = nextpn, pn
        return pn[0]




h, m = read_int_array()
print(Solver().solve(h, m))

