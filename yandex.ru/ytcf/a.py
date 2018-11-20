#!python3

n, r = [int(i) for i in input().strip().split(' ')]
if n == 0:
    print(n)
    exit()
p = [int(i) for i in input().strip().split(' ')]  # points
assert len(p) == n
p = sorted(p)
m = 1  # least number of recommended points
l, c = p[0], p[0]  # left, center
for i in range(1, n):
    if p[i] - c > r:
        m += 1
        l, c = p[i], p[i]
    elif p[i] - l <= r:
        c = p[i]
print(m)
