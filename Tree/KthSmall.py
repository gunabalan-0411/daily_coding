# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # sorted_ar = [float('inf')]
        # def dfs(node):
        #     if not node:
        #         return
        #     if node.val < sorted_ar[0]:
        #         sorted_ar.insert(0, node.val)
        #     else:
        #         i = 0
        #         while node.val>sorted_ar[i]:
        #             i += 1
        #         sorted_ar.insert(i, node.val)
        #     dfs(node.left)
        #     dfs(node.right)        
        # dfs(root)
        # return sorted_ar[k-1]
        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right