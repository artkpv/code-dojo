#!/bin/python3

import math

A,B,a = [int(i) for i in input().strip().split(' ')]
print(math.floor(a*B/A))
