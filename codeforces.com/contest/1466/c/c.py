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
freq = [0] * 10**5
for t in range(tests):
    s = list(input().strip())
    n = len(s)
    if n == 1:
        print(0)
        continue
    for i in range(n):
        freq[i] = 0
    def inc(i, j):
        if j < n and s[i] == s[j]:
            freq[i] += 1
            freq[j] += 1
    for i in range(1, n):
        inc(i-1, i)
        inc(i-1, i+1)
    def subs(i, j):
        if j < n and s[i] == s[j] and s[i] != '.':
            k = i if freq[i] > freq[j] else j 
            m = 0
            for d in (-2, -1, 1, 2): 
                p = k+d
                if not (0 <= p < n):
                    continue
                if s[p] != '.' and s[p] == s[k]:
                    freq[p] -= 1
                    m += 1
            s[k] = '.'
            assert freq[k] == m
            freq[k] = 0
            return 1
        return 0
    count = 0
    for i in range(1, n):
        count += subs(i-1, i)
        count += subs(i-1, i+1)
    print(count)


'''
0123456
b..b..b
freq
0000000
      i
count 4


'''





'''
0123456
bbbbbbb
. . .. 
01
02
12
13
23
24
34
35
45
46
56


0 2
1 3
2 4
3 4
4 4
5 3
6 2


I1 
BF. Choose chars and check
T: 2^N * N
S: N

0
I2
Count freq
Substit

*aa*
*aba*

aaa

ababa

abacada

'''
