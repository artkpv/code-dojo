#!python3
"""

5 3 4 5  0 0
3 4 5  5 0
3 4    5 5
3      9 5 wins


Idea
BF
T: 2*n
0 - takes left
1 - takes right
S: n

Idea
DP
F(left, right, is_A) =
 return a, b for max( a in
    a, b = F(left+1, right, not is_A),
    a, b = F(left, right+1, not is_A)
)
if is_a
a,b = a,b
else
a,b = b ,a
return a,b

"""

import unittest


class Solution:
    def stoneGame(self, piles):
        n = len(piles)
        O = {}
        for i in range(n):
            O[(i, i)] = (0, piles[i])
        for size in range(2,n+1):
            i = 0
            # import pdb; pdb.set_trace()
            while i + size - 1 < n:
                left = i
                right = i + size - 1

                is_a = size % 2 == 0

                a, b = O[(left, right-1)]
                if is_a:
                    a, b = a + piles[right], b
                else:
                    a, b = a, b + piles[right]

                a2, b2 = O[(left+1, right)]
                if is_a:
                    a2, b2 = a2 + piles[left], b2
                else:
                    a2, b2 = a2, b2 + piles[left]

                if is_a:
                    a, b = (a, b) if a > a2 else (a2, b2)
                else:
                    a, b = (a, b) if b > b2 else (a2, b2)
                O[(left, right)] = (a, b)
                i += 1
        a, b = O[(0, n-1)]
        return a > b

"""
5 3 4 5

O
0 0 5
1 1 3
2 2 4
3 3 5

size=2
i=0
left = 0
right 1
a, b = 0 5
a2, b2 = 0 3


"""


class Tests(unittest.TestCase):
    def test_tests(self):
        self.assertTrue(Solution().stoneGame([5,3,4,5]))


unittest.main()

