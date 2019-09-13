#!python3
"""
1 2
2 1 2

1 2 3
3
2
1 2
1 3 2

n! = 6

1*(n-1) + 2*(n-2) + 3*(n-3) + .. + (n-2)*2 + (n-1)*1 + n = sum( k*(n-k), k=1..n-1 ) + n

2(n-1) + 2*2*(n-2) + 2*3(n-3) + .. +


n=3
2+2+3 = 7

n=2
1+2

n=1
1

n=4
3+4+3+4
14

"""

n = int(input().strip())

res = 0
for k in range(1, n):
    res += k*(n-k)
res += n
print(res)


