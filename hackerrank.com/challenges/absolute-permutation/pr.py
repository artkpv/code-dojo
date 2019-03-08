#!python3
"""

I1. BF. Iterate all permutations and find the one.

Time: O(n!*n)

I2.
Iterate all possible elements at i-th position.

Time: O(2^n)
Space: O(n+n)

At i-th index 0-based possible candidates: i+1+k, i+1-k


I3
if i - k


E1
3
2 1
3 0
3 2

Ex2
3 0
1 2 3

Ex3
n = 4, k = 2
1 2 3 4
3 4 1 2
3 4 1 2

1 2 3 4 5  k = 1
2 1 4 3

1 2 3 4 5 6 7  k=3
4 5 6 1 2 3
"""


def find(permutation, n, k):
    elements = set(range(1,n+1))
    for i in range(n):
        if i+1-k in elements:
            elements.remove(i+1-k)
            permutation[i] = i+1-k
        elif i+1+k in elements:
            elements.remove(i+1+k)
            permutation[i] = i+1+k
        else:
            return False
    return True

tests = int(input().strip())
for test in range(tests):
    n,k = [int(i) for i in input().strip().split(' ')]
    permutation = [None] * n
    if find(permutation, n, k):
        print(' '.join(str(i) for i in permutation))
    else:
        print(-1)

