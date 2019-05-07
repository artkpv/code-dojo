#!python3
"""

i1
n*m

"""

n, m = [int(i) for i in input().strip().split(' ')]
shifts = set()
dist_arcs = {}
arcs = set()
for _ in range(m):
    a, b = [int(i) for i in input().strip().split(' ')]
    a, b = min(a,b), max(a,b)
    d = b - a
    arcs.add((a,b))
    dist_arcs[d] = dist_arcs.get(d, [])
    shifts.add(d)
    for arc in dist_arcs[d]:
        shift = max(arc[0], a) - min(arc[0], a)
        shifts.add(shift)
    dist_arcs[d] += [(a,b)]

found = False
for shift in shifts:
    false_shift = False
    for arc in arcs:
        a, b = arc[0] + shift, arc[1] + shift
        while a > n:
            a -= n
        while b > n:
            b -= n
        a, b = min(a,b), max(a,b)
        if (a,b) not in arcs:
            false_shift = True
            break
    if not false_shift:
        found = True
        break
print("Yes" if found else "No")










