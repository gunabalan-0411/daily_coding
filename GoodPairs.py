'''
https://leetcode.com/problems/number-of-good-pairs/
'''
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        ans = 0
        count = [0] * 101

        for num in nums:
            ans += count[num]
            count[num] += 1

        return ans
        