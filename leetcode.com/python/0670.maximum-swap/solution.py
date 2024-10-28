# Created by Artyom K. at 2024/10/17 09:18
# leetgo: 1.4.9
# https://leetcode.com/problems/maximum-swap/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = [int(e) for e in str(num)]
        n = len(arr)
        for i in range(n-1):
            m = max(arr[i+1:])
            if arr[i] < m:
                j = n - arr[i+1:][::-1].index(m) - 1
                arr[i], arr[j] = arr[j], arr[i]
                return int(''.join(str(e) for e in arr))
        return num
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().maximumSwap(num)
    print("\noutput:", serialize(ans, "integer"))
