# Created by Artyom K. at 2024/10/19 09:39
# leetgo: 1.4.9
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

from typing import *
from leetgo_py import *

# @lc code=begin

'''
n , k
s_i-1 + 1 + rev(inv(s_i-1))

lx2+1

I1 BF
just do it
T: O( 2^20 * 10^6 ~= 10^12)
S: 10^6


I2
can get len for k:
((1x2 + 1) x 2 + 1) x 2 + 1) ... > k

1: 2 2 + 1
2: (2 2 + 2 + 1) 2 + 1
3: 2 2 2 + 2 2 + 2  

n: 2^n + 2^(n-1) + .. + 2^2 + 2 + 1 > k

geom prog

sum = (2^(n+1) - 2) / (2 - 1) = 2^(n-1) - 2

n = ceil( log2(k + 2) + 1 ) )


I3
Two pointers?
Construct the string at once: 
i and j 
i when gets to empty, puts 1 ; j at 0
i reverses j that goes backward
repeats

T: log2(k) or O 20
S: O 20


'''

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        arr = [False]
        j = -1
        while len(arr) < k:
            if j < 0:
                arr += [True]
                j = len(arr) - 2
            else:
                arr += [not arr[j]]
                j -= 1
        return str(int(arr[-1]))


        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKthBit(n, k)
    print("\noutput:", serialize(ans, "character"))
