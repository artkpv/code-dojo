#!python3

import math
from functools import reduce
import itertools


def factors(n):
    """
    Finds factors of n, other than n or 1.
    """
    nn = n
    r = []  # result
    while nn % 2 == 0:
        r += [2]
        nn //= 2
    while nn % 3 == 0:
        r += [3]
        nn //= 3
    # Remaining numbers are: i*6 +/- 1 for i=1..inf:
    # 5 7 11 13 17 19 23 25 ..
    i = 1
    left_right = (-1,1)
    while nn > 1:
        for j in left_right:
            k = i*6 + j
            while nn % k == 0:
                r += [k]
                nn //= k
        i += 1
    if len(r) == 1: # it is prime:
        assert(r[0] == n)
        return []
    return r



k = int(open('input.txt','r').read())

i = k
max_divs = 0
lim = 2
max_tests = 0
while i >= lim:
    Fs = factors(i)
    divisors = [1]
    i_max_div = None
    if Fs:
        combinations = (c for n in range(1, len(Fs)) for c in itertools.combinations(Fs, n))
        divs = set(reduce(lambda x,y: x*y, c) for c in combinations)
        max_div = max(divs)
        divisors += divs
    divisors += [i]
    if i % 100 == 0:
        print("%d\n factors: %s\n divs: %s\n" % (i, repr(Fs), repr(divisors)))
    if max_divs <= len(divisors):
        max_divs = len(divisors)
        if i_max_div:
            lim = i_max_div
        max_tests = k - i + 1
    i -= 1

open('output.txt','w').write(str(max_tests))

