#!python3
"""

I1. a

Ex1
5
1  3 5
2  1 4
3  2 4
4  1 5
5  2 3



"""

n = int(input().strip())
t = [None] * n
for i in range(n):
    x,x1 = [int(i) for i in input().strip().split(' ')]
    x,x1 = x-1, x1-1
    t[i] = [x, x1]

res = [0]
while len(res) < n:
    a = res[-1]
    b = t[a][0]
    c = t[a][1]
    if c not in t[b]:
        b, c = c, b
    res += [b, c]


print(' '.join(str(i+1) for i in res))

