#!python3

"""
100 3
3 6 9 12 15 18 21 24 27 30
      20 25 33 34 38 45 45

45*3 + 18 = 135+18 = 153

"""

for query in range(int(input().strip())):
    n, m = [int(i) for i in input().strip().split(' ')]
    base = 0
    for i in range(1, 10):
        base += (m*i)%10
    res = base * (n // (m*10))
    r = n % (m*10)
    for i in range(1, 10):
        if m*i > r:
            break
        res += (m*i)%10
    print(res)

