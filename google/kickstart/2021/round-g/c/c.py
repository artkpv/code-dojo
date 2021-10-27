# Author: Artyom K, w1ld at inbox dot ru.
 
from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt, factorial
INF = float('inf')
 
def read_int():
    return int(input().strip())
 
def read_int_array():
    return [int(i) for i in input().strip().split(' ')]
 
tests = read_int()
for test in range(1, tests+1):
    n, k = read_int_array()
    ban = read_int_array()
    if k in ban:
        print(f"Case #{test}: 1")
        continue
    res = INF
    right = {}
    for i in range(n-1, -1, -1):
        s = 0
        for j in range(i, -1, -1):
            s += ban[j]
            if s > k:
                break
            else:
                rem = k - s
                cost = i - j + 1
                if rem > 0 and rem in right:
                    cost += right[rem]
                    rem = 0
                if rem == 0:
                    res = min(res, cost)
        s = 0
        for r in range(i, n):
            s += ban[r]
            if s > k:
                break
            else:
                if s not in right:
                    right[s] = INF
                right[s] = min(right[s], r - i + 1)
    print(f"Case #{test}: {res if res != INF else -1}")

'''

  K
6 8
1 2 3 1 2 3
i
    j 

s 6 

left[0]
1 1

left[1]
1 1
3 2



'''
