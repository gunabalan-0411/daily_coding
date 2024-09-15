'''
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
'''
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    queue = collections.deque()
    result = []
    queue.append(root)

    while queue:
        lenQ = len(queue)
        level_members = []
        for i in range(lenQ):
            node = queue.popleft()
            if node:
                level_members.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        if level_members:
            result.append(level_members)

    return result
