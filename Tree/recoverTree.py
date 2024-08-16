from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        object_catcher = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            object_catcher.append(node)
            dfs(node.right)
        dfs(root)
        values_sorted = sorted(node.val for node in object_catcher)
        for i in range(len(values_sorted)):
            object_catcher[i].val = values_sorted[i]