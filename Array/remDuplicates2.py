from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        while r < len(nums):
            # to count individual duplicates
            count = 1
            while (r+1) < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1
            # shift values single double or single value
            # from right to left
            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
        