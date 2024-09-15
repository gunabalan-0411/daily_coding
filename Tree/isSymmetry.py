'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSummetric(root):
    def issymmetry(left, right):
        # Both came to the last end after passing equal condition
        if not left and not right:
            return True
        if not left or not right or left.val != right.val:
            return False
        
        # Same as "Same tree" problem but instead we are comparing the opposite ends
        return (
            issymmetry(left.left, right.right) and
            issymmetry(left.right, right.left)
        )
    
    return issymmetry(root.left, root.right)
        