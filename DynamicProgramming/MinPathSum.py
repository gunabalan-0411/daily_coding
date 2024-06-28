class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [0] * (cols+1)

        # assigning dp with last row only min path sum
        for i in range(cols-1, -1, -1):
            dp[i] = grid[-1][i] + dp[i+1]

        for r in range(rows -2, -1, -1):
            for c in range(cols-1, -1, -1):
                if (c+1) < cols:
                    dp[c] = grid[r][c] + min(dp[c], dp[c+1])
                else:
                    dp[c] = grid[r][c] + dp[c]
        
        return dp[0]


