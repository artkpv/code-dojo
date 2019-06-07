#!python3
"""
E 1
k=2
1 2 5

lo 0
hi 2
mid 1


"""

def optimal_f(A, k):
    if k == 0:
        return A[0]
    assert len(A) >= k + 1
    lo = 0
    hi = len(A) - 1
    min_x = float('inf')
    while hi - lo + 1 >= k+1:
        mid = (lo+hi)//2
        iter_lo = max(lo, mid - k//2)
        iter_hi = min(hi, iter_lo + k)
        iter_lo = iter_hi - k
        x = (A[iter_hi] + A[iter_lo]) / 2
        x = int(round(x, 0))
        if min_x > x:
            min_x = x
        if A[iter_hi-1] - A[lo] < A[hi] - A[iter_lo+1]:
            # to left
            hi = iter_hi - 1
        else:
            lo = iter_lo + 1
    return min_x 

        

for test in range(int(input().strip())):
    n, k = [int(i) for i in input().strip().split(' ')]
    A = [int(i) for i in input().strip().split(' ')]
    print(optimal_f(A, k))
