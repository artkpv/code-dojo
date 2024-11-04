# Created by Artyom K. at 2024/11/02 10:42
# leetgo: 1.4.9
# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def makeFancyString(self, s: str) -> str:
        count = 1
        i = 1
        res = s[0]
        while i < len(s):
            if res[-1] == s[i]:
                count += 1
            else:
                count = 1
            if count < 3:
                res += s[i]
            i += 1
        return res
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().makeFancyString(s)
    print("\noutput:", serialize(ans, "string"))
