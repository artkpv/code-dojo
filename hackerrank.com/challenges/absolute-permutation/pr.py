#!python3
"""

I1. BF. Iterate all permutations and find the one.

Time: O(n!*n)

I2.
Iterate all possible elements at i-th position.

Time: O(2^n)
Space: O(n+n)

At i-th index 0-based possible candidates: i+1+k, i+1-k

Ex2
3 0
1 2 3 

Ex3

"""

import sys
sys.setrecursionlimit(99999)

def _find(inx, permutation, n, k, elements):
    if not elements and inx == n:
        return True
    for candidate in (inx+1-k, inx+1+k):
        if candidate in elements:
            permutation[inx] = candidate
            elements.remove(candidate)
            if _find(inx+1, permutation, n, k, elements):
                return True
            permutation[inx] = None
            elements.add(candidate)
    return False


def find(permutation, n, k):
    elements = set(range(1,n+1))
    return _find(0, permutation, n, k, elements)


tests = int(input().strip())
for test in range(tests):
    n,k = [int(i) for i in input().strip().split(' ')]
    permutation = [None] * n
    if find(permutation, n, k):
        print(' '.join(str(i) for i in permutation))
    else:
        print(-1)

