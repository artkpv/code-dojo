#!python3
"""
Author: w1ld [at] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, factorial
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

MOD = 998244353

def binpow(a, n, mod):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 1:
        return binpow(a, n - 1, mod) * a % mod
    b = binpow(a, n // 2, mod)
    return b * b % mod


def comb(n, k):
    x = 1
    for i in range(n-k+1, n+1):
        x = (x * i) % MOD

    y = 1
    for i in range(2, k+1):
        y = (y * i) % MOD

    y = binpow(y, MOD-2, MOD)

    return x * y % MOD


def mypow(a, x):
    return a ** x % MOD


def solve():
    n, m = read_int_array()
    if n == 2:
        print(0)
        return

    ans = comb(m, n - 1)
    ans = (ans * (n - 2)) % MOD
    ans = (ans * mypow(2, n - 3)) % MOD

    print(int(ans))


if __name__ == '__main__':
    solve()
