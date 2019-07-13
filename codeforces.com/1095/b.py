#!python3
n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
a.sort()
if a[1] - a[0] > a[-1] - a[-2]:
    print(a[-1]-a[1])
else:
    print(a[-2]-a[0])