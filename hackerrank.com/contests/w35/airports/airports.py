#!python3

import sys

def airports(d, x):
    """
    Need to make any airport not less to d to at least one other airport.
    If not so then find min cost to move airports to satisfy the condition.

    x = sorted x
    ??


    """

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, d = input().strip().split(' ')
        n, d = [int(n), int(d)]
        x = list(map(int, input().strip().split(' ')))
        result = airports(d, x)
        print (" ".join(map(str, result)))
