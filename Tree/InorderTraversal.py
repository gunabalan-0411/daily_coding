''' Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.
https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Function
def inorderTraversal(root):
    traverse = []
    def _inorder(start):
        if not start:
            return
        _inorder(start.left)
        traverse.append(start.val)
        _inorder(start.right)
    _inorder(root)
    return traverse

# Iterative solution
def inorderTraversal(root):
    res, stack = [], []
    cur = root
    #             1
    #       2           5
    #   3       4
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res

bTree = TreeNode(1)
bTree.left = TreeNode(2)
bTree.right = TreeNode(5)
bTree.left.left = TreeNode(3)
bTree.left.right = TreeNode(4)
print(inorderTraversal(bTree))



