# Created by Artyom K. at 2024/10/17 09:48
# leetgo: 1.4.9
# https://leetcode.com/problems/longest-happy-string/

from typing import *
from leetgo_py import *

# @lc code=begin

'''
I1 Greedy
from longest in a or b or c. Take 2 . Then 1? or 2? To have chars left to divide the longest.

a - longest
take 2 in a
then take 1 or 2?

aa

a 4
b 3

aabaabb

if a > b + c
    take 2 a for a - b - c times.
else 
    take 1 a 


I2 BF

for 0..a, 0..b, 0..c:
    all permutations 
T: 10^6 * !10^6 



'''

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        abc = [a,b,c]
        if max(abc) == 0:
            return ''

        def enum(f=None):
            yield from [(e,i) for i,e in enumerate(abc) if not f or f(i)]

        res = ''
        while len([e for e in abc if e > 0]) > 1:
            _, j = max(enum())
            if (abc[j] > sum(enum(j)) and res and res[-1] != 'abc'[j]):
                res += 'abc'[j] * 2
                abc[j] -= 2
            else:
                left_a = enum(f=lambda i: i != j and (not res or 'abc'[i] != res[-1]))
                if len(left_a) == 0:
                    return res
                _, k = max(left_a)
                res += 'abc'[k]
                abc[k] -= 1
        return res



                




# @lc code=end

if __name__ == "__main__":
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    c: int = deserialize("int", read_line())
    ans = Solution().longestDiverseString(a, b, c)
    print("\noutput:", serialize(ans, "string"))
