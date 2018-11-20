#!python3

import math
import os
import random
import re
import sys

# Complete the minuteToWinIt function below.
def minuteToWinIt(a, k):
    # Return the minimum amount of time in minutes.
    a0s = {}
    good_a0 = None
    for i in range(len(a)):
        a0 = a[i]-i*k
        if a0 not in a0s:
            a0s[a0] = 0
        a0s[a0] += 1
        if not good_a0 or a0s[a0] > a0s[good_a0]:
            good_a0 = a0
    minutes = 0
    for i in range(len(a)):
        if a[i] != good_a0 + i*k:
            minutes += 1
            a[i] = good_a0 + i*k
    return minutes

n, k = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
print(minuteToWinIt(a, k))
