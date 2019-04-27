#!python3

"""

I1. BF
n * m

I2
"""

import os
import sys

#
# Complete the twoStacks function below.
#
def twoStacks(x, a, b):
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))


        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
