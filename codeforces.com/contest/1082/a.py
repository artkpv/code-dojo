#!python3
"""
1<= t <= 10^3
1 <= n,d <= 10^9
x,y <= n


1)
from x:
    < y: (y - x) / d
    > y: (x - y) / d
from 1:
    y / d + x // d
from n:
    (n-y) / d + (n-x)//d



Ex1
11 4 9 2
  4 6 8 10 11 9  -> 5

Ex2
11 6 1 3  > 5
  6 9 11 8 5 2 ?
  6 3 1

"""

t = int(input().strip())

INF = 99999999999

while t > 0:
    t -= 1
    n,x,y,d = [int(i) for i in input().strip().split(' ')]
    # todo edge casees
    if x == y:
        print(0)
    elif x < y and (y-x)%d == 0:
        print((y-x)//d)
    elif x > y and (x-y)%d == 0:
        print((x-y)//d)
    elif (y-1)%d == 0 or (n-y)%d == 0:
        left = (y-1)//d + (x//d) + (1 if x%d > 0 else 0) if (y-1)%d == 0 else INF
        right = (n-y)//d + (n-x)//d + (0 if (n-x)%d==0 else 1) if (n-y)%d == 0 else INF
        print(min(left, right))
    else:
        print(-1)



