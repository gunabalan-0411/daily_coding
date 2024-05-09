'''
Patterns
   - Minimum (Maximum) Path to Reach a Target
   - Distinct Ways
   - Merging Intervals
   - DP on Strings
   - Decision Making

'''
# ---------------------------------------- Problems/ Solution
'''
	Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

	Example 1:

	Input: "babad"
	Output: "bab"
	Note: "aba" is also a valid answer.
	Example 2:

	Input: "cbbd"
	Output: "bb"
'''

def longestPalindrome(s: str) -> str:

        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        maxLength, result = 1, ''
        # Each character is a palindrome of its own
        for i in range(len(s)):
            dp[i][i] = 1
            result = s[i]
        # Just now traced the palindrome of size 1 now starting 2
        length = 2

        # This loop is to compare every character with next nth character
        # So that we can check the characters between these two character tends to palindrom sequence
        while length <= len(s):
            index_i = 0
            while index_i < len(s) - length + 1:
                index_j = index_i + length - 1

                # Special case/ edge case scenario to capture the palindrome of size 2
                if length == 2 and s[index_i] == s[index_j]:
                    dp[index_i][index_j] = 1
                    maxLength = max(maxLength, 2)
                    result = s[index_i : index_j+1]
                # This condition will trace the latest or last character of palindrom just 
                # when the between chars follow palindrome rules as per dp array

                # Additionally or Internally this below condition making the palindrome within palindrome 
                # to get the maximum possible palindrom
                elif s[index_i] == s[index_j] and dp[index_i+1][index_j-1]:
                    dp[index_i][index_j] = 1
                    # Updating the length the longest palindrome
                    if length > maxLength:
                        maxLength = max(maxLength, length)
                        result = s[index_i: index_j+1]
                index_i += 1

            length += 1
        return result

'''
	Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.
	The matching should cover the entire input string (not partial).

	Note:

	s could be empty and contains only lowercase letters a-z.
	p could be empty and contains only lowercase letters a-z, and characters like . or *.
'''

def regexMatch(s, p):
    # Creating the dp matrix to track individual matches
    # Creating One extra row and col (0th row, 0th col) to handle empty char matches
    dp = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]

    # Empty text always matches with empty pattern
    dp[0][0] = True

    # To handle patterns like a*, a*b*c with which empty text (0th row) could be matching
    for index in range(1, len(dp[0])):
         if p[index-1] == '*':
            # * always occur right after any char(alternatively) hence getting 
            # the truth value of two cell before (Ex: *a before)
            dp[0][index] = dp[0][index-2] 
            # In dp[1][:] the first column should always be False as no text should match '' empty pattern
    
    for index_i in range(1, len(dp)):
        for index_j in range(1, len(dp[0])):

            # Condition 1: Any direct matches or if '.' spotted
            if s[index_i-1] == p[index_j-1] or p[index_j-1] == '.':
                # Getting the truth value from previous step (diagnol value) 
                # just to make sure so far text matches with pattern
                # if prev step is false then false, if prev step is true its true as also matches chars
                dp[index_i][index_j] = dp[index_i-1][index_j-1]

            # Condition 2: If '*' spotted
            elif p[index_j-1] == '*':
            # Case 2.1: Ex: x can be match with xa* (where 'a*' from `pattern` could be disappear)
                # skipping 2 step(a*) back to see if x == x
                dp[index_i][index_j] = dp[index_i][index_j-2]

                # Case 2.2: Still in a case like 'a' can be match with 'a*' 
                # (where 'a' from `text` could be disapper)
                if s[index_i-1] == p[index_j-2] or p[index_j-2] == '.':
                    # Getting val from prev step to check so far(without 'a') text matches with this much pattern 
                    # (so it could be beneficial to next step)
                    dp[index_i][index_j] = dp[index_i-1][index_j] or dp[index_i][index_j] # or simply from above step
            else:
                dp[index_i][index_j] = False

    # Only if all steps (all diagonal values are true then all chars in a text matches with the pattern)
    return dp[len(s)][len(p)]

# --------------------------------------------- Testing
print(longestPalindrome("abaabcdef"))
print(regexMatch('aa', 'a*'))