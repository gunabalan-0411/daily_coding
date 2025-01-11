from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        count = Counter(s)
        odds = 0
        for ch, cnt in count.items():
            odds += cnt % 2
        return odds <= k