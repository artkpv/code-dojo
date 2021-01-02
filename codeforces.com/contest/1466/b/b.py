# Author: Artyom K, w1ld at inbox dot ru.
 
from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, factorial
 
def read_int():
    return int(input().strip())
 
def read_int_array():
    return [int(i) for i in input().strip().split(' ')]
 
'''
n <= 10**5
x_i <= 2*n
'''

tests = read_int()
for test in range(1, tests+1):
    n = read_int()
    A = read_int_array()
    A.sort()
    count = 0
    top = float('inf')
    for i in range(n-1, -1, -1):
        if A[i] + 1 < top:
            count += 1
            top = A[i] + 1
        elif A[i] < top:
            count += 1
            top = A[i]
    print(count)

'''
T: n 
S: 1

Greedy
    increase if can

1 2 2 2 5 6
i

top 1
count 5

'''


