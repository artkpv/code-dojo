#!python3
"""

13 % 4 = 1
27 % 4 = 3

4
19 10 12 24 25 22
0 1 2 3
2 1 3 1


"""
import math

n, k = [int(i) for i in input().strip().split(' ')]
A = list(set(int(i) for i in input().strip().split(' ')))
n = len(A)

R = [0] * k
for i in A:
    R[i%k] += 1

count = 0
if R[0] > 0:
    count += 1
if k%2 == 0 and R[k//2] > 0:
    count += 1
for r in range(1, math.ceil(k/2)):
    count += max(R[r], R[k-r])
print(count)

