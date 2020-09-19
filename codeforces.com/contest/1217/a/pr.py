#!/bin/python3
from math import ceil
for _ in range(int(input().strip())):
    s, i, e = [int(i) for i in input().strip().split(' ')]
    ee = max(s, (s+i+e)//2 + 1) - s
    print(max(e - ee + 1, 0))

"""
2 1 0

"""
