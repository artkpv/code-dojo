#!python3

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, ceil
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

"""
n, I
a_i

n*ceil(lg(K)) <= I*8

ceil(lg(K)) <= I*8 / n

K <= 2^(I*8/n)


"""

n, I = read_int_array()
A = read_int_array()
max_bits = I*8//n
count = Counter(A)
k = len(count)
max_k = 2**max_bits
m = k - max_k
if I*8 < n:
    print(I*8)
elif m > 0:
    print(sum(num for el, num in count.most_common()[-m:]))
else:
    print(0)
# print(max_bits, m, count.most_common())
