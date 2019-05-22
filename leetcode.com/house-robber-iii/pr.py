# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""

I1 BF
Preorder, each can be 0 or 1.
Thus O(2^n)

I2
Cache optimal for a tree if root 0 or 1.
optimal[(v,0)] - optimal if v not taken
optimal[(v,1)] - optimal if v taken
Number of optimal == n*2
Time: O(N)
Space: ~N

"""

import sys

sys.setrecursionlimit(9999999)


class Solution:
    def rob(self, root):
        if not root:
            return 0
        optimal = dict()

        def visit(v, isparenttaken):
            if not v:
                return 0
            if (v, isparenttaken) not in optimal:
                v_optimal = 0
                if not isparenttaken:
                    # case 1, rob this
                    v_optimal = (
                       v.val + visit(v.left, True) + visit(v.right, True)
                    )
                # case 2, don't rob this:
                v_optimal = max(
                    v_optimal,
                    visit(v.left, False) + visit(v.right, False)
                )
                optimal[(v, isparenttaken)] = v_optimal

            return optimal[(v, isparenttaken)]

        return visit(root, isparenttaken=False)


"""
Example1
     3
    / |
   2   3
    \   |
     3   1

3 3 1 = 7

optimal


visit 3 0
max(
 3 +
  visit 2 1
    0 + (visit 3 0 = 3) = 3
    = 3
  visit 3 1
    0 + (visit 1 0 = 1) = 1
    = 1
  = 7
 ,
 (visit 2 0)
  max (
    2 + (visit 3 1 = 0) = 2
    (visit 3 1 = 3) = 3
  ) = 3
 (visit 3 0)
  max( .. ) = 3
) = 7
> 7




"""
