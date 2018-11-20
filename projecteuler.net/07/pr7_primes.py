"""
https://projecteuler.net/problem=7
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import timeit

def primes(n):
    """
    Returns primes, <=n, by sieve.
    """
    a = list(range(2, n + 1))
    # remove all divisables of primes in the array:
    i, j = 0, 0
    while i < len(a):
        j = i + 1
        while j < len(a):
            if a[j] % a[i] == 0:
                del a[j]
                continue
            j += 1
        i += 1
    return a  # only primes remain


start = timeit.default_timer()
p = primes(200000)
print('found ' + str(len(p)) + ' primes in ' + str(int(timeit.default_timer() - start)) + ' sec')
N = 10_001
if len(p) >= N:
    print(p[N - 1])

