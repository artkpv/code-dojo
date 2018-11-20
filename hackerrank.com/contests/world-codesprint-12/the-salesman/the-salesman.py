#!/bin/python3

import sys

def minimumTime(x):
    #  Return the minimum time needed to visit all the houses.
    min_, max_ = x[0], x[0]
    for i in range(len(x)):
        if x[i] < min_:
            min_ = x[i]
        if x[i] > max_:
            max_ = x[i]
    return max_ - min_

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        x = list(map(int, input().strip().split(' ')))
        result = minimumTime(x)
        print(result)
