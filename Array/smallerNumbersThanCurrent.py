from typing import List
import collections
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        kMax = 100
        count = collections.Counter(nums)

        for i in range(1, kMax + 1):
            count[i] += count[i - 1]

        return [0 if num == 0 else count[num - 1]
                for num in nums]
        