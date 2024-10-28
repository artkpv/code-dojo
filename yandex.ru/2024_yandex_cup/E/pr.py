'''
n

number of ways to get it with powers of two while we take each power arr possible times


max is floor(log(2, n)) - one time  - one time

I1 BF?
max power is floor(log(2, n))

all variants?


'''

import math

def solve(n, arr):
    ans = 0
    arr = sorted(arr)

    dp = {0:1}
    def rec(n):
        if n not in dp:
            dp[n] = 0
            for p in range(math.floor(math.log2(n))+1):
                for v in arr:
                    if 2**p * v <= n:
                        dp[n] += rec(n - 2**p * v)

        return dp[n]

    return rec(n)


def main():
    n = int(input().strip())
    m = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    print(solve(n, arr))

if __name__ == "__main__":
    solve()
