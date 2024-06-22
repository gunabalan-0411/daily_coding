class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for n in nums:
            # check if n-1 not in the set, then its 
            # a new consecutive sequence start
            if n - 1 not in numsSet:
                length = 0
                while n + length in numsSet:
                    length += 1
                longest = max(length, longest)
        return longest