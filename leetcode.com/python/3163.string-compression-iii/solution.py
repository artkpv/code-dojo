# Created by Artyom K. at 2024/11/04 10:47
# leetgo: 1.4.9
# https://leetcode.com/problems/string-compression-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def compressedString(self, word: str) -> str:
        res = [1, word[0]]
        for e in word[1:]:
            assert res[-2] <= 9
            if res[-1] != e or res[-2] == 9:
                res.extend([1, e])
            else:
                res[-2] += 1
        return ''.join(str(e) for e in res)
        

# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().compressedString(word)
    print("\noutput:", serialize(ans, "string"))
