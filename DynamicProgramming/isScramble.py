import collections
class Solution:
    def __init__(self):
        self.char_sum = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            return s1 == s2
        if s1 == s2:
            return True
        merge = s1 + s2
        if merge in self.char_sum:
            return self.char_sum[merge]
        # Pruning part
        if collections.Counter(s1) != collections.Counter(s2):
            self.char_sum[merge] = False
            return False

        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])) or (self.isScramble(s1[:i], s2[len(s2) - i:]) and self.isScramble(s1[i:], s2[:len(s2) - i])):
                self.char_sum[merge] = True
                return True
        self.char_sum[merge] = False
        return False

            
        