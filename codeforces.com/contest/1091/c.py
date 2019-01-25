#!python3

"""
> n - num of people, 2..1e9
< people nums sum

I1 BF
O(n/2*n)



I2
a_1+a_2+..+a_m
m, number of hops = lcm(k,n)/k
biggest a_i = m - gcd +1
sum = m*biggest a_i - 1 / 2

Ex1
6
1 9 5 21


k = 1,lcm= 6 sum = 1 2 .. n, 7*6/2 = 21
k = 2, 1 3 5 1, 6*3/2 = 9, + 1 3 5 1 3 5 = 6*3/2
k = 3, 1 4 1, 5*2/2=5, 
k = 4, 1 5 3 1


Ex2
16
1 10 28 64 136

k = 0, n: 1
k = 8, n/2: 1 9 1
k = 2: 1 3 5 7 9 11 13 15 1, lcm=16, 16*8//2 = 64
k = 4: 1 5 9 13 1, lcm=16, 14*4/2 = 28
k = 6: 1 7 13 3 9 15 5 11 1, lcm=48, 12*8//2 = 48
       1 7 13 (16+3)%16 16+9 16+15 5 11 1

k = 3: 1 4 7 10 13 16 3 6 9 12 15 2 5 8 11 14 1  n


Ex3
5
k = 1; 6*5/1/2 = 15
k = 2; 5*10/2/2 = 12..13  1 3 5 2 4 1
k = 3;


"""

import math

n = int(input().strip())

res = set([1])
for i in range(1, (n+1)//2 + 1):
    gcd = math.gcd(n,i)  # optimize! O(n^2) to O(n*log^2 log log n)
    s = n*(n-gcd+2)/gcd
    res.add(int(s//2))

print(' '.join(str(i) for i in sorted(res)))

