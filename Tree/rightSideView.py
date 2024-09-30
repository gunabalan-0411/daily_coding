# Definition for a binary tree node.
from typing import Optional, List
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        q = collections.deque([root])
        ans = []
        while q:
            size = len(q)
            for i in range(size):
                root = q.popleft()
                if i == (size - 1):
                    ans.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return ans
        
