from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = nums.index(target) if target in nums else -1
        right_index = len(nums) - 1 - nums[::-1].index(target) if target in nums else -1

        return left_index, right_index
        