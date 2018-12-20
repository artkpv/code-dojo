#!python3
"""
Find all factors for N. Time: exponensial.
"""

import math

def factors(n):
    factors = []
    while n % 2 == 0:
        factors += [2]
        n //= 2
    while n % 3 == 0:
        factors += [3]
        n //= 3
    i = 1
    left_right = (-1,1)
    while True:
        if n == 1:
            return factors
        for j in left_right:
            k = i*6 + j
            if k >= n:
                return factors
            while True:
                q, r = divmod(n, k)
                if r == 0:
                    factors += [k]
                    n = q
                else:  # next
                    break
        i += 1

n = int(input().strip())
print(' '.join(str(i) for i in factors(n)))

