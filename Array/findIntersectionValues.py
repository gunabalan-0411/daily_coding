from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        return [sum(num in nums2Set for num in nums1),
                sum(num in nums1Set for num in nums2)]