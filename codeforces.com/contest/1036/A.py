#!python3
import math
n, k = [int(i) for i in input().strip().split(' ')]
q, r = divmod(k, n)
print(q + (1 if r != 0 else 0))