#!python3

n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
assert(len(a) == n)
if max(a) <= 0:
    print(max(a))
    exit()

d = [None] * n
d[n-1] = a[n-1]
if n > 1:
    d[n-2] = max(a[n-2], a[n-1])
for i in range(n-3, -1, -1):
    d[i] = max(d[i+1], a[i] + (d[i+2] if d[i+2] > 0 else 0))
print(d[0])
