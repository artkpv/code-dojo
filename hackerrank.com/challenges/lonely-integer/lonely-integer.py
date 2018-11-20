#!python3

import sys

def lonelyinteger(a):
    from functools import reduce
    return reduce(lambda x,y: x^y, a)

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
