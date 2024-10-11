# Created by Artyom K. at 2024/09/21 10:52
# leetgo: 1.4.9
# https://leetcode.com/problems/valid-parentheses/

from typing import *
from leetgo_py import *

# @lc code=begin

paranthesis = '[](){}'

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for e in s:
            ei = paranthesis.index(e)
            assert ei >= 0
            if ei % 2 == 1:
                if not stack:
                    return False
                if paranthesis.index(stack[-1]) + 1 != ei:
                    return False
                stack.pop()
            else:
                stack.append(e)
        return not stack




# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().isValid(s)
    print("\noutput:", serialize(ans, "boolean"))
