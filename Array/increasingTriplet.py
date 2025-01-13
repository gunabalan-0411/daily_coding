from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = float('inf')
        b = float('inf')
        for idx, n in enumerate(nums):
            if a >= n:
                a = n
            elif b >= n:
                b = n
            else:
                return True
        return False

                