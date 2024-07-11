class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = float('-inf')
        for banks in accounts:
            max_wealth = max(max_wealth, sum(banks))
        return max_wealth
        