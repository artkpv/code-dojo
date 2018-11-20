"""
https://projecteuler.net/problem=9

Special Pythagorean triplet Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def coprime(a, b):
    if b == 0:
        return a
    return coprime(b, a%b)


def pythogorean_non_distinct_triplets_with_range(N):
    m = 2  # min m
    while True:  # over m
        some_found_for_m = False  # to exit if too big
        n = 0  # min n
        while n < m:  # over n
            some_found_for_n = False
            # choose next n in the terms:
            n += 1
            if (m - n) % 2 != 1:  # next n (to all primitive)
                continue
            if coprime(m, n) != 1:  # next n (to all primitive)
                continue
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            k = 1
            while True:  # over k
                a2 = k*a
                b2 = k*b
                c2 = k*c
                if a2 + b2 + c2 > N:
                    break  # next n
                else:
                    some_found_for_n = True
                    some_found_for_m = True
                    if a2 + b2 + c2 == N:
                        yield (a2, b2, c2)
                k += 1
            if not some_found_for_n:  # to large
                break
            # else to next n
        if not some_found_for_m:  # then m is too big for this range
            break
        m += 1

print max(pythogorean_non_distinct_triplets_with_range(1000)))
