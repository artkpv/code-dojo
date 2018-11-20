#!/bin/python3
"""
https://www.hackerrank.com/contests/hourrank-24/challenges/strong-password/problem
"""

import sys

def minimumNumber(n, password):
    return max(6  - n,
       (1 if not any(c in "abcdefghijklmnopqrstuvwxyz" for c in password) else 0) +
       (1 if not any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in password) else 0) +
       (1 if not any(c in "0123456789" for c in password) else 0) +
       (1 if not any(c in "!@#$%^&*()-+" for c in password) else 0))

if __name__ == "__main__":
    n = int(input().strip())
    password = input().strip()
    answer = minimumNumber(n, password)
    print(answer)
