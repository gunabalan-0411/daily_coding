class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(
            # Single num edge case
            nums[0],
            # Since the houses are circle eliminate the first and last one
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )
    def helper(self, nums):
        rob1, rob2 = 0, 0
        # Using dynamic prgramming approach
        for n in nums:
            # max of current house money + old(one house before) max rob money
            latest = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = latest
        return rob2