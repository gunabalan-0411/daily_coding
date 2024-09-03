class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1
        return True
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            minCost = float('inf')
            for j in range(i, n):
                if self.isPalindrome(s, i, j):
                    cost = 1 + dp[j+1]
                    minCost = min(minCost, cost)
            dp[i] = minCost
        return dp[0]-1
    # def minCut(self, s: str) -> int:
    #     n = len(s)
    #     dp = [-1 for _ in range(n)]
    #     def recursive_partition(i, n, s, dp):
    #         if i == n: return 0
    #         if dp[i] != -1: return dp[i]
    #         minCost = float('inf')
    #         for j in range(i, n):
    #             if self.isPalindrome(s, i, j):
    #                 cost = 1 + recursive_partition(j+1, n, s, dp)
    #                 minCost = min(minCost, cost) 
    #         dp[i] = minCost
    #         return minCost
    #     return recursive_partition(0, n, s, dp) - 1
        

        