#!python3

n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
i = a.index(1)
j = a.index(n)
print(max(max(i, j), n - min(i, j) - 1))

"""
max
 max(1, 2)
 5 - min(1,2)-1
 = 3

max(0,2)
7 - min(0,2)-1
6
"""
