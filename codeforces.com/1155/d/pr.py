#!python3
"""
1 <= n <= 3*10^5
-10^9 <= a_i <= 10^9
-100 <= x <= 100 ,  0 possible!!

1) Multiply by x any l..r or none
2) Choose max interval


Idea 1 ?
If turn min iterval and *x
Or x* max iterval

if x <= 0 then
    find min sum l..r
    if negative then  * x
if x > 0 then
    find max sum l..r
    if positive then  * x
Find max sum l..r

BUT why it is correct ?


Idea 2 BF
For each iterval:  # ~ n*(n-1)/2
    * x
    Find max sum  # ~ n * (n-1) / 2
    / x
Time: ~n^4
Space: ~1


--
test it!
"""


def find_max_sum(A, direction, lo, hi):
    if lo > hi:
        return None, None, None
    if hi - lo == 0:
        return lo, hi, A[lo]
    elif hi - lo == 1:
        """
        Two elements
        -1 -1
        -1 0
        -1 1
        0 -1
        0 0
        0 1
        1 -1
        1 0
        1 -1
        """
        if direction > 0:
            if min(A[lo:hi+1]) >= 0:
                return lo, hi, sum(A[lo:hi+1])
            elif A[lo] > A[hi]:
                return lo, lo, A[lo]
            else:
                return hi, hi, A[hi]
        else:
            if max(A[lo:hi+1]) <= 0:
                return lo, hi, sum(A[lo:hi+1])
            elif A[lo] < A[hi]:
                return lo, lo, A[lo]
            else:
                return hi, hi, A[hi]
    # else N > 2:
    # Case 1, cross sum:
    mid = (lo+hi)//2
    max_sum = A[mid]
    sum_ = max_sum
    max_lo = mid
    for i in range(mid-1, lo-1, -1):
        sum_ += A[i]
        if sum_ * direction > max_sum * direction:
            max_sum = sum_
            max_lo = i
    sum_ = max_sum
    max_hi = mid
    for i in range(mid+1, hi+1):
        sum_ += A[i]
        if sum_ * direction > max_sum * direction:
            max_sum = sum_
            max_hi = i

    # Case 2 and 3, left and right sums:
    for other_lo, other_hi, other_sum in (
            find_max_sum(A, direction, lo, mid-1),
            find_max_sum(A, direction, mid+1, hi)):
        # get winner:
        if (other_sum is not None
                and max_sum * direction < other_sum * direction):
            max_sum = other_sum
            max_lo = other_lo
            max_hi = other_hi
    return max_lo, max_hi, max_sum


n, x = [int(i) for i in input('').strip().split(' ')]
A = [int(i) for i in input('').strip().split(' ')]

lo, hi, sum_ = find_max_sum(A, -1 if x <= 0 else 1, 0, n-1)
if lo is not None and sum_ * x > 0:
    for i in range(lo, hi+1):
        A[i] *= x

lo, hi, sum_ = find_max_sum(A, 1, 0, n-1)
print(sum_ if sum_ > 0 else 0)


"""

Example 1
5 2
-3 8 -2 1 -6
> 16

f 0 4
 mid 2 -2
 max_sum 2 6 7
 max_lo 2 1
 max_hi 2 3

 f 0 1
  > 1 1 8

 f 3 4
  > 3 3 1

 > 1 1 8

x[1:1+1] * 2 => x[1] == 16

f 0 4
 > 1 1 16

Example 2
5 -2
-3 8 -2 1 -6
-3 8 4 -2 12
> 22

f -1 0 4
 mid 2 -2
 max_sum -2 -2 -2 -2 -7
 max_lo 2 2 2
 max_hi 2 4

 f -1 0 1
  > 0 0 -3
 f -1 3 4
  > 4 4 -6

 > 2 4 -7

-3 8 4 -2 12

f 1 0 4
 > 1 4 22

> 22


Example 3
1 -100
2
> 2


Example 4
1 100
-2
> 0


"""





















