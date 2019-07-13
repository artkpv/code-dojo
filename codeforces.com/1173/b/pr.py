#!python3

from collections import Counter, deque, namedtuple, OrderedDict
from functools import reduce
from itertools import permutations, combinations
import math

n = int(input().strip())
distance = n - 1
m = 1 + math.ceil(distance/2)

up_r = 0
up_c = 0
lo_r = m-1
lo_c = m-1
lo = 0
hi = n-1
isup = False
out = [None] * n
while lo <= hi:
    if isup:
        out[hi] = (up_r, up_c)
        up_c += 1
        hi -= 1
    else:
        out[lo] = (lo_r, lo_c)
        lo_c -= 1
        lo += 1
    isup = not isup
print(m)
print('\n'.join('%d %d' % (r+1, c+1) for r, c in out))
