# Hackerrank. https://www.hackerrank.com/challenges/countingsort4/problem
n = int(input())
A = []
for i in range(n):
    num, s = input().strip().split(' ')
    A += [(int(num), s if i >= n//2 else '-')]

assert len(A) == n
counter = [0] * n
for i in range(n):
  counter[A[i][0]] += 1

for i in range(1, len(counter)):
    counter[i] += counter[i - 1]

B = [None] * n
for i in range(n - 1, -1, -1):
    B[counter[A[i][0]] - 1] = A[i]
    counter[A[i][0]] -= 1

import sys
for i in range(n):
    sys.stdout.write('{} '.format(B[i][1]))
