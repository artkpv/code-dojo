"""
https://projecteuler.net/problem=69
Totient maximum
Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

=====================

ANSWER: 510510


=====================

I1 BF:
loop n=1..1e6: 
    argmax_n(n/phi(n))
For phi use Euclid algo. ~min(a,b)
Time: ~(n^3). About 1e6*1e6 seconds, 31709 years?

I2 
Memoize phi(n), i.e. gcd(a,b)
Space: 1e6 * 1e6 * 3 * 4 / 2**40 = 10TB

I3
From phi(n*m) = phi(n)*phi(m), multiplicativity
loop n=1..1e6:
    argmax_n(n/phi(n))
phi(a):
 if memoized return
 else
 compute phi for a
 fill phi(a*b) = phi(a)*phi(b) for b in 1..a-1 if phi(b)

Time: ?
Space: 1e6*2*4/2**20 ~= 8MB

I4 
With I3 but use primes to get all non-prime.

----------------------

NEXT:
    - Видимо, нужно разложить на множители эти числа, потом по формуле :
\varphi(n)=n\prod_{p\mid n}\left(1-\frac{1}{p}\right),\;\;n>1,
    - seep up:
 n=3 in 0s (0 n/s)max found: n=6 phi=2 n/phi=3.0
max found: n=30 phi=8 n/phi=3.75
max found: n=210 phi=48 n/phi=4.375
 n=2003 in 2s (1001 n/s)max found: n=2310 phi=480 n/phi=4.8125
 n=11856 in 90s (131 n/s)

See
https://ru.wikipedia.org/wiki/Функция_Эйлера  (Euler's totient function)

"""
from time import time
from threading import Timer
from itertools import combinations 
from functools import reduce
from operator import mul

MAXN = 1_000_000

def gcd(a, b):
    a, b = (a,b) if a > b else (b,a)
    while b != 0:
        q, r = divmod(a, b)
        a = b
        b = r
    return a

def prod(iter_):
    r = 0.0 if not iter_ else iter_[0]
    for e in iter_[1:]:
        r *= e
    return r

def solve():
    mem_phi = [0] * (MAXN+1)
    mem_phi[1] = 0
    mem_phi[2] = 1.0
    primes = [2]
    def phi(a):
        if mem_phi[a] == 0:
            a_primes = []
            x = a
            for p in primes:
                while x % p == 0:
                    if not a_primes or a_primes[-1] != p:
                        a_primes.append(p)
                    x = x // p
            if x == a:  # Prime.
                mem_phi[a] = a - 1
                primes.append(a)
            else:
                assert x == 1.0
                mem_phi[a] = a * reduce(
                    mul, [(1 - 1.0/p) for p in a_primes], 1.0
                )
        return mem_phi[a]

    n = 3
    start = time()
    def print_progress():
        nonlocal n
        print(f"{n=} in {time() - start:n}s")
        Timer(2, print_progress).start()
    print_progress()
    max_n = 2
    max_ndp = 1
    while n < 1e6+1:
        ndp = n*1.0/phi(n)
        if max_ndp < ndp:
            max_ndp = ndp
            max_n = n
            print(f'Max: n={n} n/phi={ndp}')
        n += 1
    print(max_n)


if __name__ == '__main__':
    solve()
