#!python3

for task in range(int(input().strip())):
    k, x = [int(i) for i in input().strip().split(' ')]
    print((k-1)*9+x)