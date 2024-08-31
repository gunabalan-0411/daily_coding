from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node, path_sum):
            if not node:
                return
            if not node.left and not node.right:
                res.append(int(path_sum+str(node.val)))
                return
            path_sum += str(node.val)
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

        dfs(root, '')
        return sum(res)