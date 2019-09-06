#!/bin/python3
"""
1. l, r
2. 1 or even and a_i/2 is

n l r
4 2 2
8 16 16 16


1 2 4 8 ...

For min:
max_a_i = 2**(l-1)


For max
max_a_i = 2**(r-1)


a0*(1-q^n)/(1-q)

min = 2**l - 1 + n - l
max = 2**r - 1 + (n-r)*2**(r-1)

"""
n, l, r = [int(i) for i in input().strip().split(' ')]
print(2**l - 1 + n - l, 2**r - 1 + (n-r)*2**(r-1))

