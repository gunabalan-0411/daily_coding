'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def bst_parser(left, right):
            # When there is no more element to add left value will be more than right
            # Hence returning None
            if left > right:
                return None
            
            mid = (left + right) // 2
            # We start from middle and add the nearest elements as left and right
            # same formula calculate for root's left and right
            root = TreeNode(nums[mid])
            root.left = bst_parser(left, mid - 1)
            root.right = bst_parser(mid+1, right)

            return root
        return bst_parser(0, len(nums) - 1)