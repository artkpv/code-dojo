# Created by Artyom K. at 2024/10/14 09:55
# leetgo: 1.4.9
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

from typing import *
from leetgo_py import *

# @lc code=begin

'''
I1 BF
choose do
T: n * n 
S: 1

I2 
heap , remove and add each k operation

T: n * log(n)
s: n

'''

from heapq import heappush, heappop, heapify
from math import ceil

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-e for e in nums]
        heapify(nums)
        res = 0
        for _ in range(k):
            e = heappop(nums)
            res += -e
            heappush(nums, ceil(e//3))
        return res

        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxKelements(nums, k)
    print("\noutput:", serialize(ans, "long"))
