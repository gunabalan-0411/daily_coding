from typing import List
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        res = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]
            res += 1 if left >= right else 0
        return res