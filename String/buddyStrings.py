from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c1, c2 = Counter(s), Counter(goal)
        if c1 != c2: return False
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1
        if diff == 2:
            return True
        elif diff == 0:
            return any([cnt > 1 for ch, cnt in c1.items()])
        else:
            return False
