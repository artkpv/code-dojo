#!python3
"""

1) BF O(n!*n)

2) Inorder trav. of permut. tree
Time: O(n1)

How to speed up? Add exit condition? How to determine that no solution possible for this tree?


{d : 1..n} - possible digits
{i..n}  - possible places

d_min ? Может быть ниже, на i-k или выше, на i+k
i-k <= d_min and d_min <= n+k



"""

import sys
sys.setrecursionlimit(999999)

def find(i, perm, n, m, s):
    if i > n:
        return True
    min_s = min(s)
    if not (i-m <= min_s and min_s <= n+m):
        return False
    max_s = max(s)
    if not (i-m <= max_s and max_s <= n+m):
        return False

    for i_v in [i-m, m+i]:
        if 1 <= i_v and i_v <= n and i_v not in perm[:i]:
            perm[i-1] = i_v
            s.remove(i_v)
            if find(i+1, perm, n, m, s):
                return True
            perm[i-1] = None
            s.add(i_v)
    return False



t = int(input().strip())
while t > 0:
    t -= 1
    n,m = [int(i) for i in input().strip().split(' ')]
    s = set(range(1,n+1))
    perm = [None] * n
    if find(1, perm, n, m, s):
        print(' '.join(str(i) for i in perm))
    else:
        print(-1)

