'''
https://leetcode.com/problems/longest-valid-parentheses/description/
Given a string containing just the characters '(' and ')', return the length of the longest 
valid (well-formed) parentheses 
substring
'''
def longestValidParentheses(s):
    #Edge Case: Adding -1 to handle when its not enclosed to the very left
    stack = [-1]
    mx = 0

    for i, ch in enumerate(s):
        if ch == '(':
            # Helps to track index of left most unpaired ( until we have unpaired )
            stack.append(i)
        else:
            stack.pop()

            if not stack:
                # Helps to track index of right most unpaired )
                stack.append(i)
            else:
                # stack[-1] contains the index of last single parenthesis
                # index - stack[-1]provides the distance and using max to get the max distance
                mx = max(mx, i - stack[-1])
    return mx

print(longestValidParentheses('(()))))))((()))'))