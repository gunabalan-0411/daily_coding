'''
https://leetcode.com/problems/count-the-number-of-consistent-strings/
'''
class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        # count = 0
        # for word in words:
        #     i = 0
        #     for ch in word:
        #         if ch not in allowed:
        #             break
        #         i += 1
        #     if i == len(word):
        #         count += 1
        # return count
        return sum(all(c in allowed for c in word)
               for word in words)
        