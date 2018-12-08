#!python3
import math

with open('input.txt') as f:
    m = []
    m += [[int(i) for i in f.readline().strip().split(' ')]]
    m += [[int(i) for i in f.readline().strip().split(' ')]]
    m += [[int(i) for i in f.readline().strip().split(' ')]]

    max_ = 0
    n = 3
    for i in range(n):
        perm = [i]  # permutation
        for i1 in range(n):
            if i1 in perm:
                continue
            perm += [i1]
            for i2 in range(n):
                if i2 in perm:
                    continue
                perm += [i2]
                arr = [m[0][perm[0]], m[1][perm[1]], m[2][perm[2]]]
                t = (sum(e**2 for e in arr))**0.5
                if t > max_:
                    max_ = t
                perm.remove(i2)
            perm.remove(i1)
    with open('output.txt', mode='w') as fw:
        fw.write(str(max_))

