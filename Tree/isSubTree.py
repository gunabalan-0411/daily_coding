from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        visit_cache = set()
        def dfs_chk_same(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                return (dfs_chk_same(node1.left, node2.left) and
                dfs_chk_same(node1.right, node2.right))
            return False
        res = [False]
        def dfs_base(root_node):
            if not root_node:
                return
            if root_node and subRoot and dfs_chk_same(root_node, subRoot):
                res[0] = True
                return
            dfs_base(root_node.left)
            dfs_base(root_node.right)

        dfs_base(root)
        return res[0]
        