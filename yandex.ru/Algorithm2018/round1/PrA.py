#!python3
n, k = [int(i) for i in input().strip().split(' ')]
print(max(2, n-k+1))
