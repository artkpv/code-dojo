#!/usr/bin/env pypy
"""
0 1 2 3 4 5 6 7 8 9

9//2 = 4
0 4  5 9
0 2  3 4
0 1 2 2




"""
from edx_io import edx_io

with edx_io() as io:
    n = io.next_int()
    a = [io.next_int() for i in range(n)]

    aux = [None] * n

    def merge(a, aux, l, m, r, log):
        for i in range(l, r+1):
            aux[i] = a[i]
        i, j = l, m+1
        for ii in range(l, r+1):
            if r < j or (i <= m and aux[i] < aux[j]):
                a[ii] = aux[i]
                i += 1
            else:
                a[ii] = aux[j]
                j += 1
        log += [(l+1, r+1, a[l], a[r])]


    def mergesort(a, aux, l, r, log):
        if l >= r:
            return
        m = (l+r)//2
        mergesort(a, aux, l, m, log)
        mergesort(a, aux, m+1, r, log)
        merge(a, aux, l, m, r, log)

    log = []
    mergesort(a, aux, 0, len(a)-1, log)

    for line in log:
        io.writeln(' '.join(str(i) for i in line))

    io.writeln(' '.join(str(i) for i in a))
