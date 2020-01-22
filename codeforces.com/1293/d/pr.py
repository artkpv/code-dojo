#!python3
"""
Author: w1ld [dog] inbox [dot] ru
"""

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
# import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################


x0, y0, ax, ay, bx, by = read_int_array()
xs, ys, t = read_int_array()

def dist(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)

x, y = x0, y0
while True:
    xyD = dist(x, y, xs, ys)
    if xyD <= t:
        break
    xNext = ax*x + bx
    yNext = ay*y + by
    if dist(xNext, yNext, xs, ys) > xyD:
        break
    x = xNext
    y = yNext

points = list()
zd = float('inf')
zInx = -1
while True:
    d = dist(x, y, xs, ys)
    if d > t:
        break
    if zd >= d:
        zd = d
        zInx = len(points)
    points.append((x, y))
    x = ax*x + bx
    y = ay*y + by

if zInx == -1:
    print(0)
    exit()

tt = t - zd
maxCount = 0
for l in range(zInx, -1, -1):
    count = 0
    for r in range(zInx, len(points)):
        time = (dist(*points[l], *points[r]) 
            + min(dist(*points[zInx], *points[l]), dist(*points[zInx], *points[r]))
        )
        if time <= tt:
            maxCount = max(maxCount, r - l + 1)

print(maxCount)




