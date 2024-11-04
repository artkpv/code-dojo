# Created by Artyom K. at 2024/11/02 10:35
# leetgo: 1.4.9
# https://leetcode.com/problems/circular-sentence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if not sentence:
            return True
        if sentence[0] != sentence[-1]:
            return False
        i = 1
        j = 0
        while i < len(sentence):
            if sentence[i-1] == ' ' and sentence[i] != ' ':
                if sentence[j] != sentence[i]:
                    return False
            if sentence[i] != ' ':
                j = i
            i += 1
        return True
        

# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    ans = Solution().isCircularSentence(sentence)
    print("\noutput:", serialize(ans, "boolean"))
