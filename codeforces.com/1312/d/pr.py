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


def solve():
    n, m = read_int_array()
    if m < n - 1:
        print(0)
        return

    MOD = 998244353

    res = (n-2) * (2 << (n-2)) % MOD
    res = res * (n - 1) % MOD

    # p = n-2
    # s = m - p + 1
    # for t in range(n-3):



if __name__ == '__main__':
    solve()
