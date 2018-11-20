#!/bin/python3

import sys

def solve(a):
    return abs(sum(a[:len(a)//2]) - sum(a[len(a)//2:]))

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(a)
print(result)

