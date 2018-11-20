#!python3
"""
24       1
2 * 12   12
1 * 24   24

24          1
12 12       2
6 6 6 6     4
(3 3) * 4


"""

import sys, functools
from math import sqrt

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def isprime(a):
    if a == 2 or a == 3: return True
    if a < 2 or a%2 == 0: return False
    if a < 9: return True
    if a%3 == 0: return False
    r, f = int(a**0.5), 5
    while f <= r:
        if a%f == 0: return False
        if a%(f+2) == 0: return False
        f += 6
    return True

def longest_for_number(n):
    f = prime_factors(n)
    moves = 1
    product = 1
    for i in reversed(f):
        product *= i
        moves += product
    return moves


def longestSequence(a):
    #  Return the length of the longest possible sequence of moves.
    res = 0
    for i in a:
        if isprime(i):
            res += i+1
        else:
            res += longest_for_number(i)
    return res


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = longestSequence(a)
    print(result)
