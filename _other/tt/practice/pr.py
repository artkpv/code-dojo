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

class LL:
    def __init__(self):
        self.left = None
        self.right = None

    def addright(self, n):
        assert(n)
        if self.right:
            self.right.right = n
            n.left = self.right
        self.right = n
        if not self.left:
            self.left = self.right
    
    def addleft(self, n):
        assert(n)
        if self.left:
            self.left.left = n
            n.right = self.left
        self.left = n
        if not self.right:
            self.right = self.left

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

tests = read_int()
for test in range(tests):
    n = read_int()
    lls = set()
    for tokNum in range(n):
        token = input().strip()
        lc = token[0]
        rc = token[2]
        lll = None
        rll = None
        for ll in lls:
            if ll.right.val == lc:
                assert(lll is None)
                lll = ll
            elif ll.left.val == rc:
                assert(rll is None)
                rll = ll

        if lll is None and rll is None:
            nll = LL()
            nll.addright(Node(lc))
            nll.addright(Node(rc))
            lls.add(nll)
        elif lll is not None and rll is not None:
            lll.addright(rll.left)
            lll.right = rll.right
            lls.remove(rll)
        elif lll is not None:
            lll.addright(Node(rc))
        elif rll is not None:
            rll.addleft(Node(lc))

    if len(lls) != 1:
        print("-1")
    else:
        ll = next(iter(lls))
        x = ll.left
        while x:
            print(x.val, end='')
            x = x.right
    print("\n", end='')

