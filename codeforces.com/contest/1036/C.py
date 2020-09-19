#!python3
import math

t = int(input().strip())
for q in range(t):
    left,right = [int(i) for i in input().strip().split(' ')]

    classy = 0
    n = left
    while True:
        nonzero = 0
        q = n
        while True:
            q, r = divmod(q, 10)
            if r != 0:
                nonzero += 1
            if q == 0:
                break
        if nonzero <= 3:
            classy += 1

        n += 1
        if n > right:
            break
    print(classy)

