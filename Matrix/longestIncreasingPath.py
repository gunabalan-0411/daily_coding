from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = {}
        def dfs(r, c, prev):
            # Exit rules
            if (r < 0 or r == ROWS or c < 0 or c == COLS or matrix[r][c] <= prev):
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            # initialize variable
            res = 1
            # start recursion
            res = max(res, 1+dfs(r+1, c, matrix[r][c]))
            res = max(res, 1+dfs(r-1, c, matrix[r][c]))
            res = max(res, 1+dfs(r, c+1, matrix[r][c]))
            res = max(res, 1+dfs(r, c-1, matrix[r][c]))
            # final return values
            dp[(r, c)] = res
            return res
        output = 0
        for r in range(ROWS):
            for c in range(COLS):
                output = max(output, dfs(r, c, -1))
        return output


            
            
