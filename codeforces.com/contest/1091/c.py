#!python3

"""
> n - num of people, 2..1e9
< people nums sum

I1 BF
O(n/2*n)



I2
sum = (n-k+1+1)*(lcm/k)/2  ??  no because mod n

1<= sum <= n*(n+1)/2


Ex1
6
1 9 5 21


k = 1,lcm= 6 sum = 1 2 .. n, 7*6/2 = 21
k = 2, 1 3 5 1, 6*3/2 = 9
k = 3, 1 4 1, 5*2/2=5
k = 4, 1 5 3 1


Ex2
16
1 10 28 64 136

k = 0, n: 1
k = 8, n/2: 1 9 1
k = 2: 1 3 5 7 9 11 13 15 1
k = 4: 1 5 9 13 1
k = 6: 1 7 13 3 9 15 5 11 1

k = 3: 1 4 7 10 13 16 3 6 9 12 15 2 5 8 11 14 1  n


Ex3
5
k = 1; 6*5/1/2 = 15
k = 2; 5*10/2/2 = 12..13  1 3 5 2 4 1
k = 3;


"""

n = int(input().strip())

if n == 2:
    print("1 3")
    exit()

res = [1]
if n % 2 == 0:
    res += [1+n//2+1]
n += [n*(n+1)/2]

i = len(res)
even = n % 2


