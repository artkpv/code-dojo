#!python3

"""

x0 x1 x2 x3
2 <= n <= 3*10^5
p0 p1 p2
1 <= m <= 3*10^5
Find: first min, p_i ?

Idea 1

Find gcd for all nums: x1-x0, x2-x0, ..

gcd ...


4 7


Ex1
3 5
3 12 18
2 6 5 3 3


"""
import math
n, m = [int(i) for i in input('').strip().split(' ')]
X = [int(i) for i in input('').strip().split(' ')]
P = [int(i) for i in input('').strip().split(' ')]
delimiter = X[1] - X[0]
for i in range(2, n):
    if delimiter == 1:
        break
    delimiter = math.gcd(X[i] - X[i-1], delimiter)

P_inx = -1
for i, e in enumerate(P):
    if delimiter % e == 0:
        P_inx = i + 1
        break

if P_inx > 0:
    print("YES")
    print(X[0], P_inx)
else:
    print("NO")

"""

"""
