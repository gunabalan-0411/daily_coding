from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(4)

print(Solution().maxPathSum(root))
        