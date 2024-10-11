# Created by Artyom K. at 2024/09/21 11:10
# leetgo: 1.4.9
# https://leetcode.com/problems/balanced-binary-tree/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    ans = Solution().isBalanced(root)
    print("\noutput:", serialize(ans, "boolean"))
