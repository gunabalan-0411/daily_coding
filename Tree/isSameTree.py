'''
https://leetcode.com/problems/same-tree/
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    # It get false if any one is not matching
    if not p and not q:
        return True
    # Whether one node is missing or any node not equals it get false
    if not p or not q or p.val != q.val:
        return False    
    return (
        isSameTree(p.left, q.left) and
        isSameTree(p.right, q.right)
    )

