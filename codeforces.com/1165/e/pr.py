#!python3
"""
NEXT:
Need to rearrange ONLY b so that in the middle 
product is min.


Ex 1
5
1 8 7 2 4
9 7 2 9 3
646


1 2 4 7 8
9 9 7 3 2



Ex 2
1 3
4 2

1 1 = 4 
1 2 = 10
2 2 = 6
= 20
"""

n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
b = [int(i) for i in input().strip().split(' ')]
mid = n // 2 + 1
a.sort()
a = a[mid:] + a[:mid]
b.sort(reverse=True)
b = b[mid:] + b[:mid]
c = [a[i]*b[i] for i in range(n)]
print(a)
print(b)
print(c)
result = 0
MOD = 998244353
for l in range(n):
    for r in range(l, n):
        result = (
            result + sum(c[i] for i in range(l, r+1))) % MOD
print(result)