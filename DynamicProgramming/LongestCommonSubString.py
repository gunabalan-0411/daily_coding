class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # initialize dynamic programming cache
        # Adding one more column and row for empty strig
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Bottom to top approach, store the total count in successive index
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                # If matches, update the current value from the diagonal value
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                # if not match, we have to retain the max value which goes in
                # the both direction right or down
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]