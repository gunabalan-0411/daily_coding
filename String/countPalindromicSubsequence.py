import collections
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = collections.Counter(s)
        res = set()
        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            for j in range(26):
                ch = chr(ord('a') + j)
                if ch in left and ch in right:
                    res.add((ch, s[i]))
            left.add(s[i])
        return len(res)
    


s= 'aabca'
# s= 'ckafnafqo' #4
print(Solution().countPalindromicSubsequence(s))