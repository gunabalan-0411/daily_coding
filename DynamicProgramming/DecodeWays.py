'''
https://leetcode.com/problems/decode-ways/
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        # Initialize dynamic programming
        dp = {len(s) : 1}

        # calculate from last
        for i in range(len(s)-1, -1, -1):
            # This below below cases count single digit
            # decoding
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            # To count double digit decoding variations
            if ( i + 1 < len(s) and (
                s[i] == '1' or 
                s[i] == '2' and
                s[i+1] in '0123456')):
                dp[i] += dp[i+2]
        return dp[0]