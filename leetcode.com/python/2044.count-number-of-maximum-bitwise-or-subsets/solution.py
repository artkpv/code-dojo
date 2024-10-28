# Created by Artyom K. at 2024/10/18 09:24
# leetgo: 1.4.9
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

from typing import *
from leetgo_py import *

# @lc code=begin

'''
bf i1
all subsets? 2^16  . 1024* 64

I2
max bitwise or is just or of all elements
so 1 take all elements that contribute a unique 1 in max bitwise or - M.
M * 2^(N-M) 
N-M - non essential elements.

N - to find essential: calc max OR without an element and and check if equals to max_or. 

T: N
S: N

'''

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        from functools import reduce
        from itertools import combinations
        max_or = reduce(int.__or__, nums)
        res = 0
        for comb in range(1, 2**n):
            arr = [el for i, el in enumerate(nums) if (1 << i) & comb > 0]
            if arr:
                cur = reduce(int.__or__, arr)
                if cur == max_or:
                    res += 1
        return res



    def countMaxOrSubsets2(self, nums: List[int]) -> int:
        n = len(nums)
        right = [0] * n  # right[i] = bitwise OR of all nums[i+1:]
        max_or = nums[-1]
        for i in range(n-2,-1,-1):
            right[i] = max_or
            max_or |= nums[i]
            print(bin(max_or), [bin(el) for el in right])
        m = 0
        left_max_or = 0
        for i in range(n):
            if right[i] | left_max_or != max_or:
                m += 1
            left_max_or |= nums[i]
            print(bin(left_max_or))
        return m * (1 << (n-m)) if m > 0 else (1 << n) - 1
                


        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countMaxOrSubsets(nums)
    print("\noutput:", serialize(ans, "integer"))
