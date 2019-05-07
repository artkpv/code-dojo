"""

0 1 2 3 4
x   y   z
x     y
  x   y
  x     y

n
2 2 2
~

Idea 1
BF
Check all places
Time: O(2^n)
Space: ~n to store those indeces

Idea 2
Recursive
money for nums[0..n-1] = max(
 money for num[1..n-1],
 num[0] + money for num[2..n-1]
)
Time: O(2^n) ~ two calls per each element
With memoization: O(n)
Space: ~n - for stack till last el


Idea 3
Iterative
Fill from end
money[num of houses from left]
money[0] = 0
money[1] = nums[0]
money[2] = max(money[2-2] + num[1], money[2-1])
...

Time: ~n
Space: ~n

"""

class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        money = [0, nums[0]]
        for id in range(1, len(nums)):
            money += [max(
                nums[id] + money[id-1],
                money[id]
            )]
        return money[len(nums)]

"""
Ex1
1 2 3 1
id money
   0
0  1
1  2
2  4 or 2  4
3  3 or 4  4
> 4
"""
