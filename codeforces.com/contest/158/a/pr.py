#!python3

n, k = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
print(sum(
    1 for i, e in enumerate(a)
    if e > 0 and (i <= k-1 or e == a[k-1])
    )
)
