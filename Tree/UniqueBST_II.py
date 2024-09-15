# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def generateTrees(n):
    # cache to avoid repeated subtree formation
    dp = {}
    def generate(left, right):
        # if [None] return it helps the forloop to execute once for right loop to execute for sub-tree
        # formation on the right side
        if left > right:
            return [None]
        if (left, right) in dp:
            return dp[(left,right)]
        # List to store all possible BST
        res = []
        # right + 1, because In python, it is non inclusive
        # any val from this range could be the root node
        for val in range(left, right+1):
            # the node ranges for left and right side of the root
            # according BST rules
            leftTree = generate(left, val - 1)
            rightTree = generate(val+1, right)
            # To get the combinations of underlying subtree, mutiplying each and every combinations
            for l_node in leftTree:
                for r_node in rightTree:
                    root = TreeNode(
                        val = val,
                        left = l_node,
                        right = r_node
                    )
                    res.append(root)
        dp[(left,right)] = res
        return res
    # Assuming each val from this range could form a BST
    return generate(1, n)
