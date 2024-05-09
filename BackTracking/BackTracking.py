'''
Generate Parentheses
https://leetcode.com/problems/generate-parentheses/description/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

'''
def generateParenthesis(n):
    # Add Open Parenthesis when OpenN < n
    # Add Close Parentheis when CloseN < OpenN
    # Valid if OpenN == CloseN == n stop adding parenthesis and return
    #  If n = 2  (
    #        ((     ()
    #     (()    ()(    
    #   (())   ()()
    # Stack is global used for backtracking to add and pop
    stack = []
    res = []
    def backTracking(openN, closeN):
        if openN == closeN == n:
            res.append(''.join(stack))
            return
        
        if openN < n:
            stack.append('(')
            backTracking(openN+1, closeN)
            # Remove all traced brackets after successful catch
            stack.pop()

        if closeN < openN:
            stack.append(')')
            backTracking(openN, closeN+1)
            stack.pop()
        
    backTracking(0, 0)
    return res

# --------------------------------------------------------------------- Testing
print(generateParenthesis(2))