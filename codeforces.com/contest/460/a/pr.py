#!python3

"""
n socks at begining
m-th day a new pair

2 2
2 1 1 0

9 3
9 8 7 7 6 5 5 4 3 3 2 1 1 0
9 8 7 6 5 4 3 2 1 0


n + n//m + n//m//m = 9 + 3 + 1  = 13


2 + 1 = 3

10 2
10 + 5 + 2 + 1 = 18

10 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 0
1  2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
n, m = [int(i) for i in input().strip().split(' ')]
days = n
while n//m > 0:
    days += n//m
    n //= m
print(days)
exit()


"""

while n > 0:
    days += 1
    n -= 1
    if days % m == 0:
        n += 1
print(days)

"""
2 2

0 2
1 1
2 1
3 0
> 3

"""

