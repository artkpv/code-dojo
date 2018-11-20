#!/bin/python3

"""
https://www.hackerrank.com/contests/w36/challenges/a-race-against-time

    Given N-1 students, <=10^5. Their heights, 10^9. Their prices, -10^9..10^9 NEGATIVE.
    N students before Madison.
    Optimal solution to handle to Madison?
    Solution = time (distance + height diffs) + price to handle

Examples:

1.
4
5
2 6 2
2 3 2
> 8

2.
4
5
2 3 1
2 3 2
> 4

3.
10
5
6   1 2  7   3  6  1 2  7
-2 -7 7 -2 -13 -2 -7 7 -2


"""

import sys


def cost_at(C, heights, prices, N):
    for i in range(1, N):  # i - current position
        # print("cost_at({}, {})".format(i, C))
        height_sup = None  # = max { height k: j+1 <= k <= i-1 }
        for j in range(i-1, -1, -1):  # j<i
            # filter out those who can not run by :
            h_j = heights[j]
            if height_sup == None or h_j > height_sup:
                height_sup = h_j
            if h_j < height_sup:  # j student could not reach i position
                continue

            # find optimal cost (time+price) for i:
            runner = C[j][1]
            cost = C[j][0] + i - j  # cost + time to run till i
            i_h = heights[i]
            runner_h = heights[runner]
            if runner_h < i_h or prices[i] < 0:  # should exchange or cost reduce
                cost +=prices[i] + abs(i_h - runner_h)
                runner = i

            if C[i] == None or C[i][0] > cost:
                C[i] = (cost, runner)

        # print("i={} C={}".format(i, C))

def raceAgainstTime(N, heights, prices):
    C = [None] * (N) #  C[i] - optimal runner for i-th position:
    C[0] = (0, 0)  # 0 runner, 0 cost to run at 0 position
    cost_at(C, heights, prices, N)
    # C[N-1] has the runner and optimal solution
    # print(C)
    return C[N-1][0] + 1  # one more unit of distance to run

if __name__ == "__main__":
    n = int(input().strip())
    mason_height = int(input().strip())
    heights = list(map(int, input().strip().split(' ')))
    prices = list(map(int, input().strip().split(' ')))
    heights.insert(0, mason_height)
    prices.insert(0, 0)
    result = raceAgainstTime(n, heights, prices)
    print(result)
