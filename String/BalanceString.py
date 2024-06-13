class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        l_count = 0
        for i in range(len(s)):
            if s[i] == 'L':
                l_count += 1
            else:
                l_count -= 1
            if l_count == 0:
                count += 1
        return count