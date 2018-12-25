#!python3
"""
Find all factors for N. Time: exponensial.
"""

import math

def factors_easy(n):
    factors = []
    i = 2
    while n > 1:
        q, r = divmod(n, i)
        if r == 0:
            n = q
            factors += [i]
        else:
            i += 1
    return factors


def factors(n):
    factors = []
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
    while n > 1:
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

n = int(input().strip())
print(' '.join(str(i) for i in factors(n)))

