#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whichSection function below.
def whichSection(n, k, a):
    # Return the section number you will be assigned to assuming you are student number k.
    section = 0
    while k > 0:
        section += 1
        k -= a[section-1]
    return section


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nkm = input().split()

        n = int(nkm[0])

        k = int(nkm[1])

        m = int(nkm[2])

        a = list(map(int, input().rstrip().split()))

        result = whichSection(n, k, a)

        fptr.write(str(result) + '\n')

    fptr.close()
