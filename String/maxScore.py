class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = s.count('1')
        res = 0
        for ch in s[:-1]:
            if ch == '0':
                zeros += 1
            else:
                ones -= 1
            res = max(res, zeros+ones)
        return res