#!python3

"""
> n - num of people
< people nums sum 

I1 
1<= sum <= n*(n+1)/2

k even and n even:
  1 3 5 7 .. n-1
  k = 2, 4, 6, ...
  a_i = 1+2*k  k=0..n/2-1
  last: n-1  (n-1 = 1+2*k => last k = n/2-1 = k)
  sum = 


k even and n odd:
  

Ex1
6 
1 9 5 21

k = 1, n
k = 2, 1 3 5 1
k = 3, 1 4 1
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


I1 
BF ~N*N/2

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


