#!python3
"""

Optimal:
    m solved
    tt time left, >= 0

    m == max(
        d[-1][0] with n-1 solved,
        d[-1][1] with n-1 not solved)


"""

import itertools

f = open('input.txt','r')
n = int(f.readline().strip())
t = [int(i) for i in f.readline().strip().split(' ')]

left = 300*60

D = {}
s = [(0, left, 0)]
while s:
    i, left, solved = s.pop()
    p = (i, left, solved)
    if p in D:
        continue
    if i >= len(t):
        D[p] = solved
        continue
    not_taken = (i+1, left, solved)
    taken = (i+1, left-t[i], solved+1)
    if not_taken not in D:
        s += [p]
        s += [not_taken]
        if left >= t[i]:
            s += [taken]
    else:
        r = max(D[not_taken], D[taken] if taken in D else -1)
        D[p] = r

r = max(D.values())
open('output.txt', 'w').write(str(r))




