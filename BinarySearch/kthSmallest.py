from bisect import bisect
from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)
        def less_k(m):
            res = 0
            for r in range(N):
                res += bisect.bisect_right(matrix[r], m)
            return res
        while l < r:
            m = (l+r)//2
            if less_k(m) < k:
                l = m + 1
            else:
                r = m
        return l