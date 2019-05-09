"""
CLRS. Ch. 15. Dynamic programming.

Ex.15.1-3

"""

import sys
sys.setrecursionlimit(10000)

def max_cut_rod(n, p):
    revenue = [0]
    for i in range(1, n + 1):
        revenue += [-1]
    revenue[n] = p[n] if len(p) > n else 0
    cuts = []
    max_cut_rod_aux(n, p, revenue, cuts)
    return revenue[n]

def max_cut_rod_aux(n, p, r, cuts):
    if r[n] < 0:
        q = 0
        for i in range(n + 1):
            n_i_max = max_cut_rod_aux(n - i, p, r)
            if q < p[i] + n_i_max:
                q = n_i_max
            q = max(q, p[i] + n_i_max)
        r[n] = q


def cut_rod_bottom_up(n, p):
    r = [-1] * (n+1)
    r[0] = 0  # no revenue if no rod
    for j in range(n+1):
        q = -1
        for i in range(j + 1):
            q = max(q, (p[i] if i < len(p) else 0) + r[j - i])  # cutting left side + optimal solution on the right
        r[j] = q
    return r[n]

n = int(input().strip())
prices = [int(i) for i in input().strip().split(' ')]
print(max_cut_rod(4, prices))
# TODO:
# fails with "4`n1 5 8 9 10 17 17 20 24 30" | .\ch.15_cut_rod.py
print(cut_rod_bottom_up(4, prices))
