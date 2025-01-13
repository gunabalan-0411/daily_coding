from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        return sum([1 if v%2==1 else 2 for ch, v in Counter(s).items()])
            