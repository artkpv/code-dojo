#!python3


import math
from functools import reduce


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
    return factors


k = int(open('input.txt','r').read())

i = k
max_divs = 0
lim = 2
max_tests = 0
while i >= lim:
    f = factors(i)
    divisors = 2**len(f) + 2  # + 1 and i
    if max_divs < divisors:
        max_divs = divisors
        print("max_divs=%d, i=%d, divs=%d, factors=%s" % (max_divs, i, divisors, repr(f)))
        if len(f) > 1:
            lim = reduce(lambda x,y: x*y, f[1:])
        max_tests = k - i + 1
    i -= 1

open('output.txt','w').write(str(max_tests))

