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


def factor(n):
    factors = []
    if n <= 3:
        return factors
    while n % 2 == 0:
        factors += [2]
        n //= 2
    while n % 3 == 0:
        factors += [3]
        n //= 3
    i = 1
    """
    Each following 6 numbers has only 2 candidates:
        5 7 11 13 17 19 23 25 ..
    """
    left_right = (-1,1)
    nn = n
    while n > 1 and pow(i*6 + 1, 2) <= nn:
        for j in left_right:
            k = i*6 + j
            if k > n:  # can be equal (45)
                assert(n == 1)
                break
            while True:
                q, r = divmod(n, k)
                if r != 0: break
                factors += [k]
                n = q
        i += 1
    return factors

t = read_int();

while t > 0:
    t -= 1
    n = read_int()
    f = factor(n)
    if len(f) < 2:
        print("NO")
    else:
        f.sort()
        counter = Counter(f)
        ca = list(counter.items())
        ans = []
        if len(counter) >= 3:
            ans = [ca[0][0] * ca[0][1], ca[1][0] * ca[1][1], ca[2][0] * ca[2][1]]
            for e, num in ca[3:]:
                ans[-1] *= e * num
        elif len(ca) == 2:
            if ca[0][1] + ca[1][1] <= 3:
                pass
            else:
                ans = [ca[0][0], ca[0][0] * (ca[0][1] - 1), ca[1][0] * ca[1][1]]
        elif len(ca) == 1:
            if ca[0][1] >= 6:
                e = ca[0][0]
                ans = [e, e*e, e*e*e]
                for i in range(ca[0][1] - 5):
                    ans[-1] *= e

        if len(ans) == 0:
            print("NO")
        else:
            print("YES")
            print(' '.join(str(e) for e in ans))





            


        




