#!python3

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

"""
a p
N days

I 1, naive
M - kg in sum to buy.
C(N+M-1, M) = (N+M-1)! / (N-1)! / M!
Time: ~(N+M)!
Space: ~(N)

I 2
DP
m, c = f(i-1, a_i - k) for k=0..a_i,  meat and cost after i-1 day, if we need a_i-k meet
x = max(0, a_i - m) meat to buy on i-th day
m = max(0, m - a_i)  meat left on i-th day
c = x * b_i + c  - money spent till i-th day
min(c) ?

c(i, a) - money spent till i-th day on a amount of meat.

c(i, a) = min ( c(i-1, a - (a_i - k)) + (a_i - k) * p_i ) for k in 0..a_i

Time: ~(N+M)!


I3
Greedy ?


Ex 1
1 5  -- 5
2 1  -- 14*1
3 3
4 2
5 4
Min - 19


"""

n = read_int()
A = []
P = []
for _ in range(n):
    a, p = read_int_array()
    A += [a]
    P += [p]
spent = P[0] * A[0]
min_p = P[0]
for i in range(1, n):
    if P[i] < min_p:
        min_p = P[i]
    spent += A[i] * min_p
print(spent)



