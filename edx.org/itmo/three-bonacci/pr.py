#!python3
"""
T-1 + T-2 - T-4 - T-5 + T-6
"""
a0,a1,a2,n = [int(i) for i in open('input.txt','r').read().strip().split(' ')]

with open('output.txt','w') as f:
    if n == 0:
        f.write(str(a0))
    elif n == 1:
        f.write(str(a1))
    elif n == 2:
        f.write(str(a2))
    else:
        n -= 3
        while True:
            t = a2 + a1 - a0
            a2, a1, a0 = t, a2, a1
            n -= 1
            if n < 0:
                break
        f.write(str(a2))
