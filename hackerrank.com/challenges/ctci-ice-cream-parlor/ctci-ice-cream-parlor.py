#!python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(arr, money):
    d = {}
    for i in range(len(arr)):
        c = arr[i]
        if (money - c) in d:
            print(d[money-c] + 1, i + 1)
            return
        d[c] = i
    raise 'should be solution'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        solve(arr, money)
