#!python3
"""
https://www.hackerrank.com/contests/101hack52/challenges/costly-intervals/problem

"""

import sys


def cost(A, l, r):
    or_ = A[l]
    and_ = A[l]
    for i in range(l+1, r-l+1):
        or_ = or_ | A[i]
        and_ = and_ & A[i]
    # TODO invalid comptation
    return (or_ - and_) - (max(A[l:r+1]) - min(A[l:r+1]))

def costlyIntervals(n, k, A):
    # Return a list of length n consisting of the answers
    C = [-1] * len(A)
    for l in range(len(A)):
        for i in range(l, len(A)):
            c = cost(A, l, i)
            if c >= k:
                for j in range(l, i+1):
                    if C[j] < c:
                        C[j] = c
    return C


if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    A = list(map(int, input().strip().split(' ')))
    result = costlyIntervals(n, k, A)
    print ("\n".join(map(str, result)))
