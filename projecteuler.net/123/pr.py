"""
n-th prime, from 2, 3, ... 
p_n is the prime.

Remainder r = (p_n+1) ** n + (p_n - 1)** n mod p_n ** 2.

The least n for which th remainer exceeds 10**9 is 7037. 

Unknown:
The least n for which the remainder exceeds 10**10?

I1 BF. 
Iter all primes (Sieve of Eratosthen). Calc the remainder each time. 
T: O(n * log log n )

I2

 (p_n + 1) ** n mod p_n ** 2.
 (p_n - 1) ** n mod p_n ** 2.

"""

