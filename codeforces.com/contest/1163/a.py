#!python3

n, m = [int(i) for i in input().strip().split(' ')]

def calc(n, m):
    if m == 0:
        return 1
    if m == 1:
        return 1
    mid = n // 2
    if m <= mid:
        return m
    return n - m
    
print(calc(n, m))
