from typing import Optional
from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        Q = deque([root])
        while Q:
            n = len(Q)
            for i in range(n):
                node = Q.popleft()
                if Q and i < (n-1):
                    node.next = Q[0]
                if node and node.left: Q.append(node.left)
                if node and node.right: Q.append(node.right)
        return root