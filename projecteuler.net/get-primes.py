
def primes_via_sieve(n):
    """
    Returns primes, <=n, by sieve.
    See https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_and_variants
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

