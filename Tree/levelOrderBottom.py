# Definition for a binary tree node.
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return None
        queue = deque()
        queue.append(root)
        
        res = []
        while queue:
            level_values = []
            for i in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right: 
                    queue.append(node.right)
            res.insert(0,level_values)
        return res

inputTree = TreeNode(
    3,
    TreeNode(
        9
    ),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)
print(Solution().levelOrderBottom(inputTree))