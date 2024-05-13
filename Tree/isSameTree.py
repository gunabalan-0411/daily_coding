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

