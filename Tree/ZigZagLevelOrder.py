'''
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, 
then right to left for the next level and alternate between).
'''
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_levelorder(root):
    queue = collections.deque([root] if root else [])
    result = []
    queue.append(root)
    floor = 1
    while queue:
        lenQ = len(queue)
        level_members = []
        
        for _ in range(lenQ):
            node = queue.popleft()
            if node:
                level_members.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if level_members and floor%2:
            result.append(level_members)
        elif level_members:
            result.append(level_members[::-1])
        floor += 1
    return result