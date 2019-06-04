#!python3
"""
I 1 
get primes,
TIme: t*n*n+n+




"""
import functools 


def get_x(divisors):
    divisors.sort()
    factors = dict()
    for d in divisors:
        for f in factors:
            times = factors[f]
            while times > 0 and d % f == 0:
                times -= 1
                d //= f
            while d % f == 0:
                factors[f] += 1
                d //= f 
            if d == 1:
                break
        if d > 1:
            factors[d] = 1
    if len(factors) == 1:
        x = next(iter(factors.keys()))
        x **= 2
    else:
        x = functools.reduce(
            lambda e1, e2: e1**factors[e1] * e2**factors[e2],
            factors
        )
    for d in divisors:
        if x % d != 0:
            return -1
    return x


for test in range(int(input().strip())):
    n = int(input().strip())
    divisors = [int(i) for i in input().strip().split(' ')]
    print(get_x(divisors))

"""

Ex 1

2 3 4 6 8 12 16 24

d 2 3 4 6 8 12 16 
factors
2:4 
3:1

48


Ex 2
2

d 2
factors



"""