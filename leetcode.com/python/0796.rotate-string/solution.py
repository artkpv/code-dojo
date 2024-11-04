# Created by Artyom K. at 2024/11/04 10:53
# leetgo: 1.4.9
# https://leetcode.com/problems/rotate-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] == goal[:len(s) - i] and s[:i] == goal[len(s) - i:]:
                return True
        return False

        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    goal: str = deserialize("str", read_line())
    ans = Solution().rotateString(s, goal)
    print("\noutput:", serialize(ans, "boolean"))
