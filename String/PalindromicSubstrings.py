class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # Count even palindrome
            count += self.countPalindrome(s, i, i)
            # Count odd palindrome
            count += self.countPalindrome(s, i, i+1)
        return count

    def countPalindrome(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res       