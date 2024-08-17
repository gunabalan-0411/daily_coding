from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, curSum, path):
            if not node: return
            curSum += node.val
            path.append(node.val)
            if not node.left and node.right and curSum == targetSum:
                res.append(path[::])
            dfs(node.left, curSum, path)
            dfs(node.right, curSum, path)
            path.pop()
        dfs(root, 0, [])
        return res