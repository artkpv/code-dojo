#!python3
a, b, c, n = [int(i) for i in input().strip().split(' ')]
if a < 0 or b < 0 or c < 0 or n < 0:
    print(-1)
    exit()
if n == 0:
    print(-1)
    exit()
if c > a or c > b:
    print(-1)
    exit()
went = a + b - c
if went >= n:
    print(-1)
    exit()
failed = n - went
print(failed)