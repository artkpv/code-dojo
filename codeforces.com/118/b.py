"""
http://codeforces.com/contest/118/problem/B
"""
#!python3
n = int(input().strip())
m = n+1
s = ''
for i in range(1, n*2+2, 2):
    for j in range(i % ( n//2)):
        n = j % (1+i//2)
        s += str(n)
