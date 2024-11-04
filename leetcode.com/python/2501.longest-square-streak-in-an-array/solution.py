# Created by Artyom K. at 2024/10/28 10:34
# leetgo: 1.4.9
# https://leetcode.com/problems/longest-square-streak-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin


'''
I1 BF
Sort
for each i-th . Square it and find next via binary search. Keep max len seq.

T: n log(n) + n * log n
'''

from bisect import bisect_left

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numss = set(nums)
        max_l = -1
        for x in numss:
            x_len = -1
            while True:
                x = x**0.5
                if x % 1.0 != 0.0:
                    break
                x = int(x)
                if x not in numss:
                    break
                x_len = max(1, x_len)
                x_len += 1

            max_l = max(max_l, x_len)

        return max_l


        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestSquareStreak(nums)
    print("\noutput:", serialize(ans, "integer"))
