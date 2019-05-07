#!python3
class Solution:
    def _profit(prices, lo, hi):
        if lo >= hi:
            return 0
        if hi - lo == 1:
            profit = prices[hi] - prices[lo]
            return profit if profit > 0 else 0
        mid = (lo+hi)//2
        before_mid = Solution._profit(prices, lo, mid-1)
        after_mid = Solution._profit(prices, mid+1, hi)
        with_mid = max(prices[mid:hi+1]) - min(prices[lo:mid+1])
        return max(before_mid, after_mid, with_mid)

    def maxProfit_divide_and_conquer(self, prices) -> int:
        return Solution._profit(prices, 0, len(prices)-1)

    def maxProfit(self, prices) -> int:
        max_ = 0
        min_ = float('inf')
        for i, price in enumerate(prices):
            if price < min_:
                min_ = price
            elif price - min_ > max_:
                max_ = price - min_
        return max_
        

"""
I1
all pairs
T: O(n^2)
S: O(1)

I2
T(n) = 2T(n/2) + n
Master theorem. f(n) ~= n^log(2,2)  => log(n) * n^1 = log(n)n

S: stack, log(n)


E1
7 1 5 3 6 4
0 5  2
 0 1 = 0
 3 5  4
  3 3 = 0
  5 5 = 0
  min 3  max 6
   = 3
 min 1  max 6
  = 5
= 5




E2
0
= 0

E3
0 1
= 1

E4
7 6 4 3 1
0 4
 mid 2
 0 1 = 0
 3 4 = 0
 = 0
= 0


E5
10 11 7 10 6

minprice p[i]  maxprofit
10 11 1
7  10 3
6



"""
