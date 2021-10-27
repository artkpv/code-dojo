# Author: Artyom K, w1ld at inbox dot ru.
 
from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, factorial
 
def read_int():
    return int(input().strip())
 
def read_int_array():
    return [int(i) for i in input().strip().split(' ')]
 
tests = read_int()
for test in range(1, tests+1):
    n = read_int()
    arr = read_int_array()
    arr.sort()
    no = any(abs(arr[i-1] - arr[i]) > 1 for i in range(1, len(arr)))
    print("NO" if no else "YES")
