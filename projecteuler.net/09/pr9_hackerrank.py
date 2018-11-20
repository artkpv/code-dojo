#!/bin/python3

"""
YEEEEEEEEEEEEEEEEEEEEEEEEEEAAAAAAAAAAAAAAAAAAH!!!!!!!!!!!!!!!!!
https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem
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


from functools import reduce
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    max_ = -1
    for t in pythogorean_non_distinct_triplets_with_range(n):
        p = t[0] * t[1] * t[2]
        if max_ < p:
            max_ = p
    print(max_)

