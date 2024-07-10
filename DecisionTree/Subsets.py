class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res_set = []
        subset = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res_set.append(subset.copy())
                return
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # Decision to not include nums[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res_set