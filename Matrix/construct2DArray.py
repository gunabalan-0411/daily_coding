from typing import List
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): return []
        res = []
        offset = 0
        for i in range(m):
            row = []
            for j in range(offset, n+offset):
                row.append(original[j])
            offset += n
            res.append(row)
        return res


        