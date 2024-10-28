# Created by Artyom K. at 2024/10/26 07:04
# leetgo: 1.4.9
# https://leetcode.com/problems/find-the-highest-altitude/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_ = current
        for g in gain:
            current += g
            max_ = max(max_, current)
        return max_
        

# @lc code=end

if __name__ == "__main__":
    gain: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestAltitude(gain)
    print("\noutput:", serialize(ans, "integer"))
