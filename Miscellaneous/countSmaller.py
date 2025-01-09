from typing import List
class BIT:
    def __init__(self, n):
        self.sum = [0] * (n+1)
    def update(self, i, v):
        while i < len(self.sum):
            self.sum[i] += v
            i += (i & -i)
    def query(self, i):
        res = 0
        while i > 0:
            res += self.sum[i]
            i -= (i & -i)
        return res
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        e = {v: i for i, v in enumerate(sorted(set(nums)))}
        b = BIT(len(e))
        indexes = [e[v] for v in nums]
        output = []
        for i in indexes[::-1]:
            ans = b.query(i)
            output.append(ans)
            b.update(i+1, 1)
        return output[::-1]