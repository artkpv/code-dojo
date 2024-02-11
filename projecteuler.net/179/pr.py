'''

I1 BF. 
For n, find num of divs.
T: O(n^2), S: O(n)

I2 From primes?
All primes for n is P. All divs of n is D. Each d_i in D is a product of 1 or more p from P. 
Then find all primes within < 10^7. Then for each n find its primes. Then num of divs is 2^(num of primes) / permutations of each group (?) ? 

I3 
Using primes:
Go for all integers and keep primes found. For each n find its primes. If number if primes is the same then same num of divisors?

P1 - all primes for n_1. P2 - all primes for n2. If |P1| == |P2| then the same num of divs?


'''
from tqdm import tqdm

def solve_bf(max_=10**7):
    # Slow
    res = 0
    n_prev = 2
    bar = tqdm(range(3, max_))
    for n in bar:
        divs = 2
        for d in range(2, int(n**0.5)+1):
            if n % d == 0:
                divs += 1
        if divs == n_prev:
            res += 1
        n_prev = divs

    print(res)

from collections import Counter
from functools import reduce

def solve_prime(max_=10**7):
    # Slow
    res = 0
    primes = [2]
    prev_divs = 2
    for n in tqdm(range(3, max_)):
        orig_n = n
        my_p = Counter()
        for p in primes:
            if n == 1:
                break
            while n % p == 0:
                my_p[p] += 1
                n //= p
        assert len(my_p) > 0 or n > 1
        divs = None
        if n > 1:
            primes.append(n)
            divs = 2
        else:
            divs = reduce(lambda a,b: a*b, (k+1 for k in my_p.values()), 1)
        if prev_divs == divs:
            res += 1
        prev_divs = divs
    print(res)
            

solve_bf()
#solve_prime()




