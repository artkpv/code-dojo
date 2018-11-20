"""
https://projecteuler.net/problem=10
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def primes_via_sieve(n):
    """
    Returns primes, <=n, by sieve.
    """
    a = list(True for i in range(n+1))
    first_prime = 2
    i = first_prime
    import math
    while i <= math.sqrt(n):
        if a[i]:
            j = i*i
            while j <= n:
                a[j] = False
                j += i
        i += 1
    return [i for i in range(first_prime, n + 1) if a[i]]

N = 2_000_000
print(sum(primes_via_sieve(N)))
