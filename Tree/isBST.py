'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root) -> bool:
        def valid(node, left_boundary, right_boundary):
            # If any branch reaches end then its passed right 
            if not node:
                return True

            # In BST all small values on left and all big values on right
            if not (node.val > left_boundary and node.val < right_boundary):
                return False

            # iterate all left and then right
            # cur node value should be the highest value when iterate left side vice versa for right side
            #             5
            #       3           7
            #               4       8
            return (
                valid(node.left, left_boundary, node.val) and 
                valid(node.right, node.val, right_boundary)
            )

        return valid(root, float('-inf'), float('inf'))
    
bTree = TreeNode(5)
bTree.left = TreeNode(3)
bTree.right = TreeNode(7)
bTree.right.left = TreeNode(4)
bTree.right.right = TreeNode(8)
print(Solution().isValidBST(bTree))