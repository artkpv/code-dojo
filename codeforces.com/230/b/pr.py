#!python3

from collections import deque, Counter
from itertools import combinations, permutations
from math import sqrt
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

MAX = 10**6

def calc_primes(n):
    seive = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if seive[i]:
            seive[i*i::i*2]= [False] * ( (n - i*i - 1)//(i*2) + 1)
    return [2] + [i for i in range(3,n,2) if seive[i]]

primes = set(calc_primes(MAX))

n = read_int()
for m in read_int_array():
    is_tprime = m != 1 and m**0.5 % 1 == 0 and (m**0.5 in primes)
    print('YES' if is_tprime else 'NO')



