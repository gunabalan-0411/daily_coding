class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        mid = len(nums)//2
        for i in range(mid):
            res += [nums[i], nums[mid+i]]
        return res
        