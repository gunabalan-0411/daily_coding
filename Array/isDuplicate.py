'''
https://leetcode.com/problems/contains-duplicate/
'''
class Solution:
    def containsDuplicate(self, nums) -> bool:
        # 400 ms
        # return len(nums) != len(set(nums))
        # 425 ms
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return True
            hashmap.add(n)
        return False