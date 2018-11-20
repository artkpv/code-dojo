
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i < 0: neg += 1
        elif i > 0 : pos += 1
        else: zero += 1
    print("{:.6}".format(pos/len(arr)))
    print("{:.6}".format(neg/len(arr)))
    print("{:.6}".format(zero/len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
