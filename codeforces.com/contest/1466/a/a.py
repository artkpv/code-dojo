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
A = .5 * 1 * b
Count different bs. 

I1 BF
All pairs. And into set.
T: O(N^2)  50*50*100 = 250000
j

'''
tests = read_int()
for test in range(tests):
    n = read_int()
    A = read_int_array()
    s = set()
    for i in range(n):
        for j in range(i+1, n):
            s.add(A[j]-A[i])
    print(len(s))


'''
1 2 4 5

1 
3 
4
2
< 4
'''
