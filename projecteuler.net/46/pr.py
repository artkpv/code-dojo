"""
https://projecteuler.net/problem=46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

def is_prime(n, primes):
    i = 0
    while i < len(primes):
        if primes[i] == 1:
            i += 1
        if n % primes[i] == 0:
            return False
        else:
            i += 1
    return True

def solve():
    primes = [1, 2, 3, 5, 7]
    n = 9
    while True:
        if is_prime(n, primes):
            primes.append(n)
        else:
            is_g = False
            for p in primes:
                q, r = divmod(n - p, 2)
                if r == 0 and q**.5 % 1.0 == 0.0:
                    is_g = True
                    break
            if not is_g:
                return n
        n += 2
    return None

if __name__ == '__main__':
    print(solve())
