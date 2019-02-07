#!python3

"""
1<=n,k<=100
cost = (purchases + 1) * original cost

E1
3 3
2 5 6
> 13 = 6+5+2

E2
5 3
1 3 5 7 9
29 = 9 + 7 + 5 + (1+1)*3 + (1+1)*1


I1 
sort
i = n
counter = 0 
while 0 <= i:
    sum costs c[min(0,i-k):i] * (1+counter)
    counter += 1
    i -= k
Time: ~n, Space: ~1

"""
n, k = [int(i) for i in input().strip().split(' ')]
c = list(sorted(int(i) for i in input().strip().split(' ')))

i = n
counter = 0
res = 0
while i > 0:
    res += sum(c[max(i-k, 0):i])*(1+counter)
    i -= k
    counter += 1
print(res)

