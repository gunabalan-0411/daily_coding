from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        Q = deque([root])
        count = 1
        while Q:
            for _ in range(len(Q)):
                node = Q.popleft()
                if not node.left and not node.right:
                    return count
                if node.left: Q.append(node.left)
                if node.right: Q.append(node.right)
            count += 1
        return count