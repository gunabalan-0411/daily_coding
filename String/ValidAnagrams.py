from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Sol 1
        return Counter(s) == Counter(t)
        # Sol 2 
        return sorted(s) == sorted(t)
        # Sol 3
        if len(s) != len(t):
            return False
        t_chs = {}
        for ch in t:
            t_chs[ch] = 1 + t_chs.get(ch, 0)
        s_chs = {}
        for ch in s:
            s_chs[ch] = 1 + s_chs.get(ch, 0)

        for ch in t:
            if t_chs[ch] != s_chs.get(ch, 0):
                return False
        return True