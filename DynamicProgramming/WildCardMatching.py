'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

'''
def isMatch(s: str, p: str) -> bool:
        # ? matches any single char
        # * matches any sequence of characters including empty sequence

        if len(p) == 0:
            return len(s) == 0
        
        dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        
        dp[0][0] = True

        # Checking Edge case
        # First column always False as no text would pass empty pattern other than empty string
        # First row empty text always matches with *
        for index in range(1, len(dp[0])):
            if p[index - 1] == '*':
                # Since * means 0 or more occurence, we take Truth value of prev 
                # '' -> * but '' != a*
                dp[0][index] = dp[0][index - 1]

        # Iterating the chars from string
        for index_i in range(1, len(dp)):
            # Iterating the chars from pattern
            for index_j in range(1, len(dp[0])):
                # Case 1:
                # Match with same char or with `?`
                if s[index_i-1] == p[index_j-1] or p[index_j-1] == "?":
                    # Taking the value of Diagonal value which means to check if so far all
                    # texts matches with current pattern or not
                    dp[index_i][index_j] = dp[index_i-1][index_j-1]

                # Case 2:
                # Match with `*`
                elif p[index_j-1] == "*":
                    # Since `*` is zero or more occurence we need to take values from either of
                    # its capabilities
                    # sub case 1: Taking `*` as zero occurence or
                    #   Have to check if without `*` (j-1) chars from text so far(i) is True
                    # sub case 2: Taking `*` One or more occurence
                    #   Have to check if with `*` (j) prev chars other than current is True
                    dp[index_i][index_j] = dp[index_i][index_j-1] or dp[index_i-1][index_j]
                
                else:
                    dp[index_i][index_j] = False      
        
        
        return dp[len(s)][len(p)]

text = 'xaylmz'
pattern = 'x?y*z'
print(f'String: {text} & Pattern: {pattern} is {isMatch(text,pattern)}')
text = 'xylmz'
pattern = 'x?y*z'
print(f'String: {text} & Pattern: {pattern} is {isMatch(text,pattern)}')

