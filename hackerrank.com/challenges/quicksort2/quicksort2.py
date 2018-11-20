import sys
sys.setrecursionlimit(10000)

def partition(a):
    if len(a) <= 1:
        return a
    left = []
    right = []
    x = a[0]
    for i in range(1, len(a)):
        if a[i] <= x:
            left += [a[i]]
        else:
            right += [a[i]]
    left = partition(left)
    right = partition(right)
    b = (left or []) + [a[0]] + (right or [])
    print(' '.join(str(i) for i in b))
    return b

n = int(input().strip())
A = [int(i) for i in input().strip().split(' ')]
partition(A)
