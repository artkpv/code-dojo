# Created by Artyom K. at 2024/10/26 06:59
# leetgo: 1.4.9
# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

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
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    root: TreeNode = deserialize("TreeNode", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().treeQueries(root, queries)
    print("\noutput:", serialize(ans, "integer[]"))
