#!python3
from math import ceil
INF = float('inf')
for _ in range(int(input().strip())):
    n, x = [int(i) for i in input().strip().split(' ')]
    blows = set()
    for j in range(n):
        dd, hh = [int(i) for i in input().strip().split(' ')]
        blows.add((dd, hh))

    dp = dict()
    def c(x):
        if x <= 0:
            return 0
        if x not in dp:
            optimal = INF
            for d, h in blows:
                curX = x - d + h
                if curX >= x:
                    continue
                curN = c(curX) + 1
                if curN < optimal:
                    optimal = curN
            dp[x] = optimal
        return dp[x]
    ans = c(x)
    print(-1 if ans == INF else ans)

    # d = 0
    # h = float('inf')
    # for j in range(n):
        # dd, hh = [int(i) for i in input().strip().split(' ')]
        # if dd - hh > d - h:
            # h = hh
            # d = dd
    # if d - h <= 0:
        # print(-1 if x > d else 1)
    # else:
        # """
        # ((x - d + h) - d + h) - d + h ...
        # x - 2d + 2h
        # x - n*d + n*h <= 0
        # x + n * (h - d) <= 0
        # n >= x/(d-h)
        # """
        # n = ceil(x/(d-h))
        # print(n)
