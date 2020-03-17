#!/bin/python3

def binpow(a, n, mod):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n % 2 == 1:
        return binpow(a, n - 1, mod) * a % mod
    b = binpow(a, n // 2, mod)
    return b * b % mod
