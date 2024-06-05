'''
https://leetcode.com/problems/remove-outermost-parentheses/
'''
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ''
        _open = 0
        _close = 0
        _start = 0
        for i in range(len(s)):
            if s[i] == '(':
                _open += 1
            else:
                _close += 1
            if _open == _close:
                result += s[_start+1: i]
                _start = i + 1
                _open = 0
                _close = 0
        return result