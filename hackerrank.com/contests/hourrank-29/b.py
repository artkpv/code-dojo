#!python3
"""
https://www.hackerrank.com/contests/hourrank-29/challenges/array-partition

5 tests 
A, 1 <= N <= 10^5
1 <= Ai <= 10^6
Number of ways to div A so that gcd(mul(P),mul(Q))==1
Print in 10^9+ 7

1) BF, all combinations, N!/m! . T:~N!*N*g. S: O(1)

2) 


2 3 1 


"""


tests = int(input().strip())
for test in range(tests):
    n = int(input().strip())
    arr = [int(c) for c in input().strip().split()]
    
