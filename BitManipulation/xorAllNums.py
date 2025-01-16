from typing import List
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        if len(nums1) % 2:
            # if elems appear in nums1 appear even count then it would cancel each other becomes 0
            for n in nums2:
                res ^= n
        if len(nums2) % 2:
            for n in nums1:
                res ^= n
        return res