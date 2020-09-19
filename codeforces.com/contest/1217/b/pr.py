#!python3
from math import ceil
INF = float('inf')
for _ in range(int(input().strip())):
    n, x = [int(i) for i in input().strip().split(' ')]
    maxd = -1
    d = 0
    h = float('inf')
    for j in range(n):
        dd, hh = [int(i) for i in input().strip().split(' ')]
        if dd > maxd:
            maxd = dd
        if dd - hh > d - h:
            h = hh
            d = dd
    count = 0
    if x > 0:
        x -= maxd
        count += 1
    if x > 0 and d - h > 0:
        """
        ((x - d + h) - d + h) - d + h ...
        x - 2d + 2h
        x - n*d + n*h <= 0
        x + n * (h - d) <= 0
        n >= x/(d-h)
        """
        count += ceil(x/(d-h))
        x = 0

    print(count if x <= 0 else -1)

