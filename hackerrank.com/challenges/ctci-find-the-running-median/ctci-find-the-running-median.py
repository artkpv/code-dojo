"""
https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem
SAME: https://www.hackerrank.com/challenges/find-the-running-median/problem

YEAH!!!!!!!!!!!!!!!!!!!!!!! SOLVED! With two hints from CtCI
"""

#!/bin/python
import sys
from heapq import heappush as hpush, heappop as hpop

def add_el(top, bottom, x):
    """
    adds x to either top or bottom maintaining descending order of them
    """
    min_top = top[0] if len(top) > 0 else None
    max_bottom = -bottom[0] if len(bottom) > 0 else None

    if min_top == None and max_bottom == None:
        hpush(top, x)
    elif min_top <= x:
        hpush(top, x)
    else:
        hpush(bottom, -x)

    # make sure: |top - bottom| <= 1
    while abs(len(top) - len(bottom)) > 1:
        if len(top) > len(bottom):
            min_top = hpop(top)
            hpush(bottom, -min_top)
        else:
            max_bottom = -(hpop(bottom))
            hpush(top, max_bottom)


def get_median(top, bottom):
    if len(top) == 0 and len(bottom) == 0:
        return None
    assert abs(len(top) - len(bottom)) <= 1
    if len(top) == len(bottom):
        return (top[0] + (-bottom[0])) / 2
    if len(top) > len(bottom):
        return top[0]
    return -bottom[0]


n = int(input().strip())
top = []  # min heap
bottom = []  # max heap (with heapq and negative elements)


for i in range(n):
    x = int(input().strip())
    add_el(top, bottom, x)
    m = get_median(top, bottom)
    print('{:.1f}'.format(m))
